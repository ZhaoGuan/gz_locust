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
        all_duid = ['1bf95b021807428abf5d2d23f2ed2bab', '1f902bdb0a034da78fc06a392f6d70a8', '9a0031f2605f40f1b12b15218bffa830', '6d15356871154dbf88968a7497cdf286', '2e6c57ce8bad46eb8c668aec758f6278', '676e1d4e008a468c8f5ac56bb1d871f6', '3d56618f7e6536587829f2e4a0e2135e', 'ee9fcd14cf804c3db0dc6e89ff6a5386', 'f2ef367a823544c7993d1616f665e19c', '064b67e8089372aa7f363f888b2ab25b', 'd00285b87e6e41d5990a040a1a528750', '32a40ff78343427c8f6218dad92b8abb', '2cfad88e196d4327af5adcb892cb4869', '1b5fb43b72034e2b99aa44b57f998e8c', '06eb71774c5249bda638384e79fdcb67', '889a12f71ab84ab1b1ed1305b3a8fac7', '14369c9cf0b64e5cbad0dd8f9a309d30', '99904519ba29be24bf9f1dc9043f307b', '233bdcd7a67445e78ad0b595af9962e7', 'ac018bdb00514842bdb4e3a4cf8f1d85', 'cae548d706c30d1c9492e8891247bed5', 'c88ea9aa5b6d4305a632283d81ebff95', '6e4594eab3b14bee85a42a3048b3469a', '532b9265c8a3e0fbf8e71ca4227ae62b', 'b88336aaecf741a0b661063cc40fda68', 'aaad07fe215b49c9b9a76d52d724171c', 'ff4a223cf0834306b591060a9549ce8d', 'f1b0cd80d2f453fbde133e75e3517905', '8dbc7dcafe0410975dc54aa0ecba9695', '4288099343d14d38be66da8fba84c9d4', 'bf1c63b76e41469182ce9dfe8c433f14', '5e22c46fe39f400ab3c95b99daf43994', '878b7eb5aea9406ba553c02cc08ce3fc', '11871108716746f9b4ad7c5c6b0c9520', 'd2cb77fc2bc6429ab3f604b8de88eb39', '4ea9200b15c04e61bd3aa14ab41bb480', '6be42859788d691b2fa5aa1e99351501', '24560c058a2f46e2ab257fb9727a275b', '9cb5cbbe17f4487088d3bc94d55a526e', 'a20025c3eb2ab9624e5ec55ac7c3685f', '032283ef63f64edd83e3a4a0df8c58a4', '90cee0a0524144dc8e33a97bb812be41', '98f8cad999e8435427c6166618549659', '7b7ce4bd0aba4e348dda59a7065366bc', '56c84b7d110847138ce98b69b6796431', 'e9f95ad1826c4bcbb74677c06bcb83d2', 'cfa482fd7560484a98d3eb7948c3e1ad', 'dc181b7b2d904e4cad5c1465c99ab372', '097fd0c2ce134ac89299e9f04fc616ae', '7f65db48d04a24b1cd571e4f22c88847', 'a8ce170af98647a085e5b96157ae1246', 'e2095d08c39041db82aabeb016dc0578', '0aa9e42f75a749739a1e1d05dcc14483', '67387d1c9dda4ac6baac3c1e02b21de5', 'e1ee834372ea47e0ba165298455eb79c', '79b0fe31f2d244f5a73a91cdaf3971d0', 'd433022eda18fb9ccaeff616039e4453', 'fb89f8a7fd184896a9801d9658c9bc76', 'e9d329f02d8e4a4dba8ded5d240330c8', '3c7b5418467d4605bcdab3733e5d66e6', '3548e4051c6d4eeea044216a5d1d02a5', '4e34d7eb4f0f42e9bf89e03fb6d0e07d', '8f6176af583344179053d4b55beec6de', 'e5b9d3d9e6be4bbc9d3bc8a1fab54d74', 'd6b52445d58f4e41a74a52c281c5005e', '830be21750f44dee8064980a6831647b', '40ef8e412d774ad3bd19501ea5f54cba', 'c59b33cf00cc4d828b32c9f46f419420', '33f30811f5d24b9e97dc73ad54d17f88', '0a7172085b5a43f58e83ad6d6e17e063', '1fe9dae6e62546cca248303ccc6beed1', '9561805a1727416db608ce722c8738cb', '99c33a067f9140578fed44ef1e3a6e13', '55e107413ae545589d5195c9d9879a5f', 'c66da943371d4504a6835a96d2888425', '0425ab8a123f4b20a18457e1bba2e8c5', '3a0e9fdf97d54572b2bca4109f9897ba', '65957248d4a04c6ab5a5a92ff4294c49', '6980fec0ac2d4ab789a1e580089f740f', 'da5ecaaf58ad4935962a6a46423da5f5', '08c257e7d91d48fb8f0dda70658b5884', 'b0b82e0c698048ea9bd4b79f2879a846', '06f868bf489d412cbf87dbf9236c7504', '6c0cfa7a5b184ec99ceb74656c8b76a1', 'a8b4fa60daeb4ae2995d98cfc080ae0d', '162cb1544478451a8a37aba603b4ef47', '5b2c438cae4540c790c5c2b5523306ed', '7a54ab01c4ff4b38898ecf394a625444', '13d4e78c734b416a90633e1ac0055ee8', '51142102edf94f4a8825e2ebb362a334', 'c132f6df954a4652ab4bab1a7beaf109', 'de7aae05298e46d193dc03b1749b954a', '1db18560888cb9e36803b44603e525b4', '42564fc4f33047eba86b9c10cff1b267', 'c7768ab6f5ad463ea2c71204e52d75ce', '00e2b2b9f38a4414a2315a6c58e3cce7', 'c1f275e8c769404db0b2cab62e5b6200', 'd67933fcf84c45f6a7141f1476b3ed72', 'af0632646e5d4838a3aca1d5524a7bf3', '23036421abd34d81aa7d42019d2b64cc', '89ad56741e4acac306e13f4cda9c8d5c', 'eb671655d23c433aa0e1a91b6c06de21', '63bcbb7e4953454ba28d6e933a61eff8', '7325f5127fbf4060a6e4c55be81fde81', 'b993b105b85d419d9f14d38798210760', '60fa19d7b480f4b2b002cd5194ffb7cb', 'c7af90ecf7874caea7e0fd2d011be3a7', 'fdd72398cedd4efeae927017242b0466', 'cfdab76cb15114bc21a2fbbb61c5b5e2', '11568a08ab69823e0c17c77bef7c977a', '8e26d0a1b10d326f32216135ef8c2edb', 'e00379256f644f39b53f1eb0f24df74d', '67d931dbcf2eb002de4023550ce28da1', '9a801c8fb21a4580be9f2c666084712a', '927c4ea8ece24b369da85cc0d9eed12f', '96f660d9249242c7806504d1d8535d0f', 'aff4c71d149b4a7098b3cf98b68a92e2', '6a03a42a3133425ebf8267c36bc5d512', '10039432d6515679bca9e50c63360387', '551481e903c84026b766ca1726f6ac1e', '113b281bc0f3a5b3449623a473c9a641', '80e38827f1bd4f66ba2270888e0877bb', '37ad11be93d6495dbfee0053ea0754ee', 'd966e190fb394c39afc16dd692c51150', 'c56f8fb8adc94ea49b101b2a290fe58a', '0c6de0154e35b20e2bacfec795e8575a', '1d022f8e3dfa49cbbc051cbef1e4a8ac', 'c239a6e2c0071c99c3e3d83fe642679d', '223a103942674c22b481d54cb1d5bf6a', 'c1c9cbf4328493faa8e951ba1b76dd7a', '79349be695b846fb87df46a99e925ff1', '81ce29eaf13c36859e4a28984faeebcf', 'b02e99cb8fd5402d8dd1f6309bd26b6b', '72d74a877b7b4694bda183bbf7c166d2', 'ce10c091dd314b1bb1090b9a7203a319', 'b16bb978600a4903a0145d5995225af2', '57841bdddd624fd4835006951e8d07f8', '670c40d39fa04d82ae6a6d7904c0a5a5', 'd0c6b94ce45444dcb05c4b63752a5a63', 'b3306766d2a84508a4cff494771ae200', 'fb9383c86a211c4c86fa5a81f5cfb0e2', '7d02bde479aa47b0ac7b7f98cee7e015', 'c55f60fc904e471aa7af3c22a356ccde', 'b6c87af410a2bcce14c2b6038f05a290', '23916244a76e4da6bc83e48b35a43b51', '36fdd30f34f64c34ba9c1e89b9a1e21c', '311466b7f77a45e5a08e18fbd0767f95', '3a371b29b52c47c2914744a5d19505ff', '7f047d178e5c472c83042cc0b49fd817', '0d3fd79a50b848908e9fe6bf0f1ce6ea', '832092ee4e8949bc8b2ab460b25a10e0', '1825e2af44a742608e26117df133cfc2', '3fba500e82294673808495dd65f5bcdb', '29f125b0ef4f4111be5f943129637fde', 'abb667d0393d404da0d7bbc9275415ea', 'dac165f0872e4b0151e2ed410d8368c7', 'cf3cd95b38284048959a8c6e6e58b52d', 'db3b949fdb474977a098b925008f917f', '84b5aaf88a684882961e5175bed89c29', '46e9832f3ad945e0b561d8d17514b118', 'b421a2dddebc4c1bbaf858bd60c87c37', '6e388346371144a8b7edda77aea23a54', '93c7e252169c4c059e4db0864ec72acd', '6040b22c4c4d4794aae3622d25e4a31d', '16dc532757f54b20b05d468116196fbf', '96f8286c9d2d4d0ca040f3a965a7111e', '834e75540714427fb5919dc01036c761', '1cb4689f33a67b833d06d70c1d7c61c4', '7f4d5dbcd9304b48bd8fcf7ac55602f0', '74d537ecc2ab49128fed0a7fb9c9620e', 'd86c80d4a07c47439c12e6197050634a', 'c92986e032581a30a4266fefa3f7d504', '52df850d8f46481ebe8c52604b9188aa', 'b5035f02096a405ea2be253c6e85f5e4', '3fb76e190b262729dbcd4b4cc4a4631b', 'da1032ea7b4b679a82f6d5b664513192', '3489821c1773468c8052912efa9cf4e5', 'dca0003f03d543f0b834c4ccc167e70d', '8537e40d6af8634f7148e254059c33bc', '9d4b2ca8297c41629e667abf69d229ac', '353cc1fac81a45c0b4396972403f4b06', '61b099203ab84532ba3a5c0e77be3ac4', '3f9ef73b34614f188703cdb1b636a05b', '01b8c27e21db4b1a99941f3283a45b1c', '4d0697a497f44308851018918a796d45', '6b7fe50e4576424ea734adf5b6d1804d', '76a1901118274ccfab6fd6d50a95fbc8', '48a1a8b3f49694f128cf9eee969d9c56', 'b32f17c0f68b4d3a8f71c103905a640e', '9e3ac4dfe5e146748a14c6385d84cd10', '546b24a833604d2da2c5cda0ef233f35', '91c49debe59941b788ae69bf09610f98', '0f2a1db800e34b29bccac820da819540', '5e5e2f7e578f4e1f9c049df654440249', 'fadfb42bbb8a454ea9a71c18670c8563', '26db7dceaae84c4982c07dcc20d6942e', '81e1af012f264b899a8fd1a71f9b5dee', '0b3e6f278c514b988e89901dc876348a', '9759ab10d4d945e7bde062dba18b643a', '1eea2c5c3fcf4bdaba68c9f8fa581a85']
        duid = random.choice(all_duid)
        # url = "http://172.31.16.27:8080/v1/app/{}/device/test/event/recent_num_sticker?range=0-3".format(
        #     duid)
        # url = 'http://kika-data-blau-web0.intranet.com:8080/v1/app/4e5ab3a6d2140457e0423a28a094b1fd/device/{}/event/recent_tag_num_sticker?range=0-3&type=hola'.format(
        #     duid)
        url = 'http://172.31.23.134:8080/model-sticker/recommend/popup?userId={}&tag=ok&sessionId=123&language=en&type=0&country=us&mod=not2'.format(
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
