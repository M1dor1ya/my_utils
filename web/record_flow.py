# -*- coding: utf-8 -*-
# @Time    : 2018/6/21 15:09
# @Author  : Zcs
# @File    : record_flow.py

import os
import pymysql
import time
import logging

logging.basicConfig(filename='my_log.my_log',
                    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',
                    level=10)


def record_flow(name):
    config = {
                'host': '127.0.0.1',
                'port': 3306,
                'user': 'root',
                'password': 'root',
                'db': 'net',
                'charset': 'utf8',
                'cursorclass': pymysql.cursors.DictCursor
            }
    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    try:
        while True:
            fd = os.popen('ifconfig')
            result = fd.read()
            fd.close()
            block = result.split('\n\n')
            for i in block:
                if name in i:
                    lis = i.strip().split('\n')
                    for line in lis:
                        if 'RX packets' in line:
                            recieve = line.split('bytes')[1].strip().split('(')[0].strip()
                            recv_pack = line.split('bytes')[0].strip().split('RX packets')[1].strip()
                        if 'RX errors' in line:
                            recv_eror = line.split('dropped')[1].strip().split('overruns')[0].strip()
                            recv_drop = line.split('dropped')[0].strip().split('RX errors')[1].strip()
                        if 'TX packets' in line:
                            send = line.split('bytes')[1].strip().split('(')[0].strip()
                            send_pack = line.split('bytes')[0].strip().split('TX packets')[1].strip()
                        if 'TX errors' in line:
                            send_eror = line.split('dropped')[1].strip().split('overruns')[0].strip()
                            send_drop = line.split('dropped')[0].strip().split('TX errors')[1].strip()
            error_pack = send_eror + recv_eror
            drop_pack = recv_drop + send_drop
            recieve = round((float(recieve) / 1048576), 2)  # bytes 转换成MiB
            send = round((float(send) / 1048576), 2)
            fmt = '%Y-%m-%d %H:%M:%S'
            Date = time.strftime(fmt, time.localtime(time.time()))
            cursor.execute("INSERT INTO flow(recieve,send,recv_pack,send_pack,drop_pack,eror_pack,dtime) VALUE "
                           "(%s,%s,%s,%s,%s,%s,%s)", (recieve, send, recv_pack, send_pack, drop_pack, error_pack, Date))
            conn.commit()
            time.sleep(1)
    except Exception as e:
        cursor.close()
        conn.close()
        logging.debug(e)

if __name__ == '__main__':
    record_flow('ens33')


