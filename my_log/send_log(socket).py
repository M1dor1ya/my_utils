# -*- coding: utf-8 -*-
# @Time    : 2018/6/13 16:06
# @Author  : Zcs
# @File    : send_log(socket).py

import socket


#  使用socket发送msg到syslog-ng服务端，tcp/udp协议均可，syslog-ng配置如下：
#  ****syslog-ng tcp默认使用601端口，udp默认使用514端口****
#  source tcp_test { tcp(ip('192.168.205.141') port(601)); };  or  source udp_test { udp(ip(0.0.0.0) port(514)); };
#  destination d_tcp { file("/var/my_log/dtcp.my_log"); };
#  my_log { source(tcp_test);  destination(d_tcp); };


def send_log(msg, type):
    if type == 'tcp':
        _sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        _sock.connect(('192.168.205.141', 514))
        _sock.send(msg.encode())
        _sock.close()
    if type == 'udp':
        _sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        _sock.sendto(msg, ('192.168.205.141', 514))
        _sock.close()

    return 0



