# -*- coding: utf-8 -*-
# @Time    : 2018/7/2 11:14
# @Author  : Zcs
# @File    : time_module.py


"""
time模块和datetime模块相关操作
"""
import time
import calendar
import datetime


#  struct_time:具有命名元组接口的对象,值可以通过索引和属性名称来访问

obj = time.gmtime(0)  # In:时间戳  Out:struct_time  In:0  Out:1970-01-01
time.localtime()  # In:时间戳  Out:struct_time  In:0  Out:本地时间(当前时区时间)
calendar.timegm(time.localtime())  # In:struct_time(UTC国际时间)  Out:时间戳
time.mktime(time.localtime())  # In:struct_time(本地时间)  Out:时间戳
time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  # In:(fmt, struct_time)  Out:字符串时间，被fmt格式化后的时间
time.strptime('2018-07-02 14:33:00', '%Y-%m-%d %H:%M:%S')  # In:(字符串时间, fmt)  Out:struct_time  用于将时间转为struct_time
time.time()  # 返回时间戳
print()

#  datetime
print(datetime)
d = datetime.datetime.now()
oneday = datetime.timedelta(days=365)
day = d - oneday
forward_day = str(datetime.datetime(day.year, day.month, day.day, day.hour, day.minute, day.second))


#  获取N天前的日期
def get_day_nday_ago(date, n):
    t = time.strptime(date, "%Y-%m-%d")
    y, m, d = t[0:3]
    Date = str(datetime.datetime(y, m, d) - datetime.timedelta(n)).split()
    return Date[0]