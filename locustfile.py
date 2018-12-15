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

user_datas = [{'duid': '20181212-82e26ba4-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '94aa15c26a934cf3b3a66896e8b690a9'},
              {'duid': '20181212-82e889a8-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '7d7be42a73f949768bad53c6a47a4115'},
              {'duid': '20181212-82eda0a0-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '00ea3a16d9f3423dafcb462e2681ca84'},
              {'duid': '20181212-82f27396-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'f74135b8b4ab4409a1be5570794bf704'},
              {'duid': '20181212-82f7a0aa-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '0fd3a7246e17405e8cb0745127552f62'},
              {'duid': '20181212-82fc4d76-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'ccad58c8a345493d914315b2b9175797'},
              {'duid': '20181212-83011af4-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'bffae833e15f447d82b6ee1d858a6b4a'},
              {'duid': '20181212-8305fd08-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '2daf469086a146aa9102f7787f1b3ae9'},
              {'duid': '20181212-830aeba6-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '16cec8fcbd0d4aa381aa9c0acbd7d32d'},
              {'duid': '20181212-830faf1a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '1ea7ec6ecd344ff5a8184ac171fdaaeb'},
              {'duid': '20181212-83149f48-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'd28909d074a6418d8ac58cc538d47a34'},
              {'duid': '20181212-831943fe-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'ae40179b08004e798db5d94ef693da71'},
              {'duid': '20181212-831e3f9e-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'db3b16c9331241b381e7ef7e5a9708e3'},
              {'duid': '20181212-83231f82-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'd4ad063dc6af4e8bb439a326f6dfbbe5'},
              {'duid': '20181212-8328272a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '9402f47027314e95a2d77244f5112f69'},
              {'duid': '20181212-832d0b3c-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '2ec27547b03f481ebd4b788b6c14aff2'},
              {'duid': '20181212-8331dae0-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '4f2de1f0ed9841ceafe5ede28ccd451a'},
              {'duid': '20181212-8336a9f8-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '9992bd597e334ce4ab5645f2f6e81747'},
              {'duid': '20181212-833b7870-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '412970b7bd134618a6ed0fb1cd8e79a9'},
              {'duid': '20181212-83403d06-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '04914ff667244eb1a611f2a514e263c7'},
              {'duid': '20181212-834555c0-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '2708de2052e7464eabf594b1eccac3ae'},
              {'duid': '20181212-834a516a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '77752dc8576440958af9a2ba5b65abc0'},
              {'duid': '20181212-834f53a4-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '1b2430d80df6437f884d9c8442489e64'},
              {'duid': '20181212-8354aa0c-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'c7b7648d6e8547f29d47fa9bcd75fece'},
              {'duid': '20181212-8359ce24-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '6065d150aba345b98d0927f0f7bfaace'},
              {'duid': '20181212-835ed8a6-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '2c6978412fdb41fab5b06f8583c2890f'},
              {'duid': '20181212-8364593e-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '3c6a151452b146d480e76781e15846ea'},
              {'duid': '20181212-8369551a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'cdbedef54c3f4c4ebef3e8a6cd6649a3'},
              {'duid': '20181212-836e7806-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '42aaca170ac24440a496c4b90e2130a2'},
              {'duid': '20181212-83735bbe-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '7b5bd0809367481e9999fa673b762390'},
              {'duid': '20181212-837864a6-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '0a663cba6f664aa0b32ac8b95eded39d'},
              {'duid': '20181212-837d2e46-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '64a19349cac347e7ad612ebbb398155d'},
              {'duid': '20181212-8382787e-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'e76f370d43f3418ab8547e8fff36ce2c'},
              {'duid': '20181212-8387c7c0-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '311c9223ff544d7f99623349075cd77b'},
              {'duid': '20181212-838cd7ec-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '7fdecfa6909d473482a227b74e26de38'},
              {'duid': '20181212-8391fd08-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'b115aac2dd824d9f919468b5acda7b1a'},
              {'duid': '20181212-839773d2-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'ea0f4942c5bd45d596a82e43c9f5aed2'},
              {'duid': '20181212-839c5a5a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '4d5cba5dc8d04afb960f61d6610e23c8'},
              {'duid': '20181212-83a1bea0-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'dcbbc0d299b54ae98022228886778dc6'},
              {'duid': '20181212-83a6bd1a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '2f3a2c5f01944f38b394d99e2c08e84f'},
              {'duid': '20181212-83abb842-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '54d861e344364cabbcca4f3ed92dae86'},
              {'duid': '20181212-83b125d4-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'bffa3d9ee92a407f8f175ef18a10fe15'},
              {'duid': '20181212-83b614f4-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'fe4c0421ebfb4b60a3ce0bbb0f0c8242'},
              {'duid': '20181212-83bb4320-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '0cbe9500a22d4a6f9196af58fc530420'},
              {'duid': '20181212-83c025fc-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'eb4dd75fd8284ea6a7c2e17eca588d4a'},
              {'duid': '20181212-83c53eb6-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '022802f876504a9983cf0d16678b65b6'},
              {'duid': '20181212-83ca70de-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '5fd24ee12f2041549dd191d5d83c29d6'},
              {'duid': '20181212-83cf627e-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '633d3cf841234d9b887962e5cefa560d'},
              {'duid': '20181212-83d6f084-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '5dd2c6b50f374e9189be705c62f30930'},
              {'duid': '20181212-83dc5c4a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'eb6771d227fa4f5b898200b196cf4800'},
              {'duid': '20181212-83e1d490-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '74366b50cb634779a1027c1f0faf3f4b'},
              {'duid': '20181212-83e8417c-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '6751808f57364c9b882dde071ca9e622'},
              {'duid': '20181212-83ed98c0-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '5fd611be7aaf458784c2d77ebafd2c27'},
              {'duid': '20181212-83f29a3c-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'fb9eb0fd6c994200b76ae4fb1895efca'},
              {'duid': '20181212-83f80b7a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'a25e2e6d704343f3b56b2dfd6afa9867'},
              {'duid': '20181212-83fd6dae-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '4158b990528c454fb16b638edb9d69bc'},
              {'duid': '20181212-84028316-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '482399879daf42cc87f9e0488b3484a6'},
              {'duid': '20181212-84078636-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '6c0375d785dc4a74ae0ac599ebe4cd1d'},
              {'duid': '20181212-840c6976-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '89530e2bff0a4a128ba9651a77faa850'},
              {'duid': '20181212-84117056-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'db808120f7c74a41b27f1dc8e54f2182'},
              {'duid': '20181212-84168cbc-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'f6387c476dc54953840a0bfcdfeaba70'},
              {'duid': '20181212-841b625a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '4f0219e9db4a4ed7b5401d5423cb0286'},
              {'duid': '20181212-84205c60-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '0a3324ce640f41bd9e5564768cdfaf76'},
              {'duid': '20181212-842536a4-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'b5c914aa37fc41868ba1eee79eb2d051'},
              {'duid': '20181212-842a29f2-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'a7c3c51330004a01a1ac4a823bd2c7fd'},
              {'duid': '20181212-842f111a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '0f4dc0c0416a44e097a697030ac9ae3d'},
              {'duid': '20181212-84342ba0-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '3d08a832aaf843c8b5e869c57e5ea5bd'},
              {'duid': '20181212-84395ae4-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'e62143ff98a44d298162e04ce5fb2f28'},
              {'duid': '20181212-843ecb0a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'bff3a28bcb23487fbf7ac418e8888a6f'},
              {'duid': '20181212-8443b804-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'eae6feb06f724f19a1025863ba6fec79'},
              {'duid': '20181212-8448b8e0-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '79604abcbf304c1eb338004aed984fa2'},
              {'duid': '20181212-844dbffc-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '7cf8ed8192764660acb7a4e9a86d63e0'},
              {'duid': '20181212-84530a2a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'd03616be2e434f89a4591261ae380667'},
              {'duid': '20181212-8457d2da-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'a8ec95d2b4ba4e88bbbb916021921300'},
              {'duid': '20181212-845d0f0c-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '8884bf73fdd6479b8ec9579b3ac27952'},
              {'duid': '20181212-84621e98-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'e86a308e38554230b4dd45b151aa14ae'},
              {'duid': '20181212-84677884-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '18f3f0487a15453094abbbf610df33f0'},
              {'duid': '20181212-846c774e-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '09e223c93ed3435dbf8d268cf049e8fa'},
              {'duid': '20181212-84717b04-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'bfe270aa82824bb3bd32412a379ec5d7'},
              {'duid': '20181212-8476b2ae-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'f0e2a43e79c148ca9a591f1d0762cee9'},
              {'duid': '20181212-847be166-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '76c23522a395459192be5590f3410b3a'},
              {'duid': '20181212-8480c9d8-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '87788d849e434d688f151001ebafd7fc'},
              {'duid': '20181212-848644c6-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '4f650419a3a24f09b99a7121be35a3c2'},
              {'duid': '20181212-848b315c-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '2bebe7ed045743e188e44fc21a13b81d'},
              {'duid': '20181212-849021bc-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '654636def67948eaa44defeaabe2723a'},
              {'duid': '20181212-8494f7b4-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'ba858361f95c43cdb8b40057d79a18e0'},
              {'duid': '20181212-8499f980-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '8b865295c48f400583381d6e1e3d5e9e'},
              {'duid': '20181212-849ee850-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'c3e58cc1f1de41bbba466a978c154f42'},
              {'duid': '20181212-84a3dde2-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'dbd03f46026e444990b5e5110699f7b6'},
              {'duid': '20181212-84a8c3d4-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '4e14bd4710d246dfaed8e6fb0f8c96d3'},
              {'duid': '20181212-84adba24-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '55c7967769a144a0b48ff59cadcdf832'},
              {'duid': '20181212-84b2a85e-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '84c99b775fb649a299ed7a5e0478950a'},
              {'duid': '20181212-84b7d9f0-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '4a58836d7c1b4478a3b1d97bf5135549'},
              {'duid': '20181212-84bca444-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '7f4c6ee181e946c594d4420780b350f6'},
              {'duid': '20181212-84c170d2-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '6dd995c3c58c4c2897d9cea9e494660b'},
              {'duid': '20181212-84c65c0a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'feb14fe66a7c4b43bfc736200ffae2c3'},
              {'duid': '20181212-84cdbefa-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'ef763c4b82784bac9256d29f8a9405d6'},
              {'duid': '20181212-84d2ab68-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '16716beeba464a91a53ec74a777583f6'}]

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

    @task(10)
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
                                'DATA': {'token': [token], 'id': ["-1"], 'limit': [20]}}}},
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
