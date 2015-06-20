#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: PythonPie <contact@pythonpie.com>
# Copyright (c) 2015 - THSTACK <contact@thstack.com>

import simplejson as json

from django.http import HttpResponse
from ashinamo.lib.class_based import cpu, net, io, mem


def getcpu(request):
    cpudata = cpu.CpuData()
    result = json.dumps(cpudata.compute_data())
    return HttpResponse(result)


def getmem(request):
    memdata = mem.MemData()
    result = json.dumps(memdata.get_data())
    return HttpResponse(result)


def getnet(request):
    netdata = net.NetData(['eth0'])
    result = json.dumps(netdata.compute_data())
    return HttpResponse(result)


def getio(request):
    iodata = io.IoData(['sda'])
    result = json.dumps(iodata.compute_data())
    return HttpResponse(result)
