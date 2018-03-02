# -*- coding: utf-8 -*-
# __author__ = 'Gz'

# ------------服务压测内容设置------------
from locust import HttpLocust, TaskSet, task
from case_generate import Http_Test, config_reader
import random

# 放在引用前保证数据数量
test_data = config_reader('./test_case')
a = Http_Test(test_data)
all_data = a.url_keys_data()


# single_data = all_data[random.choice(range(len(all_data)))


class popup_test(TaskSet):
    @task(0)
    def popup(self):
        # self.client.header()
        header_online = {
            'User-Agent': 'com.qisiemoji.inputmethod/2021 (175b40b82dac4a5e95e3976cebccd7ac/78472ddd7528bcacc15725a16aeec190) Country/AU Language/en System/android Version/23 Screen/480',
            'Accept-Charset': 'UTF-8', 'Kika-Install-Time': '1503996692777', 'Accept-Encoding': 'gzip',
            'X-Model': 'D6603', 'If-Modified-Since': 'Mon, 04 Sep 2017 07:08:32 GMT', 'Accept-Language': 'en_AU',
            'Host': 'api.kikakeyboard.com', 'Connection': 'Keep-Alive'}
        header_test = {
            'User-Agent': 'com.qisiemoji.inputmethod/2021 (175b40b82dac4a5e95e3976cebccd7ac/78472ddd7528bcacc15725a16aeec190) Country/AU Language/en System/android Version/23 Screen/480',
            'Accept-Charset': 'UTF-8', 'Kika-Install-Time': '1503996692777', 'Accept-Encoding': 'gzip',
            'X-Model': 'D6603', 'If-Modified-Since': 'Mon, 04 Sep 2017 07:08:32 GMT', 'Accept-Language': 'en_AU',
            'Host': 'dev-api.kikakeyboard.com', 'Connection': 'Keep-Alive'}
        pop = self.client.get(
            'https://api.kikakeyboard.com/v1/stickers2/popup?tag=lol&kb_lang=en_AU&sign=87d6cf9df3294d23b6ac7d85b28d4491',
            headers=header_online, catch_response=True)
        # pop = self.client.get(
        #     'http://52.43.155.219:9090/backend-content-sending/popup?tag=lol&kb_lang=en_AU&sign=87d6cf9df3294d23b6ac7d85b28d4491',
        #     headers=header_test, catch_response=True)
        with pop as response:
            try:
                if response.json()['errorMsg'] != 'ok':
                    response.failure('wrong!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            except:
                pass
                # print(pop.json())

    @task(0)
    def baidu(self):
        url = 'https://www.baidu.com/'
        response = self.client.get(url)

    @task(0)
    def case(self):
        # 随机获取数据
        single_data = all_data[random.choice(range(len(all_data)))]
        fail = []
        if a.data == None or a.keys == None:
            url = a.url
            response = self.client.request('get', url)
        else:
            lang = single_data['kb_lang']
            duid = single_data['duid']
            app = single_data['app']
            version = int(single_data['version'])
            header = a.kika_request.set_header(duid, app=app, version=version, lang=lang, way=a.way)
            url = a.url_mosaic(single_data)
            response = self.client.get(url, headers=header, catch_response=True)
            a.asser_api(single_data, response, fail)
            if len(fail) == 0:
                response.success()
            else:
                response.failure(response.text)

    # 足迹
    @task(0)
    def kika_backend(self):
        all_duid = ['a694d52e2e824419b7531e07a702ca25', '0978f8ccd3394981ba4ace5c6335bca6',
                    '2f5011292c6849b79213c71221c84c78']
        duid = random.choice(all_duid)
        # url = "http://172.31.16.27:8080/v1/app/{}/device/test/event/recent_num_sticker?range=0-3".format(
        #     duid)
        # url = 'http://kika-data-blau-web0.intranet.com:8080/v1/app/4e5ab3a6d2140457e0423a28a094b1fd/device/{}/event/recent_tag_num_sticker?range=0-3&type=hola'.format(
        #     duid)
        url = 'http://kika-data-blau-web0.intranet.com:8080/v1/app/4e5ab3a6d2140457e0423a28a094b1fd/device/{}/event/recent_tag_num_sticker?range=0-3&type=hola'.format(
            duid)
        response = self.client.get(url)

    @task(10)
    # 强哥
    def kika_backend(self):
        # all_duid = ['a694d52e2e824419b7531e07a702ca25', '0978f8ccd3394981ba4ace5c6335bca6',
        #             '2f5011292c6849b79213c71221c84c78']
        all_duid = ['a9a22e4f665749339e00144a54316202', '573823d20e4e4315a166e8750473b374',
                    '2d1fcdfd9e86431396c67cf253f3243b', 'a24313e98acf47f39d77bc6e16b15c55',
                    'a790e9edf319431f95da10280062a213', 'da943175fab14edcbbd01a0ef84c73a9',
                    'ecc2ef0ec4312f17fd80dcda3ded72e9', 'd1cbb6f896d54b69b43132c2f69abfc3',
                    '8171eaca2a95437091e431453a3a5770', 'a027df07407c4e6bbe7d4312cd9b3778']
        duid = random.choice(all_duid)
        # url = "http://172.31.16.27:8080/v1/app/{}/device/test/event/recent_num_sticker?range=0-3".format(
        #     duid)
        # url = 'http://kika-data-blau-web0.intranet.com:8080/v1/app/4e5ab3a6d2140457e0423a28a094b1fd/device/{}/event/recent_tag_num_sticker?range=0-3&type=hola'.format(
        #     duid)
        # url = 'http://172.31.23.134:8080/model-sticker/recommend/popup?userId={}&tag=lol&sessionId=123&language=en&type=0&country=us&mod=not2'.format(
        #     duid)

        url = 'http://52.43.155.219:8080/model-sticker/recommend/popup?userId={}&tag=lol&sessionId=123&language=en&type=0&country=us&mod=not2'.format(
            duid)
        response = self.client.get(url)
        print(response.text)


class MyLocust(HttpLocust):
    task_set = popup_test
    # 任务的最小等待时间单位ms
    min_wait = 100
    # 任务的最大等待时间单位ms
    max_wait = 1000
    # host = 'api.kikakeyboard.com'
    # host = 'blau.kika-backend.com'
    host = 'kika-data-blau-web0.intranet.com'
