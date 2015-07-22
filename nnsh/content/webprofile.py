from five import grok
from plone.indexer import indexer

from z3c.form import group, field
from zope import schema
from zope.interface import invariant, Invalid, Interface
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from plone.dexterity.content import Container
from plone.directives import dexterity, form
from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone.namedfile.interfaces import IImageScaleTraversable

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder


from nnsh.content import MessageFactory as _


# Interface class; used to define content-type schema.
CONTENT_TYPES = ['Page', 'Event', 'News Item',
    'Link', 'Image', 'SubFolder', 'SurveryForm',
    'Advertising', 'Album', 'Forum', 'Epaper']

@grok.provider(IContextSourceBinder)
def availableBlock(context):
    return ObjPathSourceBinder(Type=["Page", "Folder", "Collection"])(context)

@grok.provider(IContextSourceBinder)
def availableImage(context):
    return ObjPathSourceBinder(Type=["Image"])(context)


class IWebProfile(form.Schema, IImageScaleTraversable):
    """
    Website profile
    """
    slides = RelationList(
        title=_(u'Slides'),
        description=_(u'can choice 4 images'),
        min_length = 1,
        max_length = 4,
        value_type=RelationChoice(title=_(u"Related"),
            source=availableImage),
        required=True,
    )

    blocks = RelationList(
        title=_(u'Block'),
        description=_(u'Please select choice 4 blocks'),
        min_length = 4,
        max_length = 4,
        value_type=RelationChoice(title=_(u"Related"),
            source=availableBlock),
        required=True,
    )

class WebProfile(Container):
    grok.implements(IWebProfile)


class SampleView(grok.View):
    """ sample view class """

    grok.context(IWebProfile)
    grok.require('zope2.View')
    grok.name('view')


@indexer(Interface)
def parentTitle_indexer(obj):
    if obj.Type() not in CONTENT_TYPES:
        return None

    parentNode = obj.getParentNode()
    while True:
        if parentNode.Type() in ['Folder', 'Plone Site']:
            break
        parentNode = parentNode.getParentNode()
    return parentNode.Title()
grok.global_adapter(parentTitle_indexer, name='parentTitle')
