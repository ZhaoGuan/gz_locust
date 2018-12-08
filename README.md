## locust压测
    其实很简单主要运行的任务就在locustfle.py中。
    单独的时候命令运行时: locust -f locustfile.py --host=http://api.kikakeyboard.com
    作为Master机运行时: locust -f locustfile.py --master --reset-stats --host=http://api.kikakeyboard.com
    host可以不添加 --reset-stats 必填不然CSV报告会积累结果
    作为Slave机运行时: locust -f locustfile.py --slave --master-host=对应maser ip
    Dockerfile中是对应docker的一些配置信息
    requirements.txt中是Python依赖
## 测试计划格式
    #master地址
    master_host: http://127.0.0.1:8089/
    报告文件夹
    dir : 20171117
    #测试计划
    plan : [
            {'locust_count': 10, 'hatch_rate': 1},
            {'locust_count': 20, 'hatch_rate': 1},
            {'locust_count': 30, 'hatch_rate': 1},
            {'locust_count': 35, 'hatch_rate': 1}
            ]
    #持续时间单位S
    duration : 60
