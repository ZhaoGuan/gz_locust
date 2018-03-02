# -*- coding: utf-8 -*-
# __author__ = 'Gz'
import time
from redis.client import Redis, StrictRedis
from redis.exceptions import RedisError
from locust import Locust, TaskSet, events, task


class StrictRedis_locsut(StrictRedis):
    def execute_command(self, *args, **options):
        "Execute a command and return a parsed response"
        start_time = time.time()
        pool = self.connection_pool
        command_name = args[0]
        connection = pool.get_connection(command_name, **options)
        try:
            connection.send_command(*args)
            total_time = int((time.time() - start_time) * 1000)
            events.request_success.fire(request_type="redis", name=command_name, response_time=total_time,
                                        response_length=0)
            return self.parse_response(connection, command_name, **options)
        except (ConnectionError, TimeoutError) as e:
            connection.disconnect()
            if not connection.retry_on_timeout and isinstance(e, TimeoutError):
                raise
            connection.send_command(*args)
            total_time = int((time.time() - start_time) * 1000)
            events.request_failure.fire(request_type="redis", name=command_name, response_time=total_time,
                                        exception=e)
            return self.parse_response(connection, command_name, **options)
        finally:
            pool.release(connection)


class RedisClient(StrictRedis_locsut):
    Redis(StrictRedis_locsut)


class RedisLocust(Locust):
    def __init__(self):
        super(RedisLocust, self).__init__()
        self.client = RedisClient(self.host, port=6379, db=0)


class Redis_test(RedisLocust):
    host = 'kika-data-blau-redis0.intranet.com'
    min_wait = 100
    max_wait = 1000

    class task_set(TaskSet):
        @task(10)
        def duid_data(self):
            data = self.client.lrange('USER_RECENT_NUM_b4b7d7cc9454464b938177d412874ce9', 0, 10)
            print(data)

        @task(0)
        def duid_tag_data(self):
            data = self.client.zrange('USER_RECENT_TAG_NUM_na_a1be32a10c414065a20e7b755018150c', 0, 10)
            print(data)
