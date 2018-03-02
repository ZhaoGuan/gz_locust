# -*- coding: utf-8 -*-
# __author__ = 'Gz'
import redis
from locust import Locust, TaskSet, events, task


class RedisClient():
    def __int__(self, host, port=6379, db=0):
        self.host = host
        self.port = port
        self.db = host
        self.r = redis.Redis(host=self.host, port=self.port, db=self.db)

    def get_lrange(self, keys, start=0, end=10):
        data = self.r.lrange(keys, start=start, end=end)
        return data

    def get_zrange(self, keys, start=0, end=10):
        data = self.r.zrange(keys, start=start, end=end)
        return data


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
