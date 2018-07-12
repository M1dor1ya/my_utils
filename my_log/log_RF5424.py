# -*- coding: utf-8 -*-
# @Time    : 2018/6/20 16:38
# @Author  : Zcs
# @File    : log_RF5424.py

#  pip install pysyslogclient
#  package resource : https://github.com/aboehm/pysyslogclient
import pysyslogclient

#  syslog-protocol:   RF3164(old)  and  RF5424(new)
#  client = pysyslogclient.SyslogClientRFC3164('192.168.205.141', 601, proto="TCP")
client = pysyslogclient.SyslogClientRFC5424('192.168.205.142', 601, proto="TCP")
client.log("Hello syslog server")
client.close()


"""
client.my_log("Hello syslog server",
facility=pysyslogclient.FAC_SYSTEM,
severity=pysyslogclient.SEV_EMERGENCY,
program="Logger",
pid=1)
"""