# -*- coding: utf-8 -*-
# @Time    : 2018/9/14 17:27
# @Author  : Zcs
# @File    : test.py
import pymysql
import threading
from time import ctime


def update_func():
    config = {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': 'root',
        'db': 'test',
        'charset': 'utf8',
        'cursorclass': pymysql.cursors.DictCursor
    }
    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    for i in range(10):
        cursor.execute('UPDATE test SET times=times+1 WHERE test=1')
        conn.commit()
        print('Time:%s Thread:%s' % (ctime(), threading.current_thread().name))
    cursor.close()
    conn.close()

threads = []
t1 = threading.Thread(target=update_func)  # 生成一个线程实例
t2 = threading.Thread(target=update_func)  # 生成另一个线程实例
t3 = threading.Thread(target=update_func)  # 生成另一个线程实例
threads.append(t1)
threads.append(t2)
threads.append(t3)
if __name__ == '__main__':
    for t in threads:
        t.start()
