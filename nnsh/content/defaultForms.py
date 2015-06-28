from plone.dexterity.browser.add import DefaultAddForm, DefaultAddView
from plone.dexterity.browser.edit import DefaultEditForm, DefaultEditView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from z3c.form.interfaces import HIDDEN_MODE
#from plone.z3cform.fieldsets.utils import add, remove

#from zope.component import getMultiAdapter
#from plone import api

#from zope.interface import alsoProvides, Interface
#from plone.directives import dexterity, form

from nnsh.content import MessageFactory as _


class AddForm(DefaultAddForm):
    template = ViewPageTemplateFile('template/addForm.pt')

    def update(self):
        DefaultAddForm.update(self)

    def updateWidgets(self):
        super(AddForm, self).updateWidgets()

        # override exclude_from_nav's default value
        for group in self.groups:
            if group.label == u'Settings':
                group.fields['IExcludeFromNavigation.exclude_from_nav'].field.default = True
                break
        return




class AddView(DefaultAddView):
    form = AddForm


class EditForm(DefaultEditForm):
    template = ViewPageTemplateFile('template/editForm.pt')


class EditView(DefaultEditView):
    form = EditForm
