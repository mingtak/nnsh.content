from five import grok
from plone import api
from Products.CMFPlone.utils import safe_unicode

#from Products.PlonePAS.events import UserInitialLoginInEvent, UserLoggedInEvent
#from zope.lifecycleevent.interfaces import IObjectCreatedEvent, IObjectAddedEvent, IObjectModifiedEvent
#from zope.lifecycleevent import ObjectModifiedEvent
#from Products.DCWorkflow.interfaces import IBeforeTransitionEvent, IAfterTransitionEvent
from zope.app.container.interfaces import IObjectAddedEvent
#from zope import component
#from zope.app.intid.interfaces import IIntIds
#from z3c.relationfield.relation import RelationValue
#from zope.event import notify

from plone.app.contenttypes.interfaces import IFolder, IImage, IDocument, IEvent, INewsItem, ILink, IFile
from nnsh.content.album import IAlbum


@grok.subscribe(IDocument, IObjectAddedEvent)
@grok.subscribe(IImage, IObjectAddedEvent)
@grok.subscribe(IEvent, IObjectAddedEvent)
@grok.subscribe(INewsItem, IObjectAddedEvent)
@grok.subscribe(ILink, IObjectAddedEvent)
@grok.subscribe(IFile, IObjectAddedEvent)
@grok.subscribe(IAlbum, IObjectAddedEvent)
def moveContentToTop(obj, event):
    """
    Moves Items to the top of its folder
    """
    folder = obj.getParentNode()
    if folder != None:
        folder.moveObjectsToTop(obj.id)

