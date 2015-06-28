# -*- coding: utf-8 -*-
from five import grok
from plone.app.layout.viewlets.interfaces import IPortalFooter
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.interface import Interface
from plone import api


grok.templatedir('template')
"""
  viewlet named rule: Function_ViewletManager_ContextInterface
"""

class Subscribe_IPortalFooter_Interface(grok.Viewlet):
    grok.viewletmanager(IPortalFooter)
    grok.context(Interface)
    grok.require('zope2.View')
    template = ViewPageTemplateFile('template/subscribe_epaper.pt')

    def update(self):
        return

    def render(self):
        return self.template()
