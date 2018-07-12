# -*- coding: utf-8 -*-
# @Time    : 2018/7/9 17:38
# @Author  : Zcs
# @File    : get_month.py

import datetime

d = datetime.datetime.now()
oneday = datetime.timedelta(days=182)
day = d - oneday
#  forward_day = str(datetime.datetime(day.year, day.month, day.day, day.hour, day.minute, day.second))
time_list = []  # 年月列表，例如今天为2018-07-09，那么前半年数据为 2018-01 至 2018-07
data_times = []
for i in range(day.month, day.month + 7):
    if i <= 12:
        if i < 10:
            time_str = '%s-0%s-01' % (day.year, i)
        else:
            time_str = '%s-%s-01' % (day.year, i)
    else:
        m = i - 12
        year = day.year + 1
        if m < 10:
            time_str = '%s-0%s-01' % (year, m)
        else:
            time_str = '%s-%s-01' % (year, m)

    time_list.append(time_str)
print(time_list)