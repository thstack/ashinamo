#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: PythonPie <contact@pythonpie.com>
# Copyright (c) 2015 - THSTACK <contact@thstack.com>

from django.shortcuts import render_to_response


def index(request):
    context = {
    }
    return render_to_response("index.html", context)


def cpu(request):
    context = {
    }
    return render_to_response("cpu.html", context)


def mem(request):
    context = {
    }
    return render_to_response("mem.html", context)


def io(request):
    context = {
    }
    return render_to_response("io.html", context)


def net(request):
    context = {
    }
    return render_to_response("net.html", context)
