#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: PythonPie <contact@pythonpie.com>
# Copyright (c) 2015 - THSTACK <contact@thstack.com>

import simplejson as json

from django.http import HttpResponse
from ashinamo.lib.class_data import \
    CpuClassData, NetClassData, IoClassData, MemClassData


def getcpu(request):
    cpudata = CpuClassData.CpuData()
    result = json.dumps(cpudata.compute_data())
    return HttpResponse(result)


def getmem(request):
    memdata = MemClassData.MemData()
    result = json.dumps(memdata.get_data())
    return HttpResponse(result)


def getnet(request):
    netdata = NetClassData.NetData(['eth0'])
    result = json.dumps(netdata.compute_data())
    return HttpResponse(result)


def getio(request):
    iodata = IoClassData.IoData(['sda'])
    result = json.dumps(iodata.compute_data())
    return HttpResponse(result)
