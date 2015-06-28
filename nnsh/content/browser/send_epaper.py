# -*- coding: utf-8 -*-
from five import grok
from plone import api
from zope.interface import Interface
from nnsh.content.epaper import IEpaper
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from email.mime.text import MIMEText
from Products.CMFDefault.utils import checkEmailAddress
from Products.CMFDefault.exceptions import EmailAddressInvalid
from Products.CMFPlone.utils import safe_unicode
import time
#from plone.app.contenttypes.interfaces import IDocument, INewsItem, IEvent


grok.templatedir('template')


class SendEpaper(grok.View):
    """
    use plone.api to operator below registry record:
        nnsh.content.configlet.IEpaper.mailList
        nnsh.content.configlet.IEpaper.epaperLog
    """
    grok.context(IEpaper)
    grok.require('cmf.ManagePortal')
    grok.name('sendEpaper')

    def mailBody(self):
        context = self.context
        bodyHtml = u'<div><h1><a href=%s>%s</a></h1><hr/><div>%s</div><ul>' % (
            safe_unicode(context.absolute_url()),
            safe_unicode(context.Title()),
            safe_unicode(context.text.raw),
        )

        for item in context.selectItems:
            obj = item.to_object
#            import pdb; pdb.set_trace()
            bodyHtml += u'<li><a href="%s">%s</a></li><p>%s</p>' % (
                safe_unicode(obj.absolute_url()),
                safe_unicode(obj.Title()),
                safe_unicode(obj.Description()))
        bodyHtml += u'</ul></div>'

        mailBody = MIMEText(bodyHtml, 'html', 'utf-8')
        return mailBody


    def update(self):
        context = self.context

        mailList = api.portal.get_registry_record('nnsh.content.configlet.IEpaper.mailList')
        if not mailList:
            return
        mailBody = self.mailBody()

        mailList = mailList.split()

        for mail in mailList:
            try:
                checkEmailAddress(mail)
                api.portal.send_email(
                    recipient=mail,
                    subject=context.Title(),
                    body=mailBody.as_string()
                )
                time.sleep(1)
            except:
                errLog = api.portal.get_registry_record('nnsh.content.configlet.IEpaper.epaperLog')
                if errLog is None:
                    errLog = ''
                errLog = u'%s: Error, %s, %s\n' % (
                    safe_unicode(time.strftime('%c')),
                    safe_unicode(context.Title()),
                    mail) + errLog
                api.portal.set_registry_record('nnsh.content.configlet.IEpaper.epaperLog', errLog)
                continue
        return
