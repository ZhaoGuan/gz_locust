# -*- coding: utf-8 -*-
# __author__ = 'Gz'

# ------------服务压测内容设置------------
from locust import HttpLocust, TaskSet, task
import os
import random
from basics_function.wuren_locust import HttpTest

PATH = os.path.dirname(os.path.abspath(__file__))

user_datas = []

source = "test"


class WuRen(TaskSet):

    @task(10)
    def login(self):
        user_data = random.choice(user_datas)
        duid = user_data['duid']
        token = user_data['token']
        case_data = {'data': {'OPERATION_MODE': 'single', 'SOURCE': {
            'test': {'URL': 'http://api.dev.wuren.com:8080/v1/identity/login',
                     'HEADERS': {'TYPE': '5NUT',
                                 'DATA': {'version': [1477],
                                          'duid': [duid],
                                          'lang': ['en_US']}},
                     'PARAMS': {'TYPE': 'NORMAL',
                                'DATA': None},
                     'MODE': {'TYPE': 'POST'},
                     'BODY': {'TYPE': 'JSON',
                              'FUNCTION': '5NUT_sigin',
                              'DATA': {"token": [token]}}}}}}
        HT = HttpTest(case_data, source)
        case = HT.case_data()
        data = HT.url_request_data(random.choice(case))
        request_header = data["request_header"]
        body = data["body"]
        request_type = data["request_type"]
        url = data["url"]
        if request_type == "post":
            response = self.client.post(url=url, headers=request_header, json=body, catch_response=True)
        else:
            response = self.client.get(url=url, headers=request_header, catch_response=True)
        if response.json()["errorMsg"] != "ok":
            response.failure("errorMsg is Fail")
        else:
            response.success()
        print(request_header)
        print(response.json())


class MyLocust(HttpLocust):
    task_set = WuRen
    # 任务的最小等待时间单位ms
    min_wait = 100
    # 任务的最大等待时间单位ms
    max_wait = 1000
    host = 'api.dev.wuren.com:8080'
