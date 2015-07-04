from five import grok

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


class IEpaper(form.Schema, IImageScaleTraversable):
    """
    Epaper content type
    """

    text = RichText(
        title=_(u"Epaper head"),
        description=_(u"Epaper head will show in deliver mail content head."),
        required=True,
    )

    selectItems = RelationList(
        title=_(u"Select epaper related contents."),
        value_type=RelationChoice(
            source=ObjPathSourceBinder(),
        ),
        required=True,
    )


class Epaper(Container):
    grok.implements(IEpaper)


class SampleView(grok.View):
    """ sample view class """

    grok.context(IEpaper)
    grok.require('zope2.View')
    grok.name('view')
