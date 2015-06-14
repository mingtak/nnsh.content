from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper

from plone.z3cform import layout
from z3c.form import form
from zope import schema
from plone.directives import form as Form

# from . import MessageFactory as _
from nnsh.content import MessageFactory as _

class IEpaper(Form.Schema):

    mailList = schema.Text(
        title=_(u"Registry to receive e-paper's mail list"),
        required=False,
    )

    Form.mode(epaperLog="display")
    epaperLog = schema.Text(
        title=_(u"Epaper history log"),
        required=False,
    )


class EpaperControlPanelForm(RegistryEditForm):
    form.extends(RegistryEditForm)
    schema = IEpaper

EpaperControlPanelView = layout.wrap_form(EpaperControlPanelForm, ControlPanelFormWrapper)
EpaperControlPanelView.label = _(u"Epaper control papel")
