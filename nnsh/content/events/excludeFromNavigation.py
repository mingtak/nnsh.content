from five import grok
from plone import api
from Products.CMFPlone.utils import safe_unicode

from zope.app.container.interfaces import IObjectAddedEvent

from plone.app.contenttypes.interfaces import IFolder, IImage, IDocument, IEvent, INewsItem, ILink, IFile
from nnsh.content.forum import IForum
from nnsh.content.epaper import IEpaper
from Acquisition import aq_base

"""
@grok.subscribe(IDocument, IObjectAddedEvent)
@grok.subscribe(IImage, IObjectAddedEvent)
@grok.subscribe(IEvent, IObjectAddedEvent)
@grok.subscribe(INewsItem, IObjectAddedEvent)
@grok.subscribe(ILink, IObjectAddedEvent)
@grok.subscribe(IFile, IObjectAddedEvent)
@grok.subscribe(IEpaper, IObjectAddedEvent)
@grok.subscribe(IForum, IObjectAddedEvent)
"""
def moveContentToTop(obj, event):
    """
    Turning off "Inherit permissions from higher levels"
    """
    obj.exclude_from_nav = True
    obj.reindexObject(idxs=['exclude_from_nav'])
