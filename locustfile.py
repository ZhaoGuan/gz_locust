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

user_datas = [{'duid': '20181212-82e26ba4-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'be1e431e977f4a349660b25094f4e5b0'},
              {'duid': '20181212-82e889a8-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '0388a1eaff4f417daa092309e64d4be2'},
              {'duid': '20181212-82eda0a0-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '37644d077dd44768af05072a66be69a5'},
              {'duid': '20181212-82f27396-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'fc0b7728b4004c0790eb1a7fbfc9c3de'},
              {'duid': '20181212-82f7a0aa-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'f57574fada5b4205a15b12a275cbd65c'},
              {'duid': '20181212-82fc4d76-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '93c386523900478e9b02172341307b8f'},
              {'duid': '20181212-83011af4-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'f021f4badc8f48d88266f8f1f652c5cf'},
              {'duid': '20181212-8305fd08-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'b561994dd76c4d23b561ab321896f740'},
              {'duid': '20181212-830aeba6-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'd9f5f4d02d98446fa76774142c12660b'},
              {'duid': '20181212-830faf1a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '419aa20e4e1f41bdbbacd4f847a45466'},
              {'duid': '20181212-83149f48-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'f5d0438222e545e198f81886d4401c26'},
              {'duid': '20181212-831943fe-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '0cccf8c4562140148806a4f586a1d995'},
              {'duid': '20181212-831e3f9e-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'b987c80eb9a9495096b07ee959e419af'},
              {'duid': '20181212-83231f82-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'c284a3a3eba84748acdeb62ec357f044'},
              {'duid': '20181212-8328272a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '00a434dfb07c49fb902f78be167f7682'},
              {'duid': '20181212-832d0b3c-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'aa059ff9352c456886cb0ee405e2fbf3'},
              {'duid': '20181212-8331dae0-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '934010df0a23447db73bf25c4046a10f'},
              {'duid': '20181212-8336a9f8-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '1da50ea266694d369df40a102e0d7620'},
              {'duid': '20181212-833b7870-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '8ac00100eb24461f85f94bf5d6a553b1'},
              {'duid': '20181212-83403d06-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '807b555a5bca4812a906167d1d962bf7'},
              {'duid': '20181212-834555c0-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'f1bd12beb6f340a1a75ec8e5580d9622'},
              {'duid': '20181212-834a516a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '3b5ba008237945a3ac38a6f17d1ed4f1'},
              {'duid': '20181212-834f53a4-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '5623d92dc55d45538606d70d5329e025'},
              {'duid': '20181212-8354aa0c-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '663cb3538819484bbbf36b644cd1f2f5'},
              {'duid': '20181212-8359ce24-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '76e5044aa90a4677af1f5eb3d5ad7bd4'},
              {'duid': '20181212-835ed8a6-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'cb02edc61fdf4ee2acdb5271d4a837b3'},
              {'duid': '20181212-8364593e-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'a4a6cadf55db4b6ab48b5d4da3cd5cc6'},
              {'duid': '20181212-8369551a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'fab90ca9dcca44258c78a3d2ed2e42eb'},
              {'duid': '20181212-836e7806-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'f34ef42a4aba46989e4ef8d7765e6ba2'},
              {'duid': '20181212-83735bbe-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '9281877ad1134b6398c6291fb45c21fb'},
              {'duid': '20181212-837864a6-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '81147a4d6245466f9195098ec644244b'},
              {'duid': '20181212-837d2e46-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'b3abf65d92e6497d8e4812b9f2ff40e4'},
              {'duid': '20181212-8382787e-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '49e4773d1b0640018e8e29d29ce354e6'},
              {'duid': '20181212-8387c7c0-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '3d7801e4a24e40b690bb1af6863dd8da'},
              {'duid': '20181212-838cd7ec-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'ea86106d77da437cbb68374f0b43a770'},
              {'duid': '20181212-8391fd08-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'ce9f1b1c976d45448813114f0358d857'},
              {'duid': '20181212-839773d2-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '4e058f7c9c584b2aa4d4a2bac435bea7'},
              {'duid': '20181212-839c5a5a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'e09b258934ab4e5c8c6ba599f7385907'},
              {'duid': '20181212-83a1bea0-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'd1ddce45d9414edbbe0eb1689e38836d'},
              {'duid': '20181212-83a6bd1a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'f245c1098a5b4d5fbb541fb6589bd5b2'},
              {'duid': '20181212-83abb842-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'c78211e708c6483aaf5733aa47d0c3e0'},
              {'duid': '20181212-83b125d4-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '0fea2891f687414185fb3c24fa5aa4c3'},
              {'duid': '20181212-83b614f4-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '2648a830dddd44f28c66bd460263fc3a'},
              {'duid': '20181212-83bb4320-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '070604b91b694fd18e144f7f9c38e6c8'},
              {'duid': '20181212-83c025fc-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'e898a5f95b2740a5a4f5080e9c8c5c52'},
              {'duid': '20181212-83c53eb6-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'cc30b3e3955e43e4ac9225dfdbfeb448'},
              {'duid': '20181212-83ca70de-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'b1b4ab66c15f4e249ad5f5f0147ea48b'},
              {'duid': '20181212-83cf627e-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '4fe375fd91b545aeaebd6ee8e780911e'},
              {'duid': '20181212-83d6f084-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'ddd8385c8e9b4d04995cf79005b16743'},
              {'duid': '20181212-83dc5c4a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '63701164bad3465e9268902b8ec2ff47'},
              {'duid': '20181212-83e1d490-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '98f659537f0b4d82b4ced7815bbf495f'},
              {'duid': '20181212-83e8417c-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'ccc6ac0f49194fc3b5d1d461287dc900'},
              {'duid': '20181212-83ed98c0-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '4a8f7a91c21d41668b4f8bfd8bc5eff5'},
              {'duid': '20181212-83f29a3c-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '000be1af038f4400a307bbac9bf7eb5d'},
              {'duid': '20181212-83f80b7a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'ce7a427290ab4d1c929df857582d586d'},
              {'duid': '20181212-83fd6dae-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'bbcbe04218e141c5bab99ce6bdc1e235'},
              {'duid': '20181212-84028316-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'f812919af48e46daa62c38321536fe71'},
              {'duid': '20181212-84078636-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'dfca8e3d7e4a444598e104eca00d9316'},
              {'duid': '20181212-840c6976-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '24142442781a42e3a0cf5bf5c76b0a79'},
              {'duid': '20181212-84117056-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '5240cad173e146f998fe7ff9c870a589'},
              {'duid': '20181212-84168cbc-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '6fd14949522e49abadd3ef8c0d3cbebd'},
              {'duid': '20181212-841b625a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'e77dc8aff04b4a58abc7793422f68e7a'},
              {'duid': '20181212-84205c60-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '0d6b5bd924744bcfbd5f27f0eb40b2c2'},
              {'duid': '20181212-842536a4-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '04288cbcd9bb412c8646e097dee4604d'},
              {'duid': '20181212-842a29f2-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '1f9b496191254d73b303e3aa5875135b'},
              {'duid': '20181212-842f111a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '384a83a57ea14a69a89c666bc0fb7132'},
              {'duid': '20181212-84342ba0-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '9d45ca58fc3c4706abeb7da6df8d42bd'},
              {'duid': '20181212-84395ae4-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '055f1745fa8148458e65e7dce9028d3c'},
              {'duid': '20181212-843ecb0a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'f542addd149f498497ec5b13571abea6'},
              {'duid': '20181212-8443b804-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'b07fa93b8f284506a83f9bbf13e6a951'},
              {'duid': '20181212-8448b8e0-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'f6904c52e2744b91938ac86995cd5071'},
              {'duid': '20181212-844dbffc-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'f0c9be56661b41ab92c9d360bf18a98a'},
              {'duid': '20181212-84530a2a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '09ad5e55d6aa430394aa867765bf9b70'},
              {'duid': '20181212-8457d2da-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '72ceddd275b243448240b252511843c5'},
              {'duid': '20181212-845d0f0c-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '9390cff634124afd8d64eac0570d51ea'},
              {'duid': '20181212-84621e98-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'c6a279a67d3546c9937cc89a82c5bb9e'},
              {'duid': '20181212-84677884-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '92bcf497f46b4999b4dbdb71e7d6addd'},
              {'duid': '20181212-846c774e-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'd2635f2a9400434b8560ae5e1d9a1b6e'},
              {'duid': '20181212-84717b04-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '779786c809a840f8b8288117dca251fa'},
              {'duid': '20181212-8476b2ae-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'e0eb1f1d79ec4244b3afe5d9105e2d72'},
              {'duid': '20181212-847be166-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'f246f45ae38b42c9a047197b8dac0ac3'},
              {'duid': '20181212-8480c9d8-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '4eaacfcf0de4462e9fad1acf6fcd6721'},
              {'duid': '20181212-848644c6-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '0f6891f6f10a493da4a10b1f4198aabc'},
              {'duid': '20181212-848b315c-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '40f13706b7a645a99760930fd93dd577'},
              {'duid': '20181212-849021bc-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '59daf8125689463987206ee6c1448500'},
              {'duid': '20181212-8494f7b4-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'd26ebec4a9ef4353871211af88df121d'},
              {'duid': '20181212-8499f980-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'b8fbba6ecb4f492fbe29d82e95ec5a79'},
              {'duid': '20181212-849ee850-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '55316b732f9f4f158062cc5430eb8abd'},
              {'duid': '20181212-84a3dde2-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '413f6f219eda4b22976fd1fb87791e2a'},
              {'duid': '20181212-84a8c3d4-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '5f225ced3a864b929a90fcf53bfe8df5'},
              {'duid': '20181212-84adba24-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'a0f0e6aab713433b82b3cae60a1ac943'},
              {'duid': '20181212-84b2a85e-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'b06b461119e94c13a5d6ffcf30e37616'},
              {'duid': '20181212-84b7d9f0-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'f15105041cfc4872bb4389efd7a1b634'},
              {'duid': '20181212-84bca444-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '9e992f631c364987a9c9a1488704d571'},
              {'duid': '20181212-84c170d2-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'a6278c084c9246c78dcc9a52fb9fd8a5'},
              {'duid': '20181212-84c65c0a-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': '7c26151d86d348938e0a8c40912d3fd0'},
              {'duid': '20181212-84cdbefa-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'c3f3736c87ca4d24bc2c67ac36527d71'},
              {'duid': '20181212-84d2ab68-fdfc-11e8-8cb0-069c9c0fbe5e', 'token': 'f3ab0c8c367d47aca01f8b1373170607'}]

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
