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


import pymysql
from g_conf.config import config_template
from DBUtils.PooledDB import PooledDB


class MysqlPool:
    config = {
        'creator': pymysql,
        'host': config_template['MYSQL']['HOST'],
        'port': config_template['MYSQL']['PORT'],
        'user': config_template['MYSQL']['USER'],
        'password': config_template['MYSQL']['PASSWD'],
        'db': config_template['MYSQL']['DB'],
        'charset': config_template['MYSQL']['CHARSET'],
        'cursorclass': pymysql.cursors.DictCursor
    }
    pool = PooledDB(**config)

    def __enter__(self):
        self.conn = MysqlPool.pool.connection()
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, type, value, trace):
        self.cursor.close()
        self.conn.close()


#  使用方法：
from g_utils.db_helper import MysqlPool
def my_paginator(sql, count, page):
    with MysqlPool() as db:
        sql += ' %s'
        limit = 'LIMIT %s,%s' % ((page-1)*count, count)
        db.cursor.execute(sql % limit)
        data = db.cursor.fetchall()
    return data
