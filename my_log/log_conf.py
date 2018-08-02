# -*- coding: utf-8 -*-
# @Time    : 2018/8/2 11:41
# @Author  : Zcs
# @File    : log_conf.py
# encoding=utf-8

LOG_FORMAT = '[T:%(asctime)s|E:%(filename)s|F:%(funcName)s|L:%(lineno)d|L:%(levelname)s]|%(message)s'


def basic_config(is_debug=True, log_level="DEBUG", host='remote.log.host', port=6923):
    import logging
    if is_debug is True:
        import sys
        logging.addLevelName(logging.WARNING, "\033[1;31m%s\033[1;0m" % logging.getLevelName(logging.WARNING))
        logging.addLevelName(logging.ERROR, "\033[1;41m%s\033[1;0m" % logging.getLevelName(logging.ERROR))
        logging.addLevelName(logging.DEBUG, "\033[1;42m%s\033[1;0m" % logging.getLevelName(logging.DEBUG))

        logging.basicConfig(level=log_level,
                            format=LOG_FORMAT,
                            datefmt='%Y-%m-%d %H:%M:%S', stream=sys.stdout)
    else:
        import logging.handlers

        formatter = logging.Formatter(LOG_FORMAT)  # 时间 调用的函数名 行号   级别  消息
        handler = logging.handlers.SocketHandler(host, port)
        handler.setFormatter(formatter)

        logging.root.setLevel(log_level)
        logging.root.addHandler(handler)


"""
Exp:
from log_conf import basic_config

#  在最顶层代码处运进行日志初始化配置
#  在后续的模块只需获得同名记录器即可，无需再配置
basic_config(host='127.0.0.1')
G_Logger = logging.getLogger('Logger')

"""