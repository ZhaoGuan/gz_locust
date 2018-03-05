# -*- coding: utf-8 -*-
# __author__ = 'Gz'
import time
from redis.client import Redis, StrictRedis
from redis.exceptions import RedisError
from locust import Locust, TaskSet, events, task
import random


class StrictRedis_locsut(StrictRedis):
    def execute_command(self, *args, **options):
        start_time = time.time()
        pool = self.connection_pool
        command_name = args[0]
        connection = pool.get_connection(command_name, **options)
        try:
            connection.send_command(*args)
            result = self.parse_response(connection, command_name, **options)
            total_time = float((time.time() - start_time))
            total_time_int = int((time.time() - start_time) * 1000)
            print(total_time)
            events.request_success.fire(request_type="redis", name=args[1], response_time=total_time_int,
                                        response_length=0)
            return result
        except (ConnectionError, TimeoutError) as e:
            connection.disconnect()
            if not connection.retry_on_timeout and isinstance(e, TimeoutError):
                raise
            connection.send_command(*args)
            result = self.parse_response(connection, command_name, **options)
            total_time = float((time.time() - start_time))
            total_time_int = int((time.time() - start_time) * 1000)
            print(total_time)
            events.request_failure.fire(request_type="redis", name=args[1], response_time=total_time_int,
                                        exception=e)
            return result
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
            keys = ['USER_RECENT_NUM_82c0aee98c6f4cc7852ee607442bb44a',
                    'USER_RECENT_NUM_678adaa7edc2439bb7a3676930aa662c',
                    'USER_RECENT_NUM_f1011b8ebc334ba29e63ff0e79ae37a2',
                    'USER_RECENT_NUM_b7a398fb3dba4f45ba51039270b7a8a',
                    'USER_RECENT_NUM_63ea375632cd4b259f9b65f45c1d4c26',
                    'USER_RECENT_NUM_785dbc80aa3447e8aa0db1f683dde100',
                    'USER_RECENT_NUM_9765211813224cf1bf8173181dfa972e',
                    'USER_RECENT_NUM_3a60f61a3b074c85b0221fa18325751d',
                    'USER_RECENT_NUM_4fc38c2958764702825f7f6c2168ecf1',
                    'USER_RECENT_NUM_15c10e66c37243e4998eb6cc40ae75c0',
                    'USER_RECENT_NUM_c77149b8e8a34d4f992837341f763d88',
                    'USER_RECENT_NUM_3da61509e3284f00a5692557d5dc06c9',
                    'USER_RECENT_NUM_62b8146c66084e0db6022af18af82e71',
                    'USER_RECENT_NUM_a6ea722e30cf4acaade101784f5ba0c9',
                    'USER_RECENT_NUM_fbad23ccf70b46db9994d0d4f12a47e2',
                    'USER_RECENT_NUM_22b6f82c990b424cafbcab8043caafe9',
                    'USER_RECENT_NUM_2fed0707371284ca3ff21be58e9d655f',
                    'USER_RECENT_NUM_78da448d186946f289619d02db0925c3',
                    'USER_RECENT_NUM_09df7b541a58457ab1d1810da32b6620',
                    'USER_RECENT_NUM_594dc0395ccd41d49479da04b8d70dd0',
                    'USER_RECENT_NUM_4edeacc1588b43d79b9c554ee5802242',
                    'USER_RECENT_NUM_94143c8b9793492a9c3f2a89e558372f',
                    'USER_RECENT_NUM_2d1411656b0d4c8cac5725760608a20e',
                    'USER_RECENT_NUM_824114420a8147c394d8bec7e077f388',
                    'USER_RECENT_NUM_fb8073187f15410bbb0be522a6cc69a0',
                    'USER_RECENT_NUM_76d73f5ab2be4bf58df527c1deda6286',
                    'USER_RECENT_NUM_99c0b82b952d4656b593bfd637cf1efb',
                    'USER_RECENT_NUM_e78bca502f244225ac1e077f45092776',
                    'USER_RECENT_NUM_dd7d278321ae400d87168d3a59fe734d',
                    'USER_RECENT_NUM_988055cb904c4da8b1058607fe3b4b6a',
                    'USER_RECENT_NUM_e15d10d03c8549f69f4b7f866cb97c5f',
                    'USER_RECENT_NUM_15ab630d12cb4e12b71f467600c458ad',
                    'USER_RECENT_NUM_4fd526ae98c449059e0fc39736b318f3',
                    'USER_RECENT_NUM_ced92652d7e34a9888e034a97c1bb9dc',
                    'USER_RECENT_NUM_70182005cddd4f6894945223651a835d',
                    'USER_RECENT_NUM_bc1ce1aa974842dfa8ff092f68c6018a',
                    'USER_RECENT_NUM_9e89e8f4ac504fefa7888fb8713df323',
                    'USER_RECENT_NUM_1a75952198160d4f278067673a579d12',
                    'USER_RECENT_NUM_1f7227e2bdf9405a80883f0d68258784',
                    'USER_RECENT_NUM_c07ec2a84e594a7bbf408f4732bb5c67',
                    'USER_RECENT_NUM_25edee64d47b4f36b081d38da109645c',
                    'USER_RECENT_NUM_b3d72c94b8a6495d8443733f873407d1',
                    'USER_RECENT_NUM_4a324a8c6fbacbb68ef0a9685b16014f',
                    'USER_RECENT_NUM_51ef910bef6f42e9828a19ce52f691da',
                    'USER_RECENT_NUM_3f6af76a28144d019d617be41618411e'
                    ]
            key = random.choice(keys)
            data = self.client.lrange(key, 0, 10)
            print(data)

        @task(0)
        def duid_tag_data(self):
            data = self.client.zrange('USER_RECENT_TAG_NUM_na_a1be32a10c414065a20e7b755018150c', 0, 10)
            print(data)
