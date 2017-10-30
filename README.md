##locust压测
# 其实很简单主要运行的任务就在locustfle.py中。
# 单独的时候命令运行时: locust -f locustfile.py --host=http://api.kikakeyboard.com
# 作为Master机运行时: locust -f locustfile.py --master --host=http://api.kikakeyboard.com
# 作为Slave机运行时: locust -f locustfile.py --slave --master-host=对应maser ip
# Dockerfile中是对应docker的一些配置信息
# requirements.txt中是Python依赖