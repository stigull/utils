#! /usr/bin/env python
# -*- coding: utf8 -*-

import simplejson

from django.http import HttpResponse
from django.db.models import permalink
from django.template.loader import render_to_string
import django.forms as forms

class XMLResponse(HttpResponse):
    """ A HttpResponse with content type 'text/xml' """

    def __init__(self, template, context = {}, *args, **kwargs):
        xml = render_to_string(template, context)
        super(XMLResponse, self).__init__(content=xml, content_type='text/xml',
                                                mimetype = 'text/xml', *args, **kwargs)

class JSONResponse(HttpResponse):
    """ A HttpResponse with content type 'application/json' """

    def __init__(self, object, *args, **kwargs):
        """
        Usage:  response = JSONResponse(object, *args, **kwargs)
        Pre:    object is a dictionary
        Post:   response is a HttpResponse with object serialized as a JSON object
        """
        jsonobject = simplejson.dumps(object)
        super(JSONResponse, self).__init__(content=jsonobject, content_type='application/json',
                                                mimetype = 'application/json', *args, **kwargs)

class ModelField(forms.Field):

    def __init__(self, model, required = True, label =None , initial = None, widget = forms.HiddenInput, help_text = None):
        super(ModelField, self).__init__(required = required, label = label,
                                            initial = initial, widget = widget, help_text = help_text)
        self.model = model

    def clean(self, instance_id):
        return self.model.objects.get(pk = instance_id)


