# -*- coding: utf-8 -*-
from five import grok
from plone.app.layout.viewlets.interfaces import IBelowContent
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from nnsh.content.epaper import IEpaper
from nnsh.content.forum import IForum
#from plone.app.contenttypes.interfaces import IDocument, IEvent, IFile, INewsItem
from plone import api


#grok.templatedir('template')
"""
  viewlet named rule: Function_ViewletManager_ContextInterface
"""

class Disqus_IBelowContent_IForum(grok.Viewlet):
    grok.viewletmanager(IBelowContent)
    grok.context(IForum)
    grok.require('zope2.View')
    template = ViewPageTemplateFile('template/disqus.pt')

    def isAnonymous(self):
        return api.user.is_anonymous()

    def render(self):
        return self.template()
