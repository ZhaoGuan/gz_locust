# -*- coding: utf-8 -*-
# __author__ = 'Gz'

# ------------服务压测内容设置------------
from locust import Locust, TaskSet, events, task
import random
from kafka import KafkaProducer
import uuid
import time


# self.producer = KafkaProducer(bootstrap_servers='172.31.31.80:9092')
class kafka_producer_Client():
    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers='172.31.31.80:9092')

    def send_kafka(self, item, message):
        start_time = time.time()
        total_time = int((time.time() - start_time) * 1000)
        events.request_success.fire(request_type="kafka", response_time=total_time, name=message,
                                    response_length=0)
        self.producer.send(item, bytes(message, 'utf-8'))
        self.producer.flush()


class kafukaLocust(Locust):
    def __init__(self):
        super(kafukaLocust, self).__init__()
        self.client = kafka_producer_Client()


class kafka_test(kafukaLocust):
    host = ''
    min_wait = 100
    max_wait = 1000

    class task_set(TaskSet):
        @task(10)
        def train(self):
            message_list = [
                'e2934742f9d3b8ef2b59806a041ab389,e06932350d6030495caf055b1e9a7d5a,172.58.75.133,,1523333340,{"oid":"f8e87d8719babe02c284e18707d1284d","tp":"event","l":"keyboard_sticker2_suggestion_pop","iid":"send","otp":"item","value":0,"extra":{"package_name":"com.snapchat.android","realtime_event":"1","pop_delay":"0","kb_lang":"hr","source":"recommend","kb_current_time":"1523333338","kb_time_zone":"-8","tags":"hahaha","extra":"{\\"taghit\\":\\"hit\\",\\"bucketName\\":\\"EnUsBeforeNotMod2GBDTBucket\\",\\"product\\":\\"\\",\\"thresholdScore\\":\\"0.1\\",\\"language\\":\\"en\\",\\"recommend\\":\\"15:EnUsBeforeNotMod2GBDTBucket\\",\\"source\\":\\"CF\\",\\"sessionId\\":\\"sticker8256381a413b11e8828c0670cf14ebd4\\",\\"bucket\\":\\"15:EnUsBeforeNotMod2GBDTBucket\\",\\"alg_hit\\":\\"1\\",\\"scenario\\":\\"EnUsBeforeNotMod2Scenario\\",\\"cf_score\\":\\"0.9766543\\",\\"gbdt_threshold\\":\\"0.095\\"}","key_word":"hahaha","pop_type":"sticker","item_id":"9405ed72-4f28-4b5e-95d3-3ad7fa187905","lang":"en","na":"us","app":"4.8.2.1638","app_vcode":"163801","aid":"b75f9a2e689c576423f6f70f384615369177f1a3","os":"7.1.1","net":0},"ts":1523333338953}',
                'e2934742f9d3b8ef2b59806a041ab389,ff2865ea386048faa4d8e6e8478b36b2,172.58.75.133,,1523333340,{"oid":"f8e87d8719babe02c284e18707d1284d","tp":"event","l":"keyboard_sticker2_suggestion_pop","iid":"send","otp":"item","value":0,"extra":{"package_name":"com.snapchat.android","realtime_event":"1","pop_delay":"0","kb_lang":"es","source":"recommend","kb_current_time":"1523333338","kb_time_zone":"-8","tags":"wow","extra":"{\\"taghit\\":\\"miss\\",\\"bucketName\\":\\"EnUsBeforeMod2Bucket\\",\\"product\\":\\"\\",\\"thresholdScore\\":\\"0.1\\",\\"language\\":\\"en\\",\\"recommend\\":\\"5:EnUsBeforeMod2Bucket\\",\\"source\\":\\"CF\\",\\"sessionId\\":\\"sticker82eb73da413b11e8828c0670cf14ebd4\\",\\"bucket\\":\\"5:EnUsBeforeMod2Bucket\\",\\"alg_hit\\":\\"1\\",\\"scenario\\":\\"EnUsBeforeMod2Secnario\\",\\"cf_score\\":\\"0.9766543\\",\\"gbdt_threshold\\":\\"0.095\\"}","key_word":"wow","pop_type":"sticker","item_id":"","lang":"en","na":"us","app":"4.8.2.1638","app_vcode":"163801","aid":"b75f9a2e689c576423f6f70f384615369177f1a3","os":"7.1.1","net":0},"ts":1523333338953}',
                'e2934742f9d3b8ef2b59806a041ab389,8c8f95d3740a4406b30621b519947d02,172.58.75.133,,1523333340,{"oid":"f8e87d8719babe02c284e18707d1284d","tp":"event","l":"keyboard_sticker2_suggestion_pop","iid":"send","otp":"item","value":0,"extra":{"package_name":"com.snapchat.android","realtime_event":"1","pop_delay":"0","kb_lang":"pt_BR","source":"recommend","kb_current_time":"1523333338","kb_time_zone":"-8","tags":"kkkk","extra":"{\\"taghit\\":\\"hit\\",\\"bucketName\\":\\"PtBeforeBucket\\",\\"product\\":\\"\\",\\"thresholdScore\\":\\"0.1\\",\\"language\\":\\"pt\\",\\"recommend\\":\\"2:PtBeforeBucket\\",\\"source\\":\\"CF\\",\\"sessionId\\":\\"sticker82eefa78413b11e8828c0670cf14ebd4\\",\\"bucket\\":\\"2:PtBeforeBucket\\",\\"alg_hit\\":\\"1\\",\\"scenario\\":\\"PtSecnario\\",\\"cf_score\\":\\"0.9766543\\",\\"gbdt_threshold\\":\\"0.095\\"}","key_word":"kkkk","pop_type":"sticker","item_id":"b4443280-a6ba-4ca6-94b7-f707f44d75d9","lang":"pt","na":"us","app":"4.8.2.1638","app_vcode":"163801","aid":"b75f9a2e689c576423f6f70f384615369177f1a3","os":"7.1.1","net":0},"ts":1523333338953}',
                'e2934742f9d3b8ef2b59806a041ab389,26075db20c1c4901990ad46a0b39c26c,172.58.75.133,,1523333340,{"oid":"f8e87d8719babe02c284e18707d1284d","tp":"event","l":"keyboard_sticker2_suggestion_pop","iid":"send","otp":"item","value":0,"extra":{"package_name":"com.snapchat.android","realtime_event":"1","pop_delay":"0","kb_lang":"tl","source":"recommend","kb_current_time":"1523333338","kb_time_zone":"-8","tags":"hahahaha","extra":"{\\"taghit\\":\\"hit\\",\\"bucketName\\":\\"EnUsBeforeNotMod2GBDTMLeapBucket\\",\\"product\\":\\"\\",\\"thresholdScore\\":\\"0.1\\",\\"language\\":\\"en\\",\\"recommend\\":\\"7:EnUsBeforeNotMod2GBDTMLeapBucket\\",\\"source\\":\\"CF\\",\\"sessionId\\":\\"sticker82f5a38c413b11e8828c0670cf14ebd4\\",\\"bucket\\":\\"7:EnUsBeforeNotMod2GBDTMLeapBucket\\",\\"alg_hit\\":\\"1\\",\\"scenario\\":\\"EnUsBeforeNotMod2Scenario\\",\\"cf_score\\":\\"0.9766543\\",\\"gbdt_threshold\\":\\"0.095\\"}","key_word":"hahahaha","pop_type":"sticker","item_id":"zqlvctnhpqrio","lang":"en","na":"us","app":"4.8.2.1638","app_vcode":"163801","aid":"b75f9a2e689c576423f6f70f384615369177f1a3","os":"7.1.1","net":0},"ts":1523333338953}',
                '78472ddd7528bcacc15725a16aeec190,fc63362071e8490391c547a2b7dbd46c,172.58.75.133,,1523333340,{"oid":"f8e87d8719babe02c284e18707d1284d","tp":"event","l":"keyboard_sticker2_suggestion_pop","iid":"send","otp":"item","value":0,"extra":{"package_name":"com.snapchat.android","realtime_event":"1","pop_delay":"0","kb_lang":"en_US","source":"recommend","kb_current_time":"1523333338","kb_time_zone":"-8","tags":"hey","extra":"{\\"taghit\\":\\"hit\\",\\"bucketName\\":\\"KikaEnUsBeforeBucket\\",\\"product\\":\\"\\",\\"thresholdScore\\":\\"0.1\\",\\"language\\":\\"en\\",\\"recommend\\":\\"16:KikaEnUsBeforeBucket\\",\\"source\\":\\"CF\\",\\"sessionId\\":\\"sticker8332fb42413b11e8828c0670cf14ebd4\\",\\"bucket\\":\\"16:KikaEnUsBeforeBucket\\",\\"alg_hit\\":\\"1\\",\\"scenario\\":\\"KikaEnUsScenario\\",\\"cf_score\\":\\"0.9766543\\",\\"gbdt_threshold\\":\\"0.095\\"}","key_word":"hey","pop_type":"sticker","item_id":"onnuzxchsbbn6","lang":"en","na":"us","app":"4.8.2.1638","app_vcode":"163801","aid":"b75f9a2e689c576423f6f70f384615369177f1a3","os":"7.1.1","net":0},"ts":1523333338953}',
                'e2934742f9d3b8ef2b59806a041ab389,1557f2fe20014162869fc9218f697ea2,172.58.75.133,,1523333340,{"oid":"f8e87d8719babe02c284e18707d1284d","tp":"event","l":"keyboard_sticker2_suggestion_pop","iid":"send","otp":"item","value":0,"extra":{"package_name":"com.snapchat.android","realtime_event":"1","pop_delay":"0","kb_lang":"en_GB","source":"recommend","kb_current_time":"1523333338","kb_time_zone":"-8","tags":"hi","extra":"{\\"taghit\\":\\"hit\\",\\"bucketName\\":\\"EnNotUsBeforeGBDTMLeapBucket\\",\\"product\\":\\"\\",\\"thresholdScore\\":\\"0.1\\",\\"language\\":\\"en\\",\\"recommend\\":\\"12:EnNotUsBeforeGBDTMLeapBucket\\",\\"source\\":\\"CF\\",\\"sessionId\\":\\"sticker83388080413b11e8828c0670cf14ebd4\\",\\"bucket\\":\\"12:EnNotUsBeforeGBDTMLeapBucket\\",\\"alg_hit\\":\\"1\\",\\"scenario\\":\\"EnNotUsBeforeScenario\\",\\"cf_score\\":\\"0.9766543\\",\\"gbdt_threshold\\":\\"0.095\\"}","key_word":"hi","pop_type":"sticker","item_id":"","lang":"en","na":"us","app":"4.8.2.1638","app_vcode":"163801","aid":"b75f9a2e689c576423f6f70f384615369177f1a3","os":"7.1.1","net":0},"ts":1523333338953}',
                'e2934742f9d3b8ef2b59806a041ab389,0ce025703ae648138ec2d592d05bdc67,172.58.75.133,,1523333340,{"oid":"f8e87d8719babe02c284e18707d1284d","tp":"event","l":"keyboard_sticker2_suggestion_pop","iid":"send","otp":"item","value":0,"extra":{"package_name":"com.snapchat.android","realtime_event":"1","pop_delay":"0","kb_lang":"es_MX","source":"recommend","kb_current_time":"1523333338","kb_time_zone":"-8","tags":"va","extra":"{\\"taghit\\":\\"hit\\",\\"bucketName\\":\\"EnNotUsBeforeGBDTBucket\\",\\"product\\":\\"\\",\\"thresholdScore\\":\\"0.1\\",\\"language\\":\\"en\\",\\"recommend\\":\\"11:EnNotUsBeforeGBDTBucket\\",\\"source\\":\\"CF\\",\\"sessionId\\":\\"sticker83769c1c413b11e8828c0670cf14ebd4\\",\\"bucket\\":\\"11:EnNotUsBeforeGBDTBucket\\",\\"alg_hit\\":\\"1\\",\\"scenario\\":\\"EnNotUsBeforeScenario\\",\\"cf_score\\":\\"0.9766543\\",\\"gbdt_threshold\\":\\"0.095\\"}","key_word":"va","pop_type":"sticker","item_id":"a21a4da8-0bd7-4838-a3cd-a92b2cddfe51","lang":"en","na":"us","app":"4.8.2.1638","app_vcode":"163801","aid":"b75f9a2e689c576423f6f70f384615369177f1a3","os":"7.1.1","net":0},"ts":1523333338953}']
            message = random.choice(message_list)
            self.client.send_kafka('emoji_appstore', message)
