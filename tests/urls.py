# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.http import HttpResponse
from django.urls import path


def view(_request):
    return HttpResponse()


urlpatterns = [path("", view)]
