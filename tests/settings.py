# -*- coding: utf-8
from __future__ import absolute_import, unicode_literals

import sys

import django

DEBUG = True
USE_TZ = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "g$(*_d#bd!9g=3ze9j^xyr@j+oko$j@__&*e6ni(x((ypk!5$c"

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}}

ROOT_URLCONF = "tests.urls"

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "disable_cache_headers",
]

SITE_ID = 1

if django.VERSION >= (1, 10):
    MIDDLEWARE = ("disable_cache_headers.middleware.DisableCacheControl",)
else:
    MIDDLEWARE_CLASSES = ("disable_cache_headers.middleware.DisableCacheControl",)
