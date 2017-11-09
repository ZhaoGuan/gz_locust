# -*- coding: utf-8 -*-
# __author__ = 'Gz'
import daemon
import os

host = input('输入master的host:')
with daemon.DaemonContext():
    os.system('locust -f locustfile.py --slave --master-host=%s' % host)
