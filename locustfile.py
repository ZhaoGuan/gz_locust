# -*- coding: utf-8 -*-
# __author__ = 'Gz'
from locust import HttpLocust, TaskSet, task


class popup_test(TaskSet):
    @task(1)
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
        # pop = self.client.get(
        #     'https://api.kikakeyboard.com/v1/stickers2/popup?tag=lol&kb_lang=en_AU&sign=87d6cf9df3294d23b6ac7d85b28d4491',
        #     headers=header_online, catch_response=True)
        pop = self.client.get(
            'http://52.43.155.219:9090/backend-content-sending/popup?tag=lol&kb_lang=en_AU&sign=87d6cf9df3294d23b6ac7d85b28d4491',
            headers=header_test, catch_response=True)
        with pop as response:
            if response.json()['errorMsg'] != 'ok':
                response.failure('wrong!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print(pop.json())

        # @task(10)
        # def baidu(self):
        #     url = 'https://www.baidu.com/'
        #     response = self.client.get(url)


#


class MyLocust(HttpLocust):
    task_set = popup_test
    # 任务的最小等待时间单位ms
    # min_wait = 500
    # 任务的最大等待时间单位ms
    # max_wait = 2000
