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

user_datas = [{'duid': '20181207-6a06f180-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7620af4083754abcb33d33bda96bf55c'},
              {'duid': '20181207-6b1499f6-f9cf-11e8-bf1c-ea00e4d87701', 'token': '5a19208aa2f24248bfcaba7b8f1df8da'},
              {'duid': '20181207-6bce83c0-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'efe0f8f5ff654d1ab485786f82311be3'},
              {'duid': '20181207-6c7a6f8c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7333facbb0e94ba583b6087608714028'},
              {'duid': '20181207-6d265cb6-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7dd688f2009b4432853106f7e1ce64cc'},
              {'duid': '20181207-6de1d5cc-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1a183d4498114b038b8294a112bc30f7'},
              {'duid': '20181207-6e9d75ca-f9cf-11e8-bf1c-ea00e4d87701', 'token': '64ed6937beb342aaba5af5328037bfdd'},
              {'duid': '20181207-6f3965ac-f9cf-11e8-bf1c-ea00e4d87701', 'token': '0cd6f3d8e5424e13bf58cb1edc5698c0'},
              {'duid': '20181207-6fe57bb2-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1cb1a422ed6545839932786339fa7408'},
              {'duid': '20181207-70a0a608-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4151c7aba13b445a8a144c59673a50a0'},
              {'duid': '20181207-713d14de-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f0b5c096a2c148fab4bb31229c6e49e4'},
              {'duid': '20181207-71e8cb12-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a561c9eacb1d419294964620ced009d2'},
              {'duid': '20181207-72a3ba94-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd958fe8b69a54e47bad4bb8f9662d625'},
              {'duid': '20181207-735ff092-f9cf-11e8-bf1c-ea00e4d87701', 'token': '71c8f50d35b6402d97e448222875db08'},
              {'duid': '20181207-7403f160-f9cf-11e8-bf1c-ea00e4d87701', 'token': '92ad1793e9fe4a4ea94a0929bbd04834'},
              {'duid': '20181207-74afeae2-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'fff332a5ff18404b90c7c699eb986a16'},
              {'duid': '20181207-7563a5f0-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b98f4adf2e1844f795f3dd45943fa35b'},
              {'duid': '20181207-760f3460-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7708f623a86c453e9c35579e0d56ea1a'},
              {'duid': '20181207-76cb3c28-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b3344fa50889445e84db977bf224645b'},
              {'duid': '20181207-7776f69e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '2bf51cbb5cd245dab7aced282b89dd0f'},
              {'duid': '20181207-7832754a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4c32d8ed874446379b05cc9ee9fc8b16'},
              {'duid': '20181207-78edae0a-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f49db52e7ca8446dab8371b93ef7abb0'},
              {'duid': '20181207-79a9430e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a2a2cf434ccc456499d42de89acdfa0d'},
              {'duid': '20181207-7a558272-f9cf-11e8-bf1c-ea00e4d87701', 'token': '6a7b2b5f742c4f36ae9c75f84195dd09'},
              {'duid': '20181207-7b10f408-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'aa5dbbe68cb9416ca508d3d95007c9b2'},
              {'duid': '20181207-7bc4e436-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f7fb59ec4e2942bab3d5a86e79242089'},
              {'duid': '20181207-7c7851f6-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4511abaaceb7402785886d8294d77208'},
              {'duid': '20181207-7d33fc6c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '750309064a2547e99a21431ebab51a72'},
              {'duid': '20181207-7ddfa792-f9cf-11e8-bf1c-ea00e4d87701', 'token': '20ebdb0f4a88436f911319be8c5bc086'},
              {'duid': '20181207-7e8b8cec-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e4fe7699a306459ea1d40e0ea35ef6ad'},
              {'duid': '20181207-7f38d618-f9cf-11e8-bf1c-ea00e4d87701', 'token': '0fd6f418068e43df942ce91c4c20011d'},
              {'duid': '20181207-7fdf5790-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'be12fe9e7fc543779cf69eec5b67d4c0'},
              {'duid': '20181207-809eaee2-f9cf-11e8-bf1c-ea00e4d87701', 'token': '0a6e3389a93143c98853e850573a540e'},
              {'duid': '20181207-813b18a4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3c4e9bd649e0488aaf5147e5a24dde3d'},
              {'duid': '20181207-81d748c8-f9cf-11e8-bf1c-ea00e4d87701', 'token': '22325987323845e9bcf264715a72c020'},
              {'duid': '20181207-8273999e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b3192e224d584bdda97429b309eac2ea'},
              {'duid': '20181207-830e4ee4-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b7caa911d643469cb90ecd400873c64b'},
              {'duid': '20181207-83cb13da-f9cf-11e8-bf1c-ea00e4d87701', 'token': '33a1573da5ab4b27a5497bf6c01205da'},
              {'duid': '20181207-84773b6a-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'be4207a544504b449c7585463dd4fbd2'},
              {'duid': '20181207-85137dd6-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e0b4c447b7a14e2abab02fe18def7b4d'},
              {'duid': '20181207-85ce9a26-f9cf-11e8-bf1c-ea00e4d87701', 'token': '34966aba4626400a9224cf3642fc2d39'},
              {'duid': '20181207-86739288-f9cf-11e8-bf1c-ea00e4d87701', 'token': '2a13d3ade17a494e9818225fca11bb5c'},
              {'duid': '20181207-870f43d6-f9cf-11e8-bf1c-ea00e4d87701', 'token': '08979306e1c945e1abfcef5a83f27084'},
              {'duid': '20181207-87c30560-f9cf-11e8-bf1c-ea00e4d87701', 'token': '30d436b7b8504bd1b8816be2d50ad5d9'},
              {'duid': '20181207-886eed4e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'beffa1149f334eb8937af696670bf3ba'},
              {'duid': '20181207-890fa626-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'cd39e7fca9764029a5cde4d9f47638ae'},
              {'duid': '20181207-89b2de22-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ecfca6dbfe4c4c41804e38f3c663c864'},
              {'duid': '20181207-8a62d71e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd1f3de8cb71941a3bc647c506ce84146'},
              {'duid': '20181207-8b07380e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '5298ba715a8942c5957db995200ef939'},
              {'duid': '20181207-8ba360d0-f9cf-11e8-bf1c-ea00e4d87701', 'token': '97b75162293a40b3b44b9bf1f6735709'},
              {'duid': '20181207-8c471626-f9cf-11e8-bf1c-ea00e4d87701', 'token': '69179e883574404c84ad024739e4367c'},
              {'duid': '20181207-8cf2f5fe-f9cf-11e8-bf1c-ea00e4d87701', 'token': '5bcedcd3892c4e3580a257728427eb2b'},
              {'duid': '20181207-8da77d80-f9cf-11e8-bf1c-ea00e4d87701', 'token': '8ac677920f32412a9651ee899047de79'},
              {'duid': '20181207-8e42c98e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7d76b3e0c3744ac6b2ef69b60a426fe6'},
              {'duid': '20181207-8ef6c060-f9cf-11e8-bf1c-ea00e4d87701', 'token': '22f0558770814512ba57de47fd1648a0'},
              {'duid': '20181207-8fae6bde-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd09faf61b9fa4e5d9b39dc58f6084d10'},
              {'duid': '20181207-905e0468-f9cf-11e8-bf1c-ea00e4d87701', 'token': '64ab7b98f95547a4b64feba29612634d'},
              {'duid': '20181207-90fa1394-f9cf-11e8-bf1c-ea00e4d87701', 'token': '63c6e6b0b4f34be28944228aad0e9903'},
              {'duid': '20181207-919657f4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9a334bb32c664f14999c546fa29aa4ba'},
              {'duid': '20181207-922f7fc4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '60c7a254afba42b6a6ac917f300572fc'},
              {'duid': '20181207-92ceec9e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '2d3cf0b710fb41cc91be22e51227f075'},
              {'duid': '20181207-936b6b1e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '5a051a0e90e343deaeea84cb22bb9d93'},
              {'duid': '20181207-94073936-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ab49893610b041449653d33aacf966ea'},
              {'duid': '20181207-94a3ed8a-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b76008928f8a4f65ab21bd84ae603eb8'},
              {'duid': '20181207-953fe58c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '90084a3f4a5349b79049e845a2b2f839'},
              {'duid': '20181207-963821c0-f9cf-11e8-bf1c-ea00e4d87701', 'token': '678adc53f96646bc8c78d572ed8df228'},
              {'duid': '20181207-96e60e20-f9cf-11e8-bf1c-ea00e4d87701', 'token': '6406032fd3ab434bb19afc62b4cf8a5d'},
              {'duid': '20181207-97927e9e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e62d56896a2d493c8c88755936ae6420'},
              {'duid': '20181207-983d9b80-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4cb1937115d54a5197cb623c0521f78c'},
              {'duid': '20181207-98da0e20-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'bfde6f3365c8484f85bc22bc3ab0a213'},
              {'duid': '20181207-99a4db00-f9cf-11e8-bf1c-ea00e4d87701', 'token': '166630a86b1449cfba9d46f9e5ca27ea'},
              {'duid': '20181207-9a605c5e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'c90989a6ac1b4a71924cdc38c9c3fca4'},
              {'duid': '20181207-9b0c833a-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a42bf4919a234866af8242d6af3aa9ab'},
              {'duid': '20181207-9bb8a566-f9cf-11e8-bf1c-ea00e4d87701', 'token': '00cbff66a08c4a3c912073d45eeab115'},
              {'duid': '20181207-9c656a30-f9cf-11e8-bf1c-ea00e4d87701', 'token': '691689e477d64219ac9fd69a80315f79'},
              {'duid': '20181207-9cfe2ee6-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7c682c77dfba472eab660ee480b0d450'},
              {'duid': '20181207-9dac6934-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1b6b923f626f4523b21fed1153c26a20'},
              {'duid': '20181207-9e43b9ec-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'bc86b6553ce14d48bbcabb63b7272a90'},
              {'duid': '20181207-9edb4564-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4392573b2d464b6a83c0ba068a42cdc9'},
              {'duid': '20181207-9f7f193c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '34af412f3041413ea3da514718673731'},
              {'duid': '20181207-a03c71e4-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd23e5e76760548d38fcea3a18d464e60'},
              {'duid': '20181207-a0f7e0fa-f9cf-11e8-bf1c-ea00e4d87701', 'token': '5bb807e7aec84ae284a90489ed617d1f'},
              {'duid': '20181207-a1e0428c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '0a425e2f8b4648c692f12d6256090428'},
              {'duid': '20181207-a27df5ae-f9cf-11e8-bf1c-ea00e4d87701', 'token': '02b76dfbc8dd457baf1ef3b5de95fd1e'},
              {'duid': '20181207-a339ff92-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f676f7865eca4e13a96d62d065afbe3d'},
              {'duid': '20181207-a3edf43e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e161a4b513bf43d6837bec8e647bb4cb'},
              {'duid': '20181207-a4a18dbe-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'dbeed47e998a47f9af1cd39e1f0b3010'},
              {'duid': '20181207-a55d314a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '22fb046b6a2d4f4aae05a645bb71bf0d'},
              {'duid': '20181207-a60903c6-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4710e0bb68ae43a2b8621990a5bcfd17'},
              {'duid': '20181207-a6c46c60-f9cf-11e8-bf1c-ea00e4d87701', 'token': '90069e7898b64201b19f3abe6feb3cd9'},
              {'duid': '20181207-a7704706-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ba42ea0a2ce046e49698bf94a8482c7c'},
              {'duid': '20181207-a82bc864-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9a8ed35ab0184ea7b73baef89bb18cb6'},
              {'duid': '20181207-a8d7e7d4-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'c78c6137ed14493fa24081f7fa2d9992'},
              {'duid': '20181207-a9934858-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'fe23dd0c609d46868ad22140973f2c14'},
              {'duid': '20181207-aa475c94-f9cf-11e8-bf1c-ea00e4d87701', 'token': '21f4dd144eb1421c9bbc46a3ef1175ce'},
              {'duid': '20181207-aafa7414-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b68c2e84036b4e4cba43bd7cb28b2cf8'},
              {'duid': '20181207-aba7162e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'eae774579f2749fb9377cb4c85a72daf'},
              {'duid': '20181207-ac620f74-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a63b629749e24854a2b01af7a808b7b2'},
              {'duid': '20181207-ad0e0ad6-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e07b8ef4ca524b6dae064fa7688580ec'},
              {'duid': '20181207-adb9ca92-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'da8cbcd4acc84500b0761f51269e9641'},
              {'duid': '20181207-ae5f86f8-f9cf-11e8-bf1c-ea00e4d87701', 'token': '61f9d13ac3eb466199dc69f453233696'},
              {'duid': '20181207-af09e756-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b5bc91d093c942a19b86c90c26d90740'},
              {'duid': '20181207-afad9f36-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f5177b832f0a4e19980581a880a264fb'},
              {'duid': '20181207-b057b8a4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '838e01f2c66b4206ad5bfba41dd2ed42'},
              {'duid': '20181207-b0f5c404-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1ed459671c494d29af460bfabc81eca7'},
              {'duid': '20181207-b1a9f726-f9cf-11e8-bf1c-ea00e4d87701', 'token': '69e2a026bf074abf839269b7f55c2643'},
              {'duid': '20181207-b24dc310-f9cf-11e8-bf1c-ea00e4d87701', 'token': '61ae2e332faa44d79663fc612e0e4264'},
              {'duid': '20181207-b2f9abda-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f304d48f1082489395256448f48348ac'},
              {'duid': '20181207-b3b52e0a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '19c649c309054c26aecc2623a9704ea8'},
              {'duid': '20181207-b468e76a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7cd3c1993f0a4c51b02b103ec7bf1b5e'},
              {'duid': '20181207-b51c8126-f9cf-11e8-bf1c-ea00e4d87701', 'token': '15d1b56e34254610a68f67305f2eae73'},
              {'duid': '20181207-b5c81590-f9cf-11e8-bf1c-ea00e4d87701', 'token': '92c64f73ee204e9496124d0df31276c2'},
              {'duid': '20181207-b674254c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '493a3714fa904c65af01a4e30c73dd66'},
              {'duid': '20181207-b718a450-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7ee12a0cd5a04f02ae3f98ce6c8d271f'},
              {'duid': '20181207-b7bc71de-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ae8a4f07d28243dc83bd881e866d3a5e'},
              {'duid': '20181207-b869e3fa-f9cf-11e8-bf1c-ea00e4d87701', 'token': '14594e7340e14ef68d13c0b844bca9fc'},
              {'duid': '20181207-b9059a84-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b8c3cc9bce344563970e13a7e4c8dbf1'},
              {'duid': '20181207-b9b06324-f9cf-11e8-bf1c-ea00e4d87701', 'token': '92c27cf1ec1e41759b57e725f3e2b681'},
              {'duid': '20181207-ba641e32-f9cf-11e8-bf1c-ea00e4d87701', 'token': '41d47d44a5934c00b2ba7db8efe7c395'},
              {'duid': '20181207-bb17c7b6-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a7fbd95fb8f74f80b1459d9065a03bc0'},
              {'duid': '20181207-bbd2f7d4-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'cfcc17c5629b4a5c9c077486c00aff68'},
              {'duid': '20181207-bc7ef0e8-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1248672aa0f14613adb567398ea67410'},
              {'duid': '20181207-bd3acd86-f9cf-11e8-bf1c-ea00e4d87701', 'token': '217681be91874d3eba369619d0b7ecd0'},
              {'duid': '20181207-bdf628f6-f9cf-11e8-bf1c-ea00e4d87701', 'token': '759c3880252e42a6a24a8a6240963a3c'},
              {'duid': '20181207-bf1f89de-f9cf-11e8-bf1c-ea00e4d87701', 'token': '07f5150a82124b7e86997810289ff391'},
              {'duid': '20181207-c0118108-f9cf-11e8-bf1c-ea00e4d87701', 'token': '55a412704a3f48feb0df2603e863898a'},
              {'duid': '20181207-c0d8a990-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e9ed3ffe321347a9b6e1a8afee074d58'},
              {'duid': '20181207-c1bf0fac-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f04e25bd694f4284867f199b0eaa33ba'},
              {'duid': '20181207-c299b7ce-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'bafddb3b85a941fb9415692a0c57045c'},
              {'duid': '20181207-c3759384-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3a77e4d67b7a4af1ad39ea268e4a011d'},
              {'duid': '20181207-c45ebde8-f9cf-11e8-bf1c-ea00e4d87701', 'token': '501bc629c7d74fe18ffe69afb3a7065a'},
              {'duid': '20181207-c5438e50-f9cf-11e8-bf1c-ea00e4d87701', 'token': '958318378964436c88bc88b997255518'},
              {'duid': '20181207-c623fdb4-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'fadd0e2baeea492a9bff2092431ece21'},
              {'duid': '20181207-c6ff682c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4c71529f5b134ff38b3a902a413c3c4e'},
              {'duid': '20181207-c7c9b9e2-f9cf-11e8-bf1c-ea00e4d87701', 'token': '596775a910184cd19afca4b7206dfec7'},
              {'duid': '20181207-c8c3bf46-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'eadf5f4a6843452b8b8a43fe641c7058'},
              {'duid': '20181207-c99fc86a-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd27a2cf75d63476f91fd2beac65f16af'},
              {'duid': '20181207-ca5de502-f9cf-11e8-bf1c-ea00e4d87701', 'token': '803397dc0a7043029682bf20cfac6d99'},
              {'duid': '20181207-cb35e06a-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'c1f65cb791cf4a4aab94dd7da3aed481'},
              {'duid': '20181207-cc0f6088-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7e3fda763dfa49cdb4f3cfc31726ab31'},
              {'duid': '20181207-ccdc08fe-f9cf-11e8-bf1c-ea00e4d87701', 'token': '436f925159774ee8bbaa525dcd5de3c7'},
              {'duid': '20181207-cdbcb322-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a334d009408144b681cf182fdc7cad61'},
              {'duid': '20181207-ce999e5e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4ac81d85bef94c4ea0640af4cd0f4986'},
              {'duid': '20181207-cf6ceab6-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd2a8d10411cc47a8beaad12800e4fbe0'},
              {'duid': '20181207-d035e7fe-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ed1b3b9cd8d74c9c92f3f3001deca5a1'},
              {'duid': '20181207-d100f93a-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd56a8a7871734d57b0aa7c8de2b1b20e'},
              {'duid': '20181207-d1bca572-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'becc36346dc040ce8d2f21d1f2066a98'},
              {'duid': '20181207-d25904d0-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3ae0e9eeb5af427782b01009650e036f'},
              {'duid': '20181207-d308e936-f9cf-11e8-bf1c-ea00e4d87701', 'token': '371aad4e09ff410b8edc3de01eef9882'},
              {'duid': '20181207-d3b8e0e8-f9cf-11e8-bf1c-ea00e4d87701', 'token': '791da3e930754fe38714bf03ee3f0e25'},
              {'duid': '20181207-d4549218-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'cf0cb15d0355450791157584de038c50'},
              {'duid': '20181207-d4f16d7c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '6e7761899ae34835ad69b1ecf7df1f42'},
              {'duid': '20181207-d594ef42-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a66fb03354314fbd8d234f486fd0163d'},
              {'duid': '20181207-d650a296-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'efa4468377c64c85b3adf5ea569a632f'},
              {'duid': '20181207-d703dc26-f9cf-11e8-bf1c-ea00e4d87701', 'token': '71f92d7cfa3142a0a7baf23f77d85f59'},
              {'duid': '20181207-d7b7ee96-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'aec07a5dbe9849ad8ae5924b5ef2c2e1'},
              {'duid': '20181207-d8616e80-f9cf-11e8-bf1c-ea00e4d87701', 'token': '52303d96dafe4364a49f4a5549591aca'},
              {'duid': '20181207-d91f210a-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'aad0884b7ac54b4292d2f708cd6d5d85'},
              {'duid': '20181207-d9cb11f4-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b309874d345047ff8ee3c5ddfc3ea6cb'},
              {'duid': '20181207-da6fc01e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '24896ed8dff84dda901985776d515573'},
              {'duid': '20181207-db111748-f9cf-11e8-bf1c-ea00e4d87701', 'token': '68fda5170b5944b5bb0d613b4a7e536c'},
              {'duid': '20181207-dbb841ee-f9cf-11e8-bf1c-ea00e4d87701', 'token': '8e717ec8a67b446a9b1a004a41f00fc8'},
              {'duid': '20181207-dc737568-f9cf-11e8-bf1c-ea00e4d87701', 'token': '27f101e909be4df0816c204f763ac635'},
              {'duid': '20181207-dd14e77c-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e69491a54b7a4c30856581b25c1a9778'},
              {'duid': '20181207-ddb09b40-f9cf-11e8-bf1c-ea00e4d87701', 'token': '479869f58f374a73a8702214f118e0c4'},
              {'duid': '20181207-de493df0-f9cf-11e8-bf1c-ea00e4d87701', 'token': '281a0819e4cd4ee2bc04f129b163c332'},
              {'duid': '20181207-dee17eee-f9cf-11e8-bf1c-ea00e4d87701', 'token': '6a5812558fee4881987504915da5a927'},
              {'duid': '20181207-df78da6e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '02bbdd8c1ad842f1b0ddce0a3116197d'},
              {'duid': '20181207-e013263c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '91227e7c581a4019b2efa6a63947a4b2'},
              {'duid': '20181207-e0b5432c-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f171bc6dbdd849dabeaa84e4c9e749f2'},
              {'duid': '20181207-e15a5128-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1afb4d36703f468c97da227b9aa322f5'},
              {'duid': '20181207-e1f2145e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '799f9a06d08140a8aae6cf24592a45bc'},
              {'duid': '20181207-e28afa98-f9cf-11e8-bf1c-ea00e4d87701', 'token': '79cc2597625a40a99406a2aad97d09b6'},
              {'duid': '20181207-e330e2d2-f9cf-11e8-bf1c-ea00e4d87701', 'token': '6a4355a66eec4916ba6b6e14eca895ba'},
              {'duid': '20181207-e3d5d620-f9cf-11e8-bf1c-ea00e4d87701', 'token': '8463cfde2dfd44e8b1f251b56ba73564'},
              {'duid': '20181207-e476e132-f9cf-11e8-bf1c-ea00e4d87701', 'token': '0e125e0195674fb7a75d2b97b7496fba'},
              {'duid': '20181207-e50e3ee2-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7ad5a2f7a5ce41adab813a139c106124'},
              {'duid': '20181207-e5a54986-f9cf-11e8-bf1c-ea00e4d87701', 'token': '890c883d6b094b9aafb0fa2bec14bc33'},
              {'duid': '20181207-e63c7112-f9cf-11e8-bf1c-ea00e4d87701', 'token': '08fc3cbb3f1745b681fcb55456d2603e'},
              {'duid': '20181207-e6d471ba-f9cf-11e8-bf1c-ea00e4d87701', 'token': '264028dfb70243caa298760cbe856c0e'},
              {'duid': '20181207-e77d41be-f9cf-11e8-bf1c-ea00e4d87701', 'token': '5dfa8ee69a37401b88573220eb7d267d'},
              {'duid': '20181207-e81b378e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4511ad4dccca42309a26badce07dbd3e'},
              {'duid': '20181207-e8b34934-f9cf-11e8-bf1c-ea00e4d87701', 'token': '2117c9dcb44841afad2613fcfcb989be'},
              {'duid': '20181207-e960413e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '959d0f3d37e842879178fb5f6e60519f'},
              {'duid': '20181207-e9f94884-f9cf-11e8-bf1c-ea00e4d87701', 'token': '70256e8c2a644594b1e1914b9682db06'},
              {'duid': '20181207-ea900fc6-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f79c994cc5934c1789868d15cd80ee00'},
              {'duid': '20181207-eb2e1dd8-f9cf-11e8-bf1c-ea00e4d87701', 'token': '79c8337cbd964a58ad6dc0b040036a07'},
              {'duid': '20181207-ebe431fe-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3c35508a56e34c2ca9d7ef01630daeee'},
              {'duid': '20181207-ec882ade-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'cd821972315047b5a4320863d9019229'},
              {'duid': '20181207-ed33d6fe-f9cf-11e8-bf1c-ea00e4d87701', 'token': '8361ef82421f46f6a5d392559c673a6e'},
              {'duid': '20181207-edeaea1a-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'bab96e2b2ef14241b7803cc85bafc155'},
              {'duid': '20181207-ee842d88-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b6c4e8d02dcd46abaa82d9b17633f28a'},
              {'duid': '20181207-ef280eb2-f9cf-11e8-bf1c-ea00e4d87701', 'token': '44f2f8d9c3ae4b5081a25c8e7c3abebf'},
              {'duid': '20181207-efc42e96-f9cf-11e8-bf1c-ea00e4d87701', 'token': '6ab8aab5a22f4ea497db7cf370f10ccd'},
              {'duid': '20181207-f05c5824-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'acd9248403684a13a2d1bb933c560a15'},
              {'duid': '20181207-f10175d4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '54eaa2c27cc34ea1a89fc27f59cf4e96'},
              {'duid': '20181207-f199bd76-f9cf-11e8-bf1c-ea00e4d87701', 'token': '8d1f348cffab46d79a294b1462998cdd'},
              {'duid': '20181207-f241ab6c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '04faff6d0a854b9b8d5b11c4b63f88a9'},
              {'duid': '20181207-f2d85788-f9cf-11e8-bf1c-ea00e4d87701', 'token': '72ee2988ad5f47e59135adcfcce8d121'},
              {'duid': '20181207-f36dc2b4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '41a00715e4a94469863fdf7c584e2080'},
              {'duid': '20181207-f40718c4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '66b99a342a2b42d39026c19b4ba3717f'},
              {'duid': '20181207-f49fe2f2-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3b4bddcefcf2430e8021b4baa70385e6'},
              {'duid': '20181207-f53889a8-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'cf6ec5678f844f839d7a496de801b123'},
              {'duid': '20181207-f5d7511e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f22d1a363cbd48758f1cc6e556763aad'},
              {'duid': '20181207-f68234da-f9cf-11e8-bf1c-ea00e4d87701', 'token': '91a8687cb3914e38a566dc6369aa2937'},
              {'duid': '20181207-f7176dd4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '89d78e94ca074c4d9896dc11c6e11c40'},
              {'duid': '20181207-f7b31914-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3c4cc7fe74ac4fc19dfed2941a64f38d'},
              {'duid': '20181207-f85223e2-f9cf-11e8-bf1c-ea00e4d87701', 'token': '6520f28e91644328ad16278fe2416d71'},
              {'duid': '20181207-f8ef4672-f9cf-11e8-bf1c-ea00e4d87701', 'token': '01d1b007395a4f8aa0ee050724f96fd8'},
              {'duid': '20181207-f98777e4-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd156b4c625d44b958dc2611a33ef75de'},
              {'duid': '20181207-fa247fee-f9cf-11e8-bf1c-ea00e4d87701', 'token': '506ecb691f524df5bf4b5f77a9306ea1'},
              {'duid': '20181207-fabb2c46-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4dacc206d61547b8be29a45d793369b4'},
              {'duid': '20181207-fb6cb150-f9cf-11e8-bf1c-ea00e4d87701', 'token': '862887c8b54d4a2296b6733e1b754b95'},
              {'duid': '20181207-fc0cda0e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7de44e21e7ba4dcebc51d5e0f4ac1bf2'},
              {'duid': '20181207-fcb50526-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7740b996513743d7a7f10be271afd3ca'},
              {'duid': '20181207-fd605c50-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a8df7c02353c426bb4f17e85e7e9bc0a'},
              {'duid': '20181207-fe046660-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a3cc1b23f9b6450b828d763b177a4408'},
              {'duid': '20181207-fe9d9984-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e44b04324b3d493fac61aa2e888ce9d5'},
              {'duid': '20181207-ff347dfe-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a90465b002fe4294b57846e89daa4934'},
              {'duid': '20181207-ffc9cc2e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e42a4e94c5684c7288fc65aa625dfaed'},
              {'duid': '20181207-00624742-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'f4b1f4acf1d848e2848b047145a7b762'},
              {'duid': '20181207-0101e554-f9d0-11e8-bf1c-ea00e4d87701', 'token': '353b8e8901714823bfe2563030c6d43e'},
              {'duid': '20181207-019e1fe6-f9d0-11e8-bf1c-ea00e4d87701', 'token': '0d2bc4a23483429484cd27ba23e9a8bc'},
              {'duid': '20181207-0234e9a8-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'fe642b5b78b14cdf96289f18d6498f53'},
              {'duid': '20181207-02ca1cf8-f9d0-11e8-bf1c-ea00e4d87701', 'token': '7110ea7ee94447c2ae4dc6c1e32168a7'},
              {'duid': '20181207-03600f56-f9d0-11e8-bf1c-ea00e4d87701', 'token': '75ccbb283b82487f8532a0ec81cbe4ad'},
              {'duid': '20181207-03fa163c-f9d0-11e8-bf1c-ea00e4d87701', 'token': '65309e33f5c04b11b3def9f5233d6fbb'},
              {'duid': '20181207-049281a6-f9d0-11e8-bf1c-ea00e4d87701', 'token': '70738d858d834f66a679e59ccf48dae2'},
              {'duid': '20181207-052b381a-f9d0-11e8-bf1c-ea00e4d87701', 'token': '21e4a68280694b478e7253d707fff5ff'},
              {'duid': '20181207-05c4311e-f9d0-11e8-bf1c-ea00e4d87701', 'token': '84f4fae951db4b8980eb370959277360'},
              {'duid': '20181207-065b9b8a-f9d0-11e8-bf1c-ea00e4d87701', 'token': '0f23e32dafcd48cc87bf73d3edef0fdd'},
              {'duid': '20181207-06f4ae1a-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'd0c0ddf82fc149b39114ed47c9d9dbff'},
              {'duid': '20181207-078c3e10-f9d0-11e8-bf1c-ea00e4d87701', 'token': '29e0e8f2d8b841fb86cdbdaa325db999'},
              {'duid': '20181207-082e2cb6-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'ce64327883eb48f78d377dc5dd0d3694'},
              {'duid': '20181207-08da10b2-f9d0-11e8-bf1c-ea00e4d87701', 'token': '46aeb1a180874b12a9bc376961a8e62e'},
              {'duid': '20181207-097b0292-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'c4d8d399ab6a4351892eb28e06912162'},
              {'duid': '20181207-0a1fc20a-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'b0144c5a18b54296b7a6740d6db8a04d'},
              {'duid': '20181207-0ada90b2-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'bc196b291374416e915c0c81f9da9da6'},
              {'duid': '20181207-0b992fe0-f9d0-11e8-bf1c-ea00e4d87701', 'token': '0f8b96dd93cf4e93bc0b63776f1b0873'},
              {'duid': '20181207-0c3b11fc-f9d0-11e8-bf1c-ea00e4d87701', 'token': '8057518f83344658b6315aba453d6513'},
              {'duid': '20181207-0cd2a288-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'ae66bcf9c49b492c820a54fb105dd611'},
              {'duid': '20181207-0d694c9c-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'f7d66d1172ee4a4188105ee9fda67a21'},
              {'duid': '20181207-0e00f9de-f9d0-11e8-bf1c-ea00e4d87701', 'token': '3d1c1a367e584414a7e96196ef88b47c'},
              {'duid': '20181207-0eab4b64-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'bfc2ead303b64bbdb79d8b029f2663af'},
              {'duid': '20181207-0f4af308-f9d0-11e8-bf1c-ea00e4d87701', 'token': '97819ae4c6a041869180605d9f7ec069'}]

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
