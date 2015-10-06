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

#grok.templatedir('template')


class GetThemeId(grok.View):
    """ get selectTheme value, default value is 'porto' """

    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('get_theme_id')

    def render(self):
        if not hasattr(self.context, 'portal_catalog'):
            return
        catalog = self.context.portal_catalog
        folder = self.context
        while folder.Type() not in ['Folder', 'Plone Site', 'WebProfile']:
            folder = folder.getParentNode()
        theme = getattr(folder, 'selectTheme', None)
        if theme is not None:
            themeId = theme.to_object.getId()
        else:
            try:
                homepage = catalog({'Type':'WebProfile', 'id':'index_html'})[0]
                themeId = homepage.selectTheme
            except:
                themeId = 'porto'
        return themeId


class PreviewTheme(grok.View):
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('preview_theme')

    def render(self):
        view = api.content.get_view(
            name='view',
            context=self.context,
            request=self.request,
        )
        if self.context.Type() == 'Plone Site':
            return
        api.portal.show_message(message=_(u'This is preview page.'), request=self.request, type='info')
        return view()


class IsManager(grok.View):
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('is_manager')

    def render(self):
        if api.user.is_anonymous():
            return False
        return 'Manager' in api.user.get_roles()

class IsAnonymous(grok.View):
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('is_anonymous')

    def render(self):
        return api.user.is_anonymous()


class HasLeadImage(grok.View):
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('has_lead_image')

    def render(self):
        return bool(self.context.image)


class GetType(grok.View):
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('get_type')

    def render(self):
        try:
            return self.context.Type()
        except:
            pass
