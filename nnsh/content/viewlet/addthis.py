# -*- coding: utf-8 -*-
from five import grok
from plone.app.layout.viewlets.interfaces import IAboveContentTitle
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from nnsh.content.epaper import IEpaper
from nnsh.content.album import IAlbum
from plone.app.contenttypes.interfaces import IDocument, IEvent, IFile, INewsItem
from plone import api


grok.templatedir('template')
"""
  viewlet named rule: Function_ViewletManager_ContextInterface
"""

class Addthis_IAboveContentTitle_INewsItem(grok.Viewlet):
    grok.viewletmanager(IAboveContentTitle)
    grok.context(INewsItem)
    grok.require('zope2.View')
    grok.template('addthis')

    def update(self):
        return


class Addthis_IAboveContentTitle_IFile(grok.Viewlet):
    grok.viewletmanager(IAboveContentTitle)
    grok.context(IFile)
    grok.require('zope2.View')
    grok.template('addthis')

    def update(self):
        return


class Addthis_IAboveContentTitle_IEvent(grok.Viewlet):
    grok.viewletmanager(IAboveContentTitle)
    grok.context(IEvent)
    grok.require('zope2.View')
    grok.template('addthis')

    def update(self):
        return


class Addthis_IAboveContentTitle_IDocument(grok.Viewlet):
    grok.viewletmanager(IAboveContentTitle)
    grok.context(IDocument)
    grok.require('zope2.View')
    grok.template('addthis')

    def update(self):
        return


class Addthis_IAboveContentTitle_IAlbum(grok.Viewlet):
    grok.viewletmanager(IAboveContentTitle)
    grok.context(IAlbum)
    grok.require('zope2.View')
    grok.template('addthis')

    def update(self):
        return


class Addthis_IAboveContentTitle_IEpaper(grok.Viewlet):
    grok.viewletmanager(IAboveContentTitle)
    grok.context(IEpaper)
    grok.require('zope2.View')
    grok.template('addthis')

    def update(self):
        return
