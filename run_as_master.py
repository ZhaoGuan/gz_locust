# -*- coding: utf-8 -*-
# __author__ = 'Gz'
import os

host = input('输入master的host:')
file = input('请处输入执行文件:')
os.system('nohup locust -f %s --master --reset-stats &' % file)
