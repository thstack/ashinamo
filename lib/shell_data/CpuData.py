#!/usr/bin/env python
#-*- coding:utf-8 -*-

import simplejson as json
import time

while True:
    now_data = {} # 当前 /proc/stat 的值
    last_data = {} # 上一次 /proc/stat 的值，时间跨度足够短
    
    # 获取当前数据
    raw_data = file('/proc/stat').readlines()
    results = raw_data[0].strip()
    cpu_all =results.split()
    cpu_all.pop(0)
    cpu_data = [int(i) for i in cpu_all]
    now_data['idle'] = cpu_data[3]
    now_data['total'] = sum(cpu_data)
    
    # 获取历史数据
    try:
        raw_data = file('/tmp/proc_stat').read()
        last_data = json.loads("%s" % raw_data.strip())
    except:
        last_data = now_data
    
    # 保存当前数据到历史数据表中
    fp = file('/tmp/proc_stat', 'w')
    fp.write(json.dumps(now_data))
    fp.close()
    
    # 处理两个数据，得到要计算的值
    results = {}
    diff_total = int(now_data['total'])-int(last_data['total'])
    diff_idle=(int(now_data['idle'])-int(last_data['idle']))
    if diff_total > 0:
        results['cpuuse']=int(round(100*(float(diff_total-diff_idle)/diff_total)))
    else:
        # 第一次加载的时候，历史数据为空，无法计算， 所有初始化为0
        results['cpuuse']=0 
    print results
    time.sleep(1)
