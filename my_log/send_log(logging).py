# -*- coding: utf-8 -*-
# @Time    : 2018/6/19 17:05
# @Author  : Zcs
# @File    : send_log(logging).py

#  使用tcp协议向日志服务器发送日志
import logging.handlers
import socket

msg = 'test'
ip = '192.168.205.141'
port = 601
logger = logging.getLogger('SysLogger')
#  socktype -- tcp:socket.SOCK_STREAM -- udp:socket.SOCK_DGRAM
fh = logging.handlers.SysLogHandler((ip, port), logging.handlers.SysLogHandler.LOG_AUTH, socktype=socket.SOCK_STREAM)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)
logger.warning(msg)
fh.close()
