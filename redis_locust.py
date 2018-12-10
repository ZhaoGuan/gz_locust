# -*- coding: utf-8 -*-
# __author__ = 'Gz'
import time
import redis
from redis.client import Redis, StrictRedis
from locust import Locust, TaskSet, events, task
import random


class StrictRedisLocsut(StrictRedis):
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


class RedisClient(Redis):
    # Redis(StrictRedis_locsut)
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


class RedisLocust(Locust):
    def __init__(self):
        super(RedisLocust, self).__init__()
        # self.client = RedisClient(self.host, port=6379, db=1)
        # 修改后传值有问题所以需要两个都填写
        pool = redis.ConnectionPool(host=self.host, port=6379, db=1, max_connections=200)
        self.client = RedisClient(host=self.host, port=6379, db=1, connection_pool=pool)


class RedisTest(RedisLocust):
    host = 'kika-data-blau-redis0.intranet.com'
    min_wait = 100
    max_wait = 1000

    class TaskSet(TaskSet):
        @task(10)
        def duid_data(self):
            keys = ['USER_RECENT_NUM_82c0aee98c6f4cc7852ee607442bb44a',
                    'USER_RECENT_NUM_678adaa7edc2439bb7a3676930aa662c',
                    'USER_RECENT_NUM_f1011b8ebc334ba29e63ff0e79ae37a2',
                    'USER_RECENT_NUM_b7a398fb3dba4f45ba51039270b7a8ab',
                    'USER_RECENT_NUM_63ea375632cd4b259f9b65f45c1d4c26',
                    'USER_RECENT_NUM_785dbc80aa3447e8aa0db1f683dde100',
                    'USER_RECENT_NUM_9765211813224cf1bf8173181dfa972e',
                    'USER_RECENT_NUM_3a60f61a3b074c85b0221fa18325751d',
                    'USER_RECENT_NUM_4fc38c2958764702825f7f6c2168ecf1',
                    'USER_RECENT_NUM_15c10e66c37243e4998eb6cc40ae75c0']
            data = self.client.lrange('USER_RECENT_NUM_3f6af76a28144d019d617be41618411e', 0, 10)
            print(data)

        @task(0)
        def duid_tag_data(self):
            keys = ['USER_RECENT_TAG_NUM_bom dia._7db0d4ae1f424662b8731b8852257a05',
                    'USER_RECENT_TAG_NUM_en serio_8516fa617c2c4218b4cf5de6b90c13f7',
                    'USER_RECENT_TAG_NUM_oi_f5bdd538a6804c43881f5f8c7509fe0b',
                    'USER_RECENT_TAG_NUM_miga_cc851dc27266407e9afeea550b92df14',
                    'USER_RECENT_TAG_NUM_noo_fcf546c904a74ca1a168e244e01dd7fd',
                    'USER_RECENT_TAG_NUM_mierda_b8831aa94b594757944da9040c1834d1',
                    'USER_RECENT_TAG_NUM_tu vai_a3c7deda2f044594b11e6d88b06fda2f',
                    'USER_RECENT_TAG_NUM_jajaja_e1d325afec7542fb873aede69f482971',
                    'USER_RECENT_TAG_NUM_kkkkkkkkk_059a6bea2ab64b3181c2ffc90d2c846e',
                    'USER_RECENT_TAG_NUM_noo_af69676a95c4473799e20b4751e9907a',
                    'USER_RECENT_TAG_NUM_como estas_d1bc1b85635847088c9af2f02429b76d',
                    'USER_RECENT_TAG_NUM_kkkkk_a153dbb3c2f24f94a6d828d5217db136',
                    'USER_RECENT_TAG_NUM_ata_9f5722090d884297b060501144db4f41',
                    'USER_RECENT_TAG_NUM_coraz00f3n_34cbf8aee15a459193739feb493c1215',
                    'USER_RECENT_TAG_NUM_bj_31640f974d9f4b8ea1e48362ec539266',
                    'USER_RECENT_TAG_NUM_bueno_bbd0c5b0e71840309f36f7093e805082',
                    'USER_RECENT_TAG_NUM_amo_98dd6a1bb48f453a8f010ae92500c617',
                    'USER_RECENT_TAG_NUM_jajaj_8d981521b82c4fc4a2109cdf917ea216',
                    'USER_RECENT_TAG_NUM_boa noite_8ac5539172714c179a68d0cc3d2f73ac',
                    'USER_RECENT_TAG_NUM_jajajaja_4c60ada18c254c0daa1412c8347e929b',
                    'USER_RECENT_TAG_NUM_habla_1d20959760c6408ab69cfbb50773aeaf',
                    'USER_RECENT_TAG_NUM_kkkkkk_0c270fe4600b48ffab278821088cf8c4',
                    'USER_RECENT_TAG_NUM_2764_84596998955846209045a3ddeaab6cf1',
                    'USER_RECENT_TAG_NUM_kkkk_85733863a2ee42d9b24a83846c8f8619',
                    'USER_RECENT_TAG_NUM_really_efefad4b23abab9a247be0138e776a86',
                    'USER_RECENT_TAG_NUM_gracias_ad1da66493e24bfa8e727b1d224c2a21',
                    'USER_RECENT_TAG_NUM_d83dde02d83dde02d83dde02_9b1a490321fa4021a05df240bc3fc32d',
                    'USER_RECENT_TAG_NUM_kkkk_a6f2b278f22445a6af27a13fd1500e00',
                    'USER_RECENT_TAG_NUM_kkkkkk_059a6bea2ab64b3181c2ffc90d2c846e',
                    'USER_RECENT_TAG_NUM_oiii_8bcdf8d7e30a4082a2c6360f6f311ebd',
                    'USER_RECENT_TAG_NUM_ss_348182e9d2f6461b82892d6ca27ae233',
                    'USER_RECENT_TAG_NUM_jajajaja_8f4c4577d91d4243b5b9b96bdd291cd7',
                    'USER_RECENT_TAG_NUM_que_496808b00043432ca0b6347e1308f65d',
                    'USER_RECENT_TAG_NUM_nmms_a0408fbc1c0a4255adae7781845c8de3',
                    'USER_RECENT_TAG_NUM_no se_3402147b442f4260b09e3de7b0c3f529',
                    'USER_RECENT_TAG_NUM_:(_823cafb16a3440e88ac506890837bee1',
                    'USER_RECENT_TAG_NUM_si_9e4f9c5a99164666afba9e19646a6833',
                    'USER_RECENT_TAG_NUM_jajaj_49c85a11fe334440aa45f52d77938b74',
                    'USER_RECENT_TAG_NUM_mmm_2d6d36a9edfd40cd847a25fe0ab88a0e',
                    'USER_RECENT_TAG_NUM_si_b52dc2d098bf36f85da1cfefaec953cf',
                    'USER_RECENT_TAG_NUM_sip_b8c4abcf8f45468e95982c3a598c3f94',
                    'USER_RECENT_TAG_NUM_blz_0f01a9e609d34e26b036a8858cdadd82',
                    'USER_RECENT_TAG_NUM_amor_914d61e26e1e4b2fb9eb43aef8ff9d28',
                    'USER_RECENT_TAG_NUM_xd_ec4e8ffca4db41079f9c8d409e378a1c']
            key = random.choice(keys)
            data = self.client.zrange(key, 0, 10)
            print(data)
