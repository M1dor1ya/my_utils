# -*- coding: utf-8 -*-
# @Time    : 2018/7/11 14:54
# @Author  : Zcs
# @File    : mysql_pool.py

import pymysql
from DBUtils.PooledDB import PooledDB

config = {
            'creator': pymysql,
            'host': 'localhost',
            'port': 3306,
            'user': 'root',
            'password': 'root',
            'db': 'test',
            'charset': 'utf8',
            'cursorclass': pymysql.cursors.DictCursor,
            'maxconnections': 5,

        }

# pool = PooledDB(**config)
# conn = pool.connection()  # 以后每次需要数据库连接就是用connection（）函数获取连接就好了
# cur = conn.cursor()
# SQL = "select * from test"
# r = cur.execute(SQL)
# data = cur.fetchall()
# cur.close()
# conn.close()


class MysqlPool(object):

    print('初始化连接池')
    __pool = PooledDB(**config)

    def __enter__(self):
        if self.__pool is None:
            self.__pool = PooledDB(**config)
        self.conn = self.__pool.connection()
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, type, value, trace):
        self.cursor.close()
        self.conn.close()

#  在代码主文件进行一次初始化即可： MysqlPool()
#  使用方法：
with MysqlPool() as db:
    db.cursor.execute('SELECT * FROM test')
    data = db.cursor.fetchall()
