# -*- coding: utf-8 -*-
from five import grok
from zope.interface import Interface
from plone.app.layout.viewlets.interfaces import IBelowContent, IPortalFooter
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
#from nnsh.content.epaper import IEpaper
#from nnsh.content.forum import IForum
#from plone.app.contenttypes.interfaces import IDocument, IEvent, IFile, INewsItem
from nnsh.content.webprofile import IWebProfile
from plone import api


#grok.templatedir('template')
"""
  viewlet named rule: Function_ViewletManager_ContextInterface
"""

class Slide_IPortalFooter_Interface(grok.Viewlet):
    grok.viewletmanager(IPortalFooter)
    grok.context(IWebProfile)
    grok.require('zope2.View')
    template = ViewPageTemplateFile('template/slide.pt')

    def isAnonymous(self):
        return api.user.is_anonymous()

    """
    def getSlides(self):
        context = self.context
        catalog = context.portal_catalog
        brain = catalog({'Type':'WebProfile'})
        if brain:
            slides = brain[0].getObject().slides
            return slides
    """
    def render(self):
        return self.template()
