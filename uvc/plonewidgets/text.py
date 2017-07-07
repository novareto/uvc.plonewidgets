# -*- coding: utf-8 -*-

from five import grok
from zope.interface import Interface
from zeam.form.ztk.widgets.text import TextField, TextareaWidget 


class TinyMCEWidget(TextareaWidget):
    grok.name('tinymce')
    grok.adapts(TextField, Interface, Interface)
    defaultHtmlClass = ['field', 'field-text', 'pat-tinymce', 'mce_editable']
    defaultHtmlAttributes = set(['maxlength', 'placeholder', 'required',
                                 'rows', 'warp', 'readonly', 'cols', 'style'])
