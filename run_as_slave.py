# -*- coding: utf-8 -*-
# __author__ = 'Gz'
import os

host = input('输入master的host:')
run_no = input('请输入要启动的slave数量:')
file = input('请处输入执行文件:')
for i in range(int(run_no)):
    os.system('nohup locust -f %s --slave --master-host=%s >/dev/null  &' % (file, host))
