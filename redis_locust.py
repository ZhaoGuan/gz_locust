# -*- coding: utf-8 -*-
# __author__ = 'Gz'
import time
import redis
from locust import Locust, TaskSet, events, task


class RedisClient(redis):
    # def __int__(self, host, port=6379, db=0):
    #     self.host = host
    #     self.port = port
    #     self.db = host
    #     self.r = redis.Redis(host=self.host, port=self.port, db=self.db)
    #
    # def get_lrange(self, keys, start=0, end=10):
    #     try:
    #         result = self.r.lrange(keys, start=start, end=end)
    #     except xmlrpclib.Fault as e:
    #         total_time = int((time.time() - start_time) * 1000)
    #         events.request_failure.fire(request_type="xmlrpc", name=name, response_time=total_time, exception=e)
    #     else:
    #         total_time = int((time.time() - start_time) * 1000)
    #         events.request_success.fire(request_type="xmlrpc", name=name, response_time=total_time,
    #                                     response_length=0)
    #     return data
    #
    # def get_zrange(self, keys, start=0, end=10):
    #     data = self.r.zrange(keys, start=start, end=end)
    #     return data
    def __getattr__(self, name):
        func = redis.Redis.__getattr__(self, name)

        def wrapper(*args, **kwargs):
            start_time = time.time()
            try:
                result = func(*args, **kwargs)
            except redis.Fault as e:
                total_time = int((time.time() - start_time) * 1000)
                events.request_failure.fire(request_type="redis", name=name, response_time=total_time, exception=e)
            else:
                total_time = int((time.time() - start_time) * 1000)
                events.request_success.fire(request_type="redis", name=name, response_time=total_time,
                                            response_length=0)

        return wrapper


class RedisLocust(Locust):
    def __init__(self, *args, **kwargs):
        super(RedisLocust, self).__init__(*args, **kwargs)
        self.client = RedisClient(host=self.host, port=6379, db=0)


class Redis_test(RedisLocust):
    host = 'kika-data-blau-redis0.intranet.com'
    min_wait = 100
    max_wait = 1000

    class tast_set(TaskSet):
        @task(10)
        def duid_data(self):
            data = self.client.get_lrange('b8c4abcf8f45468e95982c3a598c3f94')
            print(data)

        @task(0)
        def duid_tag_data(self):
            data = self.client.get_zrange('sip_b8c4abcf8f45468e95982c3a598c3f94')
            print(data)
