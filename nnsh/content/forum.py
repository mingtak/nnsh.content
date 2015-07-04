from five import grok

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


class IForum(form.Schema, IImageScaleTraversable):
    """
    Forum content type, allow discussion.
    """
    text = RichText(
        title=_('Text'),
        required=True,
    )


class Forum(Container):
    grok.implements(IForum)


class SampleView(grok.View):
    """ sample view class """

    grok.context(IForum)
    grok.require('zope2.View')
    grok.name('view')

    # Add view methods here
