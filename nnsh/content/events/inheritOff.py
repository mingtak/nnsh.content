from five import grok
from plone import api
from Products.CMFPlone.utils import safe_unicode

from zope.app.container.interfaces import IObjectAddedEvent

#from plone.app.contenttypes.interfaces import IFolder, IImage, IDocument, IEvent, INewsItem, ILink, IFile
from nnsh.content.forum import IForum
from Acquisition import aq_base


@grok.subscribe(IForum, IObjectAddedEvent)
def moveContentToTop(obj, event):
    """
    Turning off "Inherit permissions from higher levels"
    """
    aq_base(obj).__ac_local_roles_block__ = True
