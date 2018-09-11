# -*- coding: utf-8 -*-
# @Time    : 2018/8/7 10:43
# @Author  : Zcs
# @File    : time_utils.py

import time
import datetime
import calendar


#  返回N天前的年月日
def get_day_nday_ago(date, n):
    """
    :param date: '2018-08-09'
    :param n: 5
    :return: '2018-08-04'
    """
    t = time.strptime(date, "%Y-%m-%d")
    y, m, d = t[0:3]
    Date = str(datetime.datetime(y, m, d) - datetime.timedelta(n)).split()
    return Date[0]


#  获取某个月的最后一天
def get_month_last(d):
    """
    :param d: datetime type '2018-02'
    :return: datetime type '2018-02-28'
    """
    days = calendar.monthrange(d.year, d.month)[1]
    return datetime.date(d.year, d.month, days)


#  获取上个月的第一天
def get_last_month_first(d):
    """
    :param d: datetime type '2018-02'
    :return: datetime type '2018-01-01'
    """
    return datetime.date(d.year - (d.month == 1), d.month - 1 or 12, 1)


#  获取上个月最后一天
def get_last_month_last(d):
    """
    :param d: datetime type '2018-02'
    :return: datetime type '2018-01-31'
    """
    return datetime.date(d.year, d.month, 1) - datetime.timedelta(1)


#  时间生成器，输入起始时间和间隔时间
#  调用一次则返回经过间隔时间后的时间
def time_gen(start, interval):
    """
    :param start: 开始时间 '2018-07-12 00:00:00'
    :param interval: 时间间隔，时间戳，int类型
    :return: 结束时间 '2018-7-13 00:00:00'

    exp:
    my_gen = time_gen('2018-07-12 00:00:00', 3600)
    for i in range(10):
        print(next(my_gen))
    """
    while True:
        timeArray = time.strptime(start, "%Y-%m-%d %H:%M:%S")  # 起始时间的时间数组
        timeStamp = int(time.mktime(timeArray))  # 时间戳
        end = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timeStamp + interval))
        start = end
        yield end

if __name__ == '__main__':
    pass
