#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: PythonPie <contact@pythonpie.com>
# Copyright (c) 2015 - THSTACK <contact@thstack.com>

""" 获取内存数据, 从 /proc/meminfo 文件 """
""" @Site: www.pythonpie.com
    @Date: 2015-05-23
    @Version: v1.2
    @Note:
        /proc/meminfo 中所需数据的解释：
            [root@ashinamo ~]# head -n 4 /proc/meminfo
            MemTotal:        1017812 kB
            MemFree:           67768 kB
            Buffers:           10280 kB
            Cached:           283708 kB
            MemTotal:总内存大小
            MemFree:空闲内存大小
            Buffers和Cached：磁盘缓存的大小
            Buffers和Cached的区别：
            buffers是指用来给块设备做的缓冲大小，他只记录文件系统的metadata以及
            tracking in-flight pages.
            cached是用来给文件做缓冲。

"""


def get_ProcMeminfo():
    """ 获取内存数据
    @Return: (status, msgs, results)
        status = INT, # Fuction execution status, 0 is normal,
                        other is failure.
        msgs = STRING, # If status equal to 0, msgs is '',
                         otherwise will be filled with error message.
        results = DICT {
            'memtotal': 1017812, #单位都是 KB
            'memused': 283708
        }
    """

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
        results['memused'] = int(now_data['MemTotal:']) - \
            int(now_data['MemFree:'])
        results['buffers'] = int(now_data['Buffers:'])
        results['cached'] = int(now_data['Cached:'])
        return (status, msgs, results)
    except Exception, e:
        return (-1, 'data error!' + e, '')

if __name__ == "__main__":
    print get_ProcMeminfo()
