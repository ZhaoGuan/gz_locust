# -*- coding: utf-8 -*-
# __author__ = 'Gz'

# ------------服务压测内容设置------------
from locust import HttpLocust, TaskSet, task
from case_generate import Http_Test, config_reader
import random
import json
import hashlib
from base_function.kika_base_request import Kika_base_request

# 放在引用前保证数据数量
test_data = config_reader('./test_case')
a = Http_Test(test_data)
all_data = a.url_keys_data()

# single_data = all_data[random.choice(range(len(all_data)))
kika = Kika_base_request('api.kikakeyboard.com')


def random_duid():
    all_world = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
    world = random.sample(all_world, 5)
    result_world = ''
    for i in world:
        result_world += i
    m = hashlib.md5()
    m.update(result_world.encode('utf-8'))
    MD5 = m.hexdigest()
    # print(MD5)
    return MD5


def get_sign(self, app, version, duid):
    if app == None or version == None or duid == None:
        sign = False
    else:
        if 'pro' == app:
            app_key = '4e5ab3a6d2140457e0423a28a094b1fd'
            security_key = '58d71c3fd1b5b17db9e0be0acc1b8048'
            # package_name =

        elif 'ikey' == app:
            app_key = 'e2934742f9d3b8ef2b59806a041ab389'
            security_key = '2c7cd6555d6486c2844afa0870aac5d6'
            # package_name =
        else:
            app_key = '78472ddd7528bcacc15725a16aeec190'
            security_key = '6f43e445f47073c4272603990e9adf54'
            # package_name =
        base = 'app_key' + app_key + 'app_version' + str(version) + 'duid' + str(duid)
        m = hashlib.md5()
        m.update(base.encode('utf-8'))
        sign = m.hexdigest()
    # print(sign)
    return sign


class popup_test(TaskSet):
    @task(10)
    def popup(self):
        # self.client.header()
        lang = ['en_AU', 'pt_BR', 'es_AR', 'in_ID', 'fr']
        # lang = ['en_AU']
        tag_list = ['mais ou menos', 'yo también amor', 'gn streaks']
        tag = random.choice(tag_list)
        kb_lang = random.choice(lang)
        lang = kb_lang.split('_')[0]
        country = kb_lang.split('_')[1]
        header_online = {
            'User-Agent': 'com.qisiemoji.inputmethod/2021 (175b40b82dac4a5e95e3976cebccd7ac/78472ddd7528bcacc15725a16aeec190) Country/' + country + ' Language/' + lang + ' System/android Version/23 Screen/480',
            'Accept-Charset': 'UTF-8', 'Kika-Install-Time': '1503996692777', 'Accept-Encoding': 'gzip',
            'X-Model': 'D6603', 'If-Modified-Since': 'Mon, 04 Sep 2017 07:08:32 GMT', 'Accept-Language': kb_lang,
            'Host': 'api.kikakeyboard.com', 'Connection': 'Keep-Alive'}
        header_test = {
            'User-Agent': 'com.qisiemoji.inputmethod/2021 (175b40b82dac4a5e95e3976cebccd7ac/78472ddd7528bcacc15725a16aeec190) Country/' + country + ' Language/' + lang + ' System/android Version/23 Screen/480',
            'Accept-Charset': 'UTF-8', 'Kika-Install-Time': '1503996692777', 'Accept-Encoding': 'gzip',
            'X-Model': 'D6603', 'If-Modified-Since': 'Mon, 04 Sep 2017 07:08:32 GMT', 'Accept-Language': kb_lang,
            'Host': 'dev-api.kikakeyboard.com', 'Connection': 'Keep-Alive'}
        # pop = self.client.get(
        #     'https://api.kikakeyboard.com/v1/stickers2/popup?tag=lol&kb_lang=en_AU&sign=87d6cf9df3294d23b6ac7d85b28d4491',
        #     headers=header_online, catch_response=True)
        # pop = self.client.get(
        #     'http://172.31.23.134:9090/backend-content-sending/popup?tag=' + tag + '&kb_lang=' + kb_lang + '&sign=87d6cf9df3294d23b6ac7d85b28d4491',
        #     headers=header_test, catch_response=True)
        pop = self.client.get(
            'http://172.31.24.127:8080/backend-content-sending/popup?tag=' + tag + '&kb_lang=' + kb_lang + 'sign=579fa00e0907f2cf9e57c083ed3bcb2a',
            headers=header_online, catch_response=True)
        with pop as response:
            print(pop.json())
            try:
                if response.json()['errorMsg'] != 'ok':
                    response.failure('wrong!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                # if response.json()['data'] == None:
                #     response.failure('wrong!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            except:
                pass
                print(pop.json())

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

    @task(0)
    # 强哥
    def kika_backend(self):
        all_duid = ['2259d9151ebb4b50bc245bb42959baf7', '4aa45fe3934d4d608d870fe02079f69e',
                    'db0ff4c58980441cbb92fdcf95472a6e', '794988ee1f824fdc9e8ac8946bddd204',
                    'ca63f03773e2faade9286aaa03b3930c', '3a2680e07fd148c787e28f4217c70dfb',
                    'a66227c95b3a4be98f28c2eaefdf19a5', '76f890a01d8a4d378c8f1fcbea750dc4',
                    '585d3bcd30f14499b1f1934d99373e70', '883c510d99f74f5f8c7846e3eff69246',
                    '5a4d3286b1ed4313a3bf6286fbd30459', '954832ecddcf4e839c2ef7dde0c00c7e',
                    '6f9d68dbb1214c368bb196a188ee9f29', '0575bd4da6074db7b8e12d3d191bed48',
                    '341a144890ff468f90a60c8dd480858e', '97a21a96bf4698e26ffa5867c535f5a2',
                    '8769746535424aab910fbb597d14013e', '644b64ef403a4799a0523ae548070eb1',
                    'e115d937e7d340309a214e2e3934afd7', '4db15a126ec243b795d539b12a03f34b',
                    'dfe8470c9b3e459590c946cffacc4505', '169074eed6b649328e11016e74a0ee90',
                    '442a7534ab004ec1bff781c7c0a2c7fe', '7276b85677884e11a778a91f70d8f8a7',
                    '7d3768a20670496fa13ce51858b897fa', '7449b88b32d649f7a8ba93fd6a257048',
                    '3a08234ab60f44c39d1ce0986450e2f4', 'f457399bb1034083ab19676838b11ae8',
                    'cd3134ee42604bbc8def1c122dd10342', 'e769433545284f8a9768e3cf63b8f90f',
                    '5f04a6cc3eda4c968eef66099e75cc2b', 'de35727e6a0d4ee9853cdaa85bf672f0',
                    '3f5f1e0e5a3f4347981b4f9ac9466fde', 'f4aeb0c04e124a01b2e1bc1e9b923f96',
                    '2b14fb0733ab42a5a2196707e469806d', '2d540bbcb64d4bfa91070c76b37bab28',
                    '56e9c200ca7e4e81be9859ba68264545', '5513f3f294f143669145857607682220',
                    'bd2eb314d9e94f368ccb0609cdce8e0b', 'f17235afac64453898751a8a5496baa9',
                    '528468e30a2825e0c84c5a70570bf7b6', '83dab3ed95134656a44f06be45be93f1',
                    '17d7a5173f424a69a1bab593f21a2651', 'e658fb078d13462ca8aaf35ed578056d',
                    'c733e89e4b2c42978c5850cb5c4b7c79', '0fe672d509b14d8da2b4e6f2f5aad777',
                    '7b9c978a2a1a46fd9e46aff5d697b7c7', '65c3131bc18c6adf6216347ddb009cd1',
                    '37c152f12ed045e7850ff0ee568da9cf', 'fac5d924b68a4581a4cb1323f878b7dc',
                    'c2caae673e3845c4a58b4b1218ba73d2', '179d9d6ab5cc445ca0671dac3dda4057',
                    '28a516b0597c36dc1438b98e5ea8c42b', '49a0682b16283d142e2bb0ffc53f2460',
                    'fcdeaa88e95d42eaa9ba97c469a27737', '245171d2fa934e169544f8ba63638adb',
                    '01f3a237a5fc4cdc8bade24d4244eca4', '1c67f4c5f9964f63895aa754464f0eaf',
                    '6298aee01d5e4a6b87e48eb951342323', 'acbaf3751aff4e039059132844700258',
                    '0bda99ad45f9460b9258202956bec543', '0ef317c0770442c98b9f85764ac973c8',
                    'e20c4f0cfade4783b5716089064cde44', 'a19e2feb7b7a4497a3b2a79cda23b102',
                    'ce31c891052246e5b42577c04673a989', '13b4ca10b2604cc6b2e82c4559167551',
                    'e9156acfc9f749259a52e3a3f8a17dba', 'a94efb31d0f34a919d811a3ef2699b02',
                    'c3ab7eece8d84174a01c324d97b3600a', '67fdeb0548f34d6f93a85fd82856bcac',
                    '2090b5bf145c4fcd836f8af3e56e1d5d', 'e7c396d311d249548f86e954b982c336',
                    'f8d5b46c0457406fbdef945c3756ce8f', '2d972ab679a04abbbb9481a89dfb1719',
                    '4cdb4d148f7142c3929b9b66bc636aa9', '2075e3433e494f75bb0876e0e929bb77',
                    '6cb5834fe2ac42a0ae0d040d20bcd0d8', 'd59811e8baf443a6a9fb3156e8a0e069',
                    'b221b01bd39144bcb353e26ebb660fe0', '5c020fd24ef64f2784797d6600c1634d',
                    '89c3f5eabcb045e48d39a3e5dae8503e', '435b4b56545144c6a07566040c147fd2',
                    'cd98358048654206b69c1de8021a9188', '2e9777f8d4204892a82ffa2fd5233522',
                    '2f9ad77301504eb8a3b006dddcfcda41', 'e233477998af4450ac8db3a12713f4d3',
                    'b8500ff75fc8412d9521c3c36b2c7d98', '77ce862774e44f25a3a9a12a4be1248c',
                    '6b2ff9049bbb4f3c987ba13e91898777', 'bab32de4d5704b8c9afbfadee6213f3a',
                    '26ea3d2f613141fa8c71b021b8d6194d', '6f1ac950727949a99b98398be60de670',
                    'c25cde0e774e4bd398a827648207a43f', 'a679922441db4229931cace4cd45ec72',
                    '8f6fcaeb42344d91993d0440a42f51a6', 'e58ea64124af494894a6dffaf1522cc8',
                    'afe40dfa7b12483fbdfd123c7ccc29d0', '8e55d515a5e94f12b192a2b7e3266ab8',
                    '715ce540bc1a4b66dceefce29d203bd7', '25541e5547c997826df86705e0b6b912',
                    '2deab6f327a24485a4f5a5a46bd5dddc', 'baddb94e9fa042d2a403320fbd9cc976',
                    '4de227c960624539bf82e6ba3591b75d', '85e45862f56c4616b0f75818dde1959c',
                    '32dfaba71c764d7e87f811dd27510e10', 'f9315c7e1d6443cb9ac69cbb2ad66a13',
                    '2fc7ca0cc21047dfac7bd4476f9ca243', '4e661f79f1c24c24ae73b4fba49f2f6d',
                    '58e0bc1fe15144f19d3b7b6ffbbb94e1', '06b5701d7330447192a675f9cc2ba824',
                    '7ae5da6ce2254889a0bae227d89553d5', '68f75394be8c44b79352303f67b8d022',
                    'e8fed58561f54e0fbc4fdbcb0fd371e5', 'ea2b0f6c4ca5446c99a775021f590633',
                    '5087f8bfc6194f74913f74806a14ebf6', '00221888fc4e493e8179173aa0f27c9d',
                    'b363c18e85d741bcb65a5a397550ec35', '86ae79480be54c969b4ebbb45bfa9893',
                    'fb6d3d1da5ca4ab5b24b81b55841d44d', '3469790de6d1443a8e7042e737101a83',
                    '95fa41abdd4c7a42523596483c329790', '43f8136e47c94129bbd59184048a426b',
                    '99fd766205484c2085ee6e6ab3fbe4a0', '552cc43f72dc65a75a649ac302ccab3c',
                    'a4e3d6bee9ad49b6958c072687643cb1', 'bd0cdac97a0d44f5862cf458cd5e46e3',
                    '086383e4378a4113af1ce02da47095e0', 'b9570635ba114c3ea971a03412c99d74',
                    'a1e8127bf82e4445961e9247275133d2', '788310cdebef47fc95cffe0634dec6d1',
                    '918a8fd88d9f406bba8e3ee9ee8b6ca8', '84a1b795b3f24144999bd2035da615d9',
                    'ee2e2445b4c94948a7599c74c08199ed', '32486426847a4723a8d9c864dc9f0b1a',
                    '6d9bf0b7f777420dabd376ba209ed21e', 'c2828111f3984b269c2527983ca50b43',
                    'bf6169def274409698b3d90dca8f9e84', '91048e21be4c42dcbe98a3702402e2e2',
                    'd615b826fa4a479ea495180a1c9cef5e', '4ab75683c43d486dbb53b65fd43880ee',
                    '65b0ffe7c92341459740a978a5bad265', 'e2c3e88a48654ae0b7ec7b21218ddae3',
                    '6cf1452625df444898f383c5fdb88893', '4561eb0a866c61a5363f114350a1081a',
                    'bf06c96ce2994376a0e0f565a1daeff6', 'e2526a7994a04f46b474a92e5b8ea55b',
                    '9aecaabaf3828549b5c316e991d4c4a0', '8156a6cadd834ce9aa891625a7062494',
                    '86e55ee963854b8fa2e77915e7e4aa0f', '0cb83af311f84769bea7d29ab6ae840d',
                    'e833ebdfb51c429fa073c47694eed869', 'c66e5fe676e84cfdb2dddb2fa39d2901',
                    'cf86adba547d4be9b14a7af81cb20a7f', '0b053ba909ff4adc9b1c191b4c2c3ee0',
                    'cd5d242af0cf45579b6c56913d03dad5', '5d89319a7385488cba2d98ce677e3f0d',
                    '7a2616aa338c4c37bd42e33b6b2ef9e5', 'e6c4dd18bb6c427ba63686016d5dd5a4',
                    '5fd232f0919d43b9a9ba567ceec40297', '7ec9bf442bf94f3298e4c7e66ba6e301',
                    'da9c171dfd8383be7aa395108728e4bd', '9d9aa3770fa74e91bec66dc18dab08bd',
                    '841521d5414540e0b69a396a1b74cba0', '98ef9500cc944a3486b1acf59b3f032f',
                    '60b1554984674005b23a114562278216', '4e605ec8ea624d479b91b6c367662c82',
                    '2528837171ae46578bb977de013deac7', '056bd87ccaf447f8b877195fc02bab7f',
                    '08650f8797744baeb2731a3e73f377f1', '3d03fc689c1e4d3a82508d132810e047',
                    'f169df72e6f44b48b68e51fb5eb028d6', '35c5a3500d41499eb67961f2745b9e17',
                    '3e2905fed4c2460daabf6787f044f07d', '848c62ee8de04e0e94d53c42d5d1afe5',
                    '9d4cd2a19ce34da4a71dadbf8652fed9', 'fe29cc4a5b2a4a38911098356af4f86b',
                    '440ab978a52c49199d75d1c14c59fa29', 'a603a316fe654229be6d868b21f2a558',
                    '6921a2c8d3fe4ea49e284d9146cf4d32', '880ef17e949e4b3a8915ce0a3f047676',
                    '8247140e34f24624ac0b3716fb76d86c', '41d20d4ce45442c4b10dffc46374f9f6',
                    '7495bc4c2dcb44a3a473bdeb4ee63e57', '8575ef921fe04e03ab4314096a7d9049',
                    '9a423d1129674143ba4dcca5af926dc2', 'c4e51589535c49cc9ecd9cab6022ee77',
                    '9a63e5084ea642c2a8406c9199ad9d96', '0ac023f879a643e7839d4f6f145e92f9',
                    '0733f4ee2acace81f1d318fe8912461f', '46df4e8ebc584c7f94a2118dbeac62fc',
                    '13e89e1a1a4248cb977c1cce9c26c7b6', 'c607cc61c51f468cb2df4dbab6c22b60',
                    '3ce27bcbfb434a50ac1545c5b4f897c9', 'd20b5a94a524449585b7007969eb4103',
                    '423d203231c6428fa9544f241cc24369', 'af1667d375ae4233b7c16e4ec92ef0d0',
                    '067d349f8f86402e8131b9ed97762318', '27a4466caf9b43698805c08816e3631d',
                    'c0b4e08a76b14a62931e0a1057c2c912', '9407dc7942514c4d9297ecb67457971d',
                    '8fc594bedf7549e38e153d3beda5aa74', 'f0a94c2eec004277a77636ef2657f123',
                    '47f7763b24284a3c9ee893b842115a20', 'e5817e4a48414d5abfd96f155ab94b80',
                    '14845b74c85b4e12a10a9aa187b176ac', '3accfef271284cbca60c193305b46b47',
                    'e96651bf9d5a4e6f93456f5fa60d0ccd', 'd92ff8a513b415c71671476d5dfb3400',
                    '99d8fcfda3994109b4a846b94575ee05', '7407aea0d19e4ba7875f3cb6639fdaa0',
                    '1e5824535a494f0e8636558e839575d4', '793796672e754cc3aaf6a67e9aec69c5',
                    'af559948b9434af69721783089cb289e', '9afc451f11454a14822d7861511a72ad',
                    'f47c02f51dab4961b86a2d3fde8429e1', 'b957b332055f46ddb58c98cb24598e97',
                    '6b215cac509943aba2b8d563cd1d398d', '1bce09304d6dc5cfce350d30ff03bda9',
                    'a54c2dae46964a2688642c2edf4c5647', 'fe7b3047cbc3459998659156987eee56',
                    '86cd82b83666487498315fe56f4c5547', 'a6ec94f1640340dfa22820e11f0d399f',
                    '21805b10ebdd4c1e845169b89c93a993', '2e4b191246a74e84be6ffeb8f211354b',
                    'e845bbbac5e44d99afeebe2e34befcad', 'd5934208d31f42939e5893969728e1d9',
                    'a068aa28731042b0964c79f21cae144b', 'ca9f435ec70b4eb9baa6b0ee10205506',
                    'f274ff74e75947dda4ed44d0fae97bf0', '993cbc2d0e64433fa35bae55f546b4a2',
                    'd261110c7253498fa8ff0e0eaf83bb62', '843a88975f0dd1944c5e650808ff9be6',
                    '5a2b1e2b9f7243f18827f120b3185d5e', '477df3eecfdf49b2b31ce1c3d54386ad',
                    '96ffdbc4d7154b878f530e2527b6c8a5', '8ad2562551574585be348d27d54f492c',
                    '657360475a2943798195dd5ff0eff668', '7469d3445d0d4ae4b9d5d90fb72c4c8f',
                    'b00cc55a24fc4e2392918a311562b7e6', 'd1f213d40b154753928e126391d87af3',
                    '586c795ed5534e35b64e890a9d79e30b', '461c583bf01d4e1c8e336b0c1241300d',
                    '6d67eb2df6d441cfb55ececf04bb5c10', '42d758a566a84308998550c44a1540c2',
                    'b34284e72b6241d58d38e83af83bd575', '871355c5f0cf4d4b9cc401a952889c65',
                    '97ed4041708e489e82788b6f95fd5c28', '90acf7cf91214fe1be01b3c94d1ebb05',
                    '6f95d7e72da042e4860cf36b8a6822ef', 'f3d175e8bc0047fdac94729f147f99ee',
                    '9ddd678eae584b0b984e2401ca73c11d', '70b85e0d4c8e4299a09eeff1c6a989a5',
                    '3398dde68f1444238d045fde38457e6c', 'ddec59c2d78b4e4896ced644a015d3e2',
                    '83f27665823947e29eef720f4bbe12bb', 'd0df05e6128748fcaa50979ba28a75d8',
                    'b4ac19ebcd3a46a1bd4509104944263d', '7d87b0441a8f4b5ba1b71019da4f89e9',
                    '0e5e9a72fe6b49afa67d43564d7aabad', '4978938606444da5afc34be1ecf05d90',
                    'a4e645e5cdff4826851fdedcae0eb941', '1b5209c54a9b4f77ac7c3fbc6037f945',
                    '68c8256e7ff34aa2928835ed9dd7228c', '020a673c3ee24cbf9f0ac95297687c38',
                    'd8385fd6401c416dabe4f88d0826eb4c', '99a3aa5a21664603a4df652087bdd011',
                    '1d64d3b5b42a4d06b82471f613927640', '8d145e6fd5f14dfc8edc41d6d9380228',
                    '468b553c3bb8403a90f9fc2dbdf8a25a', '273085c586cc474f910f7366b1eadf30',
                    '3249e00745de4d3da8772aa774665803', '24d5d58c312e43caa15e8b1ce92d4a42',
                    '979d72eac88d4210a5f78fefa1c3cd72', '32031b7f70cb500756adc77028651230',
                    '1db65f2a69b14bfb884b3bafc931fe1d', 'd56599d1b3694252bd4e0bfd15a6563f',
                    '70771e4aab254697b6bf2379a4c2e6dd', '60e023e8162942b8a7a5fe094836c509',
                    '2a3b2e7250394af9b24fac0712de35eb', '6e879e6b8a434a028521d1a7f94b8d42',
                    'e36284edbab34de69da1808a5163af5d', '23eec5622e51ca68eb80859250f27160',
                    '471efaef038f4517b3ca79691ef1f735', 'd7b2bb0fcf34475c9edf9fbc5aa82186',
                    '13d81e2a0980435886f07771cbacbcd8', '9cf52b4b348b442a93a701d39018975f',
                    '28fd26ae0ef04ca98f3ea2a703da1e40', '819bb5de5f9c469bb910be0b571ab074',
                    '90746ceef75d461abf93090ca14391d6', 'ef197098f0a945caa8b825ca7770318a',
                    '64b300d696d941b29796185a41d6872d', '773642cfaa3e4941b0d320b0cd169dcf',
                    '76dc61203c144b2bbea5317fc3ec538d', '55c499e37a814722ad14def0160f8ac5',
                    '2d3558aa6c934691863b4ce13f316874', '092bcb14dba1487794c1850e4bf3f01c',
                    'e960bd8173fa48ad9b311f6a5fa5d49e', 'd8ae4c48c4f547529692b18e71dfb2f8',
                    'cb8ea7883a5947bd80859b5836de0938', '0d09f23047a54a4991bf827a9c1ca62b',
                    '8eb45f25f72b469e96eba1bbdf29c786', '16692177ca834dec8f9f8f9839241c11',
                    '68189b2579e242259711677b4a1e88d5', 'f4f9a61d22f94bbea68c317701ed7a91',
                    '60011e2c917643f897c4525d214a36de', '2c3b659a3d024480b1bcdc10cac87325',
                    'ba42272340114ddfbaaf4cce90ff473c', '93b6394f98d44fc89b71c12770ab7fcd',
                    'c84e1a49ac004ad5933fa106eb8a3b0d', '6fe64ecbcd004abf881fd909e7a61b6d',
                    '56b0273a72c145cfa491362fff6daa81', 'fb271939a7e34d73b211ae7e44fb3afd',
                    'ca2207b27e1d4b3288c41c07a754a385', 'b2ae425cb9dd43c9b3b8d66b502e6cc1',
                    '309c7891615b4ef0a0961deb03088f35', 'fb08ba8c50a04621ad0854cf2963a772',
                    '070c55201eb44d1ebd84aca5223901c4', '197dd5c56cb045fface830b2074f0e41',
                    '83ab811cbf864e8ab273b21e1bbbf59d', '8c8c8c1ac9134dbfb6936deb81ec2b71',
                    '99027bf56e264835accfd0eacaee3230', 'b91b4d96389247f08391275cea086007',
                    '928a5796fbf847c185b9c923f32cf324', '96d7bac8e9e6414294dcf5837d0ce836',
                    'f5196b1fb6cf433984dce2bc59ce490e', '38ee2d59042f40e2b9c46e947471642d',
                    'b77f578b91f04c6cacdd1e9e2da36e80', 'c3ea634faa504a5cbcdbc19cf266acdf',
                    '333dda4c214742dca725118c118b524a', '92834018ba444fecbd31578d698f0165',
                    '1f8c1fa8632043f18f3f62ace7868642', 'cc87783c33204160b7a610f8653f5387',
                    'deab2152ffe14ae1b6199f16999f59e9', '35fc9846f62e453286501232e0d18b7a',
                    'a358f15e1c92453fb000e0341237d141', '9e124ac3cac4418abae579de0887615b',
                    'ece2eea102cf4f34bc511790a891e1f7', '8b6a7a5f84e1442aa370ab5979148cb8',
                    '2182ebc74b584006a3bf101b64731333', 'd1ec443d450c44f9ab8ae8468a0d5f76',
                    '68bbfaf2b459f6b772524c61e13b0e1c', '2f7cdc0ab49742b6892d6ce23afc36dc',
                    '1c8647d8868b4812a2f4e52b5ae6968a', 'acbbb500d7054b488f7f02fa8c8aeaf5',
                    'd797ca7ae51a4f639b21ca5f7ba88b4d', '2d39f0111891453c88dac2462ae55528',
                    '081b6731f5a140be889341516e2532f1', '75028b0fb6f9880bf44c16918bd44b1f',
                    'f73befd6b4d64e8eab7fabf5602c4a9a', 'f410a32da30f4a7ca3bbb31461f58d0e',
                    '5af2c10c478a4b16ba020b7e1308d42e', '242cf270df634e0b91d6f6b26dcf52ce',
                    '1b9c5c59f7a84b868eb9b1cd78ba8573', '75e5aa0603db451ba5f9584f31ed8fa5',
                    '35ab8259d7964e3da2e0fda8fa72e2df', '3ae76082fb4149e5a1cd0cea99e48a5b',
                    '5dafab0856184e08a87db98b0117b768', '6d32245bace14405b3697b5bb2e75a15',
                    '898f563b25494a08a3a96f0c605eb693', '545883cfc55f455e9fc93436dfaad93c',
                    '9467c00d1b1a4ee092d3a552a4a195cb', '0bbafabbe2914298bfc069a143934523',
                    '15f593cf381e461cbb1132fc4caa1631', '31dbe1b9f40540c3950a7ac7e3954fcf',
                    '988221d8d44a4bdba4113efd527b46d0', '6e96ee77abac45ccabd65ef74f605e46',
                    '4caff1fe202046e892d50e536b2ce781', '8808e99743e742d9a8a46da6253d82ea',
                    '240cf2801eeb4360a38c987b6c88b905', 'a0999f9a9f2a44ff83b1bf97f5931e3c',
                    '99b498c14f4642f9bce25e5fbc4156d5', '17dbc599091a436bb140dc71eeb7edda',
                    'bbb6355f9af040158a73863bf1564dd5', '763a7576b5454015ad9987e99f84b770',
                    '17ab1255acd040d0bf97751dfc24af7b', '85f25845367d423c954b7571e1b5e27d',
                    'df180889af1b4273abd72ebf041d658f', '0344ce44530742079b7249a84119d9a1',
                    '329628f603174e8fb6290b68e31c484d', 'edd91d95c6dd4d4293dd74b8ede5a543',
                    '9aef1cd0721249d8a33c873ae8140e82', 'cf8462b4c073460595c8b01ff890a383',
                    '10f1dfb637fc4e58bec7a2508aabd6a3', '6f34bd94f8954ae3a9e38b20a816fe08',
                    '5ef1415524fa42388132c0068342e744', '3213b33f8e4648eda1041f048b089039',
                    'c73a5798033e4a43a5a4e23348c2c8dd', 'edcb03a81a7749dfbe76b71deb5d76b1',
                    '33f4124d09e64c4da1e75776c97ae99b', 'f38783ffade94a2aa5f55ad29402f229',
                    '9bc8053e36e24e43bdc441d068f13254', '8c22eb0faef7465387ba4dc37c0741bc',
                    '47192314966c4035b0d2bb060696d9d0', 'be19e310b5f5459085afa19eeb57f647',
                    'db993c15201845f7b4a8b59a00a73c99', 'eea821c22883465981c215120d28f9c9',
                    '50ff15c8dc174fedaaaf13f5fe0ddb10', '7e843edbcf584e229d24ff66e897207d',
                    '400675ec87474c6ab8fc8013c6650f09', 'dabfb16092e948f3a09bec0d4cdcd9f9',
                    '07f32fd34cfe48989669aa5cb67a8e4a', 'fb771ea81c7541a5a1cd493ecad1fd25',
                    '2af4644b31b548c5a7d1bd973309d0d8', 'a35d3e134a47478ea7b8997cf623cb07',
                    '205c779999764ed6ae8341a0d1ac23e4', '5a30614f887e4ee98231af51100610b8',
                    '4edcdb859ab646648d6573e041130886', 'f23ce7b9482344199a8e72dbc5532385',
                    'a6a00cb2932a4bf4a72fe3b94e0530d6', 'c339d9aa840ea6c992f96b5653205380',
                    '1dd04b9008144014925a65ab59b15bfa', 'a3bfec04e73b4f39aaa4b6fd51495175',
                    'd1843087fa6b4fabaa84b84e89c1ebb7', 'a739b38ae48341bb954d0d93189c287c',
                    '362629bac23d4029a1b95090ccf0535f', 'c88b8ba59e0f468091c30eaaaa059ed9',
                    'd32702e50ef74beaa5834ec344dea2f2', '43467157198b4d2da53762da62451f32',
                    'a69adac020d842b39a1eca0bed3706fc', 'ee1d19039c624dca86f244df5c4a1955',
                    '2cbe8d79b2f1419184d4f66e56a8d148', 'a9bf6206b11948b28004953a378b1d8f',
                    '59f1a0a6915c4e09a341258b56120f0d', '8536d46e2665408eac86cd94a7f120bd',
                    'e77e40b0703a45eebc81afc0ccfc06e6', 'a20386aa053b4fbaae12a32312235e95',
                    'b4134ab940bb4000a75f2669db59e549', 'dd9cd2bbb83c458287f614f1da8881ec',
                    '9f327b91f5374eae85aeebf7760092a3', '211b95d666174ba08892e6e40b8f20fd',
                    '557382ec38544dc6ab1bc4fe0ecf0375', '3457a2b57d0790b86a4f492dc07aa500',
                    '39594ff5e15e4ed38d3e48b98ccb7e1b', 'd7bb3974ac3d4f109aeac56508e16527',
                    '1ef8c0766def40a882bd74f62b2b2aab', 'e119b70620e2496f819e98d90055a284',
                    'a0b90a4e887344ce8c4f61690d63615e', '6d631cfd1c114d23b823840a51aed694',
                    '1daf1526c5234a66a366c67d38d86447', '4bed96fcc5554a92b0d8a7077bfa34bf',
                    'f1520030c21f9bcd3bff2cb6d89ce223', 'a4a2f24fb59e4adf8ee7988c25bb5163',
                    '2cdda083a95d41cfb4c4f3c45230b487', 'ff3a827ad04c4e4db26630631b685bcf',
                    'd915b4388a914ece980bceeccc1f9ae2', '2c33662f946f4217ab8cc57cb9c40c1f',
                    'b4efae47fb9d4095a60f186bb71b09ff', '0883a7b7ab954ae795a5e7e0fd19ce5a',
                    '884e3267afc24b3593998846764d5a15', '40ed3c8d328847b5b897e526fc4241bd',
                    '2be96e9bbbd84c9d8e787161c6284bea', 'caaeee51791f4c2eb6e860a9abdd8229',
                    'a6a53b2e71da4cd0924b05d3ea564278', '388010c43a9944dc9fd8d4c1e3c4dbbc',
                    '1fa2b11967d148ca98a3a6e91100a1ce', 'a197d43ae35af4d1e8482b0cb782b57e',
                    'dfe3562a26114102916007336658eff7', 'e63b749062fe696322fce1adbcd40c18',
                    '231e76446e09e9937641df0c06bccc5d', 'c0c300cd22524e39bc30ddd02b45f2d9',
                    '49b42aac21d949a3b1a98db9e5cdf836', '8ff82ba803604350896c734fc48cc78b',
                    '709b70168c1e485ba38e934b240d2416', '87860e40b87446fb9955f041db7eadca',
                    'fedc38e7f6644919b546744508981a86', '8f5b6f4c10794e0fab3426e2295c7f9e',
                    '028023cf94d14aa988303ff5ac51077d', '078abd28bf994b85a3401c2b05966423',
                    'cef6415e7f5142409efe20f223f809b6', 'ea0753d7dfa34fffb75a5d05f124b4ba',
                    '3191475038434393988e4170f75ac18e', 'd1ba686d3e99caa437b9446cc8a60cfc',
                    'b97d869267734191a4d133b0866176df', '499fe6aedbeb4646808fd2ac6d88149c',
                    '9d08685208974aa5a460a9c57843d095', 'a5404dd0f6eb4cdfb7320c05f2cf2aab',
                    'bec016d697724bfb90b835c71d08157a', 'd72f758f22104cefa31c789c0b1b368d',
                    '56ba2e26cb494bb5b06645e2fac3dcd3', 'a2a97470cbb1497da9cadb4f6560b63c',
                    '536bc383d7634b2c8bea78145b8d42b3', '90ebfe02a2c7479cb114a6a16ce27d82',
                    '81c3be48baae4ff3b345cb4903d62325', 'c248e631ad1b4f49a2e3310180ea25bc',
                    '1950f776c790bd1c2fa4f6339ba45ef6', 'd041b3bc51424a2dbd2acb949b3aa39b',
                    '95c492dd3b404017828325f541ca937c', 'a4fcc9775273472e91f13abc460b4255',
                    '5472eca527bf473281811c6d8d6866a5', '11381048c5b142fe8a80d747ae25a59f',
                    'a7c1bc592e144f51898ec51a4936e92b', 'be8b165032b86dd165a2735ff7fdb15a',
                    '9c333d22124246efb2ef9d6cb745b6ea', '74181f81563d45ff86aaf4f5dc9adfb1',
                    '0029785a02e3473bbb22250eedbc3ce1', 'eb2edac77d5a4217bea53c660c95161b',
                    '73a46c439d8e4ca4b9dbc885a426c96a', '30ae7edea5314ba487d64bfcd62d5918',
                    'ba0ea841365d4dbb9c20636d6ca2b04e', 'a6ebf1fa987a4a1ca5047dbf5954f6d1',
                    '62f2533f5fe547c898b5bcededb3c8dd', '455be34c952d4126b72f7eefe2a28fe7',
                    '13d63cec74354d4e8ab307412e49752d', 'f7b7d08f3140439f8e964974b6ab6052',
                    'c507c2bb3b404a89ab970d968457919b', '9e9e84d0cf544d9ebc3ce5a40c1921da',
                    'e6cfee4469ab48d38e73e0d0659db7b6', '531dcd953871466d93bcfbbd31391a0d',
                    '8be78132b2b44eef97d2aec4e4fe46a8', '360c5f78f33f4e2e922b1d13929998e6',
                    '79066e928a0043c199a37b9e0d0bbdab', '9dc2155e486d48c983311c625b38c2bf',
                    'a17763a713fc4ed2be0103089a6ac351', 'e27eb42a55ab47d18f457206a1cb9ba4',
                    '3e25fbe7645742d28a3e86d95084379e', '258ce16d91af477490a4201bed92b7b8',
                    '742cacf61ca04e298a1e6b3561a6d807', '190ee2996bab4b56a91c26f7c88516fe',
                    'd966417eb71f4f45a178455deae5e7a7', 'ad966819968f48399ee40b2fa3b9ebf9',
                    '42284c57d0380d86e2fd1658e7c537a5', '7ba51810eaba4b0181fa07aa6fa5dde1',
                    'c9bee81f0cf249f19f9543f9badc9a64', '360eada8a5bf436ebe0fe4843e7f01b8',
                    'ca9171424e4bd5e016f7957aa166d765', '33a7d232c748419cb2caaaeb74394be8',
                    '5038ac59873d455c8d6bc15e8a098991', 'a23fbd38c8a142698935731b2b0ffec6',
                    '9f00785d5c0c466fad5bdeb59c86d0ea', 'd35ac9af86944cc3aa4e46e5813ef098',
                    'a21e74d19a3340eb910300c13b81057a', '6443acea1d95e405670becbd4d0da453',
                    'd5ed308c51ed45018af2db43c516704d', '261a6dc4b24c484aa5670277de835837',
                    '3764b7a88feb463bb6d7b01e01c0ccfa', '081c4f89e70645a9b13bb100ba88c60a',
                    '6a852e7d14494029a55f2b3bcb36bae9', '135fdf9abb6e46b4a7fb45bb3b69a4c9',
                    '2a9bface91c44329b59c8db1ab918993', 'd9bfa8026a984ccbadc365a350924d1d',
                    '0c4278acdf914f6db748d87c2db3a5fa', 'e9ba1984603b4f679103c5d6c096498c',
                    'aff4ab4a960549e29e989f995cc92a6d', '9b5a61f457884ca9a044330d75d3fe79',
                    '12c80c647fc248f39f927a763b62e138', '9c23423210744e6dbd4ca71620676052',
                    'ff0b157fc35d4e04ad740b241290c2f0', '54ba52c4381b434f95996b3cd54f9c16',
                    'affdb27009aa43f7ad2ff150e9c4f96b', '30b35e1f3f954b6481d9cb985a668738',
                    '6b0eeab99e564188892746753a88f72b', '2602bbccd2954d41ac60c4f7995ed1a9',
                    'ad2cb5138ec2aed57441dacacfbd5600', 'fbefd7a9142540ff87c388b58f6dc823',
                    '4d3bf6c8b3c644ccbd2b3884af7686f3', '8018c0d3b61347a893046334d7737154',
                    '3e6b2879c99d4cb6833fb16a894d1f06', '6f922fed1b8f4c7892656ad3540520e8',
                    'c109aa7f78ab423f8c44ffeca3c33824', 'dfa9da88d0fd47c4a62320c646831aef',
                    'e507dce86d82488fb89a78994ea0af99', '858599e90bbc6f14a86170edec3d4ca6',
                    '0a2569ce479f4d8e83eff0610f4fc0d5', 'da6f3a8dfb0b480fa8bf11af326cfa77',
                    '6e6fa680d9a04b258c7cce751d2ecbd7', '64f049ff0a794cbb8b825748bf29b8e3',
                    '7143a067546f41b499cdd81f38ca0253', 'b5d53efd85bf465b94df17bd1bfa8a01',
                    '0b6548a1df2e48dfafa4572ae36f94cf', '99b98822631a4bfea850e451dce897fd',
                    '7684012573b84ef0947116579f1687cd', '62918bbf3ecb4db3bd1d1713843c64ad',
                    'b43f31cd128d40a19ded3202a122669d', '5014fb29a3eb45ac91d7e7e6b066af32',
                    '6d1efc618dbf4bae8fc3cbfd793f1039', '7d67e0b414a340ea9156ed38cbc253dd',
                    '659ce51cf36e4b1a867c4d8cfa2ac017', '580a493d12cf4567b4de1a645a063e60',
                    '68e99ae2362b480a9fcad1cac112585f', 'ae2cbca7975e4df7b9d2c515362398f0',
                    'ea94e2137bc04193a1c75a5ebe0ce683', '2d9ed99216e64b1188be2d9b384b89e3',
                    '57d749e9df914ca3829e6f13f47c368a', '0059b6cb049d4bf29753e9d0bee27136',
                    'f30e0498ea8c4d02bfd23cb35affd25f', '284eb9969da24852af336354c9cdbaa7',
                    'c770edcc26c24a988fb02bc79e3da69b', '0463c6268cb449c9a95676a0dea6e68f',
                    'a6bd367e71624766aeb33b7d8b6ee73e', '22f7c8ba3e47afb6de14eb7bda5d3d1f',
                    '1b1d784d6cfc4be4ad45cb40c0b54e8a', '001e4cd331644be380f1709ade670f98',
                    '134da2c40e8340dc816aa26b33fcc7f4', '27e99509fba44ce1a636bc61fc1dc94c',
                    '83e8a6b1a1224837b16232ed7b764522', 'a4b74bbfa0094a1caa2977ae37923188',
                    'c91515aa87044b03985e8157dbdcdb48', 'd509cad79ef34ce9858d46695aa9d827',
                    '6ab31ebfbffc4473949c19eb99a4895b', '6621be9c1fd747efb8fce4c02d3c5a20',
                    '80a4eaa3dac840ec899910115342f464', '5b4bde45ad1a414d9f83f6ee82b5846e',
                    '82151834389142ca9865742aa3d59e3e', 'a7b9bd63d1f8485b92e6cd62e6e09ab9',
                    '48e04e95bd534de3a1c980aaaa835cf2', '8eda4604ed224e1689d7e44bf9d4e060',
                    '8bad2b07e3b24e3ebb1c4a19d90421de', '862ec1241f9f4f7bbd10373087a4bc3c',
                    '27b1408fcb474bbabbc8f0d41546dd81', '4be7d79210db47c482d4d7e0ba78a144',
                    '7454dd5de5cd253d351f4ee35489bbce', '8649bd544e9540ce9688845ccd6036b5',
                    '79fbb62acfa54a36896527d00eba71cd', '23968f71a25e7c8a9059aad9fca9ad01',
                    '0fb0b59b24c24bd8a5ee8f45ebbc2ccc', '5a36a4eb211c468d96a46935715f8f38',
                    'de7b0aedc75a417cac851a0d4ee0d3a9', 'ff4cd68bf00744ebaa13b31504b049d6',
                    'afd0c3ada0954a7b8597628ca511a239', 'ef4e99f1c6d34e67b60138739375ea0b',
                    'e4eec854029f40d49c60b5ca7f14106b', 'e913d03b266e4b4f81dd562d0cbedbc1',
                    '6620288abf904790a1a6a604ff27da7f', '37264abc4505437da03808d49a753cd9',
                    '802f2e5c279098cf918692fdd8d1874d', 'c46e4b01df80c537a1fd9a919c1920e3',
                    '5891c099a5c148beaa67d77a4bb97ada', '35dc5d771d43417ba82778fed8716e7f',
                    '5d4d2a7a10704dd4920f971f2e76cc13', 'a12964d406fe4990b1dbe41ed1c7ed1f',
                    '84c402f89f2c45249cd14a958f94191c', 'bd8cd351724547578dad098cc766d225',
                    'b44bd108caea40f884e7945087fbeecf', 'cfe941b40e08466b8ffc434898071951',
                    '38b9e686f4a446388d6592a6855a1274', '04925a15605d4e2b9226c7a7aa46452e',
                    '2409c3478be14fbaa845c2b187c94a61', 'a66b7d5648cb4f8fa04ff821c5dd8eef',
                    '9138f485e3fc4407b6648daf790ea0a0', 'c5fa929864494f72b1a91f946a257bfd',
                    'c26b856d71f94ac682bc7549cba3b665', '8bff798c032b46d8af4f1ce41b787c23',
                    'c2d986456f784386a6d493b38262f061', '485ec5608aef4c268f2449b759321da8',
                    'af06de7694c24bdb9e48c853c1b649ba', 'a52a69c5b6954f6b89361218e518f635',
                    'd2f687b340324bce9d1b8d14fb780386', '2016a60fca5b48928c5e5e48696d66f0',
                    'f593563062914ba192e911c37805791b', '8457916d877345f590237afced0f4c23',
                    'f2109e8c19094ee2afdb53dcd06c7fbf', '06dc5d24e7e7479eaba9c9166430f6b3',
                    'a51f0fa6d2934e4eb87047d4d8276938', '6ac23d101a4f41e6b845207f441b11db',
                    '219abae9c40629917cb2599fe9345d8b', 'f6b7dd749a6c449db9a23a2e2794db87',
                    'b858ef061bee4a6d9ec8dd8591782794', '1ad158d04b0f4762810b5816d97144f3',
                    '4b37be87307446eb88ae45139fa6da86', 'd080f3fda9e14532a9c36f668b7f8dfb',
                    '39fa6a8a56024b999d3c7099d3175598', 'b589d5c2ef540eccc9dbedd876fc641f',
                    '9eb50328ef7b47878fa085a78359931b', '1a9729020a944dfd901f9da7ca08b2a1',
                    '7be953763c684131b196a46d9e6672a0', '1b24c8a21c4643188979d0db6ff1363f',
                    '3211567b3bca46a48916c60683f18dee', 'eb278f1802464e0d9d843ee817cbbcac',
                    '7b134cc5f5454b40909e869e95e6ecff', 'e10a569108cf45c3b5807c09e134200d',
                    '449a76f01b8943b4b1542c0bdba8a389', 'fb133d2d0fa1b63c62d0af64efaf81cb',
                    '63df1509be3b48fc84e0deac2262d5b2', '92841970dc7b4ea3aa20a58435938a9a',
                    '9eccd2515bad466a9d22c6c51bab13b9', '1f161d40bb100619ead6600a6d1893b4',
                    '1a59b1d0cae542d397671ae506dfdc75', '89f88f34f7874697a093c20753ad391f',
                    '54a8f66e23584a9a9650f01120791b5a', '90439c69e5584db1a3c2adbd0af18bc9',
                    '978245d56d994e3583f02b75242bd7f9', '83bd6e2e177640aa9f366b44058e1509',
                    '73ed24a77d1740c6839168547505ce76', '5ea21e4255fb48c081b7848704f6617e',
                    '4be20a26da0f42b0ad1c7def55c064d8', '2468c4835ca64d12bcb1ce2939cd6cf0',
                    '5c670ec5e6d44d51aecc0d1b4f8b4501', 'eee1923434864730b40e94b298117259',
                    '309abb1c41be4fb9ab4cdd3237de64ca', 'b5a4149b19f249fb9edc1114d48de844',
                    'eac73a450da24d8c8a7ca151409113c8', 'a3cac4568a484780b2fe7d7e6a1717bb',
                    '3115f8fd8090497f90453ea9711db76c', '82e1f8c8f00d48c0b21b4160487955c6',
                    'f7725b40ac3e420eac4df9e8375bef1b', 'ffb85ee7338a40ce9f5d550d479a7f30',
                    '4ecf98b89dc049bbb743406fbba41815', '7fb9a9a985494764b0191aaa13071900',
                    '0671d9e92e2e44f2a056a321f05dac94', '072c380f7749443fb0c4691de81f8d36',
                    '7c4db19cfe56461ba3d80bda554eaed0', '9c64439aec074974bd40315a8d548f69',
                    '81508bb7ae7e4997b78cb9e173835e4e', '79eb52c30c674c6d916017a1bb2d7095',
                    'a17f68e1bbf5495abdf4397bfe6c686e', '391840b4342b4a178515381ba4600830',
                    'c6ac725f1a16493fb2d75e3871fddf1e', 'dd46ab1156e040d8b5566e370643ca07',
                    'e064d0ac0a1f473d9c18e9168bef2058', 'af8d9f211656464c8876773e6923b066',
                    'b43d2314eec749c99a8c0c8f850e9adc', '993782fd2d0f486c9dffa8d33f5ea13f',
                    '38a3b58efd0e47fe9fa591fa561f8db5', 'bddbdad0703d47fb92c1367211a80332',
                    '916597d140f54cfb92f26f4c5b0e040b', '714aa1cac82d4c22ad06f481eb4aed56',
                    '14843f7d59b5451da56d7b12604e9768', '35a9b3c632ca43da96e3f9934394696d',
                    '9b4a90e95b2a4dd29ba626221bc09273', '43cd058555fa4304a8d9d2f55f0cffad',
                    '9813f2fe7c1dd72d974a9b0657993620', 'f7083942f3d44d1a96a9fd18ff8aa6f4',
                    'f7315a73fefa43398c8e33fdda1dde62', 'ee3444f8c0a04320a5c8fb5781629eef',
                    'b4fcf235c8f6f048f321761757edc6c7', '740c96034cf04ff5ac38c3fdbea151aa',
                    '4333b1653b6142d0b1abf39353666306', 'ded7d661cd0e4163ae74f9bf27d63cc3',
                    '0967cfb5d28344719daa2258208913ab', 'aca9d5277d764fdaa4441ca53687e7bf',
                    'a8a1c24d1bcf416590961df445878d7f', 'e02a133781d146d893f399205044c311',
                    '683c2291804d419e97f1aefdf3030cc2', '89756e792cd44250a0ddd7f4c8d86163',
                    '49274e0973214661b700031a03f32345', 'c44b9aadcf4f4f64b79e6027d2eabbcd',
                    '50f19cfcbe5f4c4b8890ad51360800f1', '778b941d364d4eb1baffa87f6306104b',
                    '15aa09a4a30f4fad8ea32763de1867c6', '7833f4d1b15545febf11304eb42498ba',
                    'f984030f33784c8ab9648b588851db54', 'cf7b806f56294798a441bb11741a6ad6',
                    '596648db814b4c808359d5cb814ca3b3', '679954b800be4031b3b8e80d4b25bcea',
                    '514bd317a1264ad39fab6f833c8968d2', '54269fcefb044ca180211c9c9eed47dd',
                    '43bb9d9043514ca3b10ab5f9cbf95566', 'f65308904db64e198e847e2de756779b',
                    'ff1dfcef45f9481a83749d742c7c8efa', '7a348a7ff2684760b1492a1db7371516',
                    'bb2114f3d96e41f096d11d87677a5919', '61d753cd994440fa8db61647b07341f6',
                    '543c3e01b29c4eeda51f944278ebb7d4', 'b36b4141060142d1b8348795ebb46ddf',
                    '993cd89a0470458d85fbf08196a7f565', '7afab878c2664c57b5a8f9b28e8afde2',
                    'a223a1e9b498ed7f21e716e5b9d54885', '2ef156f76f184106b9e82db1bad32848',
                    'e8fb2f8876c44376b9402ab4e79a7053', 'ccfba972326c4cd38b278aaeba95c226',
                    'af0943624ab04868928b3956a08d9d3c', 'c482b7d130da466fb701d21d93bcc859',
                    '1a6a44497854449a9ae3ffe4d5eb248f', 'd713c702b3cc43c1bb8898d6afe3eccc',
                    '4904a29666aa471c8cf1ae832b760b90', '897ce69a5e41432bbeb8e2ad6cde9366',
                    'b005b6cbabe74a6c87d42e880fc4149a', 'f28b9fd81f364137ba7fe4280549bb18',
                    'fddbadacb5b34d348bf96c7cffbacad7', '8e29acf9e1904f4c90481f6eec6bedcb',
                    'ae34d1d456684f11b5ddfdd826afb990', 'd86ac04d74ca4d9aba5478a1e4eaabec',
                    '48800cc6e8b24145a9c2c123387c8b09', '39959cec-5b8a-47fa-ae2c-68ad6d9898f6',
                    '420742f33d1c41b2a4eca0c3bce69a03', '4af07882b1ff410ab3be01c49d21ecba',
                    'dd596f5bef974351b97ca422c8e116bc', '8569780c79904d988dbbd6769366b806',
                    '5d2b77ee21f74a678d32419654e376dd', 'd99406c0f1ca4cc9969f9c0e4c05673c',
                    'b1d456e2c9d1456eb9b198e4589ec58c', '44c9dc2a1115f8d49d9f89eed3b06af7',
                    '76072579aa0a4aec9132b81f0501e4e8', 'ca92760fadd241be88d6fda38a8e5915',
                    'f65e3ba0b64f497b8465e0826ae6d440', 'f5e60b95761a4ffd8d655e377f6a5295',
                    'c8097cba9ebc43079b9923f8cc87c8b2', '9f78373d96b94a7888ce99d468ce3114',
                    '4d8cb899cc7c4f27b38426ede9b57e99', '9bed46b4579e46d586d7de614f0ea24c',
                    '8279c40098474893b3eb4db7215f379e', 'efbd8e4f4d604d15b96d7a116b72423e',
                    '924be84e15c44038960b61bcdf1bd0ce', '4b130c3b716444d294df93eec878a17c',
                    '38ca4de1fdde446784175eab0938d567', '5d1161059b79419db1ea8deb1424f3aa',
                    'b032412fb1d14134a17be87d493b82a2', 'efc3b12ba4be48dc950c5f08883d85d1',
                    '810b2ce2371146c8aaae58760bfff117', '2173c7399cbc4e33a13526f170c99332',
                    'afb28610cfca41ea839fe1fdaa98562c', '3c32c6ee0ec147fd9adc492d4579c45f',
                    'bfa759398cb14f71b96c5d9463eaf460', '8890ebd305044deabcc94696a98f49e9',
                    '36e10c9a63f0d2ff1ad4fcf31f0b1c3d', 'cdeda16a447f443eb4c6040c109a33cf',
                    '3b1a15b6611143d6b390eb7b7a3beeb0', '1460cbdf532a4ec5ae94e959af860e0c',
                    'ca0ad6f912fd4a43a9442941dd76123b', 'c9ed1421b8b0468d84cc2dfaaf1832a8',
                    '3d932d5cc9b949c79e0a26245cd3e4ca', '69f44ec41d214ba9aebc410a1b6a6c54',
                    'bab187f6ce89401f9144eb0a35252cdb', '8e7677efc7f94ba5a0bca4ff9043175b',
                    '4455863eafb04b2a97756ea905e08044', '72322fe0a81f4c1b98aab3716d775cc7',
                    '127168760a2341eda983f948affb5148', '05621155de4f49079ea5b9565a01f3ec',
                    'f49da630ea10450a90293a3de155b038', '7c076abe2fc3f28552f8fb56e168514e',
                    '8843ed26022d43e6bfac3fe286d35b15', '8f717475e3f74acfac450a0a94a20919',
                    'bb12497b598945eead249f57549e0226', 'eb8364bc4eca4490972ecd174d50e161',
                    '93d94ec6b3354097b2fe5f7aa810e70c', 'ae14cc9d303e4b1a9ca1294421be4e26',
                    'fd7418f2ede24c018f355b00ce280d71', 'e7e803dfddf7404ebc1cfcd43485ff4e',
                    '4fbaf73a01404f6394dd576e476d0b94', 'b67a87e72fcb42a2b01a353f96a39d1a',
                    '91600617b87140d4bbc98392bcef135e', '7a84fad51bb146b4b661220952d5eb44',
                    '506948dfbdab4850815a630a83ced771', '7341b63ba76b4b51833ceddd8a8a20cc',
                    '8c976cdcb0144e88b4a7e7c919498f23', 'baa18cd3afce4a4589352e277152d998',
                    '8aed4c422fe64a9f83ca1457a292f390', '23615265eae5449e9913d0d9299ed1fa',
                    'f679c07757894f02a3af64aeadca608c', '4dd54ed4c828411aa4f678391dc58302',
                    'a45fd34678574ca2ab2a955b3d5beff6', '3c2de6882c9640b9a03a83a138e2046b',
                    'e6bda818903441ad9306631775534d00', '763c805b8123409ba6d1593e257f0caf',
                    'd55e720bb983495ab40930acab18b62d', 'f55043fff60b4b77b60fc8a2752aa8a8',
                    '64e5092580654605b955540eda9eb64a', '7c6abc05ee8686b767f652506fbe6a46',
                    'd1663afb913b45218eea2c30ff3129bf', 'e9f35a29bcb34f56904c53600773a2cd',
                    'ee36de950ee047918c4ffd0318e0c493', 'ac8ff94f07d94798b5eff6220549bfba',
                    '0a4d951b20f247c29f70695d43498b1b', '54189c32e4f4480ba4334a3a15cfa932',
                    '3574b3a4776040c1a67e051db4338328', 'de5b2fccf55f482b96d2c9848cb68b56',
                    '47bca8d76554426eae266d4edd1685a9', 'b1c91944d32e4553add5a2a95aebb5e7',
                    '86753a87ee844843b174c8776b7d4472', '863b7800647445b7bbc9ad57772d8a93',
                    '5545d620b1a34512aca1877acf3fb390', '46b6abe971f647ac996dfb6a3a2868d2',
                    '4c8463614ee340039b2f94d0d503cd1e', '15986c242b56452cbf2b3495602e2237',
                    'f8d6f459f46b4974b0a0f1ae48395466', '90556b40221d2fd113ebbe500ddf86b2',
                    'd58a54867c274ceaa7548c4653b9e014', 'fd53e11268d04fc7b4141b12473c9eea',
                    '52efc8113d6140edbb6011c24bf387f1', '0d4847c10251421e8a685600e9a79294',
                    'd721c60cc64c404f86b4e5d1fd91984f', '9308975b318f4da095ae143eb7db272b',
                    'a16fed7c736348e798a92fe57cb5417c', '236fbf9615214149ae2112fb429b0f29',
                    'c14e80f4022c4e7e950a6109a0253f1b', '4712df6e311444b4ac69c0462ac6dcd1',
                    'c447b5e311144ca4875b6f169d26fcd9', '2332658049144c1faff3022dac1990ef',
                    'd09cd208ce624b65838c522a5ff7a9a0', '0606ae7e9adc4229ad04f628f07341f3',
                    '68aac29997364a9b85082c63ea867719', 'deb4ac2d37674544abea8b53d3a57355',
                    'c26684b80d034fea878ec4f9b9f926ab', '3e3c906ee3024793a6031f94008affcc',
                    '6c1ab883a2c246fa97f4a24fff751843', '053556fd084145ca933d5c9fb2267285',
                    'd6cb82d0e80448ee8309f2b95744758c', 'adff37ba652d402483de238253722ddd',
                    'e241a112c2e241ceacfefa31d334ff2b', '8863b1b5c02440598466bf6f7069d519',
                    '0f2ce0685bd940349e526320638d1055', '44c069c7ac424130a945896b7d87bbb5',
                    '9a113742f3f74b0ba83f2feb09edd392', '04310a5575964fff96719c42abd6fce7',
                    '255e4d0acf3f40239389a051f4f1f573', 'f88fd2ae4ff9418e8a6fead9447b3dbe',
                    'a5d62dbe74b84a88a59caad550926224', 'e535e578fbb04afc81c9b19a7b970741',
                    '760e76cf598a4e9087c7f71b1b95f4e1', '2f302f662a814d219d8a0360aef381ed',
                    'c904ee97de4f4c01a608549f8306311d', '4fc90a41639041b8b765092e84e4a67d',
                    '5c21caaf0aba40b2baee6e4c34eb4985', '07f0e52759334fb38365636e89b87e33',
                    'f71c5dc6a67842b0966d7099ae2b02af', '54dbcfb578e8413b9d26710f0e65e2ec',
                    '9ee7e2fa703c49eeab5e7bf3d5888eb7', 'a372da6006124691aab15000ed52128e',
                    'cdcad0cf58634db6b82966cc54ae597a', 'a5e11ac2297c4d2493bde9a5e5f1da58',
                    '7cfe1370516e4bfebffe9a7c1e5e0847', 'bebc795e21c74125a22010e0d4e3e05e',
                    '847be0dc197346d4975f7e3b91f8dfa2', 'a803c7c618284352b4a1c9b3549ae961',
                    'ff5ed28d2200459985a47160afc1feb9', 'f96ba48dc6df45869709eb76ac45b214',
                    '7166e9379e3843538333e66aed3ac1e0', '7082aada3c5041deb8cc72cb1ff926af',
                    'cdafc3c37a0b495ba01d0ebc31dd510a', '24ab871293e042b5a939ca8fd7493903',
                    'ba8253e8c9494772a19fed2d982787d3', '7e62384c0cb94f25a3002b5c5218ce6d',
                    '816028e3f87045b3962ab2a0d9173d97', 'b5d1d81231204eeb9f97f94855442380',
                    '4d7a1a3634c1429bb45ca2ca01a0aa90', '023f921e9b3649559a12db6ed1f65694',
                    '639b8f578f5b4cff82733363f9ab147d', '8d905329543b44469a5d27323c1ea284',
                    '95840fd2423b4b61922702c5b99dc104', 'a66772466ea34c229bf5daa8e7fed7a0',
                    '54433cdb834a4923987ca4acfa5ac976', '149673cbde374236afbe78a984da464f',
                    'a1cdd5e81449452a8a0d8e304822cb6d', '7c9f7b21de314bf3a711aeeeea599224',
                    '5d32a507033140678e1ebc7d2eded0a6', 'd25f7376b61142ffb0d2f281a05d6ff2',
                    '5b0bbc88cf6845cd8f6a633863e4ee87', '3ba3ea0ea6414227a89138d622d21c72',
                    '1ddee480c2214de19b8b269d2ce143f3', '2139a1c58d424ddb865f7e31507e13b0',
                    'a9df2600c57049d3b43299e9eb517df4', '19da2af3195b4d66a598ad0f1708021a',
                    '67cda9c6091d433295dc4ec78ba39b1d', 'f46598e65d744de4ad9eb4aec9d4f127',
                    'f718dba7e1c54864be3179feab3e19af', '9337f33f334a4b58acab452e2538847e',
                    '02512ddd0ac24ccc99826c6687e34f22', '3ad183852ba54488a6148f974909cd7b',
                    '9e1d9806a4734d41817e4ac44862a826', '1d45a2be8180c84ee352afaf280451a3',
                    'adc71e1bd14a410da2f8c8be7206b98d', '424a1886828b4c3d8e1aff6922451804',
                    '6b23422cae5b45a5a04f0772047b1629', 'b507de85da24403a88d5e0ef082f4d3c',
                    'c6e668a893ae46d9b44e5637afbf05da', '59c63a087a044a139defa6491c5f337c',
                    '228ab28d686640a48dc66d7fee6ab4ff', '6e977734464943d28e6945a978c492a1',
                    '70f44f4056c04f1d9b3699fe2ebb8c2a', '394a160cda7c402eb411e0a310bfdc78',
                    '3a5e79603ca6464b98b3f2f5eb37873b', '4911595af9984da2bb4726fbc88bdea3',
                    '93e5ed2a9bcb440999ea7fdd10a75ff5', '8e619c69b863449e829ee531c91571c3',
                    '84ad2902151045629d3cfa510d0b4694', '8cb243d3ad51bfcffd87bca936be55c1',
                    '4dbf25a999784c519b132e7bdc3f5819', '42361d1886884a9bb30d66cf53e82c25',
                    '47462061dab841e9aeda004857981e90', '98bb72f2ff1f4539bc599c1835cc8cdc',
                    'd9998828bcb848f6a19c7ebb41d5ea69', 'f0a66c88f14b4056b960b09252f46103',
                    '9a5194b01a4e413fb13c8d84f89d4d87', '8c084088d9e24d45b40c16f5d2568f79',
                    '9a90a4aa62e6401ebdff0f0833ca466d', '2e980cec2975cba8c9aa3907773b4df7',
                    'c7a3598c87e744738052354987cdafa4', 'b9743ff3ba8c41b7a07ebb594ebf3c3e',
                    '3e5782ff89774ea5895bdd15fbe68efd', '88f44bdd89ff4e869eaf83face7a7a56',
                    '100b229e119f4e6eaa71fcf1087bb4bf', '06c068db78da449d8c611b2ccbdadd0e',
                    '51ba35bfe3694d58ab4969ee468340da', 'b747fb62ef224e13a6e1f19fc245d2de',
                    '07ea60e7a9044266bcc20f1493721b8b', 'e8505be0741248adba787191d4866007',
                    'c7729aa102b2481b9b424f7e0e5716eb', '59f1311a3db443c582fdb393f00d37a7',
                    'c257e87606284603afab3cd8ee8cdf98', '8fc8a5a248bd44bebc4fc4a402fdfe46',
                    'edf5d017c07a4224b4bb9e61fcafc2b9', '83d68b4f952c41f3b4db1a1f82bcd4c2',
                    '30052c8ac89ac5007a8ec1ac82bf02ef', '92b4deb48c334c88a94ccec4f97cd5f5',
                    'fc7890054671442080d8026532cb9361', 'bd4e96826b8b46a093d80a5f19b7719d',
                    '3b6f84c73627409a9a225043096f6d94', '9f370e95f00e4145be7a9ba22e222930',
                    '802b4c485bcd4712b43e4faf5970e395', 'd66910ade35546cd95fe9e7662d3b4f1']
        hit = ['65c3131bc18c6adf6216347ddb009cd1', '77ce862774e44f25a3a9a12a4be1248c',
               '0575bd4da6074db7b8e12d3d191bed48', '2090b5bf145c4fcd836f8af3e56e1d5d',
               'ca63f03773e2faade9286aaa03b3930c', 'ce31c891052246e5b42577c04673a989',
               '76f890a01d8a4d378c8f1fcbea750dc4', '6f1ac950727949a99b98398be60de670',
               '85e45862f56c4616b0f75818dde1959c', '0ef317c0770442c98b9f85764ac973c8',
               '13b4ca10b2604cc6b2e82c4559167551', 'cd98358048654206b69c1de8021a9188',
               '644b64ef403a4799a0523ae548070eb1', '32dfaba71c764d7e87f811dd27510e10',
               '341a144890ff468f90a60c8dd480858e', '067d349f8f86402e8131b9ed97762318',
               'a679922441db4229931cace4cd45ec72', '41d20d4ce45442c4b10dffc46374f9f6',
               'f169df72e6f44b48b68e51fb5eb028d6', 'e7c396d311d249548f86e954b982c336',
               '46df4e8ebc584c7f94a2118dbeac62fc', '848c62ee8de04e0e94d53c42d5d1afe5',
               'bd0cdac97a0d44f5862cf458cd5e46e3', '5a4d3286b1ed4313a3bf6286fbd30459',
               'e9156acfc9f749259a52e3a3f8a17dba', '8f6fcaeb42344d91993d0440a42f51a6',
               'e6c4dd18bb6c427ba63686016d5dd5a4', '67fdeb0548f34d6f93a85fd82856bcac',
               'b363c18e85d741bcb65a5a397550ec35', '442a7534ab004ec1bff781c7c0a2c7fe',
               'e58ea64124af494894a6dffaf1522cc8', '25541e5547c997826df86705e0b6b912',
               'a94efb31d0f34a919d811a3ef2699b02', '89c3f5eabcb045e48d39a3e5dae8503e',
               'c3ab7eece8d84174a01c324d97b3600a', '99fd766205484c2085ee6e6ab3fbe4a0',
               '6cb5834fe2ac42a0ae0d040d20bcd0d8', 'e8fed58561f54e0fbc4fdbcb0fd371e5',
               '6f9d68dbb1214c368bb196a188ee9f29', '3ce27bcbfb434a50ac1545c5b4f897c9',
               '8fc594bedf7549e38e153d3beda5aa74', '8156a6cadd834ce9aa891625a7062494',
               'e5817e4a48414d5abfd96f155ab94b80', '47f7763b24284a3c9ee893b842115a20',
               '3a08234ab60f44c39d1ce0986450e2f4', '9aecaabaf3828549b5c316e991d4c4a0',
               'c2828111f3984b269c2527983ca50b43', 'db0ff4c58980441cbb92fdcf95472a6e',
               '7276b85677884e11a778a91f70d8f8a7', 'afe40dfa7b12483fbdfd123c7ccc29d0',
               'de35727e6a0d4ee9853cdaa85bf672f0', 'a068aa28731042b0964c79f21cae144b',
               '06b5701d7330447192a675f9cc2ba824', '6d9bf0b7f777420dabd376ba209ed21e',
               'd20b5a94a524449585b7007969eb4103', 'cd5d242af0cf45579b6c56913d03dad5',
               '0ac023f879a643e7839d4f6f145e92f9', '793796672e754cc3aaf6a67e9aec69c5',
               '5fd232f0919d43b9a9ba567ceec40297', '8769746535424aab910fbb597d14013e',
               'acbaf3751aff4e039059132844700258', 'c25cde0e774e4bd398a827648207a43f',
               '97a21a96bf4698e26ffa5867c535f5a2', '56e9c200ca7e4e81be9859ba68264545',
               '65b0ffe7c92341459740a978a5bad265', '68f75394be8c44b79352303f67b8d022',
               'bab32de4d5704b8c9afbfadee6213f3a', 'e115d937e7d340309a214e2e3934afd7',
               '7ec9bf442bf94f3298e4c7e66ba6e301', '3469790de6d1443a8e7042e737101a83',
               'd615b826fa4a479ea495180a1c9cef5e', 'a54c2dae46964a2688642c2edf4c5647',
               '9a423d1129674143ba4dcca5af926dc2', '6cf1452625df444898f383c5fdb88893',
               '9d4cd2a19ce34da4a71dadbf8652fed9', '6b2ff9049bbb4f3c987ba13e91898777',
               '00221888fc4e493e8179173aa0f27c9d', '9a63e5084ea642c2a8406c9199ad9d96',
               '918a8fd88d9f406bba8e3ee9ee8b6ca8', 'd5934208d31f42939e5893969728e1d9',
               '35c5a3500d41499eb67961f2745b9e17', '2e4b191246a74e84be6ffeb8f211354b',
               'c0b4e08a76b14a62931e0a1057c2c912', '8575ef921fe04e03ab4314096a7d9049',
               '58e0bc1fe15144f19d3b7b6ffbbb94e1', '7b9c978a2a1a46fd9e46aff5d697b7c7',
               '26ea3d2f613141fa8c71b021b8d6194d', '8247140e34f24624ac0b3716fb76d86c',
               'c607cc61c51f468cb2df4dbab6c22b60', '245171d2fa934e169544f8ba63638adb',
               '86ae79480be54c969b4ebbb45bfa9893', '0cb83af311f84769bea7d29ab6ae840d',
               'b4ac19ebcd3a46a1bd4509104944263d', '70b85e0d4c8e4299a09eeff1c6a989a5',
               '1c67f4c5f9964f63895aa754464f0eaf', '95fa41abdd4c7a42523596483c329790',
               'b221b01bd39144bcb353e26ebb660fe0', 'e658fb078d13462ca8aaf35ed578056d',
               '5c020fd24ef64f2784797d6600c1634d', '17d7a5173f424a69a1bab593f21a2651',
               '3accfef271284cbca60c193305b46b47', 'fe29cc4a5b2a4a38911098356af4f86b',
               '2e9777f8d4204892a82ffa2fd5233522', 'a4e645e5cdff4826851fdedcae0eb941',
               '86cd82b83666487498315fe56f4c5547', '2f9ad77301504eb8a3b006dddcfcda41',
               '98ef9500cc944a3486b1acf59b3f032f', '68c8256e7ff34aa2928835ed9dd7228c',
               'e233477998af4450ac8db3a12713f4d3', '6f95d7e72da042e4860cf36b8a6822ef',
               'b8500ff75fc8412d9521c3c36b2c7d98', '01f3a237a5fc4cdc8bade24d4244eca4',
               'e833ebdfb51c429fa073c47694eed869', 'e845bbbac5e44d99afeebe2e34befcad',
               '5513f3f294f143669145857607682220', 'a1e8127bf82e4445961e9247275133d2',
               '4de227c960624539bf82e6ba3591b75d', '84a1b795b3f24144999bd2035da615d9',
               'f274ff74e75947dda4ed44d0fae97bf0', '552cc43f72dc65a75a649ac302ccab3c',
               '928a5796fbf847c185b9c923f32cf324', '0b053ba909ff4adc9b1c191b4c2c3ee0',
               '27a4466caf9b43698805c08816e3631d', 'd261110c7253498fa8ff0e0eaf83bb62',
               '0733f4ee2acace81f1d318fe8912461f', '2075e3433e494f75bb0876e0e929bb77',
               'ee2e2445b4c94948a7599c74c08199ed', '96ffdbc4d7154b878f530e2527b6c8a5',
               'f4aeb0c04e124a01b2e1bc1e9b923f96', 'b34284e72b6241d58d38e83af83bd575',
               '4561eb0a866c61a5363f114350a1081a', '3d03fc689c1e4d3a82508d132810e047',
               'da9c171dfd8383be7aa395108728e4bd', '91048e21be4c42dcbe98a3702402e2e2',
               '7469d3445d0d4ae4b9d5d90fb72c4c8f', 'cd3134ee42604bbc8def1c122dd10342',
               'f9315c7e1d6443cb9ac69cbb2ad66a13', 'af1667d375ae4233b7c16e4ec92ef0d0',
               '90acf7cf91214fe1be01b3c94d1ebb05', 'd92ff8a513b415c71671476d5dfb3400',
               '6b215cac509943aba2b8d563cd1d398d', '020a673c3ee24cbf9f0ac95297687c38',
               '1b5209c54a9b4f77ac7c3fbc6037f945', '83f27665823947e29eef720f4bbe12bb',
               '08650f8797744baeb2731a3e73f377f1', '585d3bcd30f14499b1f1934d99373e70',
               '5087f8bfc6194f74913f74806a14ebf6', 'd8ae4c48c4f547529692b18e71dfb2f8',
               'd0df05e6128748fcaa50979ba28a75d8', '169074eed6b649328e11016e74a0ee90',
               '0d09f23047a54a4991bf827a9c1ca62b', '2c3b659a3d024480b1bcdc10cac87325',
               'ba42272340114ddfbaaf4cce90ff473c', '2a3b2e7250394af9b24fac0712de35eb',
               '2d39f0111891453c88dac2462ae55528', '4978938606444da5afc34be1ecf05d90',
               '883c510d99f74f5f8c7846e3eff69246', 'e960bd8173fa48ad9b311f6a5fa5d49e',
               'ef197098f0a945caa8b825ca7770318a', '0bda99ad45f9460b9258202956bec543',
               'd8385fd6401c416dabe4f88d0826eb4c', '5d89319a7385488cba2d98ce677e3f0d',
               '60e023e8162942b8a7a5fe094836c509', 'ca9f435ec70b4eb9baa6b0ee10205506',
               '1db65f2a69b14bfb884b3bafc931fe1d', '1e5824535a494f0e8636558e839575d4',
               'ea2b0f6c4ca5446c99a775021f590633', '440ab978a52c49199d75d1c14c59fa29',
               '8ad2562551574585be348d27d54f492c', 'bf06c96ce2994376a0e0f565a1daeff6',
               '461c583bf01d4e1c8e336b0c1241300d', '2528837171ae46578bb977de013deac7',
               '4e605ec8ea624d479b91b6c367662c82', '7449b88b32d649f7a8ba93fd6a257048',
               '993cbc2d0e64433fa35bae55f546b4a2', '333dda4c214742dca725118c118b524a',
               '13e89e1a1a4248cb977c1cce9c26c7b6', 'cf8462b4c073460595c8b01ff890a383',
               'b77f578b91f04c6cacdd1e9e2da36e80', '197dd5c56cb045fface830b2074f0e41',
               '32031b7f70cb500756adc77028651230', '6d67eb2df6d441cfb55ececf04bb5c10',
               '4db15a126ec243b795d539b12a03f34b', '4aa45fe3934d4d608d870fe02079f69e',
               'e2c3e88a48654ae0b7ec7b21218ddae3', 'f0a94c2eec004277a77636ef2657f123',
               '9cf52b4b348b442a93a701d39018975f', '68bbfaf2b459f6b772524c61e13b0e1c',
               '423d203231c6428fa9544f241cc24369', '773642cfaa3e4941b0d320b0cd169dcf',
               '9afc451f11454a14822d7861511a72ad', 'e96651bf9d5a4e6f93456f5fa60d0ccd',
               '4e661f79f1c24c24ae73b4fba49f2f6d', 'ddec59c2d78b4e4896ced644a015d3e2',
               'c84e1a49ac004ad5933fa106eb8a3b0d', '2f7cdc0ab49742b6892d6ce23afc36dc',
               '2d972ab679a04abbbb9481a89dfb1719', '6d32245bace14405b3697b5bb2e75a15',
               '16692177ca834dec8f9f8f9839241c11', 'fb08ba8c50a04621ad0854cf2963a772',
               '21805b10ebdd4c1e845169b89c93a993', '954832ecddcf4e839c2ef7dde0c00c7e',
               '8eb45f25f72b469e96eba1bbdf29c786', '9467c00d1b1a4ee092d3a552a4a195cb',
               '0e5e9a72fe6b49afa67d43564d7aabad', '8b6a7a5f84e1442aa370ab5979148cb8',
               '7495bc4c2dcb44a3a473bdeb4ee63e57', '37c152f12ed045e7850ff0ee568da9cf',
               '1c8647d8868b4812a2f4e52b5ae6968a', '819bb5de5f9c469bb910be0b571ab074',
               '1d64d3b5b42a4d06b82471f613927640', 'd1f213d40b154753928e126391d87af3',
               '6298aee01d5e4a6b87e48eb951342323', 'e36284edbab34de69da1808a5163af5d',
               '1bce09304d6dc5cfce350d30ff03bda9', '880ef17e949e4b3a8915ce0a3f047676',
               'c66e5fe676e84cfdb2dddb2fa39d2901', 'a6ec94f1640340dfa22820e11f0d399f',
               '8d145e6fd5f14dfc8edc41d6d9380228', 'b9570635ba114c3ea971a03412c99d74',
               '273085c586cc474f910f7366b1eadf30', 'bbb6355f9af040158a73863bf1564dd5',
               'eea821c22883465981c215120d28f9c9', '33f4124d09e64c4da1e75776c97ae99b',
               '9ddd678eae584b0b984e2401ca73c11d', '23eec5622e51ca68eb80859250f27160',
               '586c795ed5534e35b64e890a9d79e30b', '59f1a0a6915c4e09a341258b56120f0d',
               '42d758a566a84308998550c44a1540c2', 'fb271939a7e34d73b211ae7e44fb3afd',
               '545883cfc55f455e9fc93436dfaad93c', '435b4b56545144c6a07566040c147fd2',
               'ca2207b27e1d4b3288c41c07a754a385', '6921a2c8d3fe4ea49e284d9146cf4d32',
               '56b0273a72c145cfa491362fff6daa81', '5f04a6cc3eda4c968eef66099e75cc2b',
               'f17235afac64453898751a8a5496baa9', 'fb771ea81c7541a5a1cd493ecad1fd25',
               '93b6394f98d44fc89b71c12770ab7fcd', '3ae76082fb4149e5a1cd0cea99e48a5b',
               'fb6d3d1da5ca4ab5b24b81b55841d44d', '5a30614f887e4ee98231af51100610b8',
               '081b6731f5a140be889341516e2532f1', '988221d8d44a4bdba4113efd527b46d0',
               '24d5d58c312e43caa15e8b1ce92d4a42', '68189b2579e242259711677b4a1e88d5',
               '28fd26ae0ef04ca98f3ea2a703da1e40', '60011e2c917643f897c4525d214a36de',
               '64b300d696d941b29796185a41d6872d', '1dd04b9008144014925a65ab59b15bfa',
               '5dafab0856184e08a87db98b0117b768', 'd1ec443d450c44f9ab8ae8468a0d5f76',
               'a0999f9a9f2a44ff83b1bf97f5931e3c', '43467157198b4d2da53762da62451f32',
               'd32702e50ef74beaa5834ec344dea2f2', '2d3558aa6c934691863b4ce13f316874',
               '76dc61203c144b2bbea5317fc3ec538d', '31dbe1b9f40540c3950a7ac7e3954fcf',
               '1fa2b11967d148ca98a3a6e91100a1ce', '15f593cf381e461cbb1132fc4caa1631',
               '17dbc599091a436bb140dc71eeb7edda', '0fe672d509b14d8da2b4e6f2f5aad777',
               '07f32fd34cfe48989669aa5cb67a8e4a', 'f73befd6b4d64e8eab7fabf5602c4a9a',
               '13d81e2a0980435886f07771cbacbcd8', '871355c5f0cf4d4b9cc401a952889c65',
               '884e3267afc24b3593998846764d5a15', 'd7b2bb0fcf34475c9edf9fbc5aa82186',
               '2deab6f327a24485a4f5a5a46bd5dddc', 'a69adac020d842b39a1eca0bed3706fc',
               'ece2eea102cf4f34bc511790a891e1f7', '1f8c1fa8632043f18f3f62ace7868642',
               'b91b4d96389247f08391275cea086007', '55c499e37a814722ad14def0160f8ac5',
               'a358f15e1c92453fb000e0341237d141', 'fcdeaa88e95d42eaa9ba97c469a27737',
               '83ab811cbf864e8ab273b21e1bbbf59d', '85f25845367d423c954b7571e1b5e27d',
               '99a3aa5a21664603a4df652087bdd011', 'ba0ea841365d4dbb9c20636d6ca2b04e',
               '96d7bac8e9e6414294dcf5837d0ce836', '9d9aa3770fa74e91bec66dc18dab08bd',
               '13d63cec74354d4e8ab307412e49752d', '843a88975f0dd1944c5e650808ff9be6',
               'b957b332055f46ddb58c98cb24598e97', 'c3ea634faa504a5cbcdbc19cf266acdf',
               '17ab1255acd040d0bf97751dfc24af7b', 'a4a2f24fb59e4adf8ee7988c25bb5163',
               '6e879e6b8a434a028521d1a7f94b8d42', 'd56599d1b3694252bd4e0bfd15a6563f',
               '1ef8c0766def40a882bd74f62b2b2aab', '70771e4aab254697b6bf2379a4c2e6dd',
               '3a2680e07fd148c787e28f4217c70dfb', '258ce16d91af477490a4201bed92b7b8',
               '40ed3c8d328847b5b897e526fc4241bd', '329628f603174e8fb6290b68e31c484d',
               '5038ac59873d455c8d6bc15e8a098991', 'db993c15201845f7b4a8b59a00a73c99',
               'ad966819968f48399ee40b2fa3b9ebf9', '6d631cfd1c114d23b823840a51aed694',
               '763a7576b5454015ad9987e99f84b770', '8c8c8c1ac9134dbfb6936deb81ec2b71',
               '9bc8053e36e24e43bdc441d068f13254', 'cc87783c33204160b7a610f8653f5387',
               '8c22eb0faef7465387ba4dc37c0741bc', 'b4134ab940bb4000a75f2669db59e549',
               '99027bf56e264835accfd0eacaee3230', 'be19e310b5f5459085afa19eeb57f647',
               '47192314966c4035b0d2bb060696d9d0', '471efaef038f4517b3ca79691ef1f735',
               '2af4644b31b548c5a7d1bd973309d0d8', '4caff1fe202046e892d50e536b2ce781',
               '205c779999764ed6ae8341a0d1ac23e4', '8808e99743e742d9a8a46da6253d82ea',
               '90746ceef75d461abf93090ca14391d6', 'c507c2bb3b404a89ab970d968457919b',
               'a35d3e134a47478ea7b8997cf623cb07', 'eb2edac77d5a4217bea53c660c95161b',
               '38ee2d59042f40e2b9c46e947471642d', '8f5b6f4c10794e0fab3426e2295c7f9e',
               '362629bac23d4029a1b95090ccf0535f', '242cf270df634e0b91d6f6b26dcf52ce',
               'c109aa7f78ab423f8c44ffeca3c33824', 'a9bf6206b11948b28004953a378b1d8f',
               '078abd28bf994b85a3401c2b05966423', 'e507dce86d82488fb89a78994ea0af99',
               '3e6b2879c99d4cb6833fb16a894d1f06', '6f922fed1b8f4c7892656ad3540520e8',
               '11381048c5b142fe8a80d747ae25a59f', '240cf2801eeb4360a38c987b6c88b905',
               'a20386aa053b4fbaae12a32312235e95', 'fedc38e7f6644919b546744508981a86',
               '2182ebc74b584006a3bf101b64731333', 'a6a53b2e71da4cd0924b05d3ea564278',
               '8ff82ba803604350896c734fc48cc78b', '2a9bface91c44329b59c8db1ab918993',
               '092bcb14dba1487794c1850e4bf3f01c', 'acbbb500d7054b488f7f02fa8c8aeaf5',
               '62f2533f5fe547c898b5bcededb3c8dd', '7e843edbcf584e229d24ff66e897207d',
               'c9bee81f0cf249f19f9543f9badc9a64', '3457a2b57d0790b86a4f492dc07aa500',
               '9f00785d5c0c466fad5bdeb59c86d0ea', 'a17763a713fc4ed2be0103089a6ac351',
               '50ff15c8dc174fedaaaf13f5fe0ddb10', 'f38783ffade94a2aa5f55ad29402f229',
               'cf86adba547d4be9b14a7af81cb20a7f', 'd915b4388a914ece980bceeccc1f9ae2',
               '9dc2155e486d48c983311c625b38c2bf', 'c73a5798033e4a43a5a4e23348c2c8dd',
               'bf6169def274409698b3d90dca8f9e84', '10f1dfb637fc4e58bec7a2508aabd6a3',
               '92834018ba444fecbd31578d698f0165', 'f5196b1fb6cf433984dce2bc59ce490e',
               'e6cfee4469ab48d38e73e0d0659db7b6', '22f7c8ba3e47afb6de14eb7bda5d3d1f',
               'c91515aa87044b03985e8157dbdcdb48', 'ff0b157fc35d4e04ad740b241290c2f0',
               '6ab31ebfbffc4473949c19eb99a4895b', 'b4efae47fb9d4095a60f186bb71b09ff',
               '468b553c3bb8403a90f9fc2dbdf8a25a', 'd7bb3974ac3d4f109aeac56508e16527',
               '400675ec87474c6ab8fc8013c6650f09', 'f7b7d08f3140439f8e964974b6ab6052',
               '6a852e7d14494029a55f2b3bcb36bae9', 'c770edcc26c24a988fb02bc79e3da69b',
               'b2ae425cb9dd43c9b3b8d66b502e6cc1', 'aff4ab4a960549e29e989f995cc92a6d',
               'a7c1bc592e144f51898ec51a4936e92b', '2be96e9bbbd84c9d8e787161c6284bea',
               '4edcdb859ab646648d6573e041130886', '64f049ff0a794cbb8b825748bf29b8e3',
               '49b42aac21d949a3b1a98db9e5cdf836', 'dd9cd2bbb83c458287f614f1da8881ec',
               'c339d9aa840ea6c992f96b5653205380', 'ea0753d7dfa34fffb75a5d05f124b4ba',
               'd1843087fa6b4fabaa84b84e89c1ebb7', '709b70168c1e485ba38e934b240d2416',
               '2cbe8d79b2f1419184d4f66e56a8d148', '8018c0d3b61347a893046334d7737154',
               'fbefd7a9142540ff87c388b58f6dc823', '6b0eeab99e564188892746753a88f72b',
               'f23ce7b9482344199a8e72dbc5532385', 'e63b749062fe696322fce1adbcd40c18',
               '659ce51cf36e4b1a867c4d8cfa2ac017', '30b35e1f3f954b6481d9cb985a668738',
               'e77e40b0703a45eebc81afc0ccfc06e6', '73a46c439d8e4ca4b9dbc885a426c96a',
               'd9bfa8026a984ccbadc365a350924d1d', '95c492dd3b404017828325f541ca937c',
               '23968f71a25e7c8a9059aad9fca9ad01', '35fc9846f62e453286501232e0d18b7a',
               '8457916d877345f590237afced0f4c23', 'd35ac9af86944cc3aa4e46e5813ef098',
               'ff3a827ad04c4e4db26630631b685bcf', '360c5f78f33f4e2e922b1d13929998e6',
               '1b1d784d6cfc4be4ad45cb40c0b54e8a', '742cacf61ca04e298a1e6b3561a6d807',
               'd966417eb71f4f45a178455deae5e7a7', '3213b33f8e4648eda1041f048b089039',
               '06dc5d24e7e7479eaba9c9166430f6b3', '33a7d232c748419cb2caaaeb74394be8',
               'a0b90a4e887344ce8c4f61690d63615e', '190ee2996bab4b56a91c26f7c88516fe',
               '455be34c952d4126b72f7eefe2a28fe7', 'd2f687b340324bce9d1b8d14fb780386',
               '070c55201eb44d1ebd84aca5223901c4', '261a6dc4b24c484aa5670277de835837',
               'deab2152ffe14ae1b6199f16999f59e9', '2016a60fca5b48928c5e5e48696d66f0',
               '841521d5414540e0b69a396a1b74cba0', '135fdf9abb6e46b4a7fb45bb3b69a4c9',
               'd5ed308c51ed45018af2db43c516704d', 'dabfb16092e948f3a09bec0d4cdcd9f9',
               '0463c6268cb449c9a95676a0dea6e68f', '8649bd544e9540ce9688845ccd6036b5',
               'e9ba1984603b4f679103c5d6c096498c', '6ac23d101a4f41e6b845207f441b11db',
               'be8b165032b86dd165a2735ff7fdb15a', 'a6ebf1fa987a4a1ca5047dbf5954f6d1',
               '81c3be48baae4ff3b345cb4903d62325', 'c248e631ad1b4f49a2e3310180ea25bc',
               '54ba52c4381b434f95996b3cd54f9c16', 'a3bfec04e73b4f39aaa4b6fd51495175',
               'a6a00cb2932a4bf4a72fe3b94e0530d6', '3191475038434393988e4170f75ac18e',
               '0a2569ce479f4d8e83eff0610f4fc0d5', 'dfe3562a26114102916007336658eff7',
               '90ebfe02a2c7479cb114a6a16ce27d82', '858599e90bbc6f14a86170edec3d4ca6',
               'a2a97470cbb1497da9cadb4f6560b63c', '04925a15605d4e2b9226c7a7aa46452e',
               '39594ff5e15e4ed38d3e48b98ccb7e1b', 'f3d175e8bc0047fdac94729f147f99ee',
               'cfe941b40e08466b8ffc434898071951', 'e4eec854029f40d49c60b5ca7f14106b',
               '83bd6e2e177640aa9f366b44058e1509', '6620288abf904790a1a6a604ff27da7f',
               '35dc5d771d43417ba82778fed8716e7f', '87860e40b87446fb9955f041db7eadca',
               '4be20a26da0f42b0ad1c7def55c064d8', 'afd0c3ada0954a7b8597628ca511a239',
               '68e99ae2362b480a9fcad1cac112585f', '74181f81563d45ff86aaf4f5dc9adfb1',
               '12c80c647fc248f39f927a763b62e138', '82151834389142ca9865742aa3d59e3e',
               '9aef1cd0721249d8a33c873ae8140e82', 'a23fbd38c8a142698935731b2b0ffec6',
               '4bed96fcc5554a92b0d8a7077bfa34bf', 'd080f3fda9e14532a9c36f668b7f8dfb',
               '360eada8a5bf436ebe0fe4843e7f01b8', '80a4eaa3dac840ec899910115342f464',
               '27b1408fcb474bbabbc8f0d41546dd81', 'f6b7dd749a6c449db9a23a2e2794db87',
               '740c96034cf04ff5ac38c3fdbea151aa', 'edcb03a81a7749dfbe76b71deb5d76b1',
               'ca9171424e4bd5e016f7957aa166d765', '7be953763c684131b196a46d9e6672a0',
               'd509cad79ef34ce9858d46695aa9d827', 'f30e0498ea8c4d02bfd23cb35affd25f',
               '5a36a4eb211c468d96a46935715f8f38', '2d9ed99216e64b1188be2d9b384b89e3',
               'e10a569108cf45c3b5807c09e134200d', '5014fb29a3eb45ac91d7e7e6b066af32',
               '7b134cc5f5454b40909e869e95e6ecff', 'f2109e8c19094ee2afdb53dcd06c7fbf',
               '8bff798c032b46d8af4f1ce41b787c23', '0029785a02e3473bbb22250eedbc3ce1',
               '9f327b91f5374eae85aeebf7760092a3', '37264abc4505437da03808d49a753cd9',
               '38a3b58efd0e47fe9fa591fa561f8db5', '38b9e686f4a446388d6592a6855a1274',
               '6d1efc618dbf4bae8fc3cbfd793f1039', '536bc383d7634b2c8bea78145b8d42b3',
               'b5d53efd85bf465b94df17bd1bfa8a01', '5c670ec5e6d44d51aecc0d1b4f8b4501',
               'c2d986456f784386a6d493b38262f061', '072c380f7749443fb0c4691de81f8d36',
               '84c402f89f2c45249cd14a958f94191c', '75e5aa0603db451ba5f9584f31ed8fa5',
               '99b98822631a4bfea850e451dce897fd', 'b97d869267734191a4d133b0866176df',
               'b43f31cd128d40a19ded3202a122669d', 'eac73a450da24d8c8a7ca151409113c8',
               '499fe6aedbeb4646808fd2ac6d88149c', '56ba2e26cb494bb5b06645e2fac3dcd3',
               'b44bd108caea40f884e7945087fbeecf', '0059b6cb049d4bf29753e9d0bee27136',
               '35ab8259d7964e3da2e0fda8fa72e2df', 'ae2cbca7975e4df7b9d2c515362398f0',
               '81508bb7ae7e4997b78cb9e173835e4e', 'e913d03b266e4b4f81dd562d0cbedbc1',
               '5472eca527bf473281811c6d8d6866a5', '73ed24a77d1740c6839168547505ce76',
               'c46e4b01df80c537a1fd9a919c1920e3', 'c6ac725f1a16493fb2d75e3871fddf1e',
               'ff1dfcef45f9481a83749d742c7c8efa', '388010c43a9944dc9fd8d4c1e3c4dbbc',
               'c26b856d71f94ac682bc7549cba3b665', '993782fd2d0f486c9dffa8d33f5ea13f',
               '5ea21e4255fb48c081b7848704f6617e', 'bb2114f3d96e41f096d11d87677a5919',
               'e8fb2f8876c44376b9402ab4e79a7053', '1a59b1d0cae542d397671ae506dfdc75',
               '9eccd2515bad466a9d22c6c51bab13b9', '90439c69e5584db1a3c2adbd0af18bc9',
               '9c23423210744e6dbd4ca71620676052', '0883a7b7ab954ae795a5e7e0fd19ce5a',
               '0344ce44530742079b7249a84119d9a1', '2cdda083a95d41cfb4c4f3c45230b487',
               '6621be9c1fd747efb8fce4c02d3c5a20', '449a76f01b8943b4b1542c0bdba8a389',
               '4b130c3b716444d294df93eec878a17c', 'f7083942f3d44d1a96a9fd18ff8aa6f4',
               '89756e792cd44250a0ddd7f4c8d86163', '8569780c79904d988dbbd6769366b806',
               '0c4278acdf914f6db748d87c2db3a5fa', '862ec1241f9f4f7bbd10373087a4bc3c',
               '57d749e9df914ca3829e6f13f47c368a', '2468c4835ca64d12bcb1ce2939cd6cf0',
               'c0c300cd22524e39bc30ddd02b45f2d9', '978245d56d994e3583f02b75242bd7f9',
               'a12964d406fe4990b1dbe41ed1c7ed1f', '284eb9969da24852af336354c9cdbaa7',
               '48800cc6e8b24145a9c2c123387c8b09', 'cef6415e7f5142409efe20f223f809b6',
               '5891c099a5c148beaa67d77a4bb97ada', 'd72f758f22104cefa31c789c0b1b368d',
               'a3cac4568a484780b2fe7d7e6a1717bb', 'd041b3bc51424a2dbd2acb949b3aa39b',
               '309abb1c41be4fb9ab4cdd3237de64ca', '2409c3478be14fbaa845c2b187c94a61',
               '5d4d2a7a10704dd4920f971f2e76cc13', '6e96ee77abac45ccabd65ef74f605e46',
               'ccfba972326c4cd38b278aaeba95c226', '7c076abe2fc3f28552f8fb56e168514e',
               '7fb9a9a985494764b0191aaa13071900', '391840b4342b4a178515381ba4600830',
               '7d67e0b414a340ea9156ed38cbc253dd', '7afab878c2664c57b5a8f9b28e8afde2',
               'af06de7694c24bdb9e48c853c1b649ba', '580a493d12cf4567b4de1a645a063e60',
               '39959cec-5b8a-47fa-ae2c-68ad6d9898f6', 'a7b9bd63d1f8485b92e6cd62e6e09ab9',
               '27e99509fba44ce1a636bc61fc1dc94c', '6443acea1d95e405670becbd4d0da453',
               '0fb0b59b24c24bd8a5ee8f45ebbc2ccc', 'efbd8e4f4d604d15b96d7a116b72423e',
               '810b2ce2371146c8aaae58760bfff117', '0967cfb5d28344719daa2258208913ab',
               '1daf1526c5234a66a366c67d38d86447', '39fa6a8a56024b999d3c7099d3175598',
               '5d1161059b79419db1ea8deb1424f3aa', '7833f4d1b15545febf11304eb42498ba',
               '9b5a61f457884ca9a044330d75d3fe79', '596648db814b4c808359d5cb814ca3b3',
               '4be7d79210db47c482d4d7e0ba78a144', '9b4a90e95b2a4dd29ba626221bc09273',
               '89f88f34f7874697a093c20753ad391f', 'af8d9f211656464c8876773e6923b066',
               '8e29acf9e1904f4c90481f6eec6bedcb', '028023cf94d14aa988303ff5ac51077d',
               '4af07882b1ff410ab3be01c49d21ecba', 'e9f35a29bcb34f56904c53600773a2cd',
               '9c333d22124246efb2ef9d6cb745b6ea', '7a348a7ff2684760b1492a1db7371516',
               '82e1f8c8f00d48c0b21b4160487955c6', '3115f8fd8090497f90453ea9711db76c',
               '5d2b77ee21f74a678d32419654e376dd', 'eee1923434864730b40e94b298117259',
               '0b6548a1df2e48dfafa4572ae36f94cf', '91600617b87140d4bbc98392bcef135e',
               'c482b7d130da466fb701d21d93bcc859', '4ecf98b89dc049bbb743406fbba41815',
               'd713c702b3cc43c1bb8898d6afe3eccc', '7c4db19cfe56461ba3d80bda554eaed0',
               '8f717475e3f74acfac450a0a94a20919', 'b005b6cbabe74a6c87d42e880fc4149a',
               'dfa9da88d0fd47c4a62320c646831aef', 'eb8364bc4eca4490972ecd174d50e161',
               'fddbadacb5b34d348bf96c7cffbacad7', '43cd058555fa4304a8d9d2f55f0cffad',
               '72322fe0a81f4c1b98aab3716d775cc7', '9c64439aec074974bd40315a8d548f69',
               'c8097cba9ebc43079b9923f8cc87c8b2', 'af0943624ab04868928b3956a08d9d3c',
               '54189c32e4f4480ba4334a3a15cfa932', '92841970dc7b4ea3aa20a58435938a9a',
               'a52a69c5b6954f6b89361218e518f635', '63df1509be3b48fc84e0deac2262d5b2',
               'ff4cd68bf00744ebaa13b31504b049d6', '683c2291804d419e97f1aefdf3030cc2',
               'dd46ab1156e040d8b5566e370643ca07', 'bab187f6ce89401f9144eb0a35252cdb',
               'f65e3ba0b64f497b8465e0826ae6d440', '69f44ec41d214ba9aebc410a1b6a6c54',
               '7684012573b84ef0947116579f1687cd', '1a9729020a944dfd901f9da7ca08b2a1',
               '54269fcefb044ca180211c9c9eed47dd', '8279c40098474893b3eb4db7215f379e',
               '763c805b8123409ba6d1593e257f0caf', 'e02a133781d146d893f399205044c311',
               '778b941d364d4eb1baffa87f6306104b', '134da2c40e8340dc816aa26b33fcc7f4',
               '8bad2b07e3b24e3ebb1c4a19d90421de', '3211567b3bca46a48916c60683f18dee',
               'd1663afb913b45218eea2c30ff3129bf', 'eb278f1802464e0d9d843ee817cbbcac',
               'de7b0aedc75a417cac851a0d4ee0d3a9', '9813f2fe7c1dd72d974a9b0657993620',
               'b43d2314eec749c99a8c0c8f850e9adc', 'ee3444f8c0a04320a5c8fb5781629eef',
               'cf7b806f56294798a441bb11741a6ad6', '127168760a2341eda983f948affb5148',
               'b1d456e2c9d1456eb9b198e4589ec58c', 'da6f3a8dfb0b480fa8bf11af326cfa77',
               'c5fa929864494f72b1a91f946a257bfd', 'c88b8ba59e0f468091c30eaaaa059ed9',
               '15986c242b56452cbf2b3495602e2237', '1a6a44497854449a9ae3ffe4d5eb248f',
               'ae34d1d456684f11b5ddfdd826afb990', 'ffb85ee7338a40ce9f5d550d479a7f30',
               '897ce69a5e41432bbeb8e2ad6cde9366', 'b1c91944d32e4553add5a2a95aebb5e7',
               '639b8f578f5b4cff82733363f9ab147d', 'f28b9fd81f364137ba7fe4280549bb18',
               '46b6abe971f647ac996dfb6a3a2868d2', '5545d620b1a34512aca1877acf3fb390',
               '44c9dc2a1115f8d49d9f89eed3b06af7', '8e7677efc7f94ba5a0bca4ff9043175b',
               'b032412fb1d14134a17be87d493b82a2', 'b36b4141060142d1b8348795ebb46ddf',
               '76072579aa0a4aec9132b81f0501e4e8', 'ef4e99f1c6d34e67b60138739375ea0b',
               'c44b9aadcf4f4f64b79e6027d2eabbcd', 'f679c07757894f02a3af64aeadca608c',
               '23615265eae5449e9913d0d9299ed1fa', '3c32c6ee0ec147fd9adc492d4579c45f',
               '35a9b3c632ca43da96e3f9934394696d', '8890ebd305044deabcc94696a98f49e9',
               'a223a1e9b498ed7f21e716e5b9d54885', '38ca4de1fdde446784175eab0938d567',
               '679954b800be4031b3b8e80d4b25bcea', 'cdcad0cf58634db6b82966cc54ae597a',
               'f7315a73fefa43398c8e33fdda1dde62', 'a45fd34678574ca2ab2a955b3d5beff6',
               'd55e720bb983495ab40930acab18b62d', 'cdeda16a447f443eb4c6040c109a33cf',
               'cdafc3c37a0b495ba01d0ebc31dd510a', 'bfa759398cb14f71b96c5d9463eaf460',
               '04310a5575964fff96719c42abd6fce7', 'ca0ad6f912fd4a43a9442941dd76123b',
               'f46598e65d744de4ad9eb4aec9d4f127', '514bd317a1264ad39fab6f833c8968d2',
               '44c069c7ac424130a945896b7d87bbb5', '993cd89a0470458d85fbf08196a7f565',
               '02512ddd0ac24ccc99826c6687e34f22', 'd86ac04d74ca4d9aba5478a1e4eaabec',
               '053556fd084145ca933d5c9fb2267285', '863b7800647445b7bbc9ad57772d8a93',
               'f65308904db64e198e847e2de756779b', '86753a87ee844843b174c8776b7d4472',
               '3e3c906ee3024793a6031f94008affcc', '93d94ec6b3354097b2fe5f7aa810e70c',
               'b67a87e72fcb42a2b01a353f96a39d1a', '0d4847c10251421e8a685600e9a79294',
               '4d7a1a3634c1429bb45ca2ca01a0aa90', 'bb12497b598945eead249f57549e0226',
               'b5a4149b19f249fb9edc1114d48de844', '9308975b318f4da095ae143eb7db272b',
               '6e6fa680d9a04b258c7cce751d2ecbd7', '51ba35bfe3694d58ab4969ee468340da',
               '236fbf9615214149ae2112fb429b0f29', '8843ed26022d43e6bfac3fe286d35b15',
               'f49da630ea10450a90293a3de155b038', 'a5d62dbe74b84a88a59caad550926224',
               'c26684b80d034fea878ec4f9b9f926ab', '43bb9d9043514ca3b10ab5f9cbf95566',
               '4fbaf73a01404f6394dd576e476d0b94', '79fbb62acfa54a36896527d00eba71cd',
               'baa18cd3afce4a4589352e277152d998', '420742f33d1c41b2a4eca0c3bce69a03',
               'f8d6f459f46b4974b0a0f1ae48395466', '7a84fad51bb146b4b661220952d5eb44',
               '54a8f66e23584a9a9650f01120791b5a', 'b4fcf235c8f6f048f321761757edc6c7',
               'ac8ff94f07d94798b5eff6220549bfba', '7082aada3c5041deb8cc72cb1ff926af',
               'a17f68e1bbf5495abdf4397bfe6c686e', '3d932d5cc9b949c79e0a26245cd3e4ca',
               '714aa1cac82d4c22ad06f481eb4aed56', '3574b3a4776040c1a67e051db4338328',
               '7166e9379e3843538333e66aed3ac1e0', '5c21caaf0aba40b2baee6e4c34eb4985',
               '93e5ed2a9bcb440999ea7fdd10a75ff5', 'a5e11ac2297c4d2493bde9a5e5f1da58',
               '70f44f4056c04f1d9b3699fe2ebb8c2a', '54dbcfb578e8413b9d26710f0e65e2ec',
               '3c2de6882c9640b9a03a83a138e2046b', 'dd596f5bef974351b97ca422c8e116bc',
               '9f78373d96b94a7888ce99d468ce3114', '8aed4c422fe64a9f83ca1457a292f390',
               '7c9f7b21de314bf3a711aeeeea599224', '4c8463614ee340039b2f94d0d503cd1e',
               'a66772466ea34c229bf5daa8e7fed7a0', 'c447b5e311144ca4875b6f169d26fcd9',
               'fd53e11268d04fc7b4141b12473c9eea', '0606ae7e9adc4229ad04f628f07341f3',
               '9a113742f3f74b0ba83f2feb09edd392', '2173c7399cbc4e33a13526f170c99332',
               '2f302f662a814d219d8a0360aef381ed', '5d32a507033140678e1ebc7d2eded0a6',
               'ae14cc9d303e4b1a9ca1294421be4e26', '07ea60e7a9044266bcc20f1493721b8b',
               'fd7418f2ede24c018f355b00ce280d71', 'd58a54867c274ceaa7548c4653b9e014',
               '8fc8a5a248bd44bebc4fc4a402fdfe46', '68aac29997364a9b85082c63ea867719',
               '2ef156f76f184106b9e82db1bad32848', 'a4fcc9775273472e91f13abc460b4255',
               '92b4deb48c334c88a94ccec4f97cd5f5', 'edf5d017c07a4224b4bb9e61fcafc2b9',
               '506948dfbdab4850815a630a83ced771', '0a4d951b20f247c29f70695d43498b1b',
               '7e62384c0cb94f25a3002b5c5218ce6d', 'ff5ed28d2200459985a47160afc1feb9',
               'f96ba48dc6df45869709eb76ac45b214', '4fc90a41639041b8b765092e84e4a67d',
               'e535e578fbb04afc81c9b19a7b970741', '59c63a087a044a139defa6491c5f337c',
               'f71c5dc6a67842b0966d7099ae2b02af', 'afb28610cfca41ea839fe1fdaa98562c',
               'c904ee97de4f4c01a608549f8306311d', 'a8a1c24d1bcf416590961df445878d7f',
               'aca9d5277d764fdaa4441ca53687e7bf', 'ca92760fadd241be88d6fda38a8e5915',
               '255e4d0acf3f40239389a051f4f1f573', '3ad183852ba54488a6148f974909cd7b',
               'ee36de950ee047918c4ffd0318e0c493', 'bddbdad0703d47fb92c1367211a80332',
               'a9df2600c57049d3b43299e9eb517df4', '924be84e15c44038960b61bcdf1bd0ce',
               'a16fed7c736348e798a92fe57cb5417c', 'd6cb82d0e80448ee8309f2b95744758c',
               '30052c8ac89ac5007a8ec1ac82bf02ef', '8863b1b5c02440598466bf6f7069d519',
               'd66910ade35546cd95fe9e7662d3b4f1', 'ee1d19039c624dca86f244df5c4a1955',
               '023f921e9b3649559a12db6ed1f65694', 'd721c60cc64c404f86b4e5d1fd91984f',
               '2139a1c58d424ddb865f7e31507e13b0', '543c3e01b29c4eeda51f944278ebb7d4',
               '83d68b4f952c41f3b4db1a1f82bcd4c2', '67cda9c6091d433295dc4ec78ba39b1d',
               '9bed46b4579e46d586d7de614f0ea24c', 'a372da6006124691aab15000ed52128e',
               '6c1ab883a2c246fa97f4a24fff751843', '84ad2902151045629d3cfa510d0b4694',
               '228ab28d686640a48dc66d7fee6ab4ff', '4dbf25a999784c519b132e7bdc3f5819',
               '9e1d9806a4734d41817e4ac44862a826', '1d45a2be8180c84ee352afaf280451a3',
               'a803c7c618284352b4a1c9b3549ae961', '7c6abc05ee8686b767f652506fbe6a46',
               '760e76cf598a4e9087c7f71b1b95f4e1', 'efc3b12ba4be48dc950c5f08883d85d1',
               '7cfe1370516e4bfebffe9a7c1e5e0847', 'f718dba7e1c54864be3179feab3e19af',
               '98bb72f2ff1f4539bc599c1835cc8cdc', 'b5d1d81231204eeb9f97f94855442380',
               '64e5092580654605b955540eda9eb64a', 'bd4e96826b8b46a093d80a5f19b7719d',
               '3ba3ea0ea6414227a89138d622d21c72', 'c257e87606284603afab3cd8ee8cdf98',
               '802b4c485bcd4712b43e4faf5970e395', '5b0bbc88cf6845cd8f6a633863e4ee87',
               'f88fd2ae4ff9418e8a6fead9447b3dbe', '3a5e79603ca6464b98b3f2f5eb37873b',
               '847be0dc197346d4975f7e3b91f8dfa2', 'b507de85da24403a88d5e0ef082f4d3c',
               'c6e668a893ae46d9b44e5637afbf05da', '8c084088d9e24d45b40c16f5d2568f79',
               'bebc795e21c74125a22010e0d4e3e05e', '24ab871293e042b5a939ca8fd7493903',
               '816028e3f87045b3962ab2a0d9173d97', 'd9998828bcb848f6a19c7ebb41d5ea69',
               '2e980cec2975cba8c9aa3907773b4df7', '9a90a4aa62e6401ebdff0f0833ca466d',
               'fc7890054671442080d8026532cb9361', 'c7a3598c87e744738052354987cdafa4',
               'c7729aa102b2481b9b424f7e0e5716eb', '06c068db78da449d8c611b2ccbdadd0e',
               '3e5782ff89774ea5895bdd15fbe68efd', '3b6f84c73627409a9a225043096f6d94',
               '19da2af3195b4d66a598ad0f1708021a', 'adff37ba652d402483de238253722ddd',
               '42361d1886884a9bb30d66cf53e82c25', '394a160cda7c402eb411e0a310bfdc78',
               'e241a112c2e241ceacfefa31d334ff2b', 'b9743ff3ba8c41b7a07ebb594ebf3c3e',
               '8e619c69b863449e829ee531c91571c3', '424a1886828b4c3d8e1aff6922451804',
               '4911595af9984da2bb4726fbc88bdea3', '54433cdb834a4923987ca4acfa5ac976',
               '07f0e52759334fb38365636e89b87e33', 'b747fb62ef224e13a6e1f19fc245d2de',
               '1ddee480c2214de19b8b269d2ce143f3', '47bca8d76554426eae266d4edd1685a9',
               'f55043fff60b4b77b60fc8a2752aa8a8', 'e8505be0741248adba787191d4866007',
               'd09cd208ce624b65838c522a5ff7a9a0', '149673cbde374236afbe78a984da464f']
        duid = random.choice(hit)
        url = 'http://172.31.21.219:8080/model-sticker/recommend/popup?userId={}&tag=lol&sessionId=123&language=en&country=us&product=kika'.format(
            duid)
        # url = 'http://52.43.155.219:8080/model-sticker/recommend/popup?userId={}&tag=lol&sessionId=123&language=en&country=test'.format(
        #     duid)
        response = self.client.get(url)
        print(response.text)

    # gif search
    @task(0)
    def gif_search(self):
        tags = ['ok', 'lol', "bueno", "bueno amor", "buenos días", "?", "??", "???"]
        lang = ['en', 'es', 'in', 'pt', 'fr', 'ru', 'el', 'mn']
        # url = 'http://kika-backend-sticker-web0.intranet.com:8080/backend-content-sending/v1/gifsticker/search?lang=' + random.choice(
        #     lang) + '&tag=' + random.choice(
        #     tags) + '&offset=' + str(random.choice(range(1, 50))) + '&limite=' + str(random.choice(range(1, 50)))
        url = 'http://172.31.21.26:8080/v1/gifsticker/search?lang=' + random.choice(lang) + '&tag=' + random.choice(
            tags) + '&offset=' + str(random.choice(range(0, 50))) + '&limite=' + str(random.choice(range(1, 50)))
        print(url)
        response = self.client.get(url)
        try:
            if response.json()['errorMsg'] != 'ok':
                response.failure('wrong!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        except:
            pass

    @task(0)
    def search(self):
        tags = ['ok', 'lol', "bueno", "bueno amor", "buenos días", "😘😘", "?", "??", "???"]
        # giphy
        # url = 'http://api.giphy.com/v1/gifs/search?q='+random.choice(tags) +'&api_key=3otOKnzEUBswRmEYr6&limit='+str(random.choice(range(1, 50)))+'&ffset='+str(random.choice(range(0, 50)))
        # tenor
        url = 'https://api.tenor.com/v1/search?q=' + random.choice(tags) + '&api_key=WL0AFGT9P4D1&limit=' + str(
            10) + '&pos=' + str(0)
        response = self.client.get(url)
        print(response)

    @task(0)
    def spring(self):
        hit = ['c55f64b78df14008adbaeff615e35c4c', '50a4ecbbb8474a1cbd7737a029e155ac',
               'cc8a440f70aa44779559627be07ff59f',
               'd91ea26a9b6d4e8885cb2acace4c30a1', '7b3dc5a04dd0469abc8bde1764160899',
               '8224c2c0c5aa442f99586a57cd35133d',
               'c782bb7a9f524a568cfd81d6666e417c', '4ff328c8b4d7445facd8d9532116205c',
               'beca0c0ed31e4552b791dd5f2136e903',
               '215c3a6f41c84d0a817ad69f2a4bc495', '06d6333e6e6a492883bb30ddff775d81',
               '70a2997ed6a0483a86df23ba7b99d07c',
               '82b5a6c28475925607e397a998a3374b', 'dcde17e6275947ce99ac3f47b19a326d',
               'd8383ac9fd7444b281f049b15ca1e276',
               '19ce03fa4f464e2f836a5d7a345297ee', 'a24883f83e944299bdc6d38d923076ac',
               '8c0ee25aa3382c8e9ac7530495eaeec3',
               '81f7ea63fae38de326937b0b7ea895bf', '68445cd1869e46a0ad4a6e25e9198603',
               '0dadbf8949554ffd954a981a40c3b724',
               '2ee7fe857ee540838b87a946c0953158', '652db7139b204b8db1c49f059242db93',
               '86936561d6e64bc9b3431558dd5691e4',
               '5f2686bcfe914b6a8eb4dd282c5ed17a', 'cc0e2b3a5a434968ba655da5594d525b',
               '0c744ea5f75b46f58d4abea791df8188',
               '30981c13d3534020bd8645644201b08a', 'a55f136291d74b73843887a8812f97f1',
               '6196ee370d2f474ba779462e8540f216',
               '84451f451dc44685bb1aeb47fab9c151', '965a39c29ab2477f9c3c512696b022ad',
               '09c9c7739eee4b2f8da7ab36d8b214da',
               '8e57a2d1970949bba90c3ab35f14f63d', 'dbbde590248c4651b5f05b3d660c5411',
               'cea99385e252418a9d534ed26cf4f386',
               '3cfc950bd565419ab731c9ecca138fa0', 'd66f594226dd427bac13c67a8a5aee71',
               '38acff2aba14464ab44ac840b9b032b7',
               'e742947f1f614ebd894e1a58f42ea368', 'f7dbd671bbf7455f9c99f1e37c83c327',
               'b67063377b004dd0a8dc90e31dc6b768',
               'c96c34c1eaa548c88513808feda26935', '51e9638cc420400cae83d00071768007',
               '555ebb7c3bc34a449d2293b712c3b3a5',
               '89659bfd34d04e0eab140984c213dd85', '49674aea545841b1a015ccc7eff6ae66',
               'a8a8feaa2c6e4ab2b94c53caa49150da',
               'b50a0cd9d6b4446bb3073bf7138a2161', 'a53d0916c5434aaab61f27bd2901c74a',
               '5d11e386e5784d1581b64ce0c77203ef',
               'ea6a2a9e8d984a5489f35abd5e6ca7cc', '4c470e6fba4a4da8800304cd96083190',
               '5df7aa33e70b4d1698e1706dc2419f3e',
               '2addbc0c117d424883bd3898c8b16297', 'eb67768b3a372c851550b14c6ce78073',
               '6834995ea46e4de285070b2f47459330',
               'c5d1112963a74f9b8928631eda403a08', 'b77b051eae38bb92c8b3cc632cbcbf28',
               '00ac89c1c921421cb9923e28bb4f3e32',
               '005509eb14ba41c0b1c89c48a5c00c18', '48191e1eb43644eda2cc65c004d0830a',
               'aaa30d180b934173b3345d28741380cf',
               '4500b082905a49d0a040976230ca273d', 'c6dbff2e32dd483a8f68240b2ac76db5',
               '344f49f847ff4a0ebfeda6c3b6c8d83c',
               '758b46475c12433d8633ef9fffcae707', '52aea0ee75d34b259ec1e328f398372b',
               '4398db0d987144db82959170f2e5f26e',
               '07d126ec668b97cc995bd4fa3dbadb72', '1534ee327dde40f891bf8d89d93cb051',
               'b950d94b7e9f4a0a9c244baf4ae5fc3b',
               '302a0cd0fff643edb6265fdea082c4f0', 'a6bf17cf12a877894f0e530f22625b5e',
               '6dfc923bbb6082acb1bda9b044a167e5',
               '40baafb04e914ee38f9825542c55252b', '4d25f0bf01a041c1a3961ebddc705bda',
               'fa8230afbad54754841c75bd695ce290',
               '78a4d85d56494668aaa345e58b806aaa', '868a9b8946704b71acb2d355cc80b8a9',
               '14fc8be32f2f40a1b8bbb4f063bfc283',
               '2ce4ed354f6a420b87b2aa2f67f3ef66', 'eaba9e9d7b8e31b64f167ec16ac9d775',
               '2066e2579717416189c6b2c1768c05b4',
               '0a7c6231eab04dd4818c606e329598cb', '27c9efdf9a724dceba3f5781cb948a1f',
               'cf4713952ca644beb5350d3447387bc9',
               '5305d9afc01346cea4249fd1f115c794', 'd145478960e347daadf46f3503d03a2e',
               '2c8bba2cadda453ea5085b7bc9e99cdd',
               'f1da5d31955845bda6b4d4b42c3897ad', 'c4c2b1bf2f294cfe9bb0738fe10df7c5',
               '8e7470a260ee45d4bdb48db75ac92039',
               '5b5ea4a4774b4dfc996551c8102e8727', '0aa966c337cc4e4fbeb015ab8f908b25',
               'ff0ecf762e244bd7acf56d47d73eb2af',
               '0426e39417ed4821bad49f24ba501b6c', '5cad96637f65447eaf0f070dedd655bb',
               '40b1f7d1d2c1c97c718cddecf1eef104',
               '681d3ec29802462eb5ca75f0450355c5', 'b6abeca96552dab9360be75fac2df1a4',
               '93e4673733f143638870cc590ffb747d',
               'daa07a157f1d41458eef1aefcd7fdeeb', '810949e3200e4fac873b1fd828729711',
               '2eaafd5f0d7d4d2ab60fef4954f1e625',
               '708851bd19794ca5bca7df3ac6b3334f', 'b86458cba2124ad3b3b2c92eeedb44ca',
               'd7a953a8ec4d4b8baf8926da5b75fb83',
               'ee097b15ed4a446f9d0a6519028c8756', '4656593bb1354fe7801b7011e96e5b0b',
               'aeb0ca93ce754afba6e025bed66adbe6',
               'c4acd2c8a7da4180bf397a4610a661fa', '4b3d6a38a81a469aa233e021087fbb1c',
               '8cb2d3dad2c945c49c03069709dae49a',
               '22badc5d5fba4808bf58473a9ef6a802', '2542ad4dd79e478ea149ebf97ed9e9f5',
               '347b60ed24de446d8bdb720289d671b5',
               '851d3f4ffe1dff39a6f81fdf682812ba', '1e7efe178de643c2a8232372eab0b671',
               '222343cad36346a3890c4e8d0480b797',
               '1569959deeb8440d9864c09d49ccb8e0', '2da20c31fd62453eace59b7c7c39361e',
               '503a9f9bf2694a1ea1d225a377efaa9f',
               'ae83a428e2f9e99344486c277901f09a', '0bad0fbc28fd4246bb8a7dad24e52e86']
        duid = random.choice(hit)
        # url = 'http://172.31.23.134:10010/recommend/popup?userId={}&tag=lol&sessionId=123&language=en&country=us&product=kika'.format(
        #     duid)
        # url = 'http://172.31.23.134:10010/recommend/popup?sessionId=123&tag=ok&userId={}&language=pt&type=0'.format(
        #     duid)
        url = 'http://172.31.23.134:8080/model-sticker/recommend/popup?sessionId=123&tag=ok&userId={}&language=pt&type=0'.format(
            duid)
        response = self.client.get(url)
        print(response.text)

    @task(0)
    def gif(self):
        # url = 'http://api.giphy.com/v1/gifs/random?api_key=3otOKnzEUBswRmEYr6&tag=ok&fmt=json&rating=g'
        url = 'https://api.tenor.com/v1/random?q=ok&api_key=WL0AFGT9P4D1&limit=1&pos=0'
        response = self.client.get(url)
        print(response.text)

    @task(0)
    def data_modle(self):
        duid_list = ['209b0de72562441a0b820892c692cf62', 'da611e8ec26ffcb2cd07ce14383d246f']
        tag_list = ['ok', 'lol', 'yes', 'good', 'no']
        url = 'http://172.31.31.224:8080/recommend/maturity/popup?sessionId=123123123123&tag=' + random.choice(
            tag_list) + '&userId=' + random.choice(duid_list) + '&product=api_test'
        # url = 'http://172.31.23.134:8080/model-sticker/recommend/maturity/popup?sessionId=123123123123&tag=' + random.choice(
        #     tag_list) + '&userId=' + random.choice(duid_list) + '&product=api_test'
        pop = self.client.get(url)
        print(pop.text)
        with pop as response:
            try:
                if response.json()['errorCode'] != '0':
                    response.failure('wrong!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            except:
                pass

    @task(0)
    def api_test_popup(self):
        tag_list = ['ok', 'lol', 'yes', 'good', 'no']
        duid = kika.get_duid_in_way(8, 0)
        sign = kika.get_sign(app='pro', duid=duid)
        tag = random.choice(tag_list)
        kb_lang = 'en_US'
        # pop = self.client.get(
        #     'http://172.31.24.127:8080/backend-content-sending/popup?tag=' + tag + '&kb_lang=' + kb_lang + '&sign=' + sign,
        #     headers=kika.set_header(duid=duid, lang=kb_lang, app='pro'), catch_response=True)
        pop = self.client.get(
            'http://172.31.23.134:9090/backend-content-sending/popup?tag=' + tag + '&kb_lang=' + kb_lang + '&sign=' + sign,
            headers=kika.set_header(duid=duid, lang=kb_lang, app='pro'), catch_response=True)
        print(pop.text)
        with pop as response:
            try:
                if 'from' not in response.json()['data']['sticker'][0]['key']:
                    response.failure('wrong!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            except:
                pass
                print(pop.json())

    @task(0)
    def ip_pic(self):
        url = 'https://activity.api.kikatech.com/ip-groups/v1/activity/pic?activity=worldcup&tag=gz&style=page'
        pic = self.client.get(url, catch_response=True)
        with pic as response:
            try:
                if response.json()['errorMsg'] != 'ok':
                    response.failure('wrong!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            except:
                pass

    @task(0)
    def ip_tag(self):
        url = 'https://activity.api.kikatech.com/ip-groups/v1/activity/tag?activity=worldcup&style=all'
        pic = self.client.get(url, catch_response=True)
        with pic as response:
            try:
                if response.json()['errorMsg'] != 'ok':
                    response.failure('wrong!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            except:
                pass

    @task(0)
    def ip_new(self):
        url = 'https://activity.api.kikatech.com/ip-groups/v1/match/worldcupnews'
        pic = self.client.get(url, catch_response=True)
        with pic as response:
            try:
                if response.json()['errorMsg'] != 'ok':
                    response.failure('wrong!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            except:
                pass

    @task(0)
    def ad(self):
        header = {'Kika-Install-Time': '1505198889124', 'Host': None, 'Accept-Encoding': 'gzip',
                  'Accept-Charset': 'UTF-8',
                  'Connection': 'Keep-Alive',
                  'User-Agent': 'com.qisiemoji.inputmethod/1477 (5a215835df204115ee3d2d4ec0c528aa/78472ddd7528bcacc15725a16aeec190) Country/US Language/en System/android Version/20 Screen/480',
                  'Accept-Language': 'en_US', 'X-Model': 'D6603'}
        url = 'http://172.31.7.36:8080/v1/advertising/online'
        response = self.client.get(url, headers=header, catch_response=True)
        with response as response:
            try:
                if response.json()['errorMsg'] != 'ok':
                    response.failure('wrong!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            except:
                pass

    @task(0)
    def gifkeyboard_tag(self):
        url = 'http://gifkeyboard.kikakeyboard.com/v1/tag/hot'
        response = self.client.get(url, catch_response=True)
        with response as response:
            try:
                if response.json()['errorMsg'] != 'ok':
                    response.failure('wrong!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            except:
                pass

    @task(0)
    def gifkeyboard_hot(self):
        url = 'http://gifkeyboard.kikakeyboard.com/v1/picture/hot'
        response = self.client.get(url, catch_response=True)
        with response as response:
            try:
                if response.json()['errorMsg'] != 'ok':
                    response.failure('wrong!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            except:
                pass

    @task(0)
    def advertising(self):
        url = 'https://api.kikakeyboard.com/v1/advertising/online'
        header = {'Accept-Charset': 'UTF-8', 'Accept-Encoding': 'gzip',
                  'User-Agent': 'com.qisiemoji.inputmethod/1477 (5a215835df204115ee3d2d4ec0c528aa/78472ddd7528bcacc15725a16aeec190) Country/US Language/en System/android Version/19 Screen/480',
                  'Accept-Language': 'en_US', 'Connection': 'Keep-Alive', 'Host': None,
                  'Kika-Install-Time': '1505198889124', 'X-Model': 'D6603'}
        response = self.client.get(url, headers=header, catch_response=True)
        with response as response:
            try:
                if response.json()['errorMsg'] != 'ok':
                    response.failure('wrong!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            except:
                pass

    @task(0)
    def OpTag(self):
        url = 'http://172.31.23.134:9090/backend-content-sending/popup?tag=good&kb_lang=en_US&sign=a15d5bcd3a310c773f47955a636022cc&type=0'
        header = {'X-Model': 'D6603', 'Connection': 'Keep-Alive',
                  'User-Agent': 'com.qisiemoji.inputmethod/2541 (c4b18139641abdd81512120cba3ba4fd/78472ddd7528bcacc15725a16aeec190) Country/US Language/en System/android Version/23 Screen/480',
                  'Accept-Language': 'en_US', 'Accept-Encoding': 'gzip', 'Kika-Install-Time': '1505198889124'}
        response = self.client.get(url, headers=header, catch_response=True)
        with response as response:
            try:
                if response.json()['errorMsg'] != 'ok':
                    response.failure('wrong!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            except:
                pass


class MyLocust(HttpLocust):
    task_set = popup_test
    # 任务的最小等待时间单位ms
    min_wait = 100
    # 任务的最大等待时间单位ms
    max_wait = 1000
    host = 'api.kikakeyboard.com'
    # host = 'blau.kika-backend.com'
    # host = 'kika-data-blau-web0.intranet.com'
    # host = 'api.giphy.com'
    # host = 'https://www.baidu.com/'
    # host = 'activity.api.kikatech.com'
    # host = 'api.tenor.com'
    # host = 'gifkeyboard.kikakeyboard.com'
