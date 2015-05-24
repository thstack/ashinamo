"""ashinamo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
import os
from settings import BASE_DIR 

urlpatterns = [
    url(r'^statics/(?P<path>.*)$', 'django.views.static.serve',{"document_root":os.path.join(BASE_DIR, "./static").replace("\\","/")}),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'apphome.views.index', name="index"),
    url(r'^cpu/$', 'apphome.views.cpu', name="cpu"),
    url(r'^mem/$', 'apphome.views.mem', name="mem"),
    url(r'^io/$', 'apphome.views.io', name="io"),
    url(r'^net/$', 'apphome.views.net', name="net"),


    url(r'^data/cpu/$', 'appdata.views.getcpu', name='datacpu'),
    url(r'^data/mem/$', 'appdata.views.getmem', name='datamem'),
    url(r'^data/io/$', 'appdata.views.getio', name="dataio"),
    url(r'^data/net/$', 'appdata.views.getnet', name="datanet"),
]
