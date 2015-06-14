from five import grok

from plone.indexer import indexer
from z3c.form import group, field
from zope import schema
from zope.interface import invariant, Invalid
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


class IAdvertising(form.Schema, IImageScaleTraversable):
    """
    Advertising content type
    """

    image = NamedBlobImage(
        title=_(u"Image"),
        required=True,
    )

    adLink = schema.URI(
        title=_(u"Remote URL"),
        required=False,
    )

    isBanner = schema.Bool(
        title=_(u"Is Banner ?"),
        description=_(u"If want to show at Banner, please checked it, else show at sidebar"),
        default=False,
    )

class Advertising(Container):
    grok.implements(IAdvertising)


class SampleView(grok.View):
    """ sample view class """

    grok.context(IAdvertising)
    grok.require('zope2.View')


@indexer(IAdvertising)
def adLink_indexer(obj):
    return obj.adLink
grok.global_adapter(adLink_indexer, name='adLink')

@indexer(IAdvertising)
def isBanner_indexer(obj):
    return obj.isBanner
grok.global_adapter(isBanner_indexer, name='isBanner')
