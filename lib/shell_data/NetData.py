#!/usr/bin/env python
#-*- coding:utf-8 -*-
import re
import time
import simplejson as json

devices = ['eth0', 'lo']
while True:
    now_data = {} # 当前 /proc/net/dev 的值
    last_data = {} # 上一次 /proc/net/dev 的值， 时间跨度有调用程序决定

    # 获取当前数据
    results = file('/proc/net/dev').read()
    now_data['timestamp'] = time.time()
    for device in devices:
        pat = device + ":.*"
        devicedata = re.search(pat, results).group()
        tmp_main = devicedata.split(":")
        tmp=tmp_main[1].split()
        now_data[tmp_main[0].strip()] = {
            'receive_bytes': tmp[0],
            'receive_packets': tmp[1],
            'receive_errs': tmp[2],
            'receive_drop': tmp[3],
            'receive_fifo': tmp[4],
            'receive_frame': tmp[5],
            'receive_compressed': tmp[6],
            'receive_multicast': tmp[7],
            'transmit_bytes': tmp[8],
            'transmit_packets': tmp[9],
            'transmit_errs': tmp[10],
            'transmit_drop': tmp[11],
            'transmit_fifo': tmp[12],
            'transmit_colls': tmp[13],
            'transmit_carrier': tmp[14],
            'transmit_compressed': tmp[15]
        }
    # 获取历史数据
    try:
        results = file('/tmp/proc_net_dev').read()
        last_data = json.loads("%s" % results.strip())
    except:
        last_data = now_data

    # 写当前数据到文件
    fp = file('/tmp/proc_net_dev', 'w')
    fp.write(json.dumps(now_data))
    fp.close()

    # 处理两个数据，得到要计算的值
    results = {}
    timecut = float(now_data['timestamp']) - float(last_data['timestamp'])
    if timecut > 0:
        for key in devices:
            receive = (int(now_data[key]['receive_bytes']) - int(last_data[key]['receive_bytes']))/float(1024)/timecut 
            transmit = (int(now_data[key]['transmit_bytes']) - int(last_data[key]['transmit_bytes']))/float(1024)/timecut 
            results[key] = {'receive':int(receive), 'transmit':int(transmit)}
    else:
        # 第一次加载的时候，历史数据为空，无法计算，所以初始化为0
        for key in devices:
            results[key] = {'receive':0, 'transmit':0}
    print results
    time.sleep(1)
