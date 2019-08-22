=============================
Django disable cache headers
=============================

Middleware that disables caching headers during development in Django.

In production you will typically a CDN or browser cache to speed up subsequent
reads of your pages. This ensures reads don't need to hit your DB as often.

.. code-block:: python

    from django.views.decorators.cache import cache_control

    @method_decorator(cache_control(public=True, max_age=60 * 5)), name="dispatch")
    def my_view(request):
        ...


However this is annoying during development as you always want to serve fresh
pages and static files on page refresh. Using this middleware in development
strips out the cache headers and prevents the browser (or dev cache) from
caching your content.

Quickstart
----------

Install Django disable cache headers::

    pip install django-disable-cache-headers

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'disable_cache_headers.apps.DisableCacheHeadersConfig',
        ...
    )

Add the middleware in your development settings, e.g in config/settings/local.py.

.. code-block:: python

    from .base import *
    MIDDLEWARE += ["disable_cache_headers.middleware.DisableCacheControl"]

Running Tests
-------------

.. code-block:: bash

    python -m venv venv
    source ./venv/bin/activate
    pip install -r requirements_test.txt
    pytest

