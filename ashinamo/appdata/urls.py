#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: PythonPie <contact@pythonpie.com>
# Copyright (c) 2015 - THSTACK <contact@thstack.com>

from django.conf.urls import include, url
from django.contrib import admin

from ashinamo.appdata import views


urlpatterns = [
    url(r'^cpu/$', views.getcpu, name='datacpu'),
    url(r'^mem/$', views.getmem, name='datamem'),
    url(r'^io/$',  views.getio, name="dataio"),
    url(r'^net/$', views.getnet, name="datanet"),
]
