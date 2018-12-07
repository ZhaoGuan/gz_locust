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

user_datas = [{'duid': '20181207-6a06f180-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9f395119a4064d24a7968c4e98f48b8c'},
              {'duid': '20181207-6b1499f6-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a8ac10a0beb94762a0fc9540af6714d6'},
              {'duid': '20181207-6bce83c0-f9cf-11e8-bf1c-ea00e4d87701', 'token': '6669900b4d7c4e96bca55321279ac675'},
              {'duid': '20181207-6c7a6f8c-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd3aec2d35c4c4113b52328c9af8758be'},
              {'duid': '20181207-6d265cb6-f9cf-11e8-bf1c-ea00e4d87701', 'token': '0bfdd0673f1a4d90bea2b908b366054a'},
              {'duid': '20181207-6de1d5cc-f9cf-11e8-bf1c-ea00e4d87701', 'token': '27fce80f820e4792a37093a30cb205ba'},
              {'duid': '20181207-6e9d75ca-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd1ee0f34c4e54651a84f440d9f313c0d'},
              {'duid': '20181207-6f3965ac-f9cf-11e8-bf1c-ea00e4d87701', 'token': '470be42181e34489aa2bcaa77815fcea'},
              {'duid': '20181207-6fe57bb2-f9cf-11e8-bf1c-ea00e4d87701', 'token': '88e08b2c80404ee29524a35c5920967d'},
              {'duid': '20181207-70a0a608-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f2d85a3805e2474cb6449503fc7b9a72'},
              {'duid': '20181207-713d14de-f9cf-11e8-bf1c-ea00e4d87701', 'token': '709a968e734d4a5fb4f0dd4c3080c8e0'},
              {'duid': '20181207-71e8cb12-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'cc041b3126104a9295868f4ffbad9dca'},
              {'duid': '20181207-72a3ba94-f9cf-11e8-bf1c-ea00e4d87701', 'token': '6e55255197de417093dfa806df68eebe'},
              {'duid': '20181207-735ff092-f9cf-11e8-bf1c-ea00e4d87701', 'token': '06350a378fe14c0181ab98b2010e01dc'},
              {'duid': '20181207-7403f160-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a02927987798472490557a07c7e48fc4'},
              {'duid': '20181207-74afeae2-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e56b9a48d6a44abcb39ef4ad5cbd5f68'},
              {'duid': '20181207-7563a5f0-f9cf-11e8-bf1c-ea00e4d87701', 'token': '04f8bfccb57d428889fc25291165220d'},
              {'duid': '20181207-760f3460-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3cc52b3df925452caf41c457c2a5a021'},
              {'duid': '20181207-76cb3c28-f9cf-11e8-bf1c-ea00e4d87701', 'token': '53a7231c2a424732a2bdf9f300a152a0'},
              {'duid': '20181207-7776f69e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '09d1d0edb7b84f1ca5ff3a93b5d040d6'},
              {'duid': '20181207-7832754a-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'aeefbd785d2e494d957c97e519eb1542'},
              {'duid': '20181207-78edae0a-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b69a7847af084fdeb0fc863439bfc4eb'},
              {'duid': '20181207-79a9430e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f972dd17bddb4be692d095d68a3ff167'},
              {'duid': '20181207-7a558272-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3090e91efe804603bf70640aae30d89e'},
              {'duid': '20181207-7b10f408-f9cf-11e8-bf1c-ea00e4d87701', 'token': '64dd01b7b8664784a0fa0d39716dffe8'},
              {'duid': '20181207-7bc4e436-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd85dc8b235f445aba6c2ee615c6cdecb'},
              {'duid': '20181207-7c7851f6-f9cf-11e8-bf1c-ea00e4d87701', 'token': '24c49d4008634643a617ef64865976b2'},
              {'duid': '20181207-7d33fc6c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '227e96d1c478448bb96b5458dcac9133'},
              {'duid': '20181207-7ddfa792-f9cf-11e8-bf1c-ea00e4d87701', 'token': '8324affe7c554dd9b9c7274a97e9a16d'},
              {'duid': '20181207-7e8b8cec-f9cf-11e8-bf1c-ea00e4d87701', 'token': '44dd676ab1b146138ceb58f5b61f1f9c'},
              {'duid': '20181207-7f38d618-f9cf-11e8-bf1c-ea00e4d87701', 'token': '81cb85be32aa48d6b60251bc439a89c4'},
              {'duid': '20181207-7fdf5790-f9cf-11e8-bf1c-ea00e4d87701', 'token': '32e291f380a64435bd13049408a74255'},
              {'duid': '20181207-809eaee2-f9cf-11e8-bf1c-ea00e4d87701', 'token': '6ad1174e7e75454dbd9d2a035fecd63c'},
              {'duid': '20181207-813b18a4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9bb28bb33efe4bbc953aba0418e82cf7'},
              {'duid': '20181207-81d748c8-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd3ec423db0bb4864b303d8f76cbf0b3f'},
              {'duid': '20181207-8273999e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'fca164f700c94392a121461a65de50e5'},
              {'duid': '20181207-830e4ee4-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'cfdabe93c5604b1d989d7dcd1170f0b5'},
              {'duid': '20181207-83cb13da-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3f3f5562956a40a79e210ddbae2cc2e4'},
              {'duid': '20181207-84773b6a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '22b3b5e065f44801a7513d5ecb55f8bf'},
              {'duid': '20181207-85137dd6-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'bf80e81403834684b525815fadc557d3'},
              {'duid': '20181207-85ce9a26-f9cf-11e8-bf1c-ea00e4d87701', 'token': '31594ee1a14140d59582b81f3cbf841e'},
              {'duid': '20181207-86739288-f9cf-11e8-bf1c-ea00e4d87701', 'token': '77054c80e386444d83ffdee21f2b3b79'},
              {'duid': '20181207-870f43d6-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a368c060fb1a40c69fcd444f53d9a28f'},
              {'duid': '20181207-87c30560-f9cf-11e8-bf1c-ea00e4d87701', 'token': '2a8d852706aa4cafa3b7c4b35cebda28'},
              {'duid': '20181207-886eed4e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '88d11cd210004c25ac8bd2c8b7044b5e'},
              {'duid': '20181207-890fa626-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd213a33ac169485bbe1afd21a0bfa6bc'},
              {'duid': '20181207-89b2de22-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1785b6b7cca84d7899647be3bd329d91'},
              {'duid': '20181207-8a62d71e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4bc01bbcf9f64401920815c88aa3f715'},
              {'duid': '20181207-8b07380e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '8e97c144dc49493bb210ad058b603783'},
              {'duid': '20181207-8ba360d0-f9cf-11e8-bf1c-ea00e4d87701', 'token': '35b690526ceb4d0b8d8703d3f8696773'},
              {'duid': '20181207-8c471626-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd08a7a0d3bff408ea594b1224ed3cf13'},
              {'duid': '20181207-8cf2f5fe-f9cf-11e8-bf1c-ea00e4d87701', 'token': '2fe6f55695084b48a1130867103969a3'},
              {'duid': '20181207-8da77d80-f9cf-11e8-bf1c-ea00e4d87701', 'token': '6b775c2d73224c9fbefed4a3bacb1dd9'},
              {'duid': '20181207-8e42c98e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd933dde000714a209c2bc2e25ad4f641'},
              {'duid': '20181207-8ef6c060-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f4f41ff079514d3598665c93fa9b096f'},
              {'duid': '20181207-8fae6bde-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a4f9187cd4504537a21a64243ccada2f'},
              {'duid': '20181207-905e0468-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ae8c7056b729439a81c7a17c924c6921'},
              {'duid': '20181207-90fa1394-f9cf-11e8-bf1c-ea00e4d87701', 'token': '56cdbd1b22e4419c8ac22ad00cc08f23'},
              {'duid': '20181207-919657f4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '044a395d4fbd47b69f34cbbbdc60cc4a'},
              {'duid': '20181207-922f7fc4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7ba7e57c89d64e06817500952f2dd83a'},
              {'duid': '20181207-92ceec9e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '413ac6cb7432452daccae190e46a2b6c'},
              {'duid': '20181207-936b6b1e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'aba142ade562420e8d991e29b24a3d22'},
              {'duid': '20181207-94073936-f9cf-11e8-bf1c-ea00e4d87701', 'token': '5028d0ead5ca409bac3fe3acec5e4ac1'},
              {'duid': '20181207-94a3ed8a-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'aacbd875c0a349b5b2042827038c7248'},
              {'duid': '20181207-953fe58c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '345e08fb36334bf48bcf4f73020c891d'},
              {'duid': '20181207-963821c0-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'dda8ce38e9e14ea09fa68b4e3565b769'},
              {'duid': '20181207-96e60e20-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a538b14a18954324b9eeb60752a5c306'},
              {'duid': '20181207-97927e9e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7559914d2cd94d9a9e284197f9b7c03f'},
              {'duid': '20181207-983d9b80-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4b38596a9ae041c38a90dd19726435eb'},
              {'duid': '20181207-98da0e20-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3a185b74b5eb424aa2c1f86d4417a04e'},
              {'duid': '20181207-99a4db00-f9cf-11e8-bf1c-ea00e4d87701', 'token': '2ff9125fc897468a8ecdc066735bf821'},
              {'duid': '20181207-9a605c5e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '0c1a114b843c4be3b2d62d9b7247ff3f'},
              {'duid': '20181207-9b0c833a-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e9cf850bac0d4f8996bd2b2495d1b1a2'},
              {'duid': '20181207-9bb8a566-f9cf-11e8-bf1c-ea00e4d87701', 'token': '5c3c430500de4defb0dcf6ac536f4015'},
              {'duid': '20181207-9c656a30-f9cf-11e8-bf1c-ea00e4d87701', 'token': '894b8dd8a0154c03b6de3945a803c0d6'},
              {'duid': '20181207-9cfe2ee6-f9cf-11e8-bf1c-ea00e4d87701', 'token': '49567a58040149409cb28dead39a9746'},
              {'duid': '20181207-9dac6934-f9cf-11e8-bf1c-ea00e4d87701', 'token': '0ed1a3d8074c4a528be3922d90065ea8'},
              {'duid': '20181207-9e43b9ec-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ffc710d92dd04bf79df0655a6ee457b2'},
              {'duid': '20181207-9edb4564-f9cf-11e8-bf1c-ea00e4d87701', 'token': '91a791d767044593a9e4d7992196a950'},
              {'duid': '20181207-9f7f193c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '8103e274e40b4fcd97803dab17f75f3e'},
              {'duid': '20181207-a03c71e4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '46301b3bb475421f944dd41400044139'},
              {'duid': '20181207-a0f7e0fa-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b23844c3bec64845bb530f2215fd530a'},
              {'duid': '20181207-a1e0428c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '8c9885f6e88e4f1596eb506ce17e68f2'},
              {'duid': '20181207-a27df5ae-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4b5aa25fb8174825a11b3efd025327aa'},
              {'duid': '20181207-a339ff92-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd5b309c01e554b8c8b221ac07a819b41'},
              {'duid': '20181207-a3edf43e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e78ce49d845c47ceada8989c636699d4'},
              {'duid': '20181207-a4a18dbe-f9cf-11e8-bf1c-ea00e4d87701', 'token': '27e3add5b8aa46a48b449f45f0d9f7cf'},
              {'duid': '20181207-a55d314a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '51107ef387d842db86694914349724a4'},
              {'duid': '20181207-a60903c6-f9cf-11e8-bf1c-ea00e4d87701', 'token': '0cc70516622f4ea88745a661b90671cf'},
              {'duid': '20181207-a6c46c60-f9cf-11e8-bf1c-ea00e4d87701', 'token': '306bf37deed646b5a3ae6a8def438be5'},
              {'duid': '20181207-a7704706-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9c6f0467c6ec4deaa909222e16ddf671'},
              {'duid': '20181207-a82bc864-f9cf-11e8-bf1c-ea00e4d87701', 'token': '29d81cb810a1448b9c48ffff41e6da46'},
              {'duid': '20181207-a8d7e7d4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3e434b003b9b4d18ad31c5c1084ff99f'},
              {'duid': '20181207-a9934858-f9cf-11e8-bf1c-ea00e4d87701', 'token': '8c28600e6afa481daf9613cee44a01e1'},
              {'duid': '20181207-aa475c94-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'dcafaa28623c403a919aef64297f49c5'},
              {'duid': '20181207-aafa7414-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'bbe7686f5be64d64bb991ff7abd004d6'},
              {'duid': '20181207-aba7162e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '15940389942047188d62339f0eb2ad9f'},
              {'duid': '20181207-ac620f74-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7bf6e26cec8242b891e3f652fdb57e34'},
              {'duid': '20181207-ad0e0ad6-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd8e99ee02ce54ca791bd75c4c7804e5b'},
              {'duid': '20181207-adb9ca92-f9cf-11e8-bf1c-ea00e4d87701', 'token': '96922aeb94e241f2afd83bff8466c6f9'},
              {'duid': '20181207-ae5f86f8-f9cf-11e8-bf1c-ea00e4d87701', 'token': '43ceb48f129c405e9004572cff25f6fc'},
              {'duid': '20181207-af09e756-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'c86acc48a7444fd0aa897d0b78b5f1fb'},
              {'duid': '20181207-afad9f36-f9cf-11e8-bf1c-ea00e4d87701', 'token': '518186b62cce497cb42f261de3133443'},
              {'duid': '20181207-b057b8a4-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e37d16cad2874b318f8a1f03db8eefe6'},
              {'duid': '20181207-b0f5c404-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ed3a344db7ad47089e5886522556401d'},
              {'duid': '20181207-b1a9f726-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f708671bfcd5498e9cb1e0637e82132f'},
              {'duid': '20181207-b24dc310-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e6e374aaad3e446b951df1877452813d'},
              {'duid': '20181207-b2f9abda-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3abef6df110842f6a651338f192c26d4'},
              {'duid': '20181207-b3b52e0a-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'c31ee6bb819b40f0baa74346c4b459e4'},
              {'duid': '20181207-b468e76a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3b007d2db98e491798d3d76757407aa7'},
              {'duid': '20181207-b51c8126-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9ccc9ca0d24343b0a0f070ba74c25c30'},
              {'duid': '20181207-b5c81590-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'adf1d4a9902341aa8e13ba9374f7c911'},
              {'duid': '20181207-b674254c-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'bdf2f043fd054bf8a9e2766b534ce801'},
              {'duid': '20181207-b718a450-f9cf-11e8-bf1c-ea00e4d87701', 'token': '190cf3787aff494ab109fd0153087a78'},
              {'duid': '20181207-b7bc71de-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f173d62f1afc4d63825ca00554843e95'},
              {'duid': '20181207-b869e3fa-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3415e0867e3e4ab58091ba7ba6586844'},
              {'duid': '20181207-b9059a84-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4bbc10aae8944a5aaab516aba27d8f34'},
              {'duid': '20181207-b9b06324-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ca6d707ca04c45df83bed07394868615'},
              {'duid': '20181207-ba641e32-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'be2886bedc0e4416b84956ae0bd36632'},
              {'duid': '20181207-bb17c7b6-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a26149bf087644e18afeaf35eee00be6'},
              {'duid': '20181207-bbd2f7d4-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'c4c8923681df4019ac62c15e1ba97ada'},
              {'duid': '20181207-bc7ef0e8-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a29956d882f04947b08d868c8d3cd5b0'},
              {'duid': '20181207-bd3acd86-f9cf-11e8-bf1c-ea00e4d87701', 'token': '13ebecd92bab408b8b655a3dc49506f0'},
              {'duid': '20181207-bdf628f6-f9cf-11e8-bf1c-ea00e4d87701', 'token': '0acb1b3903104d2fb41f766dc0b63dd1'},
              {'duid': '20181207-bf1f89de-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9a093a5174114da4b6d5a555ea69a989'},
              {'duid': '20181207-c0118108-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a8e83b9297ad4ae9b341686e4386421d'},
              {'duid': '20181207-c0d8a990-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'c9c7b8ee7bba48b3af8ea0bb10c87ed4'},
              {'duid': '20181207-c1bf0fac-f9cf-11e8-bf1c-ea00e4d87701', 'token': '30cb3d3c0f89462b8c2bb5f38abfc112'},
              {'duid': '20181207-c299b7ce-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'c429a1b478694b1a917d1962599d410f'},
              {'duid': '20181207-c3759384-f9cf-11e8-bf1c-ea00e4d87701', 'token': '15c5e3b8137b42cfa526efee5f2e0392'},
              {'duid': '20181207-c45ebde8-f9cf-11e8-bf1c-ea00e4d87701', 'token': '341c614c107f4c2aad5fda6cb1c6b0b6'},
              {'duid': '20181207-c5438e50-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e44b8798d022430e976a97f7de5375c4'},
              {'duid': '20181207-c623fdb4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4cd8fbd61c8740a9bdadb285a02ff67d'},
              {'duid': '20181207-c6ff682c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9837ce6a4f6645adbdf91f1d15c31af9'},
              {'duid': '20181207-c7c9b9e2-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3e2e03f30dc2419fba59af52374937f5'},
              {'duid': '20181207-c8c3bf46-f9cf-11e8-bf1c-ea00e4d87701', 'token': '8d4deee89140446fbedefacaa5df6b8d'},
              {'duid': '20181207-c99fc86a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1b09c5586875455e83739a06dc26cb12'},
              {'duid': '20181207-ca5de502-f9cf-11e8-bf1c-ea00e4d87701', 'token': '0dd68a1bf2f14cc590e5dd57118d390f'},
              {'duid': '20181207-cb35e06a-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'cb53180796bf4e75a8298af191e40c70'},
              {'duid': '20181207-cc0f6088-f9cf-11e8-bf1c-ea00e4d87701', 'token': '743151c59b664a04af545c3139f7ccec'},
              {'duid': '20181207-ccdc08fe-f9cf-11e8-bf1c-ea00e4d87701', 'token': '01d1e0abf2f94db9be59bfb6b833fc75'},
              {'duid': '20181207-cdbcb322-f9cf-11e8-bf1c-ea00e4d87701', 'token': '68c2233bde2f4fafaa0e2cff60fa69b7'},
              {'duid': '20181207-ce999e5e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f07d5ebfa90e4553a2edcb9744a946cf'},
              {'duid': '20181207-cf6ceab6-f9cf-11e8-bf1c-ea00e4d87701', 'token': '2383cef2d49b4e6f90f7e299df08a367'},
              {'duid': '20181207-d035e7fe-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ec826f41a0f043988bc8580b5d5a3914'},
              {'duid': '20181207-d100f93a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '52e9705c4b7a4efb95a1d297c266cde3'},
              {'duid': '20181207-d1bca572-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b7a3bec526234be09ad6b5d52818f2dd'},
              {'duid': '20181207-d25904d0-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'cf844173f5374dd7923968ea068f71dc'},
              {'duid': '20181207-d308e936-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1a916a2f1e41447c82c2aaab46f543fe'},
              {'duid': '20181207-d3b8e0e8-f9cf-11e8-bf1c-ea00e4d87701', 'token': '22117796840043babc7c2a744c4c8fe5'},
              {'duid': '20181207-d4549218-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1949cbd2ac324cef93b473473324fc9c'},
              {'duid': '20181207-d4f16d7c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3555985adbb3430f83b98a3cf9ff0c70'},
              {'duid': '20181207-d594ef42-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e4074a4979774fe795b20dbc42798578'},
              {'duid': '20181207-d650a296-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd71f1415dff040f9bc108270c489bb6a'},
              {'duid': '20181207-d703dc26-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a37c04c2e96c41c9bb206d4a9e2e2b38'},
              {'duid': '20181207-d7b7ee96-f9cf-11e8-bf1c-ea00e4d87701', 'token': '45051a93fb844fa396da3a57563cf8f6'},
              {'duid': '20181207-d8616e80-f9cf-11e8-bf1c-ea00e4d87701', 'token': '83b0118e4dfb4ab2b796f46baf6cef6d'},
              {'duid': '20181207-d91f210a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '77667721fd68427a8c08e39def2a1c49'},
              {'duid': '20181207-d9cb11f4-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e44392a0930d4b2fac2dad19a843b6d6'},
              {'duid': '20181207-da6fc01e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '75ee232c3f2d4d16b8d9dd3e1c95eb19'},
              {'duid': '20181207-db111748-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4f7469fdf2ea426c8c867338a745bc60'},
              {'duid': '20181207-dbb841ee-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a9ad38648d194435a5951ea6c1889f3a'},
              {'duid': '20181207-dc737568-f9cf-11e8-bf1c-ea00e4d87701', 'token': '38e9446a54ca431092d6be6274106f84'},
              {'duid': '20181207-dd14e77c-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'eb740a7e0147435f964a679a6c5d64f8'},
              {'duid': '20181207-ddb09b40-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f2fa9fff444e4ffeb1876cf7de7509ce'},
              {'duid': '20181207-de493df0-f9cf-11e8-bf1c-ea00e4d87701', 'token': '5941d5b8661b48c6adeabb187739c8ee'},
              {'duid': '20181207-dee17eee-f9cf-11e8-bf1c-ea00e4d87701', 'token': '541971db12b24a258d02122a82fd4f3f'},
              {'duid': '20181207-df78da6e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '610d7e0263fc47adb66ca04b6ee97589'},
              {'duid': '20181207-e013263c-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f2010b12b9954d6ab23e15b0bf6a4a24'},
              {'duid': '20181207-e0b5432c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '5d2e400b96c74c69bec3814d7a89b1d2'},
              {'duid': '20181207-e15a5128-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b13cecb4005146dfa6f97c65343329da'},
              {'duid': '20181207-e1f2145e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e0e3bcb6e2834ae5825b44510243a43a'},
              {'duid': '20181207-e28afa98-f9cf-11e8-bf1c-ea00e4d87701', 'token': '2220ceeea0cb4dec8601aa6f654e4480'},
              {'duid': '20181207-e330e2d2-f9cf-11e8-bf1c-ea00e4d87701', 'token': '72bf828152ab4ba69bae83b9f2c0051e'},
              {'duid': '20181207-e3d5d620-f9cf-11e8-bf1c-ea00e4d87701', 'token': '01b7d313a05140d5829f6a6a2262462f'},
              {'duid': '20181207-e476e132-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4ee0f1b42b4a4b2eaa176177342eb6cc'},
              {'duid': '20181207-e50e3ee2-f9cf-11e8-bf1c-ea00e4d87701', 'token': '5a17b4cf4cb940c6bcb33c07ed80cff9'},
              {'duid': '20181207-e5a54986-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9bac6bcefcb74297b686aff037b1b982'},
              {'duid': '20181207-e63c7112-f9cf-11e8-bf1c-ea00e4d87701', 'token': '8fcd822237b44cad835cb3bd6419311a'},
              {'duid': '20181207-e6d471ba-f9cf-11e8-bf1c-ea00e4d87701', 'token': '8f3e9e940fd0475099a72534a4ccd66b'},
              {'duid': '20181207-e77d41be-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e47623251d9e4759a614f854dd268844'},
              {'duid': '20181207-e81b378e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '521e9020def8431eb12ec744c6f30da1'},
              {'duid': '20181207-e8b34934-f9cf-11e8-bf1c-ea00e4d87701', 'token': '00885abe497342aeb36369f9aff41b15'},
              {'duid': '20181207-e960413e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '290f7b3a7aea410c9818b367cc6c385d'},
              {'duid': '20181207-e9f94884-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'da099f5c66fc4b1d87782807b08296f0'},
              {'duid': '20181207-ea900fc6-f9cf-11e8-bf1c-ea00e4d87701', 'token': '0d4e943e118d4e4fa1e1d3dba1213349'},
              {'duid': '20181207-eb2e1dd8-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4356c6ee43db4b738d27994b714927e8'},
              {'duid': '20181207-ebe431fe-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'dd10274535324f76b6a804bf58a2815b'},
              {'duid': '20181207-ec882ade-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a8d7f687a2bf482a9b12f79bc17cc205'},
              {'duid': '20181207-ed33d6fe-f9cf-11e8-bf1c-ea00e4d87701', 'token': '6163b9e988154c59a72584df72544d97'},
              {'duid': '20181207-edeaea1a-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'fe4cd09afa8e4cf59f183a0f35122f38'},
              {'duid': '20181207-ee842d88-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4eb4ff9624ed481d9f218d3faf1cd38c'},
              {'duid': '20181207-ef280eb2-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'c30dca5759f542638cb9928eb1102c5d'},
              {'duid': '20181207-efc42e96-f9cf-11e8-bf1c-ea00e4d87701', 'token': '273148644a514a59918273e37bca05f1'},
              {'duid': '20181207-f05c5824-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7c8e801014624106bba6e880b92a7e31'},
              {'duid': '20181207-f10175d4-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'bd07c03f088846e7a95f497ff0e823b8'},
              {'duid': '20181207-f199bd76-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd33ecf9e14f84aaab1a8d1de2750922a'},
              {'duid': '20181207-f241ab6c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7e917de3bfb94933afe46255c29d96eb'},
              {'duid': '20181207-f2d85788-f9cf-11e8-bf1c-ea00e4d87701', 'token': '6b762403e87d485dbf4029fd69af4600'},
              {'duid': '20181207-f36dc2b4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9f1fc0732c6e4607bab2103c7f91174f'},
              {'duid': '20181207-f40718c4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '37601c569e1b460bad68a5747e83e2b6'},
              {'duid': '20181207-f49fe2f2-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ffbc3de4d8ef48e8823589b1ca44d764'},
              {'duid': '20181207-f53889a8-f9cf-11e8-bf1c-ea00e4d87701', 'token': '33ccdcd6a6984488a664cf4b07abfd17'},
              {'duid': '20181207-f5d7511e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1b3661816b404e3a9e24e1c5fb1e12bc'},
              {'duid': '20181207-f68234da-f9cf-11e8-bf1c-ea00e4d87701', 'token': '795cc1963ad6422f9351a1adcc37fe34'},
              {'duid': '20181207-f7176dd4-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'cb3425a02f6a45a3b4a8f54e7ab42256'},
              {'duid': '20181207-f7b31914-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a591a427dc9e49949e30bba03d9eba4b'},
              {'duid': '20181207-f85223e2-f9cf-11e8-bf1c-ea00e4d87701', 'token': '18be3c3df6e5408d8c4e2bbd61e01a70'},
              {'duid': '20181207-f8ef4672-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f88ab2a5cf4845cc951163fd19bb59e5'},
              {'duid': '20181207-f98777e4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '222fd47c211f4a7f8eebf02cb4216a31'},
              {'duid': '20181207-fa247fee-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'c50b1a8249744932a73640b84a74b879'},
              {'duid': '20181207-fabb2c46-f9cf-11e8-bf1c-ea00e4d87701', 'token': '04c7970fced140a9860f4f91faee81fb'},
              {'duid': '20181207-fb6cb150-f9cf-11e8-bf1c-ea00e4d87701', 'token': '0b446f46e15c498891ab64ae26d72b5a'},
              {'duid': '20181207-fc0cda0e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'db0af731fb884ee09a01bc7b714cfa00'},
              {'duid': '20181207-fcb50526-f9cf-11e8-bf1c-ea00e4d87701', 'token': '04eb4caeffad48a0be8009402ab8dccb'},
              {'duid': '20181207-fd605c50-f9cf-11e8-bf1c-ea00e4d87701', 'token': '680938816efb47428768407fa201dc13'},
              {'duid': '20181207-fe046660-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4f606b06630f4e0195581abee9189cab'},
              {'duid': '20181207-fe9d9984-f9cf-11e8-bf1c-ea00e4d87701', 'token': '90ce8db5e6e84e65809c4be77d4b8570'},
              {'duid': '20181207-ff347dfe-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a492d080b4c74faa9cea46441eb65487'},
              {'duid': '20181207-ffc9cc2e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a8b34e7c50bc43c981e94272d51e7612'},
              {'duid': '20181207-00624742-f9d0-11e8-bf1c-ea00e4d87701', 'token': '954ff593eefb4a83992015113a8d28eb'},
              {'duid': '20181207-0101e554-f9d0-11e8-bf1c-ea00e4d87701', 'token': '1d629303b4b34e5b9340be97b6d04c01'},
              {'duid': '20181207-019e1fe6-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'a0bf4df3ad874b2aa37b0f670131649d'},
              {'duid': '20181207-0234e9a8-f9d0-11e8-bf1c-ea00e4d87701', 'token': '194ad6e628f447319ed67f3328bf8d68'},
              {'duid': '20181207-02ca1cf8-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'd5e1ff21306e488bb131566a67ada59d'},
              {'duid': '20181207-03600f56-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'c9776f14ee304a9fbcb4c4388828b07f'},
              {'duid': '20181207-03fa163c-f9d0-11e8-bf1c-ea00e4d87701', 'token': '7093609915bd4442a72c283f001061db'},
              {'duid': '20181207-049281a6-f9d0-11e8-bf1c-ea00e4d87701', 'token': '043b51ac56084c74bbdc3485ef18793b'},
              {'duid': '20181207-052b381a-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'd21eacf3c9a5427e8ca4296bac6e6508'},
              {'duid': '20181207-05c4311e-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'f910f642234341e3b6c5c4901f5701d4'},
              {'duid': '20181207-065b9b8a-f9d0-11e8-bf1c-ea00e4d87701', 'token': '096a2ceb9ae045f7925660ef0c722dd3'},
              {'duid': '20181207-06f4ae1a-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'bc7fed503a024f69ac06c85220a68ede'},
              {'duid': '20181207-078c3e10-f9d0-11e8-bf1c-ea00e4d87701', 'token': '361bc5d67ffa4ce298606839144ffca9'},
              {'duid': '20181207-082e2cb6-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'c6219d83bca64159b25d971035028674'},
              {'duid': '20181207-08da10b2-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'aa61c0ab032c4142aa107434b57b92ed'},
              {'duid': '20181207-097b0292-f9d0-11e8-bf1c-ea00e4d87701', 'token': '1553679bf25949da80a4c349d358de22'},
              {'duid': '20181207-0a1fc20a-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'c540cb641d2d4cda8fbe2ce1e056c0a9'},
              {'duid': '20181207-0ada90b2-f9d0-11e8-bf1c-ea00e4d87701', 'token': '63d2aa1e7c3c41d280840c997b0fcf0b'},
              {'duid': '20181207-0b992fe0-f9d0-11e8-bf1c-ea00e4d87701', 'token': '05d0d038c9234dadbb0f92f36a93a8b0'},
              {'duid': '20181207-0c3b11fc-f9d0-11e8-bf1c-ea00e4d87701', 'token': '43b9371a74af4e3fad6a956670d272c9'},
              {'duid': '20181207-0cd2a288-f9d0-11e8-bf1c-ea00e4d87701', 'token': '7143cc91f3a54ee9b535e7a2eddfd433'},
              {'duid': '20181207-0d694c9c-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'f23a05918fa246fbaa0853b42c1c60cc'},
              {'duid': '20181207-0e00f9de-f9d0-11e8-bf1c-ea00e4d87701', 'token': '93080bfd36464858ba00e9e0e0f9f71a'},
              {'duid': '20181207-0eab4b64-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'cb983c8443084c91b8b8c66c28bb3091'},
              {'duid': '20181207-0f4af308-f9d0-11e8-bf1c-ea00e4d87701', 'token': '81806f7f714843a486cd656ffb9b4b57'},
              {'duid': '20181207-0feed1d0-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'b44e987b05b6417395a0fa1b3d5859c1'},
              {'duid': '20181207-113f3f52-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'c196ce91df5245059dcd7900398d20c4'},
              {'duid': '20181207-11eaf284-f9d0-11e8-bf1c-ea00e4d87701', 'token': '889d308e5bd14750bd1745c8a1929689'},
              {'duid': '20181207-12969440-f9d0-11e8-bf1c-ea00e4d87701', 'token': '76df16fff1414bbab5e0fabf35d2b293'},
              {'duid': '20181207-13420c6c-f9d0-11e8-bf1c-ea00e4d87701', 'token': '471dae01da4b40d0a4f34b7f88f3beda'},
              {'duid': '20181207-13e3fdec-f9d0-11e8-bf1c-ea00e4d87701', 'token': '2965cce84be548e5998d592d85d7f59d'},
              {'duid': '20181207-149255fe-f9d0-11e8-bf1c-ea00e4d87701', 'token': '0721fbe9ce324b549376fb9e3de34ef8'},
              {'duid': '20181207-153bc5f8-f9d0-11e8-bf1c-ea00e4d87701', 'token': '2621a6e3d0cd4c978bc56b608610f616'},
              {'duid': '20181207-15df10f0-f9d0-11e8-bf1c-ea00e4d87701', 'token': '95a73910655844c4b375c65a4574d4ec'},
              {'duid': '20181207-167823a8-f9d0-11e8-bf1c-ea00e4d87701', 'token': '92b7fb87b083404ca23ab08bdf2ee75e'},
              {'duid': '20181207-171afc0e-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'd53f6619821b41069d08bf54b458bdb6'},
              {'duid': '20181207-17b72dcc-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'c3b7abd2e6754ff88d2caab354af2492'},
              {'duid': '20181207-185e5fde-f9d0-11e8-bf1c-ea00e4d87701', 'token': '10086970cf574819a43e5c575cd81ba0'},
              {'duid': '20181207-1906ed2a-f9d0-11e8-bf1c-ea00e4d87701', 'token': '2356ca82f4ed4cd79a6646982871b50b'},
              {'duid': '20181207-19a39328-f9d0-11e8-bf1c-ea00e4d87701', 'token': '5968631ac1cf486aa229e9592f8a027e'},
              {'duid': '20181207-1a4f1ea0-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'ab81737e947a40cd836c75d84c66ad6e'}]

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
        response.failure("errorMsg is Fail")
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
                                         'token': token}}}},
                              'DATA_FORMAT': {'TYPE': 'ONLY', 'DATA': {'errorCode': 'Str', 'errorMsg': 'Str', 'info': {
                                  'pic_list': [{'tiny': {'url': 'HTTP', 'height': 'Int', 'width': 'Int', 'size': 'Int'},
                                                'origin': {'url': 'HTTP', 'height': 'Int', 'width': 'Int',
                                                           'size': 'Int'}, 'item_id': 'Str', 'id': 'Str'}]}}},
                              'DATA_CONTENT': None, 'RESPONSE_HEADER': None, 'THE_FLOWING': None,
                              'THE_ABOVE': {'TYPE': 'BODY', 'KEY': None, 'DATA': 'info/group_list/^/title'}},
                     'path': './case/search/search_fall.yml'}
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
                                         'token': token,
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
                                'DATA': {"token": token, 'category': ['test'], 'index': [0], 'limit': [20]}}}},
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
                       'BODY': {'TYPE': 'JSON', 'FUNCTION': '5NUT', 'DATA': {'token': token, 'title': ['baby']}}}},
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
                                    "token": token,
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
                                'DATA': {'token': token, 'index': [0], 'limit': [20]}}}},
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

    @task(10)
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
