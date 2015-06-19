#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: PythonPie <contact@pythonpie.com>
# Copyright (c) 2015 - THSTACK <contact@thstack.com>

now_data = {}
status = 0
msgs = ""
results = ""

try:
    fp_o = file('/proc/meminfo')
    raw_data = fp_o.read()
    fp_o.close()
    temps = raw_data.strip().split('\n')
    for temp in temps:
        tmp = temp.split()
        now_data[tmp[0]] = tmp[1]
    results = {}
    results['memtotal'] = int(now_data['MemTotal:'])
    results['memused'] = int(now_data['MemTotal:']) - int(now_data['MemFree:'])
    results['buffers'] = int(now_data['Buffers:'])
    results['cached'] = int(now_data['Cached:'])
    print 0, '', results
except Exception, e:
    print 1, e, ''
