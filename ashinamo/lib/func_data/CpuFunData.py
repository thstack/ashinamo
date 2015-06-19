#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: PythonPie <contact@pythonpie.com>
# Copyright (c) 2015 - THSTACK <contact@thstack.com>

""" 获取cpu数据， 从 /proc/stat 文件 """
""" @Site: www.pythonpie.com
    @Date: 2015-05-23
    @Version: v1.2
    @Note:
        需要一个缓冲文件 /tmp/proc_stat 来保存上一次的数据。本次计算的时候，
        (用本次数据total和上次total做差 - 本次数据idle和上次idle做差/
         本次数据total和上次total做差)*100,当然两次有着足够短的时间间隔。

        /proc/stat 中相关数据解释：

            [root@ashinamo sbin]# cat /proc/stat |grep cpu\
            cpu  182835 0 64263 2012611 14849 244 20165 0 0

            单位(jiffies)：(jiffies是内核中的一个全局变量，
                            用来记录自系统启动一来产生的节拍数，在linux中，
                            一个节拍大致可理解为操作系统进程调度的最小时间片，
                            不同linux内核可能值有不同，通常在1ms到10ms之间)

            第一个域：user (182835)    从系统启动开始累计到当前时刻，
                                       处于用户态的运行时间，
                                       不包含 nice值为负进程。

            第二个域：nice (0)         从系统启动开始累计到当前时刻，
                                       nice值为负的进程所占用的CPU时间

            第三个域：system (64263)   从系统启动开始累计到当前时刻，
                                       处于核心态的运行时间

            第四个域：idle (2012611)   从系统启动开始累计到当前时刻，
                                       除IO等待时间以外的其它等待时间

            第五个域：iowait (14849)   从系统启动开始累计到当前时刻，
                                       IO等待时间(since 2.5.41)

            第六个域：irq (244)        从系统启动开始累计到当前时刻，
                                       硬中断时间(since 2.6.0-test4)

            第七个域：softirq (20165)  从系统启动开始累计到当前时刻，
                                       软中断时间(since 2.6.0-test4)

            第八个域：stealstolen(0)   which is the time spent in other
                                       operating systems when running in a 
                                       virtualized environment(since 2.6.11)

            第九个域：guest(0)         which is the time spent running a
                                       virtual  CPU  for guest operating 
                                       systems under the control of the
                                       Linux kernel(since 2.6.24)
            
"""

import simplejson as json
import time


def get_ProcStat():
    """获取cpu监控数据

    @Return: (status, msgs, results)
            status = INT, # Function execution status,
                            0 is normal, other is failure.
            msgs = STRING, # If status equal to 0, msgs is '', otherwise
                             will be filled with error message.
            results = DICT {
                "cpuuse": '34', #百分比
            }
    """

    status = 0
    msgs = ''
    results = ''
    now_data = {}  # 当前 /proc/stat 的值
    last_data = {}  # 上一次 /proc/stat 的值，时间跨度足够短

    # 获取当前数据
    try:
        fp_object = file('/proc/stat')
        raw_data = fp_object.readlines()
        fp_object.close()
    except:
        return (-1, 'system file not exist', '')

    results = raw_data[0].strip()
    cpu_all = results.split()
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
    diff_total = int(now_data['total']) - int(last_data['total'])
    diff_idle = (int(now_data['idle']) - int(last_data['idle']))
    if diff_total > 0:
        real_data = 100 * (float(diff_total-diff_idle) / diff_total)
        results['cpuuse'] = int(round(real_data))
    else:
        # 第一次加载的时候，历史数据为空，无法计算， 所有初始化为0
        results['cpuuse'] = 0
    return (status, msgs, results)

if __name__ == "__main__":
    while True:
        print get_ProcStat()
        time.sleep(1)
