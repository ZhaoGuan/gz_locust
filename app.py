# -*- coding: utf-8 -*-
# __author__ = 'Gz'
import os
while True:
    choose = input("Tell me how you're going to start？ Master or Slave")
    if choose == "Master":
        os.system('locust -f locustfile.py --host=http://api.kikakeyboard.com')
        break
    elif choose == 'Slave':
        master = input('Tall me your Master:')
        os.system('locust -f locustfile.py --slave --master-host=%s' % master)
        break
    else:
        print('You input wrong!! Try again!')
