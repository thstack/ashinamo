#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: PythonPie <contact@pythonpie.com>
# Copyright (c) 2015 - THSTACK <contact@thstack.com>

""" pymonitor client module: 获取网络数据，从/proc/net/dev 文件 """
""" @Site: www.pythonpie.com
    @Date: 2015-06-05
    @Version: v1.2
    @Note:
        需要一个缓存文件 /tmp/proc_net_dev 来保存上一次的数据
        （是一个带时间戳的数据）
        本次计算的时候，用本次数据和上一次数据做减法的值,与两个时间戳的减法的
        值做除法求得最终结果(kb/s)

        /proc/net/dev 中数据的解释：
            [root@ashinamo ~]# cat /proc/net/dev
            Inter-|   Receive                                                |  Transmit
             face |bytes    packets errs drop fifo frame compressed multicast|bytes    packets errs drop fifo colls carrier compressed
                lo:664087762 3663780    0    0    0     0          0         0 664087762 3663780    0    0    0     0       0          0
              eth0:  651822    6311    0    0    0     0          0         0   553421    6076    0    0    0     0       0          0
              eth1:  663326    6060    0    0    0     0          0         0   962066    4571    0    0    0     0       0          0
            interface:网卡名
            Receive(接受):
                第一个域(bytes)：字节数
                第二个域(packets)：包数
                第三个域(errs)：错误包数
                第四个域(drop)：丢弃包数
                第五个域(fifo)：(First in first out)包数/FIFO缓存错误数
                第六个域(frame)：帧数
                第七个域(compressed)：压缩(compressed)包数
                第八个域(multicast)：多播（multicast, 比如广播包或者组播包)包数
            Transmit(发送):
                第一个域(bytes)：字节数
                第二个域(packets)：包数
                第三个域(errs)：错误包数
                第四个域(drop)：丢弃包数
                第五个域(fifo)：(First in first out)包数/FIFO缓存错误数
                第六个域(colls): 接口检测到的冲突数
                第七个域(carrier): 连接介质出现故障次数，如：网线接触不良
                第八个域(compressed)：压缩(compressed)包数

"""

import re
import time
import simplejson as json


class NetData:
    def __init__(self, devices):
        self.now_data = {}
        self.last_data = {}
        self.devices = devices

    def get_now_data(self):
        """获取网络当前系统数据

        @Return: (status, msgs, results)
            status = INT, # Function execution status,
                            0 is normal, other is failure.
            msgs = STRING, # If status equal to 0, msgs is '',
                             otherwise will be filled with error message.
            result = DICT {
                'timestamp': 1432342587.661646, #获取数据时间
                'eth0': {
                    # 接收
                    'receive_bytes': '3196699', # 字节数
                    'receive_packets': '34412', # 包数
                    'receive_errs': '0', # 错误包数
                    'receive_drop': '0', # 丢弃包数
                    'receive_fifo': '0', # (First in first out)包数/
                    FIFO缓存错误数
                    'receive_frame': '0', # 帧数
                    'receive_compressed': '0', # 压缩包数
                    'receive_multicast': '0',  # 多播（multicast,
                    比如广播包或者组播包)包数

                    # 发送
                    'transmit_bytes': '3635965', # 字节数
                    'transmit_packets': '18783', # 包数
                    'transmit_errs': '0', # 错误包数
                    'transmit_drop': '0', # 丢弃包数
                    'transmit_fifo': '0', # (First in first out)包数/
                    FIFO缓存错误数
                    'transmit_colls': '0', # 接口检测到的冲突数
                    'transmit_carrier': '0' # 连接介质出现故障次数,
                    如：网线接触不良
                    'transmit_compressed': '0', # 压缩(compressed)包数
                }

            }
        """
        try:
            results = file('/proc/net/dev').read()
        except:
            return (-1, 'system file not exist', '')

        self.now_data['timestamp'] = time.time()
        if not self.devices or type(self.devices) != list:
            return (-2, 'devices can not be none and must be a list', '')
        for device in self.devices:
            pat = device + ":.*"
            try:
                devicedata = re.search(pat, results).group()
            except:
                return (-2, device+' not exist', '')

            tmp_main = devicedata.split(":")
            tmp = tmp_main[1].split()
            self.now_data[tmp_main[0].strip()] = {
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
            return (0, '', self.now_data)

    def get_last_data(self):
        """获取上一时刻网络系统数据

        @Return: (status, msgs, results)
            status = INT, # Function execution status,
                            0 is normal, other is failure.
            msgs = STRING, # If status equal to 0, msgs is '',
                             otherwise will be filled with error message.
            result = DICT {
                'timestamp': 1432342587.661646, #获取数据时间
                'eth0': {
                    # 接收
                    'receive_bytes': '3196699', # 字节数
                    'receive_packets': '34412', # 包数
                    'receive_errs': '0', # 错误包数
                    'receive_drop': '0', # 丢弃包数
                    'receive_fifo': '0', # (First in first out)包数/
                    FIFO缓存错误数
                    'receive_frame': '0', # 帧数
                    'receive_compressed': '0', # 压缩包数
                    'receive_multicast': '0',  # 多播（multicast,
                    比如广播包或者组播包)包数

                    # 发送
                    'transmit_bytes': '3635965', # 字节数
                    'transmit_packets': '18783', # 包数
                    'transmit_errs': '0', # 错误包数
                    'transmit_drop': '0', # 丢弃包数
                    'transmit_fifo': '0', # (First in first out)包数/
                    FIFO缓存错误数
                    'transmit_colls': '0', # 接口检测到的冲突数
                    'transmit_carrier': '0' # 连接介质出现故障次数，
                    如：网线接触不良
                    'transmit_compressed': '0', # 压缩(compressed)包数
                }

            }
        """
        # 获取历史数据
        try:
            results = file('/tmp/proc_net_dev').read()
            self.last_data = json.loads("%s" % results.strip())
        except:
            self.last_data = self.now_data

        # 写当前数据到文件
        fp = file('/tmp/proc_net_dev', 'w')
        fp.write(json.dumps(self.now_data))
        fp.close()
        return (0, '', self.last_data)

    def compute_data(self):
        """由两时刻数据，计算网络传输速率
        @Return: (status, msgs, results)
                status = INT, # Function execution status,
                                0 is normal, other is failure.
                msgs = STRING, # If status equal to 0, msgs is '',
                                 otherwise will be filled with error message.
                results = DICT {
                    'eth0': {  #网卡eth0的传输速率
                        'receive': 0, #单位无特殊说明都是 KB/s
                        'transmit': 0
                    }
                }
        """
        now_status, now_msgs, now_data = self.get_now_data()
        last_status, last_msgs, last_data = self.get_last_data()
        if now_status == last_status == 0:
            # 处理两个数据，得到要计算的值
            results = {}
            timecut = \
                float(now_data['timestamp']) - float(last_data['timestamp'])
            if timecut > 0:
                for key in self.devices:
                    now_data_rece = int(now_data[key]['receive_bytes'])
                    last_data_rece = int(last_data[key]['receive_bytes'])
                    now_data_trans = int(now_data[key]['transmit_bytes'])
                    last_data_trans = int(last_data[key]['transmit_bytes'])
                    receive = \
                        (now_data_rece - last_data_rece) / float(1024)/timecut
                    transmit = \
                        (now_data_trans - last_data_trans) / float(1024)/timecut
                    results[key] = \
                        {'receive': int(receive), 'transmit': int(transmit)}
            else:
                # 第一次加载的时候，历史数据为空，无法计算，所以初始化为0
                for key in self.devices:
                    results[key] = {'receive': 0, 'transmit': 0}
            return (0, '', results)
        elif now_status != 0:
            return (now_status, now_msgs, now_data)
        else:
            return (last_status, last_msgs, last_data)

    def run(self):
        """持续获取io数据
        @Return: None
        """
        while True:
            result = self.compute_data()
            if result[0] == 0:
                print result
            else:
                print result
                break
            time.sleep(1)

if __name__ == "__main__":
    netdata = NetData(['eth0'])
    netdata.run()
