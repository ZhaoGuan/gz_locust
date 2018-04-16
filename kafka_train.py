# -*- coding: utf-8 -*-
# __author__ = 'Gz'

# ------------服务压测内容设置------------
from locust import Locust, TaskSet, events, task
import random
from kafka import KafkaProducer
import uuid
import time


# self.producer = KafkaProducer(bootstrap_servers='172.31.31.80:9092')
# single_data = all_data[random.choice(range(len(all_data)))
class kafka_producer_Client():
    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers='172.31.31.80:9092')

    def send_kafka(self, item, message):
        start_time = time.time()
        total_time = int((time.time() - start_time) * 1000)
        events.request_success.fire(request_type="kafka", response_time=total_time,
                                    response_length=0)
        self.producer.send(item, bytes(message, 'utf-8'))


class kafukaLocust(Locust):
    def __init__(self):
        super(kafukaLocust, self).__init__()
        self.client = kafka_producer_Client()


class Redis_test(kafukaLocust):
    min_wait = 100
    max_wait = 1000

    class kafka_train(TaskSet):
        @task(10)
        def train(self):
            message_list = [
                'e2934742f9d3b8ef2b59806a041ab389,25ad4b27c4c3410784ee7fab223f3a98,172.58.75.133,,1523333340,{"oid":"f8e87d8719babe02c284e18707d1284d","tp":"event","l":"keyboard_sticker2_suggestion_pop","iid":"send","otp":"item","value":0,"extra":{"package_name":"com.snapchat.android","realtime_event":"1","pop_delay":"0","kb_lang":"pt_BR","source":"recommend","kb_current_time":"1523333338","kb_time_zone":"-8","tags":"eita","extra":"{\\"taghit\\":\\"hit\\",\\"bucketName\\":\\"PtBeforeBucket\\",\\"product\\":\\"\\",\\"thresholdScore\\":\\"0.1\\",\\"language\\":\\"pt\\",\\"recommend\\":\\"2:PtBeforeBucket\\",\\"source\\":\\"CF\\",\\"sessionId\\":\\"sticker1fa879fc413211e894460670cf14ebd4\\",\\"bucket\\":\\"2:PtBeforeBucket\\",\\"alg_hit\\":\\"1\\",\\"scenario\\":\\"PtSecnario\\",\\"cf_score\\":\\"0.9766543\\",\\"gbdt_threshold\\":\\"0.095\\"}","key_word":"eita","pop_type":"sticker","item_id":"pubxelwt57jsq","lang":"pt","na":"us","app":"4.8.2.1638","app_vcode":"163801","aid":"b75f9a2e689c576423f6f70f384615369177f1a3","os":"7.1.1","net":0},"ts":1523333338953}',
                'e2934742f9d3b8ef2b59806a041ab389,bc21bc8ea7ea480d85a0b6df109a0159,172.58.75.133,,1523333340,{"oid":"f8e87d8719babe02c284e18707d1284d","tp":"event","l":"keyboard_sticker2_suggestion_pop","iid":"send","otp":"item","value":0,"extra":{"package_name":"com.snapchat.android","realtime_event":"1","pop_delay":"0","kb_lang":"en_US","source":"recommend","kb_current_time":"1523333338","kb_time_zone":"-8","tags":"morning","extra":"{\\"taghit\\":\\"hit\\",\\"bucketName\\":\\"EnUsBeforeNotMod2GBDTBucket\\",\\"product\\":\\"\\",\\"thresholdScore\\":\\"0.1\\",\\"language\\":\\"en\\",\\"recommend\\":\\"15:EnUsBeforeNotMod2GBDTBucket\\",\\"source\\":\\"CF\\",\\"sessionId\\":\\"sticker1fbcbc0a413211e894460670cf14ebd4\\",\\"bucket\\":\\"15:EnUsBeforeNotMod2GBDTBucket\\",\\"alg_hit\\":\\"1\\",\\"scenario\\":\\"EnUsBeforeNotMod2Scenario\\",\\"cf_score\\":\\"0.9766543\\",\\"gbdt_threshold\\":\\"0.095\\"}","key_word":"morning","pop_type":"sticker","item_id":"3okipqjfyrxlghwvdk","lang":"en","na":"us","app":"4.8.2.1638","app_vcode":"163801","aid":"b75f9a2e689c576423f6f70f384615369177f1a3","os":"7.1.1","net":0},"ts":1523333338953}',
                '78472ddd7528bcacc15725a16aeec190,37dfbe888ef147c8a83b60588dc2da21,172.58.75.133,,1523333340,{"oid":"f8e87d8719babe02c284e18707d1284d","tp":"event","l":"keyboard_sticker2_suggestion_pop","iid":"send","otp":"item","value":0,"extra":{"package_name":"com.snapchat.android","realtime_event":"1","pop_delay":"0","kb_lang":"en_US","source":"recommend","kb_current_time":"1523333338","kb_time_zone":"-8","tags":"no","extra":"{\\"taghit\\":\\"hit\\",\\"bucketName\\":\\"KikaEnUsBeforeBucket\\",\\"product\\":\\"\\",\\"thresholdScore\\":\\"0.1\\",\\"language\\":\\"en\\",\\"recommend\\":\\"16:KikaEnUsBeforeBucket\\",\\"source\\":\\"CF\\",\\"sessionId\\":\\"sticker20682fae413211e894460670cf14ebd4\\",\\"bucket\\":\\"16:KikaEnUsBeforeBucket\\",\\"alg_hit\\":\\"1\\",\\"scenario\\":\\"KikaEnUsScenario\\",\\"cf_score\\":\\"0.9766543\\",\\"gbdt_threshold\\":\\"0.095\\"}","key_word":"no","pop_type":"sticker","item_id":"9855670","lang":"en","na":"us","app":"4.8.2.1638","app_vcode":"163801","aid":"b75f9a2e689c576423f6f70f384615369177f1a3","os":"7.1.1","net":0},"ts":1523333338953}',
                'e2934742f9d3b8ef2b59806a041ab389,32b4256f0c934e91aaf5f9201ccf4f54,172.58.75.133,,1523333340,{"oid":"f8e87d8719babe02c284e18707d1284d","tp":"event","l":"keyboard_sticker2_suggestion_pop","iid":"send","otp":"item","value":0,"extra":{"package_name":"com.snapchat.android","realtime_event":"1","pop_delay":"0","kb_lang":"en_US","source":"recommend","kb_current_time":"1523333338","kb_time_zone":"-8","tags":"yea","extra":"{\\"taghit\\":\\"hit\\",\\"bucketName\\":\\"EnUsBeforeMod2Bucket\\",\\"product\\":\\"\\",\\"thresholdScore\\":\\"0.1\\",\\"language\\":\\"en\\",\\"recommend\\":\\"5:EnUsBeforeMod2Bucket\\",\\"source\\":\\"CF\\",\\"sessionId\\":\\"sticker206dd044413211e894460670cf14ebd4\\",\\"bucket\\":\\"5:EnUsBeforeMod2Bucket\\",\\"alg_hit\\":\\"1\\",\\"scenario\\":\\"EnUsBeforeMod2Secnario\\",\\"cf_score\\":\\"0.9766543\\",\\"gbdt_threshold\\":\\"0.095\\"}","key_word":"yea","pop_type":"sticker","item_id":"9b302ee9-44dc-4647-a921-c92862e37735","lang":"en","na":"us","app":"4.8.2.1638","app_vcode":"163801","aid":"b75f9a2e689c576423f6f70f384615369177f1a3","os":"7.1.1","net":0},"ts":1523333338953}',
                'e2934742f9d3b8ef2b59806a041ab389,7bfe28fb712c4b2c9873d0b53458f6a8,172.58.75.133,,1523333340,{"oid":"f8e87d8719babe02c284e18707d1284d","tp":"event","l":"keyboard_sticker2_suggestion_pop","iid":"send","otp":"item","value":0,"extra":{"package_name":"com.snapchat.android","realtime_event":"1","pop_delay":"0","kb_lang":"en_US","source":"recommend","kb_current_time":"1523333338","kb_time_zone":"-8","tags":"thanks","extra":"{\\"taghit\\":\\"hit\\",\\"bucketName\\":\\"EnUsBeforeNotMod2GBDTMLeapBucket\\",\\"product\\":\\"\\",\\"thresholdScore\\":\\"0.1\\",\\"language\\":\\"en\\",\\"recommend\\":\\"7:EnUsBeforeNotMod2GBDTMLeapBucket\\",\\"source\\":\\"CF\\",\\"sessionId\\":\\"sticker20855412413211e894460670cf14ebd4\\",\\"bucket\\":\\"7:EnUsBeforeNotMod2GBDTMLeapBucket\\",\\"alg_hit\\":\\"1\\",\\"scenario\\":\\"EnUsBeforeNotMod2Scenario\\",\\"cf_score\\":\\"0.9766543\\",\\"gbdt_threshold\\":\\"0.095\\"}","key_word":"thanks","pop_type":"sticker","item_id":"l0myyda8s9ghznebm","lang":"en","na":"us","app":"4.8.2.1638","app_vcode":"163801","aid":"b75f9a2e689c576423f6f70f384615369177f1a3","os":"7.1.1","net":0},"ts":1523333338953}',
                'e2934742f9d3b8ef2b59806a041ab389,269145da9def4d52b85c7a4f2893678a,172.58.75.133,,1523333340,{"oid":"f8e87d8719babe02c284e18707d1284d","tp":"event","l":"keyboard_sticker2_suggestion_pop","iid":"send","otp":"item","value":0,"extra":{"package_name":"com.snapchat.android","realtime_event":"1","pop_delay":"0","kb_lang":"ms_MY","source":"recommend","kb_current_time":"1523333338","kb_time_zone":"-8","tags":"haha","extra":"{\\"taghit\\":\\"hit\\",\\"bucketName\\":\\"EnNotUsBeforeGBDTBucket\\",\\"product\\":\\"\\",\\"thresholdScore\\":\\"0.1\\",\\"language\\":\\"en\\",\\"recommend\\":\\"11:EnNotUsBeforeGBDTBucket\\",\\"source\\":\\"CF\\",\\"sessionId\\":\\"sticker20d3bec2413211e894460670cf14ebd4\\",\\"bucket\\":\\"11:EnNotUsBeforeGBDTBucket\\",\\"alg_hit\\":\\"1\\",\\"scenario\\":\\"EnNotUsBeforeScenario\\",\\"cf_score\\":\\"0.9766543\\",\\"gbdt_threshold\\":\\"0.095\\"}","key_word":"haha","pop_type":"sticker","item_id":"a21d5dcd-24c2-4b7d-be83-159b65811b43","lang":"en","na":"us","app":"4.8.2.1638","app_vcode":"163801","aid":"b75f9a2e689c576423f6f70f384615369177f1a3","os":"7.1.1","net":0},"ts":1523333338953}']
            message = random.choice(message_list)
            self.client(message)
