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
        # all_duid = ['a9a22e4f665749339e00144a54316202', '573823d20e4e4315a166e8750473b374',
        #             '2d1fcdfd9e86431396c67cf253f3243b', 'a24313e98acf47f39d77bc6e16b15c55',
        #             'a790e9edf319431f95da10280062a213', 'da943175fab14edcbbd01a0ef84c73a9',
        #             'ecc2ef0ec4312f17fd80dcda3ded72e9', 'd1cbb6f896d54b69b43132c2f69abfc3',
        #             '8171eaca2a95437091e431453a3a5770', 'a027df07407c4e6bbe7d4312cd9b3778']
        all_duid = ['573823d20e4e4315a166e8750473b374', '5db1fb325f594d3c894314360b76a6ed',
                    '2d1fcdfd9e86431396c67cf253f3243b', 'aac637509c2744318119183a5ab4bef5',
                    'a24313e98acf47f39d77bc6e16b15c55', '215082a53e804313ad3405cc911debc2',
                    '2fda19f840d841e7b0325b431b5a4917', '34704bbc9b294e7cb431a4c2e9e3e44b',
                    '77307a43100e4d3990d0adbeb131f6d8', 'a790e9edf319431f95da10280062a213',
                    '85ab1ed8f7c9431bba65b73057571ba1', 'a0ae6881cf3849659c28eef3c8043197',
                    'ebe4316802d5488da5f243e92e24c0bb', 'da943175fab14edcbbd01a0ef84c73a9',
                    'ecc2ef0ec4312f17fd80dcda3ded72e9', 'da851e9939c7431bb1b9dcd141b53115',
                    '8f6d272466d54312a29288b0d912574c', 'd106f421d4314e6fa7a925a461336d4c',
                    'd0302362319a4314a08089c7d64bd5a1', 'b15bb05edacc431494459009947306d2',
                    'd1cbb6f896d54b69b43132c2f69abfc3', '48239334a13f4b14a04311ec1166853b',
                    'd0b178fbd45ea59c26654923a5d431f7', '5eebe913162c42c48431974d331b3d9d',
                    'f1b431b4373a4a24b27d45c2909822b1', 'd6d5bbd3a7354b2797f8ef234315c29f',
                    'edcaee0687f2422ba431c630b78871a4', '8171eaca2a95437091e431453a3a5770',
                    '8494f83a75db43118775dd174ec11eca', '30762e4ad7684319bf8e32dece477c82',
                    'b557dc271bd84311b5acb23dfb418afc', '0eb9c65b5cdf431ca534f1ca4d0874db',
                    '363147c2ec85451095055bc2343119b1', '88643944312e4709a27055d3e0d143f3',
                    '326c4319f33246ea8dfceec9f147eae5', 'b44313cac45d4783ab94f1be3919fe1e',
                    'b579a7ff785f4313b7f8b28326aba002', '8149fa24e7d4c9d65e4aadc8431b5f6c',
                    'dd01034a5ae34dae8e05992c12431f72', 'f484323a09b3cc3431bc07ed7b341312',
                    '2bebbdd79e3d4310879be55281720b40', '30f1ebf8edcc46ca9f86431521b7865c',
                    '01501810c4314e6a8735f53f62fa3358', '4312b1042bb311323ee618c3f5d6b769',
                    'a027df07407c4e6bbe7d4312cd9b3778', 'a2c9b874315740b482b3463c59177c39',
                    '390f3f36eea74bffa531a843196d22ed', '5f8b290d99984b0baab029431d6989ff',
                    '0b0b43117317476aa79e042750abc77f', '93213b64cb01431daf603327ac25e159',
                    'cc878490431a43a88e66beff8733ec93', '788f2146431c54db32e86e8952ea37ff',
                    'e05b5a1d1768431681d0072c9e8f9d1d', '177ad510f8b3431091166a4f09a51598',
                    '7d7096a2acc94431b0673140788eb354', '2431482c852b4ba4b7708fe74513beca',
                    'edf05eae32a244319ca73c123fbaf4f4', '376e20d5d3f94d98894310b4602fe376',
                    '2431a22e6a2c4e80a7f9395cfb0cf2ab', 'c4545c1f89494c1a9dafc5343161f221',
                    'df7455b4317d4fc1b767816409040814', 'e4a95e98806641919f0329c77a724310',
                    'edd8eaf86e9c4631b31908ab2aed4315', '36ad7fdb6ee54d8183a44314972c1bda',
                    'b814424419c7431ea25e17c7adf6e0ea', '693e2202517d4315a52e8b64df456191',
                    '5cc777311da044d8ab3d431bfde54289', '7d77738828a9480ab644084310b34b66',
                    '344b1e7157c34964839377c5073431af', 'fe4ae4e576a44db28010c8c1473431f4',
                    '6ec431f039f84c5aaf9e7946aa15b4a2', 'a560ccb4317d4d7f819c8e7d8db416a8',
                    '0529836c16d3431fb5c75b0b7bedb22f', 'ac12e52c6d3a431e98ae5280de3bbc93',
                    '9a8f1eebc3fe4315a0b909509475acbc', 'e14666fc1943431eb8e86ee9db1471f6',
                    'e09a7bd3ceaf41fb88fbd729b4310008', '3ac10706431149578918559da9bad56a',
                    '2c1cc570819949bd92b47f4315b96963', '2d68e4317806678a39ae974bdf70f8bd',
                    'ddfe9a5cd03243188b70cd0728090afc', '9201d09845cc404882343135a155306d',
                    '662431898d574cb1ac1e8e16da0a2b9c', '994319124c5e435c8ac6a2fa87f2ba1d',
                    '55d1dd7001b2431487417fb8bf54b194', '2f76fe2431f5496d8e265343ca91d940',
                    '5bc68240b731431585296ca42c06e393', '2300180a6d63431aabed36769f4ca784',
                    'f67d72e09dd7443182c34d7459195e6b', '47167e85f7f24314aa57a5375581a8db',
                    'afc25f4409ae431f83fb538105933443', '1c65cdecfb05431fa125557fc3ece267',
                    '94975fbeb9544ed099a24431f8d59712', '6431ff7f312c4e94a3aa4e52477504bd',
                    '01f173250f14431f8db84a460c465aaf', '7fce2431ee1b43ad89f57bec2f8999de',
                    '4d2a64c933a24cf497ede4a5e5431a37', '130d43161f5a43d082427d4e0e2b7395',
                    '4d1d988a25714bf09c7b74744bf3431e', '8bf9526e22ed431480ab00a8ea38f937',
                    'f34935e727804313bb4c686095d5bbf6', '5a47e602414c43129e8376dfe5f739ca',
                    'ba768d7ec5c1431e88d5d97d34445abe', 'c5839f7db0c3443193303d1df24f26ee',
                    '60994319ea844762922d1e98db431b1b', '8f3055cc61c3431dac344dbc84918e4f',
                    '449d9c734313a9b2a2fa7d859fe9e8bf', '2dd5ee44efc4431fa9257bcc26b7e681',
                    '0b541661e57143189fbf9ceee2122884', '12216d2e76aa4319a8c9cc4a937d248f',
                    '7e87bbb908c24315af121eadc84472b2', '7bee629cd008454c842e61a62a431b37',
                    'd2321778b3c14024ae0b431584dee4a1', '2c0f37545691431d86127bf57620fc45',
                    '34317a1559f242cdb76c061a90d48cd1', '376e20d5d3f94d98894310b4602fe376',
                    'e894414a9fa24317997f0471118c0cbb', 'c971dc9e98ca431c979b48e4cd419bf6',
                    '2ad6e0a72c01431ea311431d5b3026f7', 'd677bb3eaabd43189d73f69388057471',
                    'ade4126fa7be4bf7ac7e486431270bd5', 'b507290f482e45b2a05940643f431daf',
                    '753ae5cf11d843109c5c9a5492432d93', '4313530e2bd84f1d8585f184baa172f1',
                    '9f9fb2ef431440328154d29def70aa63', '8acbde431f504367b165d10661cf79b7',
                    '8d092d539fe2479fb1b84316f963e854', '3dcfe68678b74c02ae3a3f21de43173d',
                    'c660bd4e6c7e4fb78ce3e73460454312', 'a24e6ffd7cc546a892144315e6263341',
                    '34317a1559f242cdb76c061a90d48cd1', 'eebc9c9ee5ea46228727087f00243121',
                    'fb840607a32b4435b3c431dc98c31f26', '8fc17f9ef3e2431ea9d3c589a5306919',
                    '2c77520fd8de4315905fedb85aca8316', 'd8effb9b6eb94315a2823fb08416ce29',
                    'ded08e9b85de487da67e7cd0431f453f', '7078a924311948c0bf0831f2f2ca0eb8',
                    '4317d9a1301e44699514037566beaca8', '8619b119806a43179a4fcf71a3294eb6',
                    '068f5e3457e0431d9d75c121c3644f1e', '1c26b2c5a5984ac3a45362f601f431d0',
                    'a96b850a40ec4c7d8314f0645680a431', '6c585310f43144c5a0fb5f954f5cd09f',
                    'c357639b64de4b9cba431afd5f0b80dd', 'e63fcdf166e540d384975843128344c1',
                    'b9073511413e4662a431be20909d11be', '84813a4310284aa88b3ff8adc97bdafb',
                    '613af7a82371431481fb4733093d62ba', 'f4afddfdd040431d95f83c553d29fefe',
                    '141d338ad654431281e0c07e8cc80549', 'ae2431fda87a4b1993dde9f7d5d357e2',
                    'c160b2ecf4074934a21a58a6dd431b39', '6423f1304cf84315b1a4f4c159a8ba1f',
                    '2f23abe04ec3431399c5b2aac4ee4f8c', 'eebc9c9ee5ea46228727087f00243121',
                    '681b6fb616744dc4bcfc2043198dff8a', '8cbb5615e0ff4b448431e1ff84ea0d26',
                    '22c4312c9e5643e4ad67d73e34d525e0', '35f95a03864f492fa3954319f854d539',
                    '60091dabc9af4ae3ad8c6431bebe28c7', '08d5e8831009431aa2bcf9ae62eb3654',
                    'aefceb47694e431db3d0aea4b447f82f', '889ebbb68132431295699f0071853855',
                    'cc8143d64257431d9f1e88f874968878', 'a6583e1ca7414310a15aec16640618ac',
                    '9eb8d2e7650431106eeb1eaf2d301f03', '6ff7d1c0c94a431183119fecd9553d53',
                    'b9c1a431b4947d29e36fc065321ea9e4', '66515a2180a84bfe9a590431f6b3dbec',
                    '3466fb3ab43c4315b75be258f169b05c', '55b98431c0ca447ea9222319ffc8758a',
                    '49584312de2447b29828e4908ec4a045', 'd0ed250134314bbaaf4969d36373e89e',
                    'ec59456871cd431b993175219be00f3d', 'ab3af889e6b34312a04a1095368827c9',
                    '5a26431a9f13484185646d144f708b1d', '2e25d667d7074b0b96e0a8f57714317b',
                    '16163b4312334007ab6c304bf88f19e1', '36ae9375315b42f08bcb7a8567f63431',
                    'e22e7bedb15541ae90001431bd8093f6', '7a55694d3a1e46d48bb11d664312b8d6',
                    '34f09d4318d1473c8ee1deea6ca024b6', 'cf85e1537b1147d5ab145d9943150dd7',
                    '405af9757dd743158b71dd1aeb4b6d8a', 'ebd749d58bdc4431a251435922059b57',
                    '4bc0d57c40664d99aaf0b5043120dc69', '4d855888128343109fc1a7e884163fb0',
                    '684afd1ff91143159fbaf491b5c8b93d', '3cc700df2992431c998adac507911c52',
                    'b1a5e16659134315b420a0ada6c790f2', '61a493f4d73249d6b7fa8078fed1e431',
                    '3afcb966fcd94314a047977f369ef40c', '6f78205424cd4b29a6431805e1a70d1e',
                    '2431a22e6a2c4e80a7f9395cfb0cf2ab', 'd991fa5b87b44313a9d3042d80e5cec0',
                    '999f77552889431bafed9f8fac99cc33', 'c042aa320a54431fa112d455c8ae087f',
                    '4310ef7dc8f4415c8e367513aad6c02f', 'c8f2dbf436064315bd677e61d11011a5',
                    'f431209136e441fcbaaaa2fb6646c309', '50fe8fae0e834ed7a9fc4ceb431e303a',
                    '00d763af001e4a6cab2d3016dd43104f', '0354e48f268e4cccb4544312bee7ca28',
                    '92afc90564314233bd6310e811cef04e', '816284e21f594319b3beb9bcd313ea46',
                    '99e49a298aff4a8aa8b0431985037dfc', '665cdfb431ca4f9099cea05e9093dfe1',
                    '2b6f9eca59794318b56924e7ab3f8acd', '2b79bed533b04313b761714b391f979c',
                    'fb502d431a4e41e086dc10aa117f3b7f', '9e032e7dc71449b49f431936b2ae8d9e',
                    'dc126d7f431f4b44bd743ca7208cf2d1', 'fd521ed6a578494b96a5e6d62443189a',
                    '72c868318cd94311be2c3fe0c28e7ce3', 'b95b184583df4e129bc31431d83dfb24',
                    'be97b8431cf1481c848f08ddc7fff494', 'ba642848f76a431daa71f4b15383db42',
                    '87e5cf9d843146aa9c9f41bd51ee5b6c', '3a54c431229c49e992322d82e32241c3',
                    'f44e5bdf70a24e16bf011bff4318d0ee', '6c7e491b76754e0f8925d16a7d431f2f',
                    '4e437431b50c4780814cc64fd0fb0916', '054401fb8a8a4a17944b310c431d70e0',
                    '6cd605f4d940431b8b883744e0d068ef', 'c15226a8385d431bb19ff4fe4309199c',
                    'bdb8ce61499543109a5cd850d7c4da9a', 'ef81abd0334f48a49e059749ffae4319',
                    '5b51b431530d4b59902ad3c766d1cba7', 'df54077a8f55431eb3ccd8d415c78d85',
                    'af1fb0431070415fb69e32da3959f330', '90f1bcfb138e4311a6758cb82e769546',
                    '011d8e65ef404312a38a988367d5206e', 'c96431936ada4df6a83a9a93732fe0a7',
                    '62e9bc43117c40a4a784cca8a93d66f4', 'a24e6ffd7cc546a892144315e6263341',
                    'ed3fc20ce47f4553a243109be5163604', 'ee4311bca4fc4ee78a056356b10d0df4',
                    '90f1bcfb138e4311a6758cb82e769546', '924315140337438f985614fc603d6462',
                    'e2f6e792f8084311ac91db4f75893c25', '6450a40058074310b2077811f817c587',
                    '0fe57c1d3c4b43199b402ed812f0e1aa', '0844b460207a4f61b431474008bb8ae1',
                    'fc2138b241cd412f9ee3f43129d9276e', 'b8c275a7026d408f9d4311126b2a5304',
                    '34210879431f48b3a6a0ff34a73e1dd4', '6e759a3343104183af71dc752c9013fa',
                    'c97a313c1ecc43109e10a50d0e82583b', '7bfb5f0d235b48a99eb29ed24319fd47',
                    'a86dfe9251884315ba9d9d9cc661e4d6', '3eff92d343144e8593029e1c02f26714',
                    '6eae612bbbaf47baa85e431072e50084', 'edd4bd05378242bba407814f43173aeb',
                    '1b6f0118e7cb43449ab5ffdb62443117', '8e0a1debc4c746f7b4a0104317c984e6',
                    '0e3bb5191b35431d9f20bee391292eb2', 'e60d34314b5f43e3bcd5fa9f85988ccc',
                    '328ca488a89b431cb627a33a7f310246', '049156818aac431ca1067360e771bbca',
                    'a55d8754fb9a431fad2fba620caccb3f', '76777aac1c424f18927b7ff4d4312ce8',
                    '48b4df8748d443108c9822eedec0d68a', '117f063b5e5343109a3bcf28a000ca9e',
                    '18829431bfc845a69abb8d89f207d178', 'abb620ab022b4538b4311bc9018d1670',
                    '45e9c51db59f431cb2cbc128e2fdbd19', 'b97233443174402484dfa570d78b7ab2',
                    '6d1fd53f643d4e5b9b524431b7cacbfd', '4775e031ea3147b889c14316f8ca08e7',
                    '29054317074f4f33b14039f7e8092d54', '431f1f4b303d49cbbc52b07e798bd319',
                    'e8471e24cbb24a67bc0629b343114206', '99041532c337a0bb834b04315e5e83ea',
                    '804311b1dfd74c50a2d7bc6d0acf2cfa', '307d9e84800e433d91619bb5d91e431c',
                    'e3f5a3005a2d4431a6e93073bd1f8503', 'e295d126de3c431bb9f1236f3ee62f75',
                    '06ff10bcfa924319bd55089bdc8ba048', 'bb7628a8285e497cea44319759e01cf0',
                    'eb94313344a8e84b77b39258ffbfb5d0', '4202b3c3805e43b88085cf5060431123',
                    '85b4dfd946244315b76bd1c9c281350d', 'a803f0acd3b8431695b79104cd0cc455',
                    'cd621c86140f4d4184cab4f431bedc9c', '5889dbb077e5431391325883bc6f9060',
                    '84e4d21b158443188d024c8a9e2423c1', '267ef924319d48b98881bd99661b63cf',
                    'b87ed431bbb94dfaa051d19d258d555c', '85c8751ed1e54313828aa24e32047c34',
                    '1e431e4ae4a8428dbb42b7f78a537b1d', 'fd4f918f3c1f431783ea96a96efd6f1a',
                    '524a431c52d74228b5cc14440c67f9a3', 'b82ea76949124be68f78a431ac64d50d',
                    '37971dce36c1430c8b07e113692a6431', '891f913b502849aebabcb061431b1cb7',
                    '3e41e0b56c324310a9ed07d9f1bd839f', '5250c58d54314d49a2c7fb684357954f',
                    'c922eb1431644cdca3c3e384bee22b66', 'd9691431a3564f159c633fdfb3c71599',
                    '2c650ba0b439431bbd6d628d7e5caded', 'd51c516e0431487fa8a60a4c72aaf6ea',
                    'ef583ac4311140b0b151e3ffe9157388', 'c2b90431be5a425aa5f6963d95423412',
                    'e3350af78fcf431c84e4440738400253', '4318cdb9d11649d6b2d4d511a2a5f0b3',
                    '808051147d444315b80f866b4f5642a9', 'f9d32d07f2744317827b430d734197a7',
                    'ed8cca8925114314ade4cbd206824a8f', 'e4cab965328c431bac0433e7278ecf15',
                    '7be8cf1e5dbc49068ce60df2054312b6', '3f0431f186c9440c86d315605778dba1',
                    'db349b42d12d431b982bf19ceb59a8d3', 'fc09d94440c84f62a74318f5c2771b54',
                    '1ab49fd9cf9c457684431b43ccbb8cab', 'fb78078c34e54fd1a6f7f48431f86747',
                    'f08479985efb477ab431dc570c989489', '8d26453e0fa64ed59164314fbf0aba61',
                    'd3d40b41a10149bd9c431a41cb49508c', '20cdc5f3b2c2431aa36a0df547a87c60',
                    'b5f2e64a8c514310b8b1c247e273332e', 'c788a4cdc4b647f2a4311eff169cda3c',
                    '5443156e5acb4ea7bc456bcfec2f7a48', '94bbc32191d64319a05f38e9177440d5',
                    'd3efc93c3772431293227d2b34f7c628', '30fa9d990c8b4310bb739ec64bdb2e58',
                    '87a230008f764311aa975b5590148cd0', 'd042ddd393db431f81d8f64ea162b96e',
                    '862ce43140794a20ade3b8064806c0d7', 'b0b0f30d62e5431bb45e865cb88d84f5',
                    '410ba0c3fb90431189819407175ab6d4', '4d431706c8084a48928809699a9e1fe6',
                    '3323aa9b78074317854facecfbd935b0', '6d43180fc143423b95b78d462252c7a2',
                    '9ef878253cb34315898b704ed73f921e', '075d7dc9f514468e9531f14c8343171c',
                    'e70bde8fb1894efaaca9a54c43196ff4', '319598f608e1431ab288a7486dba4229',
                    '0a6632ac2784431693745fe5ee84d024', '0e05af4312494f3eb8eb76b07a5f111c',
                    '431456e5d9cf4767940863860f3b7378', 'e1644ad7cb7143148eb3b661566109e9',
                    '7431ea2c69634bb45e2cbd462672e462', '52ef55932b7c4318960f5c7182b187c2',
                    'd1b9d953431e45d6b6a88dadb367e19b', '48d9691d39cc8f931eae2431b02da9ae',
                    '125f1b5978b54bd0b5b4319a59a50284', 'b5363af427ac4150adf31b1a053d6431',
                    '0eb279fead8d4431b9914ed90a7d3996', 'b9c1a431b4947d29e36fc065321ea9e4',
                    '844b7af3f1a24318a81aa95bf2039446', '1b98739112e34319a364fead0628e271',
                    '855f8d8431364e4087e779b9a827b976', '431786d8d1e01fc76a2f693460b829cd',
                    'd2b39b1431834a52b6afc73b8951292c', '40d0484070ed431f81d2235544358c3c',
                    '7d47c7e43baf43129fe1c74d4da93c46', 'ef510bccb3354e6cbe7c94311aa1bc73',
                    'ee82b2bcf85c4cfbb7af4b67c27c0431', '2b9dc517c1d8443183b060453af9a2b9',
                    '85171c11431b4cb3b9071c5b9e03dcf2', '093938834ad0431fbf682657b87aacf1',
                    'ec2aca32a0bb431fbeea2b7ad1921769', '4e43152f8758451b8750b1f1cb52a022',
                    '0f5af55b9be44c26a95ac43125361be7', 'ae3c575ddf26452d8acf94315faa8b9d',
                    '7c370277f0bd4678bfefad3233431467', '9276f07206964317a411bc0f1a7d3c94',
                    'c21727dd064a40889f299a154d54310d', 'a1ab79d843174804a17f8bd2467d9023',
                    '129517d1c0434314ad59f04f2a1cbf61', 'a4ce431770354a3cbc49f1493b5e1b9d',
                    '04b6a573f922431e9cc9cdfc812d9dfd', '20417c08135e43179fcbb95a4499ce1d',
                    '62e9bc43117c40a4a784cca8a93d66f4', '633148c31d0a4315a8b4a2736f1e60d6',
                    'efa870f714314ee0b63596b0e44ac530', '5b8ddaeaec3e43168a8729f7a5cd86a5',
                    '1204aadaef8c43139f8a51021cd414d8', 'e20b6223413748d2834312be877ba374',
                    'ac483eb6320648918431e05116f5a8c1', 'cc669dcdd4d8431092c7c7401a4d9f2d',
                    '201f9bbf6cb4431d9ba464cdda6eb257', '0d68e5ca1dad48cf9431179f1e36968b',
                    'f4b617397bdb4448b4312b1f98829a8c', 'acc79c4312654f9689955b9132fc61bc',
                    'c452319119c54310b8dc9a62e3247ca4', 'c2ecda73913345248431740e5f60bafe',
                    'ea8d86469e9f45baa08d431e9c8b6b23', 'd5b61478805b4318836a9cd8f44032c4',
                    '20de73caeec04312b29ae8d6115d7616', '1d9f9f431b33427b9659ebaf5d77ac01',
                    '8609926508c84e8ea3deb43fba431817', '1d172d3eb4319cdbd67797a90bcb05c3',
                    '3dcf0fbe4abe4316a3c434511dba5abe', '039e8b2820f745fd97950c03ca431427',
                    '389814682bce4d37ab04316da2caf0f4', '27c2344071f1431486105ece315c4086',
                    'e4d4711ddc2747909372fd431a90754a', '17499c35be04478e9a4b881cd71f4318',
                    'ce9f1a4431c745d1b0aa24d0d60978f9', 'e4442799ad8a46649943166292059f38',
                    'a14315dd5d564f6999d011093efa667c', 'a5c6a75236ca43169ecc7100c160b390',
                    '3ef431c209c1c0f1a4ca466de1f349f2', 'cff286c8312a4431bab7afb0f40a6ce2',
                    '31814bea9ab1451fa1fe2b55f431fb18', '2e77e5bc4313472d9f8013f92a07ab8c',
                    '291d191779e24319b4b5673cb8e9e675', '8327f305e5664baba8e43123ba8b4967',
                    'e03bcc251f8241c2a9433f431eed4e1d', 'bbc61b4319a04f11937780d75983b985',
                    'c3307d6043164d239d88cb6c0626911b', '9a29457021c64319829705a17a0ef610',
                    '9db3a31b6e5e4486955804318b67f759', 'f0b88ed245b64431be33d980ab6eccf5',
                    '58d9934224314c52811f560ae154abd1', '189d49e1509c431f97d42ea147b71fcf',
                    '9f75a7d45870469e8b42dc37c6fe4315', '0418351454754cc0916c431566edc3af',
                    '6c006320123843148b364d8f0b0b93a5', 'f4cc5b1be42d404f8431cbc7abb620e5',
                    'b9ea5f6865f34312b03f1dad07750d28', '56bc074b13674aaca77982e57e14319b',
                    '92a3a13ba840482b8065371ba7a54431', '56b97278754e4316bf3b9ba6ceb5d98a',
                    'd9d4314f0a8a4def918ac85d50974b6c', 'f59b1f66b779431aac5bb7b02174c002',
                    'a5f0f0c05d7541678ca2431c3b095676', '1431bec96c784792b71128fd8cdcebe0',
                    '8a69892003ee431eb09a193042d8a800', '1b09c39eac744d469a36d49676743132',
                    'ec6243191109465e9860072ae2a93b7b', '3598926606044319875f417452d65263',
                    'd537852129504313a738f80ee4d87550', 'c332c533934318dc3633d1afe4babb41',
                    '72082ae95b1a431090ca3d85b1f97449', '3b328b710d99438da28431bce5f4cfe2',
                    '4ca3d9f35cb1408da54318fc3c0e8de7', '90cfb886848f4316af1a728e9a103848',
                    '7c370277f0bd4678bfefad3233431467', '5f521bfa43144aa0a628717e57654c19',
                    '8eceb7a96d7d431a91955b27c2a876b1', '53a42c666fc743128f9cb2af34d74c41',
                    '7c45519101934d2382155de304316827', 'c5839f7db0c3443193303d1df24f26ee',
                    '7cf985aed9dc431693c7e917e24254e7', '00e2f8381417431e9545b7d94c68cbdf',
                    '0f6a57240f664b33839d928e3431dcaf', '0e96544317324cd7b6718da499296ec5',
                    'a6bfef483c59431ca5497f596db69721', 'a7014a60fb544314aea2cab58e8d2bc2',
                    'c21e2b475381431382ed1495a42af717', '0ff002431a2865c6862067f55daa58d5',
                    '77307a43100e4d3990d0adbeb131f6d8', '5a8431b0f9b24a66952f61a1009f0504',
                    'c77d1eb389474310baf27aca6a5285e8', '13defcaa431e4ffc9d93986dfb7d5978',
                    '6cf0fd2e7ff74314824737031571d39d', '7f8b3a4e38314ebf901ad724310dcb21',
                    'd74316d4ee7849e091827ff58656dfd7', 'd431a1a1443f4c668a96c89cd221587e',
                    '74ff8a6f76ba4bc3a08e5543111e2e77', '7f431692d8084559b88dadd6dd10ad60',
                    '0ac52772b87e85b844da293da4310a3e', '35b30c19ffa3443198110c1d59a0df43',
                    'db99431a4b634318aa91565d4375916f', '26a1a38344894812876ba431497dd20a',
                    'abdd8b6588c3431ab81c369d23f3d289', '6f806533c8694313a3dbf049869fee39',
                    '535652fa76444313b63720a6a444d8f5', '9eba92827dd14431bdc918a004b9cf33',
                    'f4315ad3693347f48830206c1a43e5ac', 'c00dca945e334310bcdc906d2eeb78d3',
                    'e5e0ab87157e431687cf574e0accf89b', '7a4fdd431af846b49492da36278b6e29',
                    '1f97119111aa42b5ac9b4431c4c91448', '1ff364ae4876431291372e73c58ab50f',
                    'f89545431c174194bfd2e3be6c0cc820', 'f814310460f543d5b1ddba921db70ab1',
                    '2fe8a4fc56574312a52658ff5051ca52', '4f9775d9f4b14316be8eef7e7ad575ff',
                    'd4312354c7924adabb33a7c4d7f329fd', 'a431a8b6a3ec4cf4b847af5eef8d1b8c',
                    '705c2a7c437343109f7a0847b24ce8c0', 'fda6070f668545f4be36bdb4317f2984',
                    '528c70341a354319ab6b6ee74e00cdd7', 'fca3670db944431592692a6b0336d4ff',
                    'bf651bef83b3431db2801da18a1117e0', 'dc3802c0e0724bad99c39124314110fa',
                    '609aded578e44e798cf4376043100ecf', '770e256f898c43179bbf90746e3e8490',
                    '43009c204a6f43f69e492ee25b431ffd', '354310a756a94f63b8d8e1a22d425472',
                    '5b5d3e90149043159145bbc3cff1d51b', '296569adb38d43139975193bae9460ae',
                    '6bbdd36c950845898301faf8b21b8431', '793f53bc5cc74f178bb9ea04312035bf',
                    '2431026168cf49a4a77a916e45da034e', '10d8cd431983954a9480c17e933e9b23',
                    'bec265df43154c45afb4bb65fe636bea', '4cfc91e4283b4315845019f89b0cf071',
                    '0187bfc461c24313a7e2cb43bf66d4e1', '30574522d32e4d4ab4318cce3be8f35a',
                    '8ed4503237c24312baea3f95b2f8e122', '1c1aa4fa03ff431e9e04a26465296c67',
                    'fceea0070f714c2ab37771d431a1dddd', 'fb502d431a4e41e086dc10aa117f3b7f',
                    '1c0b732700f6431688a3399c75cf316b', '55e376274f86431ea7a6213e36bb7346',
                    '9364de8a4319429086c7b15a6e4188c8', '380deb40d6b0431db12f67a3a6fc2df5',
                    'd75c04b76431473099f73941a514c919', '94314e91dee14db59467ba2db2b549f9',
                    '3c3e9e11a4c9400f82c7a17bc7343180', '7daeba34984649b18a240de03431dcf5',
                    '962257090972443195d69b919b71f54e', 'd0e02e2f6fd043168a273bb82230b1f3',
                    'b2d771683c9843128de10c869ed89619', '66e478e431c24b51889d7f4ccec63bfc',
                    '39e3f3c4634d431fbacc526f0e1787b8', 'ee8bee24315e464596588a8e3d89904f',
                    'ddf3b2736f994c09b4428557431371f8', 'e0edf0d39592430ab7598431cf69b2c0',
                    '2653a5d9e3ea44318f246f9a9f43963f', '02d5c6cc8eb14dcf8431d029e61a663e',
                    'e2968985e35c4311872a91653d64efd4', '72d43f2def5c411e9704315f2381e509',
                    '6a7b6123b450426bbb53772fcfe43193', '44fa4315d83d4c43a65b1cc2210c561b',
                    '87b4316120c8450693cb44f25286eafe', 'd103d1d183ac431f99f23ef61b93eebc',
                    '4d7054310cfa7f08b7dadb4070a0e3f6', '1a2bf585af39431caeb08d88e59ec849',
                    '1d38ed180aab431a93516e796db539ac', '9138e4d05ec848afa4548a7431d09dfb',
                    '91d893431198481280c240499c66136d', '39f8c8501f59453fabad075d1e4310e8',
                    'cfc81488ec874317abc3a12348c42ee5', '125af253db59f475a594315310fbb39d',
                    'f07e31ef4e00431b80bd327fc14f043b', 'f843136ed74e455aa2577767f9098586',
                    '9cda595ca3a34431bd918e0aa0ccba8d', 'b45b04bf07cc49b5b60f7df5643190c4',
                    'c7431cf33d584e13971a58a2ce650cd6', 'a092ecf6d963431eaaa171d81b3ba06a',
                    '421622fa1ca0425290b0e401f043135f', '74c5f93ea49249b2b1cc0a56dfee7431',
                    'dc7a5152370840178bc4119f86674316', '5b4315aff13141e1a7b8f78283ac4bf4',
                    '1d04480290ce4028aa0431685c83712c', '1254a11368144311858a0eea1e83caae',
                    'a190e33184e5431896d2cf9f07576157', 'a9ae89dd431747809d3cd6560d9f7682',
                    '2296ff71fa09431ca4655887f570d195', '76cd4311494448de811104b80c887506',
                    'eb9e69b2bf0043148159705f96acef20', '9bfd6168ecc64316ad3512605fac92b9',
                    '1ff364ae4876431291372e73c58ab50f', '7abe8e07180e4319abbc8cc8cbf78427',
                    'ef583ac4311140b0b151e3ffe9157388', 'f0dd4314fff84a028febce2379979fbc',
                    'd5b61478805b4318836a9cd8f44032c4', '08ee6431abd336a8a8dca18b4df5072b',
                    'a41acea679a14319b39809ae6f906f0d', '6a2eb4e8def644319bec575e13c272c0',
                    '8f3055cc61c3431dac344dbc84918e4f', '5aee555431fa47a6b4d51e861bc02dec',
                    '3684317cc5474f90af1c09fbd844ce7a', '5fb8752b3e934313a4443ea7ff11ae9b',
                    '50b3c0e0697843199a427f6287d4f34e', '037f327ec8454312a49ca616628443df',
                    '92bc79b9de03431d95f30e637e43cab6', '9f59efb5730843189a545c4df72efb39',
                    '9b832653ad7d43169d578af88a02a46a', 'fa05060d1b5a431b87c39c9243d62713',
                    '67b0b8f0f7c44284a3e06043136e30b7', 'dab2faae431542919b535e6b9a6c2784',
                    '80a74e3d9e2d4ad48ae022a2431d0ebe', '75dfba8a2e4d4fce9b87b24314b5cf72',
                    '42c0d4318eed4a6ab5e68aff8e4cb82e', 'e3f4afe18e22431e8d87b1180ac07551',
                    'c460be572fdb4d62a8431837f7c9021d', 'ef4a0c43159a49b09c5d09bdf86e4de3',
                    '5ef8cb036ada465ab9804318864294c7', 'b337c30546cb426d8431158bc93c8576',
                    '70609c1c16334e46abe90b74314d0ddf', 'ba2fba22543b4312b451ca251301e330',
                    'bfa0bdb4f49e43119bfa517c998605d7', 'caf8851243184257b9e9555ebbc616fe',
                    'f46ebb95ca8e4317b6c2ca6132dc84b5', '3a756058a703490fa4313ebe5269b6d9',
                    '26342a67e77e43128b39b121747ab3d7', 'c64db1a1b60c418f986c563a8661d431',
                    'adb2a384eb41431ead277deecb649dba', 'a534cbf3d42a4977b6b8aa6174310e1c',
                    '1d7c9431504245c2899048d74f867ac3', '9ff7d922c9124473bff524318da0591f',
                    '85152d40ffe2431ab9bd4c88a6447d24', '8d632b04677d4b5894c44f4312c86dea',
                    '6ca0dd71431b4102a436360380b5df39', 'e178887c2f57409a9eae7431bfe7258b',
                    'e0c6c0b7262b4cf2aa91f3743119e538', '418978df61c4431fa62313684f172cf1',
                    '734beae5ed4340c1ae4f424311010c3b', '488cb0cc00164b62ba4316c7901f6cf0',
                    '1db1a320241343169c4a5767b29184be', 'd7e7310d431547cd8106518e8d9a7471',
                    '74c5f93ea49249b2b1cc0a56dfee7431', 'bf1cc24431d04052be1c8d222adf39e1',
                    'da6b3a8335abb5431d1d3e19d2f24e5b', '4369431e8e7f41eeb4e33b54cb233dfe',
                    '76d87dfaeeb9407f975c16489f431e36', '8dd1d677f6d646eca7714417e43113f9',
                    'a19346d134914378be88414316b35c33', '04e1d43157f044dc946d5753301bcbeb',
                    '523431b0e95a409ea288fe216a714610', 'fd7af0493f0e4318b2d39f1f67907b78',
                    'b61ea16b93a5426e801204ddc6496431', '058ad1af60814310ae206aaf32356d9b',
                    '902ca2c7bc2f43118d128e8ff0f09123', '17085431cb80406e944bf8bc3589db02',
                    'd32a6b270f8e4310921aa5ff27613073', '821145940da6431389485b8c97911509',
                    'ddaa6772916e4f5bb877c43143c5594c', '5385a431a47f4f6fa6bd9851f704f0fb',
                    'a8a08d2e45ed4318970d8dc8dce73b42', '9dc189ba7dff4634a0ca111204315cd9',
                    '1c1aa4fa03ff431e9e04a26465296c67', 'c568342ab2d1431cbb4086fc8d43081e',
                    '189d49e1509c431f97d42ea147b71fcf', 'cdf3274809c248768b6b0431d57a2f94',
                    'd76ef02ee413ba431e3ce4e273f33ca5', 'ffd0d8d830b043198e91b7f2bdc867c1',
                    'bbc99421ee48431facf03185964709f7', '650090f3740d4b58983baf34431ea82e',
                    '2d7838d11eaa43128af596495a95d206', '9447006b65284719b94315fba2a8c80b',
                    '173292a92e1344c5b8431803b8ca461b', '9e9deb1d3dc94312b1fcb7b2dd1cb9f6',
                    'ef217e02145e4316b7f19e38f96065e0', '0c435a327d5843109eca47d6aa739eb8',
                    '43e067194e07431a8617cdd68a9fd78e', 'e42c128a70aa4a7abda1c14b707431b1',
                    'fe44ff929bdc446ea23431277c72577a', '71cf814650d64a059946185f33fe431e',
                    '8397ca2725da431b91f34e175794f3b8', '3b7bb431cd7d49a9bf32ebdccd17f1da',
                    '07f65f0431c445e19a708adb305f1cef', '2613570efc21470da387e431fe34402c',
                    '957db87702e0431a8c704ace127c7ff5', '57361726b6a1431f8b929e2ad513174d',
                    '8eb9e323b80141c6a937394986edb431', '80881c02277c4a40a5a1421dfd6431ee',
                    '64df3375daab4314b6df8ed8a3798c48', '0c9cb5e84dc243189eff337e87859f28',
                    '6478ab3008ef4e9f89ebb431ea4b947b', '9450ab02a4fd4314bcc8dc612f9377fb',
                    '9276f07206964317a411bc0f1a7d3c94', '53060c4fae0647a4803a7de24478431b',
                    'eaba99637e1241eea431d68805fff483', '75d1343139014cd28818a58ceeab25c3',
                    '07ca39abc19c4317838b750be296323e', '5f8e94684031403c8a6d4313ecd65f1a',
                    'ef01a1484319441b96aff5b9c98d2e83', '405e549d2125431b88a09a15a7a696cf',
                    'db71a4431bcb49309881e2f28e14b9f3', 'f12c2c912dfb44648b4318b57bbca82b',
                    '7f10687a05424af8b431e2d5807ec3c1', 'c3d9284da2f547f38c922312d659b431',
                    'a4d50dfac533d4cfa7c4311b9f02d4e0', 'bed15551775044408a30ecf2f431e8eb',
                    'eb2b431827d2495493edc50fc334173c', 'b22b9fdf59a1431d8da2628ee45759ee',
                    '6fa48de5e55d4311989a0b07a838f8f9', '5623e29bf034431d9beb901c5aab231b',
                    'be784c482753431fa654580249749b0b', 'd5eeec9431ce403882efb762d0d3ac87',
                    '86431930fa174bc9b5a47accde77053d', '004270d431f045e6962d202f55509c2c',
                    '3f9b431dccb24c42a5fb97db3cff6433', '416ab5b5d144443192b90b39039b1208',
                    '0cae1a8c431c4c20a6284bf7deb54136', '3cbe075cf88243179e196da441c5754d',
                    'b26ca34d0ea34d9eb8431c7ee377a374', '7a271091315f431db8db5e6312138e69',
                    'c3266ac60d6c4f8e9e8157bcabc431bf', '1edf2431cf764e0f99d3b46ae7183d61',
                    '41dc1d1516c6431e922e075f57c2f2bc', '7e24fba0af3e431a9dcf96dba8e54c1a',
                    'ca2af431ad734843a0b95b59ff3af09d', '118d3424313740f89b65217185994179',
                    '9c41b9fc3ca144e3bfeb3431d9cefcaa', 'ef4356010c83431f94f8e1c0a505b6e0',
                    '8d7793b3670e45c5816449308474312d', 'c83a211226dc49b4a904315f2a2c2965',
                    '843132d5fa144baba525aa2dd8e7387e', '3f3cd95091174084bfd7399664311373',
                    '63bda1f280b84e30ae17a4314bfb5659', '62fe42dee91640758943197ea9510c31',
                    '96d5aaf7ac1c4313ac8292d879171f31', 'd5a7ca9547b645d6a4a4359598e89431',
                    'b82ea76949124be68f78a431ac64d50d', '9b9b23ae392b43149cc386e633e31814',
                    'b22115de95f843178f05d07cd843e405', '78a0cb2cd5984314bfcbd0cb39432778',
                    '0356661e418a4b269854312483878aac', 'fe4a0fb2aecb4756a8858e3b57851431',
                    'a3a13eb625579d7431edf9ee44042420', 'f431adc07b1b4cbd95617602eaf6e5c3',
                    '9d384ae6cf6b4315a4ee657397c9876f', '49d431c630a2435389cef509ad3b84b2',
                    'a4314f9da09f400a9682ac2a45fbb95f', 'ab0c066c5a0a431fa9993d98ae665cda',
                    '95f2c84c3569431cb8ed467adc739c39', '0dd3c90e58b04313a7546cf8c005bdef',
                    'bd9a716571431f07d64f20b7e2e25f54', 'f6c73b005b4b431b8c6f98f13e1ad47b',
                    '65850835ed09431db795778520866a9e', 'a870be977a1a442ba11e0edb0a9ac431',
                    '4a6f503e1c764eb1a8c3634311634d68', 'cf4a1c4d0b00431b89a66478676290db',
                    'f08106d983e44311ab8da4e0643bc41f', '9ef70870431847fc84ee926292264889',
                    '345b9b1d4f654b16b3abd4621a174318', '806f054be0e04d79a479237bf0d431ec',
                    'f17189f231364319beed1f9989f648f4', '24b76d4c0e0c43129524d5714ca54956',
                    '44d8b03e3c75431fa45511d149e09a66', '328cbeabb3676721e4d5e6dd0f243166',
                    '834764b431bd49598cfc50d2c94293a5', '1f6c35a7b38243118650cfa0f6fe834f',
                    'ddff383ead2c49409a59e5b2d4431021', '78620ef1cb214ea59a0961937431308e',
                    '1a68525cf705431bb6c4d475996aab30', '493a82bf25de431bba4d5167d06e81fa',
                    '7da1c923f96ff327494d5b3d123431a8', 'a283f8e96bd045f9a83e59843135a5cc',
                    '5c0a5d9658654315bca93247ab1714fb', 'e2275afb10614315beb142ef29fb93ee',
                    '51ab2449037c405780f7754319ddc443', '3fa1811fc699431f8bd34a5dd990c751',
                    '821145940da6431389485b8c97911509', 'f431209136e441fcbaaaa2fb6646c309',
                    '86d72dd793a24e63b431036ac9cc090b', '70ce79b7072943188755d7683d3eda5e',
                    '4312ec92c2cd497fa0e3dbd6a38e84ba', 'ab43143e38734298840a53e085ddbe85',
                    '3f95446793c54312add6f735735a2af3', 'f2a7c309d33543169491039a328e9f83',
                    '249c431fb2fc47a8826e2954261129d2', '033b48362c4d431c9096e582f6200b3d',
                    'e796e5b086a04c42a0bcc41f431acdd4', 'e2d0daaf49c3431cae9e06b1a27ccb79',
                    '11752f4c88d04312bcae9e40756c670c', '50e169431beb47a59d785928c00a82e3',
                    'a0015bd9f2ec4317c96bfd124f6f699d', '7c86ac83fa75443197c7c4daebd7e987',
                    '4a3fdadfd91b4316bc3229486e7e1f24', '1f9bd69597ee4317817d9ac3af7c7329',
                    'c73f90f4c2f4431fba068dda4e63a5e0', 'a7121307fbb84913814313b57a1e542d',
                    '30e5407b43184af299240c940ff1e4c2', 'c216029a035448768e9991b41344311b',
                    'a87f2a6d6dc6431496c1999ed11231e4', '84d85431590b43f19cbd307d596fcf07',
                    '1d6c29ef8e98431dba5fb36dce7b1ec0', 'b9b484c75b804e5d851a43134453b673',
                    '156226f4310443308386f4461da35038', '7c1d7b40a179428cb56443121fc68c7e',
                    '1f5126c2431142d0b8404f679acf7da5', '7e97ef904310682b88e1b849ff6921a9',
                    '9751835fc28f4bd9b8ef33249431b01b', '3f99e0d0861e431b85c4b37772d44fce',
                    'c8b0cbb854ad4c4d921f3b4431df0a39', '6b2e848239c94431a6f9263423c3565a',
                    '7c5043157dfe115c63545e03660f8dbf', 'c6a64311785441fe9f1fd74ec0933c77',
                    '4937e192852c47ce83f7e054312615bb', 'f9431beff7a94215aff2bbe80a51af32',
                    '5bd1ff45ccb4431d932305b1772b9781', '8b3a0236dad7431b9ae1773f60d3dd64',
                    '64cd5402e53249c6acbf19431f61fcb4', '44e995a6431144d4b3702d7f9e263098',
                    '004270d431f045e6962d202f55509c2c', '123377ecac0d431fbacc6ecd70baf539',
                    'dde628536f42431f84583f587adc274a', '431c0d506b5341949468b39b9e798758',
                    '26ea9f6bf21f4bbc87fd2020a570f431', '3c080265a164431ba053accc96000b4d']
        duid = random.choice(all_duid)
        # url = "http://172.31.16.27:8080/v1/app/{}/device/test/event/recent_num_sticker?range=0-3".format(
        #     duid)
        # url = 'http://kika-data-blau-web0.intranet.com:8080/v1/app/4e5ab3a6d2140457e0423a28a094b1fd/device/{}/event/recent_tag_num_sticker?range=0-3&type=hola'.format(
        #     duid)
        # url = 'http://172.31.23.134:8080/model-sticker/recommend/popup?userId={}&tag=lol&sessionId=123&language=en&type=0&country=us&mod=not2'.format(
        #     duid)

        url = 'http://52.43.155.219:8080/model-sticker/recommend/popup?userId={}&tag=lol&sessionId=123&language=en&country=test'.format(
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
    # host = 'https://www.baidu.com/'
