# -*- coding: utf-8 -*-
# @Time    : 2018/6/29 14:56
# @Author  : Zcs
# @File    : byte2human.py


def bytes2human(n):
    symbols = ('KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')
    prefix = {}
    if n != 0:
        for i, s in enumerate(symbols):
            prefix[s] = 1 << (i + 1) * 10
        for s in reversed(symbols):
            if n >= prefix[s]:
                value = float(n) / prefix[s]
                return '%.2f%s' % (value, s), prefix[s]
    else:
        return '0KB', 1024
