# -*- coding: utf-8 -*-
# @Time    : 2018/7/12 16:15
# @Author  : Zcs
# @File    : time_gen.py
import time


#  时间生成器，输入起始时间和间隔时间
#  调用一次则返回经过间隔时间后的时间
def time_gen(start, interval):
    """
    :param start: 开始时间 '2018-07-12 00:00:00'
    :param interval: 时间间隔，时间戳，int类型
    :return: 结束时间 '2018-7-13 00:00:00'
    """
    while True:
        timeArray = time.strptime(start, "%Y-%m-%d %H:%M:%S")  # 起始时间的时间数组
        timeStamp = int(time.mktime(timeArray))  # 时间戳
        end = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timeStamp + interval))
        start = end
        yield end

my_gen = time_gen('2018-07-12 00:00:00', 3600)

for i in range(10):
    print(next(my_gen))