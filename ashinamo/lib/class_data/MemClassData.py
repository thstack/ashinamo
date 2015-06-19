#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: PythonPie <contact@pythonpie.com>
# Copyright (c) 2015 - THSTACK <contact@thstack.com>

""" 获取内存数据, 从 /proc/meminfo 文件 """
""" @Site: www.pythonpie.com
    @Date: 2015-06-05
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
            buffers是指用来给块设备做的缓冲大小，他只记录文件系统的metadata以及 tracking in-flight pages.
            cached是用来给文件做缓冲。

"""


class MemData:
    def __init__(self):
        self.now_data = {}

    def get_data(self):
        """获取系统内存数据
            @Return: (status, msgs, results)
                status = INT, # Function execution status,
                                0 is normal, other is failure.
                msgs = STRING, # If status equal to 0, msgs is '',
                                 otherwise will be filled with error message.
                result = DICT {  # 单位均为KB
                    'cached': 215008,
                    'memused': 747532,
                    'memtotal': 1011928,
                    'buffers': 201784
                }
        """
        status = 0
        msgs = ""
        results = ""
        try:
            fp = file('/proc/meminfo')
            raw_data = fp.read()
            fp.close()
            temps = raw_data.strip().split('\n')
            for temp in temps:
                tmp = temp.split()
                self.now_data[tmp[0]] = tmp[1]
            results = {}
            results['memtotal'] = int(self.now_data['MemTotal:'])
            results['memused'] = int(self.now_data['MemTotal:']) - \
                int(self.now_data['MemFree:'])
            results['buffers'] = int(self.now_data['Buffers:'])
            results['cached'] = int(self.now_data['Cached:'])
            return (status, msgs, results)
        except Exception, e:
            return (-1, e + 'data error!', '')

if __name__ == "__main__":
    meminfo = MemData()
    print meminfo.get_data()
