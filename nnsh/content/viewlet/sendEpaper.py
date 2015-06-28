# -*- coding: utf-8 -*-
from five import grok
from plone.app.layout.viewlets.interfaces import IAboveContentTitle
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from nnsh.content.epaper import IEpaper
from plone import api


grok.templatedir('template')
"""
  viewlet named rule: Function_ViewletManager_ContextInterface
"""

class SendEpaper_IAboveContentTitle_IEpaper(grok.Viewlet):
    grok.viewletmanager(IAboveContentTitle)
    grok.context(IEpaper)
    grok.require('cmf.ManagePortal')
#    template = ViewPageTemplateFile('template/blind.pt')
    grok.template('send_epaper')

    def update(self):
        return

