# -*- coding: utf-8 -*-
# __author__ = 'Gz'
import time
import redis
from locust import Locust, TaskSet, events, task


class RedisClient(redis.Redis):
    def __getattr__(self, host, port=6379, db=0):
        func = redis.Redis.__getattr__(self, host, port, db)

        def wrapper(*args, **kwargs):
            start_time = time.time()
            try:
                result = func(*args, **kwargs)
            except redis.exceptions as e:
                total_time = int((time.time() - start_time) * 1000)
                events.request_failure.fire(request_type="redis", host=host, port=port, db=db, response_time=total_time,
                                            exception=e)
            else:
                total_time = int((time.time() - start_time) * 1000)
                events.request_success.fire(request_type="redis", host=host, port=port, db=db, response_time=total_time,
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

    class task_set(TaskSet):
        @task(10)
        def duid_data(self):
            data = self.client.lrange('b8c4abcf8f45468e95982c3a598c3f94', 0, 10)
            print(data)

        @task(0)
        def duid_tag_data(self):
            data = self.client.zrange('sip_b8c4abcf8f45468e95982c3a598c3f94', 0, 10)
            print(data)
