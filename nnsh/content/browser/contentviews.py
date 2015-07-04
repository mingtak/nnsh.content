# -*- coding: utf-8 -*-
from five import grok
from plone import api
from zope.interface import Interface
from nnsh.content.epaper import IEpaper
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from email.mime.text import MIMEText
from Products.CMFDefault.utils import checkEmailAddress
from Products.CMFDefault.exceptions import EmailAddressInvalid
from Products.CMFPlone.utils import safe_unicode
import time
from plone.app.contenttypes.interfaces import IDocument, INewsItem, IEvent, IFolder
from nnsh.content import MessageFactory as _

grok.templatedir('template')


class DocumentView(grok.View):
    grok.context(IDocument)
    grok.require('zope2.View')
    grok.name('view')
    grok.template('document_view')

    def update(self):
        return


class NewsItemView(DocumentView):
    grok.context(INewsItem)
    grok.template('newsitem_view')


class EventView(DocumentView):
    grok.context(IEvent)
    grok.template('event_view')


class FolderView(DocumentView):
    grok.context(IFolder)
    grok.template('folder_view')
