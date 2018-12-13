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

user_datas = [{'duid': '20181212-82e26ba4-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'd34a75d437c6457a883b61ea2bc85733'},
              {'duid': '20181212-82e889a8-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'c3a45f073de64df9a2b21392a08be1de'},
              {'duid': '20181212-82eda0a0-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '38d13b240ca543abb313599d77ee3ea6'},
              {'duid': '20181212-82f27396-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '57bb68577305432692e627b7a9aab28e'},
              {'duid': '20181212-82f7a0aa-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '829b2426f7ba4271985067e09aa93ad4'},
              {'duid': '20181212-82fc4d76-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '11ec488cc07640a29861da5270b51918'},
              {'duid': '20181212-83011af4-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '2b3e6899259f4f718975368d5c4dba5c'},
              {'duid': '20181212-8305fd08-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'f02df49195984c4f8d276f1fa6f6e0c9'},
              {'duid': '20181212-830aeba6-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '6f360d8f040a44518166d0c14db4d64c'},
              {'duid': '20181212-830faf1a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '4f5accd96e994fe7a2ebe62047bf2e72'},
              {'duid': '20181212-83149f48-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '220b5b764b034b6f88a8dbd3a2703faf'},
              {'duid': '20181212-831943fe-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'd36d5f4e113945f4a6441d9f598faf0d'},
              {'duid': '20181212-831e3f9e-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'd1e9dc77f8824dc0a0312b31a85439ca'},
              {'duid': '20181212-83231f82-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'c103a287c2f14495a9d2eb5dc5c68c88'},
              {'duid': '20181212-8328272a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '4b7af044963e40928647c9bac566b683'},
              {'duid': '20181212-832d0b3c-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '404568889513435196d9e76d7fecc064'},
              {'duid': '20181212-8331dae0-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '88791115271c4effb8a115c3f44c1c55'},
              {'duid': '20181212-8336a9f8-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'd2af642bd1e14d7aa14e9b6ccaafc25a'},
              {'duid': '20181212-833b7870-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '9f2f902a07d143a1b196704b91579ae9'},
              {'duid': '20181212-83403d06-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '1f03a88819a94c8082d944512153da35'},
              {'duid': '20181212-834555c0-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'a617ceae23e24de4ac8aec0f175d7d91'},
              {'duid': '20181212-834a516a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '8ea2be1405f54d929d38791c013f5067'},
              {'duid': '20181212-834f53a4-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '754cda8dc61b4d07804387f9c4ae48b0'},
              {'duid': '20181212-8354aa0c-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'b4183b3b08094835a27e5906865807ad'},
              {'duid': '20181212-8359ce24-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '8736b2b1c70b41f0b81291bbadbe1320'},
              {'duid': '20181212-835ed8a6-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '96c4cf9086df4d4ca55609b27b275509'},
              {'duid': '20181212-8364593e-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '161a7168fe0d4df1a8b856fb97d190c2'},
              {'duid': '20181212-8369551a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'dfcc9aa053194bf6beacef068efc7ed3'},
              {'duid': '20181212-836e7806-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'ccc538758dba4e629720b238630549a2'},
              {'duid': '20181212-83735bbe-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'ea441b33727e44db9dce3dc2b4dd0165'},
              {'duid': '20181212-837864a6-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'e389d98f045e47c894b8a3c9c54d4ca4'},
              {'duid': '20181212-837d2e46-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '98e93611a1a94a07bd5717bc05811c6f'},
              {'duid': '20181212-8382787e-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'e80e944af70c4d5aad7923518197efc0'},
              {'duid': '20181212-8387c7c0-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '102e0e82c4814801b2807bfe634ed092'},
              {'duid': '20181212-838cd7ec-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'edcd24aa954e4dffb3639a972612e882'},
              {'duid': '20181212-8391fd08-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'd1bbba0e450c496d88ff38f3da9d8181'},
              {'duid': '20181212-839773d2-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '0f0e75ac78ca47b28736592ef4d30eb4'},
              {'duid': '20181212-839c5a5a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'd8c30757a7ad4c47ae21ffbb5084548a'},
              {'duid': '20181212-83a1bea0-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'a953e3ee6e094bb2a13df7568b55e190'},
              {'duid': '20181212-83a6bd1a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '36003cdb28944394aa5bf21c722e29db'},
              {'duid': '20181212-83abb842-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '17c7304579784cf58a61d0c90dcf06b2'},
              {'duid': '20181212-83b125d4-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '58564d628f9441debb343d6f0c815112'},
              {'duid': '20181212-83b614f4-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'fb015043042b415db5d0a1d014a829f6'},
              {'duid': '20181212-83bb4320-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '5dfd80d59f5c4a4099717a063739ee8e'},
              {'duid': '20181212-83c025fc-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '4b804df4d15b487291d2acb9202ae871'},
              {'duid': '20181212-83c53eb6-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '80cc187493cf48e591de154e05846709'},
              {'duid': '20181212-83ca70de-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'b824f5a58b574e61acc7a4601d2315e6'},
              {'duid': '20181212-83cf627e-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'f768bdd904ab4270a9be386a020bfac3'},
              {'duid': '20181212-83d6f084-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'f60d1715edcc4bce856457356c8f1b03'},
              {'duid': '20181212-83dc5c4a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'e4923d120a414f699ce758fa2b1ea969'},
              {'duid': '20181212-83e1d490-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '5c2b83da91d04c9086188d489de93c30'},
              {'duid': '20181212-83e8417c-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'c270e76ceb984586995171ef2eb2a7f2'},
              {'duid': '20181212-83ed98c0-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'a11113da811d498180c6741baf8a612e'},
              {'duid': '20181212-83f29a3c-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '09c6901c84404b629ed194e458d87ed1'},
              {'duid': '20181212-83f80b7a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '70da6cc101d24936b91c29276c80df17'},
              {'duid': '20181212-83fd6dae-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'e1bda51746274a0999d76a071180b9fb'},
              {'duid': '20181212-84028316-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'd90a2213df3c4e94ac41f5669aca0ed0'},
              {'duid': '20181212-84078636-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'e2df82b3d5544c7a897303621ed6da37'},
              {'duid': '20181212-840c6976-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '3c7144b6ce1c4b8d833f4558451964a2'},
              {'duid': '20181212-84117056-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '795969ff75364f95a47398a11789383f'},
              {'duid': '20181212-84168cbc-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'c34bd4247c884113916b9184079023fd'},
              {'duid': '20181212-841b625a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'e425db1f7b53461690b847137206ec4a'},
              {'duid': '20181212-84205c60-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'eabaa8a17cdf4ce39ff9039f5e6f486d'},
              {'duid': '20181212-842536a4-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '6d5cb83cffb247c88f4866f10375bf4b'},
              {'duid': '20181212-842a29f2-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'fd8445f5d87c4df380dea813982cdbdc'},
              {'duid': '20181212-842f111a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'd7a5f66dabfa45a89742225c7f130074'},
              {'duid': '20181212-84342ba0-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'a719fd129d6b476cbef00ba0c494ce79'},
              {'duid': '20181212-84395ae4-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '485cb69630a243af95867ac1595542e7'},
              {'duid': '20181212-843ecb0a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'ac0e6f56535d4c03bd72053d0a74c4e1'},
              {'duid': '20181212-8443b804-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'bca728bfd3e44a528d46b0bf06f4e2af'},
              {'duid': '20181212-8448b8e0-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '2e7afa54098e47f3badc49066115322e'},
              {'duid': '20181212-844dbffc-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'cf06fb8ff5564341a55a2a9aad22e45d'},
              {'duid': '20181212-84530a2a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'e116df669df047cfbb1782bbc54578dd'},
              {'duid': '20181212-8457d2da-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '266b8463658a4705bcc818ccd16516c3'},
              {'duid': '20181212-845d0f0c-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '8a8e64539a9f4a9c9188b41ba90921bb'},
              {'duid': '20181212-84621e98-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '36d7a3baf7f4416bbc17d8505ab201be'},
              {'duid': '20181212-84677884-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '5bdc00c85233494e8cf3d7cd6a4b8187'},
              {'duid': '20181212-846c774e-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'c14b7fe21dd341bab8afa45066846f9d'},
              {'duid': '20181212-84717b04-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '0e102a7d77754f12ac6a41112c0dc8ca'},
              {'duid': '20181212-8476b2ae-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'c9be64ffd0da445ebbead7181fd58625'},
              {'duid': '20181212-847be166-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '41188e9a3c0244cd939aa306b23282c3'},
              {'duid': '20181212-8480c9d8-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '48fa8e1f262e41299945eb3b51cc07d2'},
              {'duid': '20181212-848644c6-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '10b75b8bb80f474f86ac6fe9046fdb81'},
              {'duid': '20181212-848b315c-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'a3c77f4f7bc346988f287942438ac641'},
              {'duid': '20181212-849021bc-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'cd24b3add85444a09ef1b307a6b42f36'},
              {'duid': '20181212-8494f7b4-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '9cf4650026d64029901c3f726f5752b2'},
              {'duid': '20181212-8499f980-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '635886ff0faf45dd953884fb9f071534'},
              {'duid': '20181212-849ee850-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '8b0cd9d2ccb24445888c4208d75b9703'},
              {'duid': '20181212-84a3dde2-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '047c2258a0014218a0fe456952814057'},
              {'duid': '20181212-84a8c3d4-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '38f03e244677465183cbb4c70d9a638a'},
              {'duid': '20181212-84adba24-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '207863b405194b7aae4bf08746247ffc'},
              {'duid': '20181212-84b2a85e-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'b36cf26450bf431bba62c71d85b020e1'},
              {'duid': '20181212-84b7d9f0-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'ddb5d1b24ca5444ea4b362cabe447fbc'},
              {'duid': '20181212-84bca444-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '647a0d0406384bfe810185b356f9e6ed'},
              {'duid': '20181212-84c170d2-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '7f43a21cdd4a4571ae2f89e6f83d587d'},
              {'duid': '20181212-84c65c0a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'b7a0a3ca2d6b42d1b482d08674b783b3'},
              {'duid': '20181212-84cdbefa-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'fff15db2d58644ffb28fbd7d4952a03d'},
              {'duid': '20181212-84d2ab68-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'c74c4fce43694e6fb101b157932e6c2f'}]

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

    @task(0)
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

    @task(10)
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
                                                          'DATA': {"token": [token],
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
