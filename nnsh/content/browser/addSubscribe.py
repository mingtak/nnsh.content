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
from nnsh.content import MessageFactory as _

grok.templatedir('template')


class AddSubscribe(grok.View):
    """
    use plone.api to operator below registry record:
        nnsh.content.configlet.IEpaper.mailList
        nnsh.content.configlet.IEpaper.epaperLog
    """
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('addSubscribe')

    def render(self):
        portal = api.portal.get()
        context = self.context
        request = context.REQUEST
        response = request.response
        mail = getattr(context.REQUEST, 'mail', None)
        if mail is None:
            return

        mailList = api.portal.get_registry_record(name='nnsh.content.configlet.IEpaper.mailList')
        if mailList is None:
            mailList = ''
        mailList = '%s\n%s' % (mail, mailList)
        api.portal.set_registry_record(name='nnsh.content.configlet.IEpaper.mailList', value=mailList)

        api.portal.show_message(message=_(u'Thank you for subscript.'), request=request, type='info')
        response.redirect(portal.absolute_url())
        return
