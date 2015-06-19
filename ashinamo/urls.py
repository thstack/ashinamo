#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: PythonPie <contact@pythonpie.com>
# Copyright (c) 2015 - THSTACK <contact@thstack.com>

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'ashinamo.apphome.views.index', name="index"),
    url(r'^cpu/$', 'ashinamo.apphome.views.cpu', name="cpu"),
    url(r'^mem/$', 'ashinamo.apphome.views.mem', name="mem"),
    url(r'^io/$', 'ashinamo.apphome.views.io', name="io"),
    url(r'^net/$', 'ashinamo.apphome.views.net', name="net"),
    url(r'^data/cpu/$', 'ashinamo.appdata.views.getcpu', name='datacpu'),
    url(r'^data/mem/$', 'ashinamo.appdata.views.getmem', name='datamem'),
    url(r'^data/io/$', 'ashinamo.appdata.views.getio', name="dataio"),
    url(r'^data/net/$', 'ashinamo.appdata.views.getnet', name="datanet"),
]
