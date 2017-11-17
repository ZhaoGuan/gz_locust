# -*- coding: utf-8 -*-
# __author__ = 'Gz'

# ------------服务压测内容设置------------
from locust import HttpLocust, TaskSet, task
from case_generate import Http_Test, config_reader, get_duid_in_way
import random

# 放在引用前保证数据数量
test_data = config_reader('./test_case')
a = Http_Test(test_data)
all_data = a.url_keys_data()


# single_data = all_data[random.choice(range(len(all_data)))]


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

    @task(10)
    def case(self):
        # 随机获取数据
        single_data = all_data[random.choice(range(len(all_data)))]
        fail = []
        if a.data == None or a.keys == None:
            url = a.url
            response = self.client.get(url, catch_response=True)
        else:
            lang = single_data['kb_lang']
            duid = single_data['duid']
            app = single_data['app']
            header = a.set_header(duid, app=app, version=a.version, lang=lang, way=a.way)
            url = a.url_mosaic(single_data)
            response = self.client.get(url, headers=header, catch_response=True)
            if a.asser_api(single_data, response, fail) is True:
                response.success()
            else:
                response.failure(response.text)


class MyLocust(HttpLocust):
    task_set = popup_test
    # 任务的最小等待时间单位ms
    min_wait = 100
    # 任务的最大等待时间单位ms
    max_wait = 1000
    host = 'api.kikakeyboard.com'

    # if __name__=="__main__":
    #     print(os.path.dirname(os.path.abspath(__file__)))
