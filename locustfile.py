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

user_datas = [{'duid': '20181207-6a06f180-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7e435a5837a441fa9e3a92507a034803'},
              {'duid': '20181207-6b1499f6-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9be27af50ef74c04b3d63e2455bbd9ae'},
              {'duid': '20181207-6bce83c0-f9cf-11e8-bf1c-ea00e4d87701', 'token': '8907743731174b00b66dd3bab1fbd3df'},
              {'duid': '20181207-6c7a6f8c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '5dd4bb4f85e54df388a9e74c6075d24a'},
              {'duid': '20181207-6d265cb6-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd4a7e22fb6cf4f5ead5ee3d9a1a0c464'},
              {'duid': '20181207-6de1d5cc-f9cf-11e8-bf1c-ea00e4d87701', 'token': '5c173fc4f06d441ba2c7fd1c2238220d'},
              {'duid': '20181207-6e9d75ca-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ad789564dfcc4afaa532ed37c8e4fed5'},
              {'duid': '20181207-6f3965ac-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4985cf8482b6486992b19c8a4dc15fbe'},
              {'duid': '20181207-6fe57bb2-f9cf-11e8-bf1c-ea00e4d87701', 'token': '59dedb540b5849b08d2e94a3468a7626'},
              {'duid': '20181207-70a0a608-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7e5c70b3ee4f45cdab112c72c581d88c'},
              {'duid': '20181207-713d14de-f9cf-11e8-bf1c-ea00e4d87701', 'token': '809653e36d554731a3cd92972b3cc135'},
              {'duid': '20181207-71e8cb12-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3fa7dde5307e48ad8b4330b653913942'},
              {'duid': '20181207-72a3ba94-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4443228c45d94089a62188fa0977a3d1'},
              {'duid': '20181207-735ff092-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1581399b7118452a8b4d83a9b85a972a'},
              {'duid': '20181207-7403f160-f9cf-11e8-bf1c-ea00e4d87701', 'token': '253c7c9e90814e769f26c2ae808dc446'},
              {'duid': '20181207-74afeae2-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f038cda787fd4e6194feeee70381206e'},
              {'duid': '20181207-7563a5f0-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f5ae155627f542a484848d79d5bdc58e'},
              {'duid': '20181207-760f3460-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3101fe5cd75b44769f5339c278a3b987'},
              {'duid': '20181207-76cb3c28-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'db9883616cf247e4b716b0b3dddad6e7'},
              {'duid': '20181207-7776f69e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '44bdfe00a2c947568136cc02830b7eca'},
              {'duid': '20181207-7832754a-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'c6d2628d913247518f921c5fc61796e6'},
              {'duid': '20181207-78edae0a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '49500aeb0ffe4fa8a106b724c33226d9'},
              {'duid': '20181207-79a9430e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1a1b0b555cd545c9815f84fdd190e0a9'},
              {'duid': '20181207-7a558272-f9cf-11e8-bf1c-ea00e4d87701', 'token': '5e4334b178094df88c8a19db221af998'},
              {'duid': '20181207-7b10f408-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b732bb42ce4a4869a793b52fdb77fca4'},
              {'duid': '20181207-7bc4e436-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f5422133d8e94134986601dc4d0e9c76'},
              {'duid': '20181207-7c7851f6-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b71286f7b6a046358787f2e9fcaa05e7'},
              {'duid': '20181207-7d33fc6c-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd8584c3f1d34455da01b69ace8bc35bf'},
              {'duid': '20181207-7ddfa792-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e4207fac48454bedb21e8d2c3c57cbe4'},
              {'duid': '20181207-7e8b8cec-f9cf-11e8-bf1c-ea00e4d87701', 'token': '64f18459014e4782be7ea0264407deb0'},
              {'duid': '20181207-7f38d618-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'c316ecbc7d35497eaae27e6b00829ad3'},
              {'duid': '20181207-7fdf5790-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'c4b39d0a10204f0d939d1920e2f776b9'},
              {'duid': '20181207-809eaee2-f9cf-11e8-bf1c-ea00e4d87701', 'token': '185beb1cbd454528a232f8d58b3c50ef'},
              {'duid': '20181207-813b18a4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '194663ae4f004ea5b74c4328ac8aab48'},
              {'duid': '20181207-81d748c8-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a366f266f4ff4e54ae2104a698cde8ad'},
              {'duid': '20181207-8273999e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '03496b8e7582480bb98f3cbe8050a94c'},
              {'duid': '20181207-830e4ee4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '65e3071b355e4c318766b67b9567a881'},
              {'duid': '20181207-83cb13da-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e16397d3895e4016a539ecbc4a126242'},
              {'duid': '20181207-84773b6a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '0363da89a0164c14a48d2a5959a74224'},
              {'duid': '20181207-85137dd6-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b3d6e43ea5154bf5887553d6a00e44c2'},
              {'duid': '20181207-85ce9a26-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f91629ca1daa4b2d809fd85383cfc669'},
              {'duid': '20181207-86739288-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1e9246674bd044849b591619b7db6d44'},
              {'duid': '20181207-870f43d6-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ec75c767656747a187a19514de873f7e'},
              {'duid': '20181207-87c30560-f9cf-11e8-bf1c-ea00e4d87701', 'token': '99f414edd5e54697a3fe317e2bafac68'},
              {'duid': '20181207-886eed4e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '233ae8ff18d048e1ba0e634dbd9e6fcf'},
              {'duid': '20181207-890fa626-f9cf-11e8-bf1c-ea00e4d87701', 'token': '41b989f3917344a9afea37b8888b8601'},
              {'duid': '20181207-89b2de22-f9cf-11e8-bf1c-ea00e4d87701', 'token': '808d53ceb07b40b3b01ea2e700758db8'},
              {'duid': '20181207-8a62d71e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7485978c2d32491aba59633ad07d2dd7'},
              {'duid': '20181207-8b07380e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd38c2897fb6f43dc88c10b1cba9e2849'},
              {'duid': '20181207-8ba360d0-f9cf-11e8-bf1c-ea00e4d87701', 'token': '261159f44753466f8309a695f8df9c55'},
              {'duid': '20181207-8c471626-f9cf-11e8-bf1c-ea00e4d87701', 'token': '12b9a4f7400346439a69756cede00309'},
              {'duid': '20181207-8cf2f5fe-f9cf-11e8-bf1c-ea00e4d87701', 'token': '247f95116f9c4b368152c20ad1c154b7'},
              {'duid': '20181207-8da77d80-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd75beaa1e71347378af926bc0a263f3a'},
              {'duid': '20181207-8e42c98e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'de57c70e89474db987b4747374533c7d'},
              {'duid': '20181207-8ef6c060-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1f3c49a802314e36a6ff093ae409fc65'},
              {'duid': '20181207-8fae6bde-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9fc8621abb3e4e8880aeadfc22dd9ced'},
              {'duid': '20181207-905e0468-f9cf-11e8-bf1c-ea00e4d87701', 'token': '8dcb0b396b6e475c8c7ecb4732ab6a35'},
              {'duid': '20181207-90fa1394-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3e14fdfbf4df441c95215ce2c23c169e'},
              {'duid': '20181207-919657f4-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd6cd44763b4a407ca63ea18d617c21b5'},
              {'duid': '20181207-922f7fc4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '6ed0097d11ae40baa81c77046d40f5b9'},
              {'duid': '20181207-92ceec9e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ff259786fba74c14a69ede95475484d3'},
              {'duid': '20181207-936b6b1e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'dca68661d66a4964ba32e26243294b5d'},
              {'duid': '20181207-94073936-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'c25342076397421a992ed670438172eb'},
              {'duid': '20181207-94a3ed8a-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f2fcc03c8bd84477ab737ab1923cccd4'},
              {'duid': '20181207-953fe58c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4370404d8cc64600996a4944973fbb18'},
              {'duid': '20181207-963821c0-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1df9f5764acb4bd4acd00fb063331c1a'},
              {'duid': '20181207-96e60e20-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd6221befe99e42aa86244caf39875f22'},
              {'duid': '20181207-97927e9e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '22f5e5bc624a4fc0acc794d68bc8adfa'},
              {'duid': '20181207-983d9b80-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a6631c5ab0c543b9bc07463abee45eed'},
              {'duid': '20181207-98da0e20-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1bdaee5590cf4610aed5b859eccc1bd5'},
              {'duid': '20181207-99a4db00-f9cf-11e8-bf1c-ea00e4d87701', 'token': '6b532ceb344041fa99410820dcd55f4b'},
              {'duid': '20181207-9a605c5e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3150cc2a027d41b8bd4f9a8e4c09738e'},
              {'duid': '20181207-9b0c833a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '6ef7e8d7820e4f3ba3608a05215455b2'},
              {'duid': '20181207-9bb8a566-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e2dd678d1df946d586c6c384265b7a5b'},
              {'duid': '20181207-9c656a30-f9cf-11e8-bf1c-ea00e4d87701', 'token': '5991214c47014da9977394908c3d3463'},
              {'duid': '20181207-9cfe2ee6-f9cf-11e8-bf1c-ea00e4d87701', 'token': '814611462cfe478ea8099f1914776a79'},
              {'duid': '20181207-9dac6934-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ec12649105894639aaa2bafacbc575b3'},
              {'duid': '20181207-9e43b9ec-f9cf-11e8-bf1c-ea00e4d87701', 'token': '58e160ceec004bd58f5bd07cb0813414'},
              {'duid': '20181207-9edb4564-f9cf-11e8-bf1c-ea00e4d87701', 'token': '0b2a322360764ed58beca398d78b7cb9'},
              {'duid': '20181207-9f7f193c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '2fe400c927c64397baa56a374d7cebb9'},
              {'duid': '20181207-a03c71e4-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b7d41aff52734e0b8d5a0cf494afa53c'},
              {'duid': '20181207-a0f7e0fa-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3212d2552c854b37a19dc216198861b9'},
              {'duid': '20181207-a1e0428c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4d14be6bb2bb4a1697b6b26f9112d85a'},
              {'duid': '20181207-a27df5ae-f9cf-11e8-bf1c-ea00e4d87701', 'token': '54f20df76ece4a738ad55ef2e1a85b29'},
              {'duid': '20181207-a339ff92-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'c9c79c101bfa4137be925fae6c21b431'},
              {'duid': '20181207-a3edf43e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3bec15b40086407abdb3089fb84b663c'},
              {'duid': '20181207-a4a18dbe-f9cf-11e8-bf1c-ea00e4d87701', 'token': '63b531a33ae1407e95e417e928d934b5'},
              {'duid': '20181207-a55d314a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '2732e63458fa456c9382a324a47959ad'},
              {'duid': '20181207-a60903c6-f9cf-11e8-bf1c-ea00e4d87701', 'token': '207ce19992b94548834eb7fc5da2128c'},
              {'duid': '20181207-a6c46c60-f9cf-11e8-bf1c-ea00e4d87701', 'token': '67987def12744cfebab95a9f987afaec'},
              {'duid': '20181207-a7704706-f9cf-11e8-bf1c-ea00e4d87701', 'token': '11c92390d0434dc8a338cd6ae5167604'},
              {'duid': '20181207-a82bc864-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e89adceac45f464a90b65b2623d31de8'},
              {'duid': '20181207-a8d7e7d4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7c843f1c9f064b4b8331beb4539f0dd9'},
              {'duid': '20181207-a9934858-f9cf-11e8-bf1c-ea00e4d87701', 'token': '0515f7fef8c94b18b4772392dcdf360c'},
              {'duid': '20181207-aa475c94-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'fb20ed2f683546868585c9a0dc454274'},
              {'duid': '20181207-aafa7414-f9cf-11e8-bf1c-ea00e4d87701', 'token': '17e0db17fe944971a3e0ba48488625ab'},
              {'duid': '20181207-aba7162e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f61a21827dfb45829be9d9c849545789'},
              {'duid': '20181207-ac620f74-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b6b9a1a5056b4f998c4a18f955158154'},
              {'duid': '20181207-ad0e0ad6-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'c77248b5dac547649dee69b113ce6249'},
              {'duid': '20181207-adb9ca92-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd84fa4fb3d76477194e7784aef64ffdb'},
              {'duid': '20181207-ae5f86f8-f9cf-11e8-bf1c-ea00e4d87701', 'token': '805b99a3e0c24206b91a19fe5ee32013'},
              {'duid': '20181207-af09e756-f9cf-11e8-bf1c-ea00e4d87701', 'token': '75d094bda90f473ab1e43e78415adf63'},
              {'duid': '20181207-afad9f36-f9cf-11e8-bf1c-ea00e4d87701', 'token': '55138050e53b437f86790687640e9e6c'},
              {'duid': '20181207-b057b8a4-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a68cde31452045deae87184dcc59ea3e'},
              {'duid': '20181207-b0f5c404-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'fb61224a888f41d0ba925db35ec379e8'},
              {'duid': '20181207-b1a9f726-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e8893e0d3d504971b563cc0a7d904cb6'},
              {'duid': '20181207-b24dc310-f9cf-11e8-bf1c-ea00e4d87701', 'token': '77ed4cdf998346a6a9c6328ec219f1ca'},
              {'duid': '20181207-b2f9abda-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4dac942840354a47a28cae0bb8eca7f5'},
              {'duid': '20181207-b3b52e0a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '5b1fc7ca16e7429594c463577ab280e2'},
              {'duid': '20181207-b468e76a-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e25135fad68045f5a21e6d8a92484d84'},
              {'duid': '20181207-b51c8126-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a1f5ca087d1d4d9198b7c4162d36b58f'},
              {'duid': '20181207-b5c81590-f9cf-11e8-bf1c-ea00e4d87701', 'token': '89d0ae5f6027475f9450705e150a0f3a'},
              {'duid': '20181207-b674254c-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e115a3aebff74551a61b44394b3739c3'},
              {'duid': '20181207-b718a450-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1be4affde9634618bd09fa7e79b6c34a'},
              {'duid': '20181207-b7bc71de-f9cf-11e8-bf1c-ea00e4d87701', 'token': '096f8c9cf1ca454ab1eca93b76203605'},
              {'duid': '20181207-b869e3fa-f9cf-11e8-bf1c-ea00e4d87701', 'token': '242ac7c55d5a4a25bef2ce3d93b095f9'},
              {'duid': '20181207-b9059a84-f9cf-11e8-bf1c-ea00e4d87701', 'token': '87a3a4881be24c0ea82cf040cff2412c'},
              {'duid': '20181207-b9b06324-f9cf-11e8-bf1c-ea00e4d87701', 'token': '6410df3e609143d68a1196f93632e9ac'},
              {'duid': '20181207-ba641e32-f9cf-11e8-bf1c-ea00e4d87701', 'token': '771a71267f204ceaa9a0916d12d2608a'},
              {'duid': '20181207-bb17c7b6-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9dab51e11103409c9c9c5e50c5c48051'},
              {'duid': '20181207-bbd2f7d4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '5e0bbb12d7944b5e9e87a9b509b8a815'},
              {'duid': '20181207-bc7ef0e8-f9cf-11e8-bf1c-ea00e4d87701', 'token': '34eb7b984e474499894e5983c4fad5b4'},
              {'duid': '20181207-bd3acd86-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a9c1611c92ab4838999a2245aea3ad6d'},
              {'duid': '20181207-bdf628f6-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7410d0f9234d458b80f6093d9fae6d22'},
              {'duid': '20181207-bf1f89de-f9cf-11e8-bf1c-ea00e4d87701', 'token': '60400a16f28641aa86e934bf50fad71c'},
              {'duid': '20181207-c0118108-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'c9976297fef244c99ae65cae75500f1e'},
              {'duid': '20181207-c0d8a990-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ac37842288c14d1a80491fb1254761b1'},
              {'duid': '20181207-c1bf0fac-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9cae8a792eb54ee69133e5c2e7379eb1'},
              {'duid': '20181207-c299b7ce-f9cf-11e8-bf1c-ea00e4d87701', 'token': '83ab4f00ce9d4fe8abb20c209a3e7b1b'},
              {'duid': '20181207-c3759384-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4f6089225ecf4032952997365d8500ed'},
              {'duid': '20181207-c45ebde8-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4d70667679ae4479b24e8d2ec4d7730d'},
              {'duid': '20181207-c5438e50-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd40ea2abfe9b45a28030c03f84d412cc'},
              {'duid': '20181207-c623fdb4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '52cdb7a8ece847a39a4692a8b07adcd2'},
              {'duid': '20181207-c6ff682c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9ca6e6fe77674a66ab00035dbd8c206e'},
              {'duid': '20181207-c7c9b9e2-f9cf-11e8-bf1c-ea00e4d87701', 'token': '92563fc154ae4cba9d45ac3c0273e833'},
              {'duid': '20181207-c8c3bf46-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b092dc6130b84324b2c60619a55f55c7'},
              {'duid': '20181207-c99fc86a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '0ca8d2acfe35409c8608a1211c90e9e7'},
              {'duid': '20181207-ca5de502-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'df9be8eed8564428a90f1faf4f2fd9d1'},
              {'duid': '20181207-cb35e06a-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ebbd697a43614d5abc031645c8adb0ee'},
              {'duid': '20181207-cc0f6088-f9cf-11e8-bf1c-ea00e4d87701', 'token': '10790629f60f4de580c485ee4f775cb2'},
              {'duid': '20181207-ccdc08fe-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b398200c3fd245f7984da36ee63555e8'},
              {'duid': '20181207-cdbcb322-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd02b5d66aa484bbda5557b2ecabba481'},
              {'duid': '20181207-ce999e5e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '0fe6973b2b39441dae54fba49368b76c'},
              {'duid': '20181207-cf6ceab6-f9cf-11e8-bf1c-ea00e4d87701', 'token': '82c7831b129d4cd9b6d16c5a3f3f60ec'},
              {'duid': '20181207-d035e7fe-f9cf-11e8-bf1c-ea00e4d87701', 'token': '0f90245b65a347d6ab921726aeba7a10'},
              {'duid': '20181207-d100f93a-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'fd302288e80a4e94ab5adac6009c6d63'},
              {'duid': '20181207-d1bca572-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7e90ef22db9b4ee1b4aed894f7bff4f2'},
              {'duid': '20181207-d25904d0-f9cf-11e8-bf1c-ea00e4d87701', 'token': '694c036728dc473e9e4d38fb9a6ae81d'},
              {'duid': '20181207-d308e936-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b015cdef76f74aeaa2db347d7862aaae'},
              {'duid': '20181207-d3b8e0e8-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f78ed78ee4a44e84a36699942c521c2f'},
              {'duid': '20181207-d4549218-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1ae612cdd425480da485049ba2a40168'},
              {'duid': '20181207-d4f16d7c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '17db05087a1f4e9895450d73e3c69e9d'},
              {'duid': '20181207-d594ef42-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ded455a601de401c8aa41a51dbb54da7'},
              {'duid': '20181207-d650a296-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e04ace7860af4287b5a8fabfc956ba18'},
              {'duid': '20181207-d703dc26-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b94a59c8f04141a4ac46474a948600b8'},
              {'duid': '20181207-d7b7ee96-f9cf-11e8-bf1c-ea00e4d87701', 'token': '0e784aa323664cd988033630e45a65de'},
              {'duid': '20181207-d8616e80-f9cf-11e8-bf1c-ea00e4d87701', 'token': '536f0d51f2c84f9a86d45e1f4ca20504'},
              {'duid': '20181207-d91f210a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '152e03307f464da7ac0823841f1c0927'},
              {'duid': '20181207-d9cb11f4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7f2458a6fc9b4924b3f72eca76cc1889'},
              {'duid': '20181207-de493df0-f9cf-11e8-bf1c-ea00e4d87701', 'token': '365c7908a2f14a6caea680ee6693461d'},
              {'duid': '20181207-dee17eee-f9cf-11e8-bf1c-ea00e4d87701', 'token': '0ac1610b80244287877a2e2055f99e96'},
              {'duid': '20181207-df78da6e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'c3a427c41fd04541928481456e968edf'},
              {'duid': '20181207-e013263c-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b119030df5d74704b64ae281b9066a28'},
              {'duid': '20181207-e0b5432c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '57d145f5f11440c387aedb77dff87916'},
              {'duid': '20181207-e15a5128-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9f862f07cfbc4fa685c8a3e1b0b7a9d9'},
              {'duid': '20181207-e1f2145e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7d0e1b483b3444eea24253f6d8b8d21f'},
              {'duid': '20181207-e28afa98-f9cf-11e8-bf1c-ea00e4d87701', 'token': '23f2c4d28e0149d38e696566c067160d'},
              {'duid': '20181207-e330e2d2-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f08229e9802e4a859651cd2a81d446b1'},
              {'duid': '20181207-e3d5d620-f9cf-11e8-bf1c-ea00e4d87701', 'token': '63e043cb083c49e68643a9f3e90fac24'},
              {'duid': '20181207-e476e132-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3ac7ba4d86d249a9ad6aab67cc90c77a'},
              {'duid': '20181207-e50e3ee2-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'adea5ceb515947ea85e3ef4f270f1824'},
              {'duid': '20181207-e5a54986-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7149ce92005c4625ba050a8fc4a25802'},
              {'duid': '20181207-e63c7112-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9378233816d440d498371a5d4be3fc05'},
              {'duid': '20181207-e6d471ba-f9cf-11e8-bf1c-ea00e4d87701', 'token': '6a24b15f75dd4b0a8a3f24c1adae0210'},
              {'duid': '20181207-e77d41be-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a8d6b9e7f3244306ad11d3e1a019a7d5'},
              {'duid': '20181207-e81b378e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ce7a7a6fce7447f388b2c48a78ac0364'},
              {'duid': '20181207-e8b34934-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd1b60de75d9c4a98899bc07feb0d920e'},
              {'duid': '20181207-e960413e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4d9fe434346f4e2bbc4d1a72aa2fee6e'},
              {'duid': '20181207-e9f94884-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'febadfb338ca4dd181a605d6a42cf824'},
              {'duid': '20181207-ea900fc6-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd8e7fbab1c4d441ebae02fee411bd4ca'},
              {'duid': '20181207-eb2e1dd8-f9cf-11e8-bf1c-ea00e4d87701', 'token': '5278d01280fa494086f997e6d12e5952'},
              {'duid': '20181207-ebe431fe-f9cf-11e8-bf1c-ea00e4d87701', 'token': '10a904fc195348bba80fd211b5e99861'},
              {'duid': '20181207-ec882ade-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7ebe5e5ad4b24b7eacb73e72407ac37c'},
              {'duid': '20181207-ed33d6fe-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b1d40dd1ac7843e7aacd091efde65311'},
              {'duid': '20181207-edeaea1a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '57e0baf186364c0d8c325e748dd18e24'},
              {'duid': '20181207-ee842d88-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9fe683b524ff4286b9ae4d8b4945ef8d'},
              {'duid': '20181207-ef280eb2-f9cf-11e8-bf1c-ea00e4d87701', 'token': '046923211af447b78338e2d1b9f2692e'},
              {'duid': '20181207-efc42e96-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7920a2c9583040b59c01d87c0208d422'},
              {'duid': '20181207-f05c5824-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3f7e1abf172c4b6fbb5f4f5c1acc4fc9'},
              {'duid': '20181207-f10175d4-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b859059bd28e4e18bb7e891452050877'},
              {'duid': '20181207-f199bd76-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4c1bc696b4c74d79822119abf63173ef'},
              {'duid': '20181207-f241ab6c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '255b02ab18d24255806d2104b8aaba63'},
              {'duid': '20181207-f2d85788-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'fc2fa266be1347fe8305b0e7e5ea4341'},
              {'duid': '20181207-f36dc2b4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '8a47659e1aa1435084ace10901a8df95'},
              {'duid': '20181207-f40718c4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7c671ee70a6e417685dc255cb6300136'},
              {'duid': '20181207-f49fe2f2-f9cf-11e8-bf1c-ea00e4d87701', 'token': '065a6669ca9348b089941728f18f1172'},
              {'duid': '20181207-f53889a8-f9cf-11e8-bf1c-ea00e4d87701', 'token': '8a3358cf47ec46fc96642427bdd69291'},
              {'duid': '20181207-f5d7511e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '188b32f33f8348e7abbd9e5c61c6d3f1'},
              {'duid': '20181207-f68234da-f9cf-11e8-bf1c-ea00e4d87701', 'token': '99a08c2a27274f5ab560d3279ad08d02'},
              {'duid': '20181207-f7176dd4-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'cab66aac6bc04c6ea6306ca8bc36b191'},
              {'duid': '20181207-f7b31914-f9cf-11e8-bf1c-ea00e4d87701', 'token': '8b22c8f6c7f44ab48f30362f43dd95d5'},
              {'duid': '20181207-f85223e2-f9cf-11e8-bf1c-ea00e4d87701', 'token': '394c3dec86cb495598a155d8de39ac1d'},
              {'duid': '20181207-f8ef4672-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ead02e29659349528793d497b38fa690'},
              {'duid': '20181207-f98777e4-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a52f23947ede4bc5a7cc996db79d2c31'},
              {'duid': '20181207-fa247fee-f9cf-11e8-bf1c-ea00e4d87701', 'token': '655d2f37e2d14c8b8d5a8560e72f6efc'},
              {'duid': '20181207-fabb2c46-f9cf-11e8-bf1c-ea00e4d87701', 'token': '47b8ecf5e73a468e8a02ffff9f60e0fb'},
              {'duid': '20181207-fb6cb150-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'dfd72f94989c42e1ab802f7b725a33d3'},
              {'duid': '20181207-fc0cda0e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '438110618e91427697b5d49c020801a2'},
              {'duid': '20181207-fcb50526-f9cf-11e8-bf1c-ea00e4d87701', 'token': '5bd2fe11c4184b9c86a0e94f8456db83'},
              {'duid': '20181207-fd605c50-f9cf-11e8-bf1c-ea00e4d87701', 'token': '36acc1d9d798423aa978826f7aa620b1'},
              {'duid': '20181207-fe046660-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'bd689fd3e23d4877a14ef89428e89d73'},
              {'duid': '20181207-fe9d9984-f9cf-11e8-bf1c-ea00e4d87701', 'token': '95079fe274104ae6ab9e52f48d23008d'},
              {'duid': '20181207-ff347dfe-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3bd7b00528bf4b46a4c5e79d14914681'},
              {'duid': '20181207-ffc9cc2e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f3af6412dd0b4b2da851aa3e9480ae92'},
              {'duid': '20181207-00624742-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'c267f8f49fb2457186cbd3616449d3a0'},
              {'duid': '20181207-0101e554-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'c3df883232db400bac5bec53ce9fd199'},
              {'duid': '20181207-019e1fe6-f9d0-11e8-bf1c-ea00e4d87701', 'token': '10960dce40914da9829e4e6974d03558'},
              {'duid': '20181207-0234e9a8-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'ce04dbc565324bac8f35b5a10bdec499'},
              {'duid': '20181207-02ca1cf8-f9d0-11e8-bf1c-ea00e4d87701', 'token': '3a6ca5d8d2ee40d1befdd1fb541080b4'},
              {'duid': '20181207-03600f56-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'a1db7b5abb6b4cd6b0a072f4cd850064'},
              {'duid': '20181207-03fa163c-f9d0-11e8-bf1c-ea00e4d87701', 'token': '9b23f174fcc54e349c70c50466edf1a3'},
              {'duid': '20181207-049281a6-f9d0-11e8-bf1c-ea00e4d87701', 'token': '894d6ec0a412451ab51a1be02c3b9549'},
              {'duid': '20181207-052b381a-f9d0-11e8-bf1c-ea00e4d87701', 'token': '4a83530b34c84ada80e833ce7f523e33'},
              {'duid': '20181207-05c4311e-f9d0-11e8-bf1c-ea00e4d87701', 'token': '29ff9329ed364a9e9c17b0b7176e3239'},
              {'duid': '20181207-065b9b8a-f9d0-11e8-bf1c-ea00e4d87701', 'token': '2c990e92945a4ad693845909d6bb3bb7'},
              {'duid': '20181207-06f4ae1a-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'bf222a507e204c7daa1e1034ad708b57'},
              {'duid': '20181207-078c3e10-f9d0-11e8-bf1c-ea00e4d87701', 'token': '85d2f462d4d04c0d88cad6bb5b331341'},
              {'duid': '20181207-082e2cb6-f9d0-11e8-bf1c-ea00e4d87701', 'token': '34b9d2eb01c840f5a6eac665f3c016fd'},
              {'duid': '20181207-08da10b2-f9d0-11e8-bf1c-ea00e4d87701', 'token': '29ca3cd1873d4c8dbdfb19c2d9aa67b6'},
              {'duid': '20181207-097b0292-f9d0-11e8-bf1c-ea00e4d87701', 'token': '4fdcf6c021ee4899948ecb4786c0e801'},
              {'duid': '20181207-0a1fc20a-f9d0-11e8-bf1c-ea00e4d87701', 'token': '192f530a2dc04e519a165a2b6ee9a68f'},
              {'duid': '20181207-0ada90b2-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'e4714358f26145ffbe0aba920887ea3e'},
              {'duid': '20181207-0b992fe0-f9d0-11e8-bf1c-ea00e4d87701', 'token': '244601c53cd94338ac4f5047d87c495c'},
              {'duid': '20181207-0c3b11fc-f9d0-11e8-bf1c-ea00e4d87701', 'token': '25eb02ac18794a54a36162b38e5a6193'},
              {'duid': '20181207-0cd2a288-f9d0-11e8-bf1c-ea00e4d87701', 'token': '46ad263beac64d43899aaf319ad29c1b'},
              {'duid': '20181207-0d694c9c-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'ca3fc9043da1485a940abcad8a1f6781'},
              {'duid': '20181207-0e00f9de-f9d0-11e8-bf1c-ea00e4d87701', 'token': '3df3a9623c144a95a87e9fd637774f7e'},
              {'duid': '20181207-0eab4b64-f9d0-11e8-bf1c-ea00e4d87701', 'token': '553cc87eae564fb2bec73b663c6697f9'},
              {'duid': '20181207-0f4af308-f9d0-11e8-bf1c-ea00e4d87701', 'token': '3a424ecf6c8c4ef98845a7ddffc2eeb7'},
              {'duid': '20181207-0feed1d0-f9d0-11e8-bf1c-ea00e4d87701', 'token': '21e3f22b173847df988465d7bc515a11'},
              {'duid': '20181207-113f3f52-f9d0-11e8-bf1c-ea00e4d87701', 'token': '6f4b189bb9454ad1b4e535d97a5def67'},
              {'duid': '20181207-11eaf284-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'b08c0b5ec62643b69a95d678788f14e9'},
              {'duid': '20181207-12969440-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'ab9d2c03a6464324b5efeb21f0c7c4c1'},
              {'duid': '20181207-13420c6c-f9d0-11e8-bf1c-ea00e4d87701', 'token': '34818e171a654ac599e3e8831b7aa63f'},
              {'duid': '20181207-13e3fdec-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'f78209cfc47f4e908d45e6c014211440'},
              {'duid': '20181207-149255fe-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'dc75ad6bb19a4b4592f8fe3bcb2b3f21'},
              {'duid': '20181207-153bc5f8-f9d0-11e8-bf1c-ea00e4d87701', 'token': '994f63ad5c784a32b3989bb0304c95bf'},
              {'duid': '20181207-15df10f0-f9d0-11e8-bf1c-ea00e4d87701', 'token': '1706e4e6f325485bb3a210828a474eda'},
              {'duid': '20181207-167823a8-f9d0-11e8-bf1c-ea00e4d87701', 'token': '1ee014c74d354f5d956585ca958d8c3a'},
              {'duid': '20181207-171afc0e-f9d0-11e8-bf1c-ea00e4d87701', 'token': '41712c8236be45e5a617f716a1247b99'},
              {'duid': '20181207-17b72dcc-f9d0-11e8-bf1c-ea00e4d87701', 'token': '4bd83eadad5e4829857cb0363c6bf091'},
              {'duid': '20181207-185e5fde-f9d0-11e8-bf1c-ea00e4d87701', 'token': '19673848f9274e8a9538e408413e6656'},
              {'duid': '20181207-1906ed2a-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'f89a06fd19c842f7a2626028feaee2ee'},
              {'duid': '20181207-19a39328-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'a2917571f538416e8329c82e43b17ce4'},
              {'duid': '20181207-1a4f1ea0-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'd48e3154e10a4fd0950e68c3283d83f9'}]

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
                                'DATA': {"token": [token], 'category': ['test'], 'index': [0], 'limit': [20]}}}},
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
