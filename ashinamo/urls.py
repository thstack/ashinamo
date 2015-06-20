#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: PythonPie <contact@pythonpie.com>
# Copyright (c) 2015 - THSTACK <contact@thstack.com>

from django.conf.urls import include, url
from django.contrib import admin

from ashinamo.apphome import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.index, name="page_index"),
    url(r'^cpu/$', views.cpu, name="page_cpu"),
    url(r'^mem/$', views.mem, name="page_mem"),
    url(r'^io/$', views.io, name="page_io"),
    url(r'^net/$', views.net, name="page_net"),

    url(r'^data/', include('ashinamo.appdata.urls')),
]
