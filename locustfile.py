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

user_datas = [{'duid': '20181212-82e26ba4-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '67283ae0872147ef887588cb958149d9'},
              {'duid': '20181212-82e889a8-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '3c01101863df453b8756433c44ec2879'},
              {'duid': '20181212-82eda0a0-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'd483b38ca2a549acb829c534333e4317'},
              {'duid': '20181212-82f27396-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '22f8707b17e1491caba853455a04815c'},
              {'duid': '20181212-82f7a0aa-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '8f75901f587043efa7bfbf51081f6203'},
              {'duid': '20181212-82fc4d76-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'cc5d50b2aee346ab84c0217cfb5486f9'},
              {'duid': '20181212-83011af4-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'acb1b75f81004b30a026747a1d7113b2'},
              {'duid': '20181212-8305fd08-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '9c452e5e0c264851abe5dacbf933b1b6'},
              {'duid': '20181212-830aeba6-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'ef33dfa2fe61419f84f328e429f3a263'},
              {'duid': '20181212-830faf1a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '22b0188defd248f9a114e5a6230defc1'},
              {'duid': '20181212-83149f48-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '3a699762c74941cba3f0e5f95205a969'},
              {'duid': '20181212-831943fe-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '3dbae78066e9406cb7a4999092d632e1'},
              {'duid': '20181212-831e3f9e-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'da2b9746f16f4383a28af9435e722259'},
              {'duid': '20181212-83231f82-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'ce03a0836fd440cd9da21b84891de1a0'},
              {'duid': '20181212-8328272a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'c9bec5c63b204146baf9403db0bfef5f'},
              {'duid': '20181212-832d0b3c-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '86f078bd50854aa7ace90c091ccbda56'},
              {'duid': '20181212-8331dae0-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '44d0c08081774babbd8a15f7bebb30a2'},
              {'duid': '20181212-8336a9f8-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '4d2e0e615ad74807a40a4b3e4333172f'},
              {'duid': '20181212-833b7870-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'f27eeb3571f74e1d80ae96b06fd636c0'},
              {'duid': '20181212-83403d06-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'c74237758fe24799bd5398519235a6e9'},
              {'duid': '20181212-834555c0-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '59e5fd44a2e6409186c168c32f6dbb0d'},
              {'duid': '20181212-834a516a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '958ef3878210414c83faf421bbf68a69'},
              {'duid': '20181212-834f53a4-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '5ad6f93be23643bba264b301be95c4e5'},
              {'duid': '20181212-8354aa0c-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '38c7557fb28a4481ab98c585c6087743'},
              {'duid': '20181212-8359ce24-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '81013a20e81f42328da865434b6e86b7'},
              {'duid': '20181212-835ed8a6-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'bc8af707696940f68577b312d9b8a624'},
              {'duid': '20181212-8364593e-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '4572abcbd8fa43229fc576f3545aa78b'},
              {'duid': '20181212-8369551a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '6f088d670cc24d67b611a0aabcb14e6e'},
              {'duid': '20181212-836e7806-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '4b1c2c2701d646f18ec2798caa46935f'},
              {'duid': '20181212-83735bbe-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'aef350b3bf31411da0b73b8e0a80996e'},
              {'duid': '20181212-837864a6-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '192733fec4764bdb93c619ec89395eaa'},
              {'duid': '20181212-837d2e46-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '6d99e7c3985e415d8860ce712be6085f'},
              {'duid': '20181212-8382787e-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'd6098633ee2e4d9b8c12ad7a951dcb03'},
              {'duid': '20181212-8387c7c0-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'bb9391c5435646fa8983568c50a32399'},
              {'duid': '20181212-838cd7ec-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'da25aa0db92c4dd5b6db579b1f59773d'},
              {'duid': '20181212-8391fd08-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '0820b18292af475ca0ee5508235e01d3'},
              {'duid': '20181212-839773d2-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '916ff901a163492aa15f55beee50619d'},
              {'duid': '20181212-839c5a5a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'ba457ec8a12341539ecaeb83671c580c'},
              {'duid': '20181212-83a1bea0-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '59f61f92f7e64447904487719b1b8aee'},
              {'duid': '20181212-83a6bd1a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'c41598c84d1b4708bb468aa460a747c3'},
              {'duid': '20181212-83abb842-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '0c79f91d06744582a4e49dd8ff29b2ab'},
              {'duid': '20181212-83b125d4-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'e2d8c1b2ee0640a096f60f5c64392323'},
              {'duid': '20181212-83b614f4-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '13af087068d54195abad96b30ba6cb67'},
              {'duid': '20181212-83bb4320-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '4e848937714643bb907198b792c1bb2e'},
              {'duid': '20181212-83c025fc-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '0a99c611d9254beca9cb75dc594b3314'},
              {'duid': '20181212-83c53eb6-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'b08c619e92614a50afaa0245a26af5b7'},
              {'duid': '20181212-83ca70de-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '922839b9328543a2babcb3a56ab19d2c'},
              {'duid': '20181212-83cf627e-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '1a81970995ab4f54867a64dfb2989c3a'},
              {'duid': '20181212-83d6f084-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'a927fd4975bf4494abc26c549f3aa1a9'},
              {'duid': '20181212-83dc5c4a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'acb2c4b093bb4b5ebadd0952ff0ce9d8'},
              {'duid': '20181212-83e1d490-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'dcc167a99e2b4ef1952e837e596694a1'},
              {'duid': '20181212-83e8417c-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '70ae5bf8e53d49e3bbf2f3e3518a1a3d'},
              {'duid': '20181212-83ed98c0-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '4f21f06405e24ab98d2a9242b3e2fbbf'},
              {'duid': '20181212-83f29a3c-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'fa9be7808d234e0a8b4aa8a8993db25e'},
              {'duid': '20181212-83f80b7a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '4809c384554d4fb0886ccff80e829c11'},
              {'duid': '20181212-83fd6dae-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '1fbc82fc678f485191de6d88ca4531d5'},
              {'duid': '20181212-84028316-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'ab751af82ea04972ac13246aa0f8ebee'},
              {'duid': '20181212-84078636-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '2a7a50856c924f7695cb0923c75cfece'},
              {'duid': '20181212-840c6976-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '051b71464c554ddeb4b4626693d87a21'},
              {'duid': '20181212-84117056-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '9fd24ef07e354b6995bf7c775c8f00ac'},
              {'duid': '20181212-84168cbc-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'f73a9fc156dd4e7996b8b369bd5ec8e5'},
              {'duid': '20181212-841b625a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'aa87ae108f64496c90a3b7bc42b9d702'},
              {'duid': '20181212-84205c60-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'd47c9fed1932473fb344759f57796514'},
              {'duid': '20181212-842536a4-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'cc68d33e7db14762a72e1eaf264aeab9'},
              {'duid': '20181212-842a29f2-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '70e10d2260de4d01bb502afc650efe00'},
              {'duid': '20181212-842f111a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'cedf128496034827b35ae27966e9bc37'},
              {'duid': '20181212-84342ba0-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '4fc98aed009f4618940649699e28f9ee'},
              {'duid': '20181212-84395ae4-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'b9c5bebfa908447eb5df8a3693c17634'},
              {'duid': '20181212-843ecb0a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '77f3fc1255bd4aaab93dba24a00129be'},
              {'duid': '20181212-8443b804-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '6b90321bed7c480599a9e0aa160b7a56'},
              {'duid': '20181212-8448b8e0-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '68a6687f24c54ceaa80002aa9e2c7188'},
              {'duid': '20181212-844dbffc-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '326f259ed2be4b7e905b840f0863d1e8'},
              {'duid': '20181212-84530a2a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'cd892d2de24047c397cfc6b9e0bfcae9'},
              {'duid': '20181212-8457d2da-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '6a84caebc4a4448ba48b71f7c2f0227c'},
              {'duid': '20181212-845d0f0c-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'ad54b22cfe3540d091baff2eee01fe7e'},
              {'duid': '20181212-84621e98-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'c47672d9242042e4b4343875ec285bdf'},
              {'duid': '20181212-84677884-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '9bb363e7b0f6460ea3eb230b30eca4b4'},
              {'duid': '20181212-846c774e-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '970c38bf32b14219829c1753f96d4e5f'},
              {'duid': '20181212-84717b04-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'c96f6c6170c64d98a3bb66dc897645d9'},
              {'duid': '20181212-8476b2ae-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '57fa540af62f441aa203dbbbf0f976e0'},
              {'duid': '20181212-847be166-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'ec61994decd24a438b228bdcb6b9984c'},
              {'duid': '20181212-8480c9d8-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'a8a27d54cf524aeba22a21c9ff079053'},
              {'duid': '20181212-848644c6-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '88c08b9593594458908e5c6fc7427519'},
              {'duid': '20181212-848b315c-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '4a19f5cbb35d4c05a68b92403655a11a'},
              {'duid': '20181212-849021bc-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'be2d36fa2c654344addbaaf8618e4ae2'},
              {'duid': '20181212-8494f7b4-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '8651eaf51bdb4e87942e39ff8bbd92af'},
              {'duid': '20181212-8499f980-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'd57c066f0a41409cae765cef9a3016aa'},
              {'duid': '20181212-849ee850-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '8bceeb3c4b32496c9100564192eebd36'},
              {'duid': '20181212-84a3dde2-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'c2763a1e7d9840be8e453dd5e7e3c59a'},
              {'duid': '20181212-84a8c3d4-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'd5a25491e2234021ad0af683323ea781'},
              {'duid': '20181212-84adba24-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '83dc43263d0e4c0c8dbdb6ed9c5ee506'},
              {'duid': '20181212-84b2a85e-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'bdb81257135f4e42966d649e53da5030'},
              {'duid': '20181212-84b7d9f0-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'c858a2f5261247b3a553226c98bae5b7'},
              {'duid': '20181212-84bca444-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'b6a3f184fd194abdadd06a81c18be9f5'},
              {'duid': '20181212-84c170d2-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'e3d14c714c4e4d02907d5411f44fa843'},
              {'duid': '20181212-84c65c0a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '36003f05968a4426b802030e6a0efe78'},
              {'duid': '20181212-84cdbefa-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '630b989a74ae4439a84fa7be7d36048c'},
              {'duid': '20181212-84d2ab68-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '5ae91ad389fc495797362f6d102b9584'}]

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

    @task(10)
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
                                'DATA': {"token": [token], 'category': ['all'], 'index': [0], 'limit': [10]}}}},
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
                       'BODY': {'TYPE': 'JSON', 'FUNCTION': '5NUT', 'DATA': {'token': [token], 'title': ['Trump']}}}},
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
