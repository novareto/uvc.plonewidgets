# -*- coding: utf-8 -*-

import Acquisition
from five import grok
from zope.interface import Interface
from Products.CMFPlone.resources import add_resource_on_request
from zeam.form.base.widgets import FieldWidget
from zeam.form.ztk.widgets.choice import ChoiceField
from zeam.form.ztk.interfaces import ICollectionField
from zeam.form.base.interfaces import IWidget
from zeam.form.ztk.widgets.collection import (
    ListField, ChoiceField, MultiChoiceWidgetExtractor,
    CollectionField, newCollectionWidgetFactory, MultiChoiceFieldWidget)


class PloneFieldWidget(FieldWidget, Acquisition.Explicit):
    grok.baseclass()

    @property
    def context(self):
        # Plone Zope 2 template need a context.
        return self.form.context


class PloneMultiSelectFieldWidget(MultiChoiceFieldWidget, PloneFieldWidget):
    grok.adapts(CollectionField, ChoiceField, Interface, Interface)
    grok.name('INOUT')

    def __init__(self, field, value_field, form, request):
        super(PloneMultiSelectFieldWidget, self).__init__(
            field, value_field, form, request)
        add_resource_on_request(request, 'inout')


grok.global_adapter(
    newCollectionWidgetFactory(mode='INOUT'),
    adapts=(ICollectionField, Interface, Interface),
    provides=IWidget,
    name='INOUT')


class PloneSelectizeFieldWidget(MultiChoiceFieldWidget, PloneFieldWidget):
    grok.adapts(CollectionField, ChoiceField, Interface, Interface)
    grok.name('selectize')

    def __init__(self, field, value_field, form, request):
        super(PloneSelectizeFieldWidget, self).__init__(
            field, value_field, form, request)
        add_resource_on_request(request, 'selectize')


grok.global_adapter(
    newCollectionWidgetFactory(mode='selectize'),
    adapts=(ICollectionField, Interface, Interface),
    provides=IWidget,
    name='selectize')


class Extractor(MultiChoiceWidgetExtractor):
    grok.adapts(ListField, ChoiceField, Interface, Interface)
