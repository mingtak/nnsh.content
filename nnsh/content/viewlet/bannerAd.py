# -*- coding: utf-8 -*-
from five import grok
from plone.app.layout.viewlets.interfaces import IBelowContent
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
#from nnsh.content.epaper import IEpaper
#from nnsh.content.album import IAlbum
#from plone.app.contenttypes.interfaces import IDocument, IEvent, IFile, INewsItem
from zope.interface import Interface
from nnsh.content.webprofile import IWebProfile
from plone import api


#grok.templatedir('template')
"""
  viewlet named rule: Function_ViewletManager_ContextInterface
"""

class BannerAd_IBelowContent_Interface(grok.Viewlet):
    grok.viewletmanager(IBelowContent)
    grok.context(IWebProfile)
    grok.require('zope2.View')

    template = ViewPageTemplateFile('template/banner_ad.pt')

    def getAd(self):
        context = self.context
        catalog = context.portal_catalog
        brain = catalog({"Type":"Advertising", "isBanner":"True"}, sort_on="modified", sort_order="reverse")
        return brain

    def render(self):
        return self.template()
