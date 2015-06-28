# -*- coding: utf-8 -*-
from five import grok
from zope.interface import Interface
from plone.app.layout.viewlets.interfaces import IBelowContent, IPortalFooter
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
#from nnsh.content.epaper import IEpaper
#from nnsh.content.forum import IForum
#from plone.app.contenttypes.interfaces import IDocument, IEvent, IFile, INewsItem
from plone import api


#grok.templatedir('template')
"""
  viewlet named rule: Function_ViewletManager_ContextInterface
"""

class Block_IPortalFooter_Interface(grok.Viewlet):
    grok.viewletmanager(IPortalFooter)
    grok.context(Interface)
    grok.require('zope2.View')
    template = ViewPageTemplateFile('template/block.pt')

    def isAnonymous(self):
        return api.user.is_anonymous()

    def getBlocks(self):
        context = self.context
        catalog = context.portal_catalog
        brain = catalog({'Type':'WebProfile'})
        if brain:
            blocks = brain[0].getObject().blocks
            return blocks

    def render(self):
        return self.template()
