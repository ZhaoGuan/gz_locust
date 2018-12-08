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

user_datas = [{'duid': '20181207-6a06f180-f9cf-11e8-bf1c-ea00e4d87701', 'token': '828e022d7d7f41029052f932f96cd850'},
             {'duid': '20181207-6b1499f6-f9cf-11e8-bf1c-ea00e4d87701', 'token': '20fc0cf6045644ee856d390ec77452a2'},
             {'duid': '20181207-6bce83c0-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9f6cbddc35b64ad1bfec31aa56bc97c8'},
             {'duid': '20181207-6c7a6f8c-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a80503f22e274861bf89d81c14280571'},
             {'duid': '20181207-6d265cb6-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1eb7be5e01564210a9f1491dd47c65b1'},
             {'duid': '20181207-6de1d5cc-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7e674d76a09f44beadbc636b32e2f5f3'},
             {'duid': '20181207-6e9d75ca-f9cf-11e8-bf1c-ea00e4d87701', 'token': '95579fa27e19497da3d537fe0096ea29'},
             {'duid': '20181207-6f3965ac-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'df553655cda04657ba5f21f758e5da61'},
             {'duid': '20181207-6fe57bb2-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'c03ff98d5ca34e888792038358dfd552'},
             {'duid': '20181207-70a0a608-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1ac5311b9ee34708a1f7b2942b396095'},
             {'duid': '20181207-713d14de-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a1dd7775e7464f158f4771d1cc188944'},
             {'duid': '20181207-71e8cb12-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4e1cae5d9a6a4315bd8d83e725e9d7ca'},
             {'duid': '20181207-72a3ba94-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b402cb48688c4863bbd65a1a25b7bd50'},
             {'duid': '20181207-735ff092-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'cbacdeacc8784939af5f270c6fefa814'},
             {'duid': '20181207-7403f160-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b9f717eddc3644328e9cb5584048e730'},
             {'duid': '20181207-74afeae2-f9cf-11e8-bf1c-ea00e4d87701', 'token': '83945c1d1d9e4093887c5471ed7655cd'},
             {'duid': '20181207-7563a5f0-f9cf-11e8-bf1c-ea00e4d87701', 'token': '05b17a40e143494384c49b7b7d288b3d'},
             {'duid': '20181207-760f3460-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'bd68a5245c7a46f98ad816bc2795a742'},
             {'duid': '20181207-76cb3c28-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'adfa0dfc09a345d2b4e858f8336080eb'},
             {'duid': '20181207-7776f69e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '48a8846451504739b11224a506d05b95'},
             {'duid': '20181207-7832754a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '45edd86366104b1495db2ed78ecf7e09'},
             {'duid': '20181207-78edae0a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '46b739399ef244e4b82266ddc26f57bd'},
             {'duid': '20181207-79a9430e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '97f6b971b7ce440b82ab072f7450c774'},
             {'duid': '20181207-7a558272-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd85a841b849f4a888402650d26411086'},
             {'duid': '20181207-7b10f408-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd33b3d5be21c4a179728718d3cee72f8'},
             {'duid': '20181207-7bc4e436-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b8de8d592def4cf0a5c61505a0e69545'},
             {'duid': '20181207-7c7851f6-f9cf-11e8-bf1c-ea00e4d87701', 'token': '8396172606da40ed93c14c148f93197a'},
             {'duid': '20181207-7d33fc6c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1cc17aad2a834a7da5ccb6ba664c6ee8'},
             {'duid': '20181207-7ddfa792-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9a55917d278c45068c70ef43491ebfe8'},
             {'duid': '20181207-7e8b8cec-f9cf-11e8-bf1c-ea00e4d87701', 'token': '06e62db4e1094322b7d2f7978345db1d'},
             {'duid': '20181207-7f38d618-f9cf-11e8-bf1c-ea00e4d87701', 'token': '2515b099dbe34124a0392e9c88b07afe'},
             {'duid': '20181207-7fdf5790-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'cecec7fc96bb4135abaf2ca2dfc553ca'},
             {'duid': '20181207-809eaee2-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4fa0cfc4cbfc4536955a403cec627d35'},
             {'duid': '20181207-813b18a4-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'dcbb9034cc6b46ab8425503781756413'},
             {'duid': '20181207-81d748c8-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd48bd961281340c3a612d3f773035b75'},
             {'duid': '20181207-8273999e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '26251208f35e48e880da075ed51e64e8'},
             {'duid': '20181207-830e4ee4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '0aa624eb0e6244c4a268d68ca9abbd45'},
             {'duid': '20181207-83cb13da-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ca6a55d8783345268c24667253be1460'},
             {'duid': '20181207-84773b6a-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e7a63a8639f741008b148157058eeffc'},
             {'duid': '20181207-85137dd6-f9cf-11e8-bf1c-ea00e4d87701', 'token': '29c35b288bf644bfb6cdd0679f705592'},
             {'duid': '20181207-85ce9a26-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7ce42614e9cf4e788deb4c893ce7275c'},
             {'duid': '20181207-86739288-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'eb739443006245519e4c64f2577f8922'},
             {'duid': '20181207-870f43d6-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'cbf8a3f04a2d4326894deaa52b335957'},
             {'duid': '20181207-87c30560-f9cf-11e8-bf1c-ea00e4d87701', 'token': '542931488d5241be818d29b6404bc3d7'},
             {'duid': '20181207-886eed4e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '64eaa9f670334757b490ba67a0080874'},
             {'duid': '20181207-890fa626-f9cf-11e8-bf1c-ea00e4d87701', 'token': '967e7cfec8514871a1d679d1f7424b59'},
             {'duid': '20181207-89b2de22-f9cf-11e8-bf1c-ea00e4d87701', 'token': '61555379f7dc4ef5b375a88d82df301c'},
             {'duid': '20181207-8a62d71e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9f8e53457d4e4b31b6ca2f25be7c68e5'},
             {'duid': '20181207-8b07380e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '827147aeec32413b8da91ec3037063f1'},
             {'duid': '20181207-8ba360d0-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e0157e1e8c0a41abafac0b9e821d7190'},
             {'duid': '20181207-8c471626-f9cf-11e8-bf1c-ea00e4d87701', 'token': '603340820eb9468f97545010b35a0678'},
             {'duid': '20181207-8cf2f5fe-f9cf-11e8-bf1c-ea00e4d87701', 'token': '2f25eaa65e42495997737549778f6d61'},
             {'duid': '20181207-8da77d80-f9cf-11e8-bf1c-ea00e4d87701', 'token': '23aff3457060436694f8409abd8ecf14'},
             {'duid': '20181207-8e42c98e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4171d3a15cdf4c3dbc899092d80afa49'},
             {'duid': '20181207-8ef6c060-f9cf-11e8-bf1c-ea00e4d87701', 'token': '78e2367e78c04816b4535ca97ed3d6a0'},
             {'duid': '20181207-8fae6bde-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'da2c5f5670b949c5b6af5829da4c7745'},
             {'duid': '20181207-905e0468-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3c8148532e444ec6aac988a5e5929b61'},
             {'duid': '20181207-90fa1394-f9cf-11e8-bf1c-ea00e4d87701', 'token': '36cdf7f533aa46ecae06fe7b589cf0b9'},
             {'duid': '20181207-919657f4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3c724a8507ae456fb592524663cf51cd'},
             {'duid': '20181207-922f7fc4-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a3f5e694b2b444649362caabff3ec6a4'},
             {'duid': '20181207-92ceec9e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4498235fe36849db9ab7b9a1bd3ee3e9'},
             {'duid': '20181207-936b6b1e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'cc293f2edde54045a32fe96eb9dffca8'},
             {'duid': '20181207-94073936-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ac16cbb1ae6343b1bb6e1fc35d0d3486'},
             {'duid': '20181207-94a3ed8a-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ed3a3ae43ba34f7fa91d7eb5ea5a4caa'},
             {'duid': '20181207-953fe58c-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ea4e7826cfdb433aa84aab82e098e160'},
             {'duid': '20181207-963821c0-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a8cd352298c54dc09424b7582658c337'},
             {'duid': '20181207-96e60e20-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'fdf91d51ab09450393913b2b0edc9203'},
             {'duid': '20181207-97927e9e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ce48b4804ece4e69816e4d49cde81bb2'},
             {'duid': '20181207-983d9b80-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3cd7cd2428bd423aa607b9c80b15393f'},
             {'duid': '20181207-98da0e20-f9cf-11e8-bf1c-ea00e4d87701', 'token': '20cfea2d590f4e55baaee15563dad5f8'},
             {'duid': '20181207-99a4db00-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b97e04c0bc7949ffb7945fa194dc95b3'},
             {'duid': '20181207-9a605c5e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'dec127ecad9545e7999aed5164f41385'},
             {'duid': '20181207-9b0c833a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '5e05eae2711441cbb111946d14130574'},
             {'duid': '20181207-9bb8a566-f9cf-11e8-bf1c-ea00e4d87701', 'token': '383c76adaccb4795a8f150ca2c2070d8'},
             {'duid': '20181207-9c656a30-f9cf-11e8-bf1c-ea00e4d87701', 'token': '097a30e12f74425f8070acfa4055fd3e'},
             {'duid': '20181207-9cfe2ee6-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1f8ba84686514a33ad38f61fe6207da3'},
             {'duid': '20181207-9dac6934-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f9d4d2a6785941f28477542369b04674'},
             {'duid': '20181207-9e43b9ec-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd672c4ac7da8438d9b41be4dbf5a8faf'},
             {'duid': '20181207-9edb4564-f9cf-11e8-bf1c-ea00e4d87701', 'token': '228e14b048784c4393a425ad4dcab916'},
             {'duid': '20181207-9f7f193c-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'cc71a4b94230454881d51a9748ff265f'},
             {'duid': '20181207-a03c71e4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '938923cb44cc4aec98f97f2d46f05b08'},
             {'duid': '20181207-a0f7e0fa-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9351dce010af493ba16a76ce3af0c4ad'},
             {'duid': '20181207-a1e0428c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4b796c0212f84012be1d1df87f8c85ab'},
             {'duid': '20181207-a27df5ae-f9cf-11e8-bf1c-ea00e4d87701', 'token': '006020fd062c4fbc98f8a68791e20788'},
             {'duid': '20181207-a339ff92-f9cf-11e8-bf1c-ea00e4d87701', 'token': '13786352b33747d59b65ddd3284c5504'},
             {'duid': '20181207-a3edf43e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '88dc50540ecd47b4876565ab5315e939'},
             {'duid': '20181207-a4a18dbe-f9cf-11e8-bf1c-ea00e4d87701', 'token': '85295895ef5d4eb7bec2860f88ed39bd'},
             {'duid': '20181207-a55d314a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '2f668bd710cf4631982a288e6424210a'},
             {'duid': '20181207-a60903c6-f9cf-11e8-bf1c-ea00e4d87701', 'token': '907d37f10d314cc68b613d660577ed2d'},
             {'duid': '20181207-a6c46c60-f9cf-11e8-bf1c-ea00e4d87701', 'token': '0c51652651914679bb899cddb3a87c01'},
             {'duid': '20181207-a7704706-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'cc97e0ff6bfc4542984806c6cbaaae99'},
             {'duid': '20181207-a82bc864-f9cf-11e8-bf1c-ea00e4d87701', 'token': '98022f5e361b4c1894f1ae1f7c961566'},
             {'duid': '20181207-a8d7e7d4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '924dbde2e19c44be8e97482816d1ed89'},
             {'duid': '20181207-a9934858-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'fe6264b1d463430c9681ad5f8d3642c1'},
             {'duid': '20181207-aa475c94-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e7c18778b14546a4b295974830c6ab7f'},
             {'duid': '20181207-aafa7414-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9e94cfb222a347738cf0a5cb10c244d3'},
             {'duid': '20181207-aba7162e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ff65df6438944bd1bedbbfd3df63bc36'},
             {'duid': '20181207-ac620f74-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'dff532ed814747f1acc00f3097499531'},
             {'duid': '20181207-ad0e0ad6-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f550b6dc80114d2c8b9f9a01bdffb089'},
             {'duid': '20181207-adb9ca92-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3c9dd31a2150426b9e2bf32146bc3888'},
             {'duid': '20181207-ae5f86f8-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1bf5575393a94b9f8d13b4fca8c97de3'},
             {'duid': '20181207-af09e756-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd30e49393b164ef4820cb2f5257f7010'},
             {'duid': '20181207-afad9f36-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a881ba45df234751ba16a63097cf3b81'},
             {'duid': '20181207-b057b8a4-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'df010469cadf4e85ad889c8ebf8f61ad'},
             {'duid': '20181207-b0f5c404-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'df0be64f1d184c598456fe3f2c0786d1'},
             {'duid': '20181207-b1a9f726-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3e569a72a00f4bb2a994ffb01391c92c'},
             {'duid': '20181207-b24dc310-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd2acbbc5ffad4d75934456cf5053134f'},
             {'duid': '20181207-b2f9abda-f9cf-11e8-bf1c-ea00e4d87701', 'token': '53e5084bf959499ba6634261a9fe8672'},
             {'duid': '20181207-b3b52e0a-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'bbe2d613b251482ea78a7ee78c5ca32f'},
             {'duid': '20181207-b468e76a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '90568ccfaa2d491c8ae21f05c8304ef4'},
             {'duid': '20181207-b51c8126-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'c3143f4073d04a7d9a00d960f0c922e3'},
             {'duid': '20181207-b5c81590-f9cf-11e8-bf1c-ea00e4d87701', 'token': '059ba61e93ef455a81aadd5f44b6b0b2'},
             {'duid': '20181207-b674254c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3681f878bf1f40e39818df1a45cbb644'},
             {'duid': '20181207-b718a450-f9cf-11e8-bf1c-ea00e4d87701', 'token': '44b7478c5e324e528725d9b120d54661'},
             {'duid': '20181207-b7bc71de-f9cf-11e8-bf1c-ea00e4d87701', 'token': '01abb7fcea2c4e6e8ba0095dccf639ad'},
             {'duid': '20181207-b869e3fa-f9cf-11e8-bf1c-ea00e4d87701', 'token': '2c5135fcbdf044fd8b60596bbc903187'},
             {'duid': '20181207-b9059a84-f9cf-11e8-bf1c-ea00e4d87701', 'token': '15f8a902a67b402b9a2ffb0d3c7b576a'},
             {'duid': '20181207-b9b06324-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd78461d0775f4b5481ed2e0dd50da842'},
             {'duid': '20181207-ba641e32-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a0193638375545d4bcb21e963f429192'},
             {'duid': '20181207-bb17c7b6-f9cf-11e8-bf1c-ea00e4d87701', 'token': '71f403eeb588426b8be1c931a96c4dcc'},
             {'duid': '20181207-bbd2f7d4-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e8bea26c51174a1eae2288b7fdf76e5d'},
             {'duid': '20181207-bc7ef0e8-f9cf-11e8-bf1c-ea00e4d87701', 'token': '6df0d93d1afd440db18d4b13dbbf16fc'},
             {'duid': '20181207-bd3acd86-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd836916e2ecf48acb2e76e6c6d1a2d66'},
             {'duid': '20181207-bdf628f6-f9cf-11e8-bf1c-ea00e4d87701', 'token': '2b5eeb66cfc543e5835b82c16f051e26'},
             {'duid': '20181207-bf1f89de-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1efbc30f2c6d4718a4a1775584579afc'},
             {'duid': '20181207-c0118108-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'eeff43952515431385d5097f83ad3aeb'},
             {'duid': '20181207-c0d8a990-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'bff9a88ec29446d0a53a41b244e538e2'},
             {'duid': '20181207-c1bf0fac-f9cf-11e8-bf1c-ea00e4d87701', 'token': '43c9c0152b8145c6943d9261cf6a2d07'},
             {'duid': '20181207-c299b7ce-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'be4db3f4757e4aeb91e48ac7a01e122d'},
             {'duid': '20181207-c3759384-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a72ab3a427354882be4afab4177a6e7d'},
             {'duid': '20181207-c45ebde8-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4a7bc68cac5144c28083dac679fbdbf2'},
             {'duid': '20181207-c5438e50-f9cf-11e8-bf1c-ea00e4d87701', 'token': '6303aa62ceb047a88b4c956d0d50991b'},
             {'duid': '20181207-c623fdb4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4952854470a0497e938c07202854c7cd'},
             {'duid': '20181207-c6ff682c-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b47f629867b649b29b8c715d19e8fbe6'},
             {'duid': '20181207-c7c9b9e2-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b194f004b0f747c5a20fed4e238d86ae'},
             {'duid': '20181207-c8c3bf46-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd9864de6d2444dab9169d972d5459b2e'},
             {'duid': '20181207-c99fc86a-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e5d0b5960f754530ba7231cc0fb98dbd'},
             {'duid': '20181207-ca5de502-f9cf-11e8-bf1c-ea00e4d87701', 'token': '8d4f179871dc457daecbaebaafbeee15'},
             {'duid': '20181207-cb35e06a-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd9d986d6dd56480fbd706a80bed4b97b'},
             {'duid': '20181207-cc0f6088-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ee4d0eccb8a84bd4aab7e2c00995bd0c'},
             {'duid': '20181207-ccdc08fe-f9cf-11e8-bf1c-ea00e4d87701', 'token': '6bf5e47dcffa449084be3139b6675bcd'},
             {'duid': '20181207-cdbcb322-f9cf-11e8-bf1c-ea00e4d87701', 'token': '81739541b6c2424ab4a1ac9b0e81f759'},
             {'duid': '20181207-ce999e5e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b1cef67b57e24e09b62b4b8477e84328'},
             {'duid': '20181207-cf6ceab6-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b42d30f708624072b7f10a08a5fc56f9'},
             {'duid': '20181207-d035e7fe-f9cf-11e8-bf1c-ea00e4d87701', 'token': '75265f9db9dc46da9eaf921e3a76bc94'},
             {'duid': '20181207-d100f93a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '050dba8f4f53415992a817154b23d933'},
             {'duid': '20181207-d1bca572-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ddeac368bb44477688b174dadb76a547'},
             {'duid': '20181207-d25904d0-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'c9d24d9c44aa4b449a770dcde1e93e00'},
             {'duid': '20181207-d308e936-f9cf-11e8-bf1c-ea00e4d87701', 'token': '77c37b8ac88b4d2e8164755206f6ffc6'},
             {'duid': '20181207-d3b8e0e8-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ed1c194f2d3344788f984e972f83f4a2'},
             {'duid': '20181207-d4549218-f9cf-11e8-bf1c-ea00e4d87701', 'token': '62bf9847a13343ca9eed30f6b933652e'},
             {'duid': '20181207-d4f16d7c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '00bca9b7ab2b4177a954a9292dc6dc80'},
             {'duid': '20181207-d594ef42-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1349a179245f45e496411124a57c0581'},
             {'duid': '20181207-d650a296-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'fe6aadecf26a4555b5e8c9116fcdd4eb'},
             {'duid': '20181207-d703dc26-f9cf-11e8-bf1c-ea00e4d87701', 'token': '6aa66f05bb2b4d5ca71d9824117cd33b'},
             {'duid': '20181207-d7b7ee96-f9cf-11e8-bf1c-ea00e4d87701', 'token': '6f65185a1951493399eb322359add6f6'},
             {'duid': '20181207-d8616e80-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9b140173d73d440fa71ed225808b462f'},
             {'duid': '20181207-d91f210a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9e7fa8fee3134a06a4bf8347baa0fe11'},
             {'duid': '20181207-d9cb11f4-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'c35a8a4ad5864f71bef84c409c2089f9'},
             {'duid': '20181207-da6fc01e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'fa8a58dc44384c29a1c463e1d18f458a'},
             {'duid': '20181207-db111748-f9cf-11e8-bf1c-ea00e4d87701', 'token': '59a602822d674ac9b29c5d3aa3713dc3'},
             {'duid': '20181207-dbb841ee-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'db23b8b072564ea6b31dc27965f82703'},
             {'duid': '20181207-dc737568-f9cf-11e8-bf1c-ea00e4d87701', 'token': '76ec7a7a6dbb4db7b15fd5d9c09a61ba'},
             {'duid': '20181207-dd14e77c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9878ad97b6ec40a38e7d60c2ddec714f'},
             {'duid': '20181207-ddb09b40-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'dd78f9477b294c9cb058f68fb48d184d'},
             {'duid': '20181207-de493df0-f9cf-11e8-bf1c-ea00e4d87701', 'token': '777a2f4eabbe4e768880c9098a262c6b'},
             {'duid': '20181207-dee17eee-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd6ae805073e84b07982645303d58c82a'},
             {'duid': '20181207-df78da6e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1e72d668cc9042afa4648a75afe3f9ce'},
             {'duid': '20181207-e013263c-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'c9a2558d9dbd4efba6aed4e4784c3c31'},
             {'duid': '20181207-e0b5432c-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a43674315abe4f3892f4151472fc0ac8'},
             {'duid': '20181207-e15a5128-f9cf-11e8-bf1c-ea00e4d87701', 'token': '2c633e95b00c4854a3c90150d7b69a0e'},
             {'duid': '20181207-e1f2145e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '67aa6de1f4504584813966d45691f0c1'},
             {'duid': '20181207-e28afa98-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd5b7ba6d2f614b58bbec82ce5e3588bd'},
             {'duid': '20181207-e330e2d2-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4c0d507f8baa4efa8271fc4f234ab458'},
             {'duid': '20181207-e3d5d620-f9cf-11e8-bf1c-ea00e4d87701', 'token': '5ad80d96f53a4038a53983fef3f89de1'},
             {'duid': '20181207-e476e132-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7bd03d92e21242ecb7300119bf3e429a'},
             {'duid': '20181207-e50e3ee2-f9cf-11e8-bf1c-ea00e4d87701', 'token': '581165ad7b5747ceb90b73d17d6311ed'},
             {'duid': '20181207-e5a54986-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'de18cc61e5df477b8f24336ceb6241cb'},
             {'duid': '20181207-e63c7112-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9d68a1ab6de347dc95c8844f981cebee'},
             {'duid': '20181207-e6d471ba-f9cf-11e8-bf1c-ea00e4d87701', 'token': '97192087f8d94513a6f5c920f10b3e2d'},
             {'duid': '20181207-e77d41be-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'bd93f55151204fee88f6a76bb24f713c'},
             {'duid': '20181207-e81b378e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'fff249afba9040d6a06cf0b564467875'},
             {'duid': '20181207-e8b34934-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3ced3d2e6b384599b0460f3f50bae811'},
             {'duid': '20181207-e960413e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e1e8d1418df945f6baaf54a9c70f3c51'},
             {'duid': '20181207-e9f94884-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f4af3c34c40247fe99bc1c98044672ef'},
             {'duid': '20181207-ea900fc6-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'df9a783fcb4b42caa1f11871a2c943aa'},
             {'duid': '20181207-eb2e1dd8-f9cf-11e8-bf1c-ea00e4d87701', 'token': '10a3121a36704de1bf176e78014c6a5f'},
             {'duid': '20181207-ebe431fe-f9cf-11e8-bf1c-ea00e4d87701', 'token': '525b6e9a652443aabb0bb9b587dcfdf3'},
             {'duid': '20181207-ec882ade-f9cf-11e8-bf1c-ea00e4d87701', 'token': '2c6661132d9544be88a13bfe69022ba9'},
             {'duid': '20181207-ed33d6fe-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ddfbde31406b4dd49dffd88d623669f3'},
             {'duid': '20181207-edeaea1a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '312cbcc95ec3410b86f0af10085aa16e'},
             {'duid': '20181207-ee842d88-f9cf-11e8-bf1c-ea00e4d87701', 'token': '2ad9598262194400917cf97d232dc748'},
             {'duid': '20181207-ef280eb2-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b5c7b5a19aca40a5a4ba45231312964d'},
             {'duid': '20181207-efc42e96-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e422a8e477494b80ad1c97c34f468a94'},
             {'duid': '20181207-f05c5824-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'cdcfbbfbe3b245f0801b91ce71c7df3b'},
             {'duid': '20181207-f10175d4-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'bf0733867b1949efa70a8aa2da13d67e'},
             {'duid': '20181207-f199bd76-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3edc7884dcb848aaa7872392252d6479'},
             {'duid': '20181207-f241ab6c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '0b7717c7a6df4ec69da6aba8ac0086bd'},
             {'duid': '20181207-f2d85788-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3c5e8507e9514d45819b87700253e59c'},
             {'duid': '20181207-f36dc2b4-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ed117fc93f2940708ea9e1d27b032693'},
             {'duid': '20181207-f40718c4-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b5921e7e3ad74c76a22aadacb39d29c7'},
             {'duid': '20181207-f49fe2f2-f9cf-11e8-bf1c-ea00e4d87701', 'token': '79b2749968974bbb811300f2e50d82dc'},
             {'duid': '20181207-f53889a8-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'af022830453d4ccc9daf28172aace9fa'},
             {'duid': '20181207-f5d7511e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1219172c713340a0bccd434fc5643b55'},
             {'duid': '20181207-f68234da-f9cf-11e8-bf1c-ea00e4d87701', 'token': '107bb97615e04cc2bb46bf53bd59af17'},
             {'duid': '20181207-f7176dd4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '31d2febb7fef48c4a0412b65058b1945'},
             {'duid': '20181207-f7b31914-f9cf-11e8-bf1c-ea00e4d87701', 'token': '62c515cb898f4fb8a7d5a39224b12d14'},
             {'duid': '20181207-f85223e2-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ea823346d45f4fddbcfb90d9e78dda7c'},
             {'duid': '20181207-f8ef4672-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd0aa91c8a5a54c8c9578b45e6c83aab7'},
             {'duid': '20181207-f98777e4-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b5d785c24a784e95a670dcf1f9ebf1bb'},
             {'duid': '20181207-fa247fee-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'bad75dead5124f5690379e3d6a669d6b'},
             {'duid': '20181207-fabb2c46-f9cf-11e8-bf1c-ea00e4d87701', 'token': '5a2df56c45694994a69a91946dd4f2e9'},
             {'duid': '20181207-fb6cb150-f9cf-11e8-bf1c-ea00e4d87701', 'token': '29bbe7fe15444544a3b4fc77d4038a5d'},
             {'duid': '20181207-fc0cda0e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '2447b756da7549c2b27d6ec3f0ba9c24'},
             {'duid': '20181207-fcb50526-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'c17aaa84225a4ffba71f29840c9a05dc'},
             {'duid': '20181207-fd605c50-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ff844ef4c9e44ffbb3fe1b9cbdf90a1a'},
             {'duid': '20181207-fe046660-f9cf-11e8-bf1c-ea00e4d87701', 'token': '04d5af30c98c4d6ea8d24f7ffa7ecad3'},
             {'duid': '20181207-fe9d9984-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9878838bf9384974b5ff212ca5aedd07'},
             {'duid': '20181207-ff347dfe-f9cf-11e8-bf1c-ea00e4d87701', 'token': '61beb028c6864ce3a6e58aef1f17ff30'},
             {'duid': '20181207-ffc9cc2e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7657d099989e42f5997245ce2c03453d'},
             {'duid': '20181207-00624742-f9d0-11e8-bf1c-ea00e4d87701', 'token': '971103b5c047401f9a12da74db2411dd'},
             {'duid': '20181207-0101e554-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'baec8ef234464ca2b8c68171e9340a32'},
             {'duid': '20181207-019e1fe6-f9d0-11e8-bf1c-ea00e4d87701', 'token': '36e3afd25ffe403cb20a599f167887bd'},
             {'duid': '20181207-0234e9a8-f9d0-11e8-bf1c-ea00e4d87701', 'token': '95df8f6a2f744903953c45e69a1e5258'},
             {'duid': '20181207-02ca1cf8-f9d0-11e8-bf1c-ea00e4d87701', 'token': '6d70274049894d6bbe14848e62eda3a3'},
             {'duid': '20181207-03600f56-f9d0-11e8-bf1c-ea00e4d87701', 'token': '0735b6856541424594f12a5f350f3729'},
             {'duid': '20181207-03fa163c-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'bcd5f8794d214dd4bdb31cea139a0e53'},
             {'duid': '20181207-049281a6-f9d0-11e8-bf1c-ea00e4d87701', 'token': '11c2399d149241249ba7e823041ef552'},
             {'duid': '20181207-052b381a-f9d0-11e8-bf1c-ea00e4d87701', 'token': '3e23f335ec774879acca99d51b2ec865'},
             {'duid': '20181207-05c4311e-f9d0-11e8-bf1c-ea00e4d87701', 'token': '5006e85cd46b4b3c9a6db55def8186ad'},
             {'duid': '20181207-065b9b8a-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'e663d54862c6493eba51ad0eaebfb02f'},
             {'duid': '20181207-06f4ae1a-f9d0-11e8-bf1c-ea00e4d87701', 'token': '07e85b59d18045c985e693397cc77700'},
             {'duid': '20181207-078c3e10-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'f150033547f4454684dc2e46b7ad238e'},
             {'duid': '20181207-082e2cb6-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'b78e5199ba064540901c2b2ce8c2468a'},
             {'duid': '20181207-08da10b2-f9d0-11e8-bf1c-ea00e4d87701', 'token': '2006b1fdf538458192fca6f698dacc73'},
             {'duid': '20181207-097b0292-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'd468044ea5c547bba801d952ffc8ffae'},
             {'duid': '20181207-0a1fc20a-f9d0-11e8-bf1c-ea00e4d87701', 'token': '652184602554477588f1eec251d12d25'},
             {'duid': '20181207-0ada90b2-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'c02a77c085cc46c983778cf649f104ec'},
             {'duid': '20181207-0b992fe0-f9d0-11e8-bf1c-ea00e4d87701', 'token': '8fd873cb0517447a875408ed4a5c9d00'},
             {'duid': '20181207-0c3b11fc-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'a653469fb0964abe97adb79cd989eddf'},
             {'duid': '20181207-0cd2a288-f9d0-11e8-bf1c-ea00e4d87701', 'token': '5fa9eb81854a4957af6a6120e77c5cb8'},
             {'duid': '20181207-0d694c9c-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'fc54b587264844848a4f119cd8da3381'},
             {'duid': '20181207-0e00f9de-f9d0-11e8-bf1c-ea00e4d87701', 'token': '293c32ac3861482980906c1d412dcb23'},
             {'duid': '20181207-0eab4b64-f9d0-11e8-bf1c-ea00e4d87701', 'token': '90acea28275240c6aa28e0bac85cf260'},
             {'duid': '20181207-0f4af308-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'fbf095464f6540d3b407de11e91a0ec5'},
             {'duid': '20181207-0feed1d0-f9d0-11e8-bf1c-ea00e4d87701', 'token': '9e9089bc7c684a47a39a22f1db15f01d'},
             {'duid': '20181207-113f3f52-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'c640b10326174c93814a04ee73c0f12a'},
             {'duid': '20181207-11eaf284-f9d0-11e8-bf1c-ea00e4d87701', 'token': '7126578c99a044efbe1041eec358408e'},
             {'duid': '20181207-12969440-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'b29cd7f974e748aea94f23083980d190'},
             {'duid': '20181207-13420c6c-f9d0-11e8-bf1c-ea00e4d87701', 'token': '4454036fab40422a8e2c2718d352c21e'},
             {'duid': '20181207-13e3fdec-f9d0-11e8-bf1c-ea00e4d87701', 'token': '6cc1435e9e93488f928942392f5b502b'},
             {'duid': '20181207-149255fe-f9d0-11e8-bf1c-ea00e4d87701', 'token': '208a79bd87494868bbffa3662efd4f5c'},
             {'duid': '20181207-153bc5f8-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'eb0a2441a50540bb9513639f7f3e12e7'},
             {'duid': '20181207-15df10f0-f9d0-11e8-bf1c-ea00e4d87701', 'token': '43d65540b2134a9a9c18111f9c21a9b9'},
             {'duid': '20181207-167823a8-f9d0-11e8-bf1c-ea00e4d87701', 'token': '3ac63a5ef05e442499d9c4e1be0c6c48'},
             {'duid': '20181207-171afc0e-f9d0-11e8-bf1c-ea00e4d87701', 'token': '6045b6c7562e4203ab60d5b1d518ac07'},
             {'duid': '20181207-17b72dcc-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'b92cead82db149529db86d4239989b52'},
             {'duid': '20181207-185e5fde-f9d0-11e8-bf1c-ea00e4d87701', 'token': '7f52091306474750892fae5a7552bade'},
             {'duid': '20181207-1906ed2a-f9d0-11e8-bf1c-ea00e4d87701', 'token': '0a877c8233b14abf85660de6ffc9f381'},
             {'duid': '20181207-19a39328-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'c31b1a723090415bb4c8463f3cdd5f15'},
             {'duid': '20181207-1a4f1ea0-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'ba21e3afb7f245f9927f956808782962'}]

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
                                'DATA': {"token": [token], 'category': ['all'], 'index': [0], 'limit': [20]}}}},
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
                       'BODY': {'TYPE': 'JSON', 'FUNCTION': '5NUT', 'DATA': {'token': [token], 'title': ['baby']}}}},
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
