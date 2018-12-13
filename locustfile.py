# -*- coding: utf-8 -*-
# __author__ = 'Gz'

# ------------服务压测内容设置------------
from locust import HttpLocust, TaskSet, task
import os
import random
import time
import uuid
import datetime
from basics_function.wuren_locust import HttpTest
from basics_function.golable_function import MD5, config_reader

PATH = os.path.dirname(os.path.abspath(__file__))

user_datas = [{'duid': '20181212-82e26ba4-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'ddc1739e674d471d9851ac93c3ee24a6'},
              {'duid': '20181212-82e889a8-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'a11fb13d31be4d5e8e8482594544f54d'},
              {'duid': '20181212-82eda0a0-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '5ef6ee5bcfc345ff9317921cd53d6be6'},
              {'duid': '20181212-82f27396-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '2fca601373534a5bac6bf6a96f5cfeb8'},
              {'duid': '20181212-82f7a0aa-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '5e451c27259c482ab67126184019bce2'},
              {'duid': '20181212-82fc4d76-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'e82eab190836449c92c815a6798f85b7'},
              {'duid': '20181212-83011af4-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '068e5239a130439394882275581c9c99'},
              {'duid': '20181212-8305fd08-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '1006d2ade7784a8f8da8a80a9ed0e76e'},
              {'duid': '20181212-830aeba6-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '0bdc16aad0104cd6b38028a4883e9d89'},
              {'duid': '20181212-830faf1a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '863738932fa142b2aa88b26c62e446f0'},
              {'duid': '20181212-83149f48-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '74e2a3f40b434bdfa4749c27f5a98acd'},
              {'duid': '20181212-831943fe-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'c6579dc27a614a559caa4898efd383df'},
              {'duid': '20181212-831e3f9e-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'f3b05ec5fb4f4bde8ba911d1e1c7407d'},
              {'duid': '20181212-83231f82-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'c5fd54e1d55e4e1b91a8f9cc0ad29a14'},
              {'duid': '20181212-8328272a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '2397fb60dd0b49fa9e49cf21432a2068'},
              {'duid': '20181212-832d0b3c-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '28fef731a30143b0a305b5bef51d6b10'},
              {'duid': '20181212-8331dae0-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '8fe71810401f4d68878b4d4b9bf5159d'},
              {'duid': '20181212-8336a9f8-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'e486222e3a354e1e89b02cdb7730ac63'},
              {'duid': '20181212-833b7870-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '9f49821b7ca74ff19be928e4793e76bd'},
              {'duid': '20181212-83403d06-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '2d1d3f3d417748d38ca4b11e1eebcf3d'},
              {'duid': '20181212-834555c0-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '34feca134c4647bc809768397bd6b482'},
              {'duid': '20181212-834a516a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '5cbc716039bb46ec9f9a271a3e500c0c'},
              {'duid': '20181212-834f53a4-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '7525500a23d0413ca25a947c1748b036'},
              {'duid': '20181212-8354aa0c-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '4f42028664514a499f5bc9b994b726ae'},
              {'duid': '20181212-8359ce24-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '6cbd8a7ceb0842b28dd9a4a9d9307aa2'},
              {'duid': '20181212-835ed8a6-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'a9f75b3daad34b9086117259d19e3680'},
              {'duid': '20181212-8364593e-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '32ca10ccf8a0471a8c59c92bdde927dc'},
              {'duid': '20181212-8369551a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '58b0254f35644743973c677241394188'},
              {'duid': '20181212-836e7806-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'e7e1dc9acf53436db94e66edb735a94b'},
              {'duid': '20181212-83735bbe-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'd87c56dd9a5d42f4b4f8b63a79dac17f'},
              {'duid': '20181212-837864a6-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'be12d86b53a2434c9b4d8bbcb4b9e5dc'},
              {'duid': '20181212-837d2e46-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '88d4aa0a3b1e40f9b180d4552c210f9d'},
              {'duid': '20181212-8382787e-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '417797135d59428ab4e0bc1966b6472b'},
              {'duid': '20181212-8387c7c0-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'bc70ac1f66ce4deda64c486ab1de166c'},
              {'duid': '20181212-838cd7ec-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'cb009cbc5ed14853ad84f8208c9aa6d3'},
              {'duid': '20181212-8391fd08-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '4f1d19798c4049ada8252b7daf05b4b6'},
              {'duid': '20181212-839773d2-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'eb417ff09f4a4a1db435b262d0ff1c88'},
              {'duid': '20181212-839c5a5a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '397b3f024d0c4a9bbedf70d417c775a7'},
              {'duid': '20181212-83a1bea0-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '5b5d9cd1f6454de48e47d74bc5187008'},
              {'duid': '20181212-83a6bd1a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '561f23e11d5145a3b7d58ca6fab3ffdf'},
              {'duid': '20181212-83abb842-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'f94369450b494e779c595873ff26f4a1'},
              {'duid': '20181212-83b125d4-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'ca6ef1a094824fada2d13e7bf8cc52d0'},
              {'duid': '20181212-83b614f4-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'b2ac91a7647c44329ec6decfb5e1d07d'},
              {'duid': '20181212-83bb4320-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '56d18bfe15ab447d91df749d9835eaab'},
              {'duid': '20181212-83c025fc-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '3d6e251a4f424dcebcbf044182deb82f'},
              {'duid': '20181212-83c53eb6-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '5d67f98038424f5192ce2dcd72a2f749'},
              {'duid': '20181212-83ca70de-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '208467708d9445348bd9f17ea7ee7448'},
              {'duid': '20181212-83cf627e-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'c319b8bdb03543ffb1354c0792acfbaa'},
              {'duid': '20181212-83d6f084-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '9d550ca7082d4d93a63e848fe30e3a9a'},
              {'duid': '20181212-83dc5c4a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '400f138075d146c79d452bd4bf4a950e'},
              {'duid': '20181212-83e1d490-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '66dd5f47119f4871ae100cf19fb59fca'},
              {'duid': '20181212-83e8417c-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '163705e0bc034266a0f4d90009e26d6b'},
              {'duid': '20181212-83ed98c0-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '6d11a03591374622b011cd482221486e'},
              {'duid': '20181212-83f29a3c-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '7f76d0e729fc4490a860b48b8acec10d'},
              {'duid': '20181212-83f80b7a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'a0bc4d14e2414804bf918f97fbc6fe1c'},
              {'duid': '20181212-83fd6dae-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'b064648d32bd49888372c89da77b4d6e'},
              {'duid': '20181212-84028316-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'ccb666f468ee452883107ecc896729af'},
              {'duid': '20181212-84078636-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'be7007fe1504498982042806c645aa83'},
              {'duid': '20181212-840c6976-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'b8743f22951c4914bb972e7466735f6c'},
              {'duid': '20181212-84117056-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '1337ff1d202c4e22bc2b14ecdc48d713'},
              {'duid': '20181212-84168cbc-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'c7f048b9ecfa424d9f2576f66126189b'},
              {'duid': '20181212-841b625a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '1d42163e8bfa446691dd587cee19a67b'},
              {'duid': '20181212-84205c60-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'b6fb04afb7014fc6a4aa41b9d38af492'},
              {'duid': '20181212-842536a4-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '0d641f18a09341f9a26d026a380961a6'},
              {'duid': '20181212-842a29f2-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '2203d705444f4bce99a2124e805ddc76'},
              {'duid': '20181212-842f111a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'ad1da13793224306a8dc14851dbf8bd2'},
              {'duid': '20181212-84342ba0-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '45d96a6d339f429cb68286a13f9643d1'},
              {'duid': '20181212-84395ae4-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '623958674e664de0a5942abcfe65af88'},
              {'duid': '20181212-843ecb0a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'aca426053df741cb9271a30b754f9e73'},
              {'duid': '20181212-8443b804-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'de17a64c473547dcbce47e93ad75d042'},
              {'duid': '20181212-8448b8e0-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '49da1f835b4c4ba39cf10bbcfb956167'},
              {'duid': '20181212-844dbffc-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '5f220426af59400f9991930b99003c5a'},
              {'duid': '20181212-84530a2a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '0e9a0f57cc7b4faca72fbf57b77c87ac'},
              {'duid': '20181212-8457d2da-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '1e10942e0e5a4805bc0d21d3ee159ae5'},
              {'duid': '20181212-845d0f0c-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'e96d319210a24355b33c5306cf355bb4'},
              {'duid': '20181212-84621e98-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'c7c9e6a8eb32454e9db847b2107b6f45'},
              {'duid': '20181212-84677884-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'e900fad9ddfa4c83b739596bd8c3d4ef'},
              {'duid': '20181212-846c774e-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '50ae409b72e94fb281b5d43a790f247e'},
              {'duid': '20181212-84717b04-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'd6e52a0510f34d6eac6d90713cc67b9a'},
              {'duid': '20181212-8476b2ae-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'bda3a388778041ee9e0d9fb0ac859fff'},
              {'duid': '20181212-847be166-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '8acdc4a975664a4b85ca9e5e5ab174f9'},
              {'duid': '20181212-8480c9d8-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'db74ac9a7a45424fa891ace52e9f14f2'},
              {'duid': '20181212-848644c6-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'c52df1e41c714ff0a13ea1a9498d590a'},
              {'duid': '20181212-848b315c-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '3e8a1c388a6b49fbb12bf7968a06a5f3'},
              {'duid': '20181212-849021bc-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'ee16db0a78574916b23185eeca18a164'},
              {'duid': '20181212-8494f7b4-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '74cabe49470c4e8da49b08ea312442d5'},
              {'duid': '20181212-8499f980-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'f5af40ece6a74ef29cd177573d7e514d'},
              {'duid': '20181212-849ee850-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '3f9881f8c7b84f48a2ced2bd6f32d582'},
              {'duid': '20181212-84a3dde2-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'eb38573781d448c48aefdfbfe593f18e'},
              {'duid': '20181212-84a8c3d4-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '0a35cae432d0446993f3d9fe86127cb6'},
              {'duid': '20181212-84adba24-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '73f5827bcf154aeead83b05eecbd92a4'},
              {'duid': '20181212-84b2a85e-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'b36d8160b6b84e4c8a24d7088f9c2c0c'},
              {'duid': '20181212-84b7d9f0-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'b56eabb0386f4256abfa38b1f39ce019'},
              {'duid': '20181212-84bca444-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '5d16b37f40e44dbe9e3c8435477d2070'},
              {'duid': '20181212-84c170d2-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '1c4eb65df3ee44a485d1aa10411a1fee'},
              {'duid': '20181212-84c65c0a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '1f7aed11b5ce4de7b017b8e5fc297cf9'},
              {'duid': '20181212-84cdbefa-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '001f93ff1e42446ba3d9d0ea5028f4fb'},
              {'duid': '20181212-84d2ab68-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'a0d51a095a4d4a35bfe2d4eca99d2f17'}]

source = "online"
today = datetime.date.today().strftime("%Y%m%d")


def true_requets(client, case_data):
    HT = HttpTest(case_data, source)
    case = HT.case_data()
    data = HT.url_request_data(random.choice(case))
    request_header = data["request_header"]
    body = data["body"]
    request_type = data["request_type"]
    url = data["url"]
    if request_type == "post":
        response = client.post(url=url, headers=request_header, json=body, catch_response=True)
    else:
        response = client.get(url=url, headers=request_header, catch_response=True)
    print(response.json())
    print(response.status_code)
    if response.status_code == 200 and response.json()["errorMsg"] != "ok":
        response.failure("errorMsg is Fail" + str(response.json()))
    else:
        response.success()
    print(request_header)
    print(response.json())


class WuRen(TaskSet):

    @task(0)
    def login(self):
        user_data = random.choice(user_datas)
        duid = user_data['duid']
        token = user_data['token']
        case_data = {'data': {'OPERATION_MODE': 'single', 'SOURCE': {
            'online': {'URL': 'https://api.5nuthost.com/v1/identity/login',
                       'HEADERS': {'TYPE': '5NUT',
                                   'DATA': {'version': [1477],
                                            'duid': [duid],
                                            'lang': ['en_US']}},
                       'PARAMS': {'TYPE': 'NORMAL',
                                  'DATA': None},
                       'MODE': {'TYPE': 'POST'},
                       'BODY': {'TYPE': 'JSON',
                                'FUNCTION': '5NUT_sigin',
                                'DATA': {"token": [token]}}}}}}
        # true_requets(self.client, case_data)
        HT = HttpTest(case_data, source)
        case = HT.case_data()
        data = HT.url_request_data(random.choice(case))
        request_header = data["request_header"]
        body = data["body"]
        request_type = data["request_type"]
        url = data["url"]
        if request_type == "post":
            response = self.client.post(url=url, headers=request_header, json=body, catch_response=True)
        else:
            response = self.client.get(url=url, headers=request_header, catch_response=True)
        print(response.json())
        print(response.status_code)
        if response.status_code == 200 and response.json()["errorMsg"] != "ok":
            response.failure("errorMsg is Fail")
        else:
            response.success()
        print(request_header)
        print(response.json())

    @task(0)
    def search_hot(self):
        user_data = random.choice(user_datas)
        duid = user_data['duid']
        token = user_data['token']
        case_data = {'data': {'OPERATION_MODE': 'single', 'SOURCE': {
            'test': {'URL': 'http://api.dev.wuren.com:8080/v1/app/meme/search/hot',
                     'HEADERS': {'TYPE': '5NUT', 'DATA': {'version': [1477], 'duid': ['gztest'], 'lang': ['en_US']}},
                     'PARAMS': {'TYPE': 'NORMAL', 'DATA': None}, 'MODE': {'TYPE': 'POST'},
                     'BODY': {'TYPE': 'JSON', 'FUNCTION': '5NUT', 'DATA': None}},
            'online': {'URL': 'https://api.5nuthost.com/v1/app/meme/search/hot',
                       'HEADERS': {
                           'TYPE': '5NUT',
                           'DATA': {
                               'version': [1477],
                               'duid': [duid],
                               'lang': ['en_US']}},
                       'PARAMS': {'TYPE': 'NORMAL',
                                  'DATA': None},
                       'MODE': {'TYPE': 'POST'},
                       'BODY': {'TYPE': 'JSON',
                                'FUNCTION': '5NUT',
                                'DATA': {"token": [token]}}}},
                              'DATA_FORMAT': {'TYPE': 'ONLY',
                                              'EXTRA': {'LIST_REPEATED': False},
                                              'DATA': {'errorCode': 'Str', 'errorMsg': 'Str',
                                                       'info': {'hot_word': ['Str']}}}, 'DATA_CONTENT': None,
                              'RESPONSE_HEADER': None, 'THE_FLOWING': None,
                              'THE_ABOVE': {'TYPE': 'BODY', 'KEY': None, 'DATA': 'info/group_list/^/title'}},
                     'path': './case/search/search_hot.yml'}
        true_requets(self.client, case_data)

    @task(0)
    def search_fall(self):
        user_data = random.choice(user_datas)
        duid = user_data['duid']
        token = user_data['token']
        case_data = {'data': {'OPERATION_MODE': 'single', 'SOURCE': {
            'test': {'URL': 'http://api.dev.wuren.com:8080/v1/app/meme/search/fall',
                     'HEADERS': {'TYPE': '5NUT', 'DATA': {'version': [1477], 'duid': ['gztest'], 'lang': ['en_US']}},
                     'PARAMS': {'TYPE': 'NORMAL', 'DATA': None}, 'MODE': {'TYPE': 'POST'},
                     'BODY': {'TYPE': 'JSON', 'FUNCTION': '5NUT', 'DATA': {'id': ['0'], 'limit': [20]}}},
            'online': {'URL': 'https://api.5nuthost.com/v1/app/meme/search/fall',
                       'HEADERS': {'TYPE': '5NUT',
                                   'DATA': {'version': [1477],
                                            'duid': [duid],
                                            'lang': ['en_US']}},
                       'PARAMS': {'TYPE': 'NORMAL', 'DATA': None}, 'MODE': {'TYPE': 'POST'},
                       'BODY': {'TYPE': 'JSON', 'FUNCTION': '5NUT',
                                'DATA': {'id': ['0'],
                                         'limit': [20],
                                         'token': [token]}}}},
                              'DATA_FORMAT': {'TYPE': 'ONLY', 'DATA': {'errorCode': 'Str', 'errorMsg': 'Str', 'info': {
                                  'pic_list': [{'tiny': {'url': 'HTTP', 'height': 'Int', 'width': 'Int', 'size': 'Int'},
                                                'origin': {'url': 'HTTP', 'height': 'Int', 'width': 'Int',
                                                           'size': 'Int'}, 'item_id': 'Str', 'id': 'Str'}]}}},
                              'DATA_CONTENT': None, 'RESPONSE_HEADER': None, 'THE_FLOWING': None,
                              'THE_ABOVE': {'TYPE': 'BODY', 'KEY': None, 'DATA': 'info/group_list/^/title'}},
                     'path': './case/search/search_fall.yml'}
        true_requets(self.client, case_data)

    @task(0)
    def search_home(self):
        user_data = random.choice(user_datas)
        duid = user_data['duid']
        token = user_data['token']
        case_data = {'data': {'OPERATION_MODE': 'single', 'SOURCE': {
            'test': {'URL': 'http://api.dev.wuren.com:8080/v1/app/meme/search/home',
                     'HEADERS': {'TYPE': '5NUT', 'DATA': {'version': [1477], 'duid': ['gztest'], 'lang': ['en_US']}},
                     'PARAMS': {'TYPE': 'NORMAL', 'DATA': None}, 'MODE': {'TYPE': 'POST'},
                     'BODY': {'TYPE': 'JSON', 'FUNCTION': '5NUT',
                              'DATA': {'search': ['Assembly'], 'index': [20], 'limit': [20]}}},
            'online': {'URL': 'https://api.5nuthost.com/v1/app/meme/search/home',
                       'HEADERS': {'TYPE': '5NUT', 'DATA': {'version': [1477],
                                                            'duid': [duid],
                                                            'lang': ['en_US']}},
                       'PARAMS': {'TYPE': 'NORMAL', 'DATA': None}, 'MODE': {'TYPE': 'POST'},
                       'BODY': {'TYPE': 'JSON', 'FUNCTION': '5NUT',
                                'DATA': {'search': ['Assembly', "be cool", "ok", 'yes', "good"],
                                         'token': [token],
                                         'index': [0, 10, 20, 40],
                                         'limit': [20]}}}},
                              'DATA_FORMAT': {'TYPE': 'ONLY', 'DATA': {'errorCode': 'Str', 'errorMsg': 'Str', 'info': {
                                  'pic_list': [{'item_id': 'Str',
                                                'tiny': {'url': 'HTTP', 'height': 'Int', 'width': 'Int', 'size': 'Int'},
                                                'origin': {'url': 'HTTP', 'height': 'Int', 'width': 'Int',
                                                           'size': 'Int'}}]}}}, 'DATA_CONTENT': None,
                              'RESPONSE_HEADER': None, 'THE_FLOWING': None,
                              'THE_ABOVE': {'TYPE': 'BODY', 'KEY': None, 'DATA': 'info/group_list/^/title'}},
                     'path': './case/search/search_home.yml'}
        true_requets(self.client, case_data)

    @task(0)
    def create_category(self):
        user_data = random.choice(user_datas)
        duid = user_data['duid']
        token = user_data['token']
        case_data = {'data': {'OPERATION_MODE': 'single', 'SOURCE': {
            'test': {'URL': 'http://api.dev.wuren.com:8080/v1/app/meme/create/category',
                     'HEADERS': {'TYPE': '5NUT', 'DATA': {'version': [1477], 'duid': ['gztest'], 'lang': ['en_US']}},
                     'PARAMS': {'TYPE': 'NORMAL', 'DATA': None}, 'MODE': {'TYPE': 'POST'},
                     'BODY': {'TYPE': 'JSON', 'FUNCTION': '5NUT', 'DATA': None}},
            'online': {'URL': 'https://api.5nuthost.com/v1/app/meme/create/category',
                       'HEADERS': {'TYPE': '5NUT', 'DATA': {'version': [1477], 'duid': [duid], 'lang': ['en_US']}},
                       'PARAMS': {'TYPE': 'NORMAL', 'DATA': None}, 'MODE': {'TYPE': 'POST'},
                       'BODY': {'TYPE': 'JSON', 'FUNCTION': '5NUT', 'DATA': {"token": [token]}}},
            'DATA_FORMAT': {'TYPE': 'ONLY',
                            'DATA': {'errorCode': '0', 'errorMsg': 'Str',
                                     'info': {'category': ['Str']}}},
            'DATA_CONTENT': None, 'RESPONSE_HEADER': None,
            'THE_FLOWING': 'meme/content_create_home.yml', 'THE_ABOVE': {'DATA': 'info/category^'}},
                              'path': './case/meme/create_category.yml'}}
        true_requets(self.client, case_data)

    @task(0)
    def create_home(self):
        user_data = random.choice(user_datas)
        duid = user_data['duid']
        token = user_data['token']
        case_data = {'data': {'OPERATION_MODE': 'content', 'SOURCE': {
            'test': {'URL': 'http://api.dev.wuren.com:8080/v1/app/meme/create/home',
                     'HEADERS': {'TYPE': '5NUT', 'DATA': {'version': ['1.0.0'], 'duid': ['gztest'], 'lang': ['en_US']}},
                     'PARAMS': {'TYPE': 'NORMAL', 'DATA': None}, 'MODE': {'TYPE': 'POST'},
                     'BODY': {'TYPE': 'JSON', 'FUNCTION': '5NUT',
                              'DATA': {'category': ['test'], 'index': [0], 'limit': [20]}}},
            'online': {'URL': 'https://api.5nuthost.com/v1/app/meme/create/home',
                       'HEADERS': {'TYPE': '5NUT', 'DATA': {
                           'version': ['1.0.0'], 'duid': [duid], 'lang': ['en_US']}},
                       'PARAMS': {'TYPE': 'NORMAL', 'DATA': None}, 'MODE': {'TYPE': 'POST'},
                       'BODY': {'TYPE': 'JSON', 'FUNCTION': '5NUT',
                                'DATA': {"token": [token], 'category': ['all'], 'index': [0, 10, 20], 'limit': [10]}}}},
                              'DATA_FORMAT': {'TYPE': 'ONLY', 'EXTRA': {'LIST_REPEATED': False, 'LIST_EMPTY': False},
                                              'DATA': {'errorCode': 'Str', 'errorMsg': 'Str', 'info': {'group_list': [
                                                  {'title': 'Str', 'pic_list': [{'item_id': 'Str',
                                                                                 'tiny': {'url': 'HTTP',
                                                                                          'height': 'Int',
                                                                                          'width': 'Int',
                                                                                          'size': 'Int'},
                                                                                 'origin': {'url': 'HTTP',
                                                                                            'height': 'Int',
                                                                                            'width': 'Int',
                                                                                            'size': 'Int'},
                                                                                 'descriptions': [{'top': 'Str|null',
                                                                                                   'bottom': 'Str|null'}]}]}]}}},
                              'DATA_CONTENT': None, 'RESPONSE_HEADER': None,
                              'THE_FLOWING': 'meme/content_create_list.yml',
                              'THE_ABOVE': {'DATA': 'info/group_list/^/title'}}, 'path': './case/meme/create_home.yml'}
        true_requets(self.client, case_data)

    @task(10)
    def create_list(self):
        user_data = random.choice(user_datas)
        duid = user_data['duid']
        token = user_data['token']
        case_data = {'data': {'OPERATION_MODE': 'content', 'SOURCE': {
            'test': {'URL': 'http://api.dev.wuren.com:8080/v1/app/meme/create/list',
                     'HEADERS': {'TYPE': '5NUT', 'DATA': {'version': [1477], 'duid': ['gztest'], 'lang': ['en_US']}},
                     'PARAMS': {'TYPE': 'NORMAL', 'DATA': None}, 'MODE': {'TYPE': 'POST'},
                     'BODY': {'TYPE': 'JSON', 'FUNCTION': '5NUT', 'DATA': {'title': ['baby']}}},
            'online': {'URL': 'https://api.5nuthost.com/v1/app/meme/create/list',
                       'HEADERS': {'TYPE': '5NUT', 'DATA': {'version': [1477], 'duid': [duid], 'lang': ['en_US']}},
                       'PARAMS': {'TYPE': 'NORMAL', 'DATA': None}, 'MODE': {'TYPE': 'POST'},
                       'BODY': {'TYPE': 'JSON', 'FUNCTION': '5NUT',
                                'DATA': {'token': [token],
                                         'title': ['be smart', 'cat', "confused", "dafuq", "dog", "grandma",
                                                   "give up", "election", "dumb"]}}}},
                              'DATA_FORMAT': {'TYPE': 'ONLY', 'DATA': {'errorCode': 'Str', 'errorMsg': 'Str', 'info': {
                                  'pic_list': [{'item_id': 'Str',
                                                'tiny': {'url': 'HTTP', 'height': 'Int', 'width': 'Int', 'size': 'Int'},
                                                'origin': {'url': 'HTTP', 'height': 'Int', 'width': 'Int',
                                                           'size': 'Int'},
                                                'descriptions': [{'top': 'Str', 'bottom': 'Str'}]}]}}},
                              'DATA_CONTENT': None, 'RESPONSE_HEADER': None, 'THE_FLOWING': None,
                              'THE_ABOVE': {'TYPE': 'BODY', 'KEY': 'title', 'DATA': 'info/group_list/^/title'}},
                     'path': './case/meme/create_list.yml'}
        true_requets(self.client, case_data)

    @task(0)
    def create_template(self):
        user_data = random.choice(user_datas)
        duid = user_data['duid']
        token = user_data['token']
        case_data = {'data': {'OPERATION_MODE': 'single', 'SOURCE': {
            'test': {'URL': 'http://api.dev.wuren.com:8080/v1/app/meme/create/template',
                     'HEADERS': {'TYPE': '5NUT', 'DATA': {'version': ['1.0.0'], 'duid': ['gztest'], 'lang': ['en_US']}},
                     'PARAMS': {'TYPE': 'NORMAL', 'DATA': None}, 'MODE': {'TYPE': 'POST'},
                     'BODY': {'TYPE': 'JSON', 'FUNCTION': '5NUT',
                              'DATA': {'itemId': ['6e55a422a6e716099855fa6e635c4046']}}},
            'online': {'URL': 'https://api.5nuthost.com/v1/app/meme/create/template',
                       'HEADERS': {'TYPE': '5NUT',
                                   'DATA': {'version': ['1.0.0'],
                                            'duid': [duid],
                                            'lang': ['en_US']}},
                       'PARAMS': {'TYPE': 'NORMAL', 'DATA': {
                           'itemId': ['6e55a422a6e716099855fa6e635c4046', "e22035b3493667e5ee407b04f6d36ba5",
                                      "7554e5ba2dd05b0989a20e6420da71ae", "aff362bd018860d154e8781447da9491",
                                      "aaa39926c9c2a0a9e25eac85016a7ea7", "a9e4204848196084b9bdc534c46fdc9d"]}},
                       'MODE': {'TYPE': 'POST'}, 'BODY': {'TYPE': 'JSON', 'FUNCTION': '5NUT',
                                                          'DATA': {"token": token,
                                                                   'itemId': ['6e55a422a6e716099855fa6e635c4046']}}}},
                              'DATA_FORMAT': {'TYPE': 'ONLY', 'EXTRA': {'LIST_REPEATED': False, 'LIST_EMPTY': False,
                                                                        'URL_FROM': '5nuthost.com'},
                                              'DATA': {'errorCode': 'Str', 'errorMsg': 'Str', 'info': {'itemId': 'Str',
                                                                                                       'origin': {
                                                                                                           'url': 'HTTP',
                                                                                                           'height': 'Int',
                                                                                                           'width': 'Int',
                                                                                                           'size': 'Int'},
                                                                                                       'descriptions': [
                                                                                                           {
                                                                                                               'top': 'Str',
                                                                                                               'bottom': 'Str'}]}}},
                              'DATA_CONTENT': None, 'RESPONSE_HEADER': None,
                              'THE_FLOWING': 'meme/content_create_list.yml',
                              'THE_ABOVE': {'DATA': 'info/group_list/^/title'}},
                     'path': './case/meme/create_template.yml'}
        true_requets(self.client, case_data)

    @task(0)
    def user_upload(self):
        user_data = random.choice(user_datas)
        duid = user_data['duid']
        token = user_data['token']
        case_data = {'data': {'OPERATION_MODE': 'single', 'SOURCE': {
            'test': {'URL': 'http://api.dev.wuren.com:8080/v1/app/meme/user/upload',
                     'HEADERS': {'TYPE': '5NUT', 'DATA': {'version': [1477], 'duid': ['gztest'], 'lang': ['en_US']}},
                     'PARAMS': {'TYPE': 'NORMAL', 'DATA': None}, 'MODE': {'TYPE': 'POST'},
                     'BODY': {'TYPE': 'JSON', 'FUNCTION': '5NUT', 'DATA': {'pic_infos': [[{'info': 'test',
                                                                                           'origin_id': 'test',
                                                                                           'url': 'https://imgflip.com/s/meme/The-Most-Interesting-Man-In-The-World.jpg'}]]}}},
            'online': {'URL': 'https://api.5nuthost.com/v1/app/meme/user/upload',
                       'HEADERS': {'TYPE': '5NUT', 'DATA': {'version': [1477], 'duid': [duid], 'lang': ['en_US']}},
                       'PARAMS': {'TYPE': 'NORMAL', 'DATA': None}, 'MODE': {'TYPE': 'POST'},
                       'BODY': {'TYPE': 'JSON', 'FUNCTION': '5NUT',
                                'DATA': {
                                    "token": [token],
                                    'pic_infos':
                                        [[{'info': 'test',
                                           'origin_id': 'test',
                                           'url': 'http://pic.cdn.5nuthost.com/imgflip/Joe_Biden.jpg'}],
                                         [{'info': 'test',
                                           'origin_id': 'test',
                                           'url': 'http://pic.cdn.5nuthost.com/imgflip/Barack_And_Kumar_2013.jpg'}],
                                         [{'info': 'test',
                                           'origin_id': 'test',
                                           'url': 'http://pic.cdn.5nuthost.com/imgflip/Baromney.jpg'}],
                                         [{'info': 'test',
                                           'origin_id': 'test',
                                           'url': 'http://pic.cdn.5nuthost.com/imgflip/Obama_Romney_Pointing.jpg'}],
                                         [{'info': 'test',
                                           'origin_id': 'test',
                                           'url': 'http://pic.cdn.5nuthost.com/imgflip/Maroney_And_Obama_Not_Impressed.jpg'}],
                                         [{'info': 'test',
                                           'origin_id': 'test',
                                           'url': 'http://pic.cdn.5nuthost.com/imgflip/Obama_Cowboy_Hat.jpg'}],
                                         [{'info': 'test',
                                           'origin_id': 'test',
                                           'url': 'http://pic.cdn.5nuthost.com/imgflip/Bubba_And_Barack.jpg'}],
                                         [{'info': 'test',
                                           'origin_id': 'test',
                                           'url': 'http://pic.cdn.5nuthost.com/imgflip/Bart_Simpson_Peeking.jpg'}],
                                         [{'info': 'test',
                                           'origin_id': 'test',
                                           'url': 'http://pic.cdn.5nuthost.com/imgflip/Not_Bad_Obama.jpg'}],
                                         [{'info': 'test',
                                           'origin_id': 'test',
                                           'url': 'http://pic.cdn.5nuthost.com/imgflip/Obama_No_Listen.jpg'}],
                                         [{'info': 'test',
                                           'origin_id': 'test',
                                           'url': 'http://pic.cdn.5nuthost.com/imgflip/And_then_I_said_Obama.jpg'}],
                                         [{'info': 'test',
                                           'origin_id': 'test',
                                           'url': 'http://pic.cdn.5nuthost.com/imgflip/Pissed_Off_Obama.jpg'}],
                                         [{'info': 'test',
                                           'origin_id': 'test',
                                           'url': 'http://pic.cdn.5nuthost.com/imgflip/First_World_Problems.jpg'}],
                                         [{'info': 'test',
                                           'origin_id': 'test',
                                           'url': 'http://pic.cdn.5nuthost.com/imgflip/Angry_Chef_Gordon_Ramsay.jpg'}]]}}}},
                              'DATA_FORMAT': {'TYPE': 'ONLY', 'DATA': {'errorCode': '0', 'errorMsg': 'ok', 'info': {}}},
                              'DATA_CONTENT': None, 'RESPONSE_HEADER': None}, 'path': './case/meme/!user_upload.yml'}
        true_requets(self.client, case_data)

    @task(0)
    def user_list(self):
        user_data = random.choice(user_datas)
        duid = user_data['duid']
        token = user_data['token']
        case_data = {'data': {'OPERATION_MODE': 'single', 'SOURCE': {
            'test': {'URL': 'http://api.dev.wuren.com:8080/v1/app/meme/user/list',
                     'HEADERS': {'TYPE': '5NUT', 'DATA': {'version': [1477], 'duid': ['gztest'], 'lang': ['en_US']}},
                     'PARAMS': {'TYPE': 'NORMAL', 'DATA': None}, 'MODE': {'TYPE': 'POST'},
                     'BODY': {'TYPE': 'JSON', 'FUNCTION': '5NUT', 'DATA': {'index': [0], 'limit': [20]}}},
            'online': {'URL': 'https://api.5nuthost.com/v1/app/meme/user/list',
                       'HEADERS': {'TYPE': '5NUT', 'DATA': {'version': [1477], 'duid': [duid], 'lang': ['en_US']}},
                       'PARAMS': {'TYPE': 'NORMAL', 'DATA': None}, 'MODE': {'TYPE': 'POST'},
                       'BODY': {'TYPE': 'JSON', 'FUNCTION': '5NUT',
                                'DATA': {'token': [token], 'index': [0], 'limit': [20]}}}},
                              'DATA_FORMAT': {'TYPE': 'ONLY', 'EXTRA': {'LIST_REPEATED': False},
                                              'DATA': {'errorCode': 'Str', 'errorMsg': 'Str',
                                                       'info': {'pic_list': [{
                                                           'tiny': {
                                                               'url': 'HTTP',
                                                               'height': 'Int',
                                                               'width': 'Int',
                                                               'size': 'Int'},
                                                           'origin': {
                                                               'url': 'HTTP',
                                                               'height': 'Int',
                                                               'width': 'Int',
                                                               'size': 'Int'},
                                                           'item_id': 'Str'},
                                                           'None']}}},
                              'DATA_CONTENT': None, 'RESPONSE_HEADER': None}, 'path': './case/meme/user_list.yml'}
        true_requets(self.client, case_data)

    @task(0)
    def registry(self):
        language = "en_US"
        version = "1"
        salt = "3*y4f569#tunt$le!i5o"
        time_stamp = str(int(round(time.time() * 1000)))
        duid = str(today) + "-" + str(uuid.uuid1())
        header = {'User-Agent': duid + "#&#" + language + "#&#" + time_stamp + "#&#" + str(version)}
        data = duid + "_" + language + "_" + time_stamp + "_" + str(version) + "_" + salt
        sign = MD5(data)
        token_url = "https://api.5nuthost.com/v1/identity/registry"
        response = self.client.post(token_url, json={"sign": sign, "identity": "meme-app"}, headers=header,
                                    catch_response=True)
        print(response.json())
        print(response.status_code)
        if response.status_code == 200 and response.json()["errorMsg"] != "ok":
            response.failure("errorMsg is Fail")
        else:
            response.success()
        print(response.json())


class MyLocust(HttpLocust):
    task_set = WuRen
    # 任务的最小等待时间单位ms
    min_wait = 100
    # 任务的最大等待时间单位ms
    max_wait = 1000
    host = 'api.5nuthost.com'
