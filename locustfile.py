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

user_datas = [{'duid': '20181207-6a06f180-f9cf-11e8-bf1c-ea00e4d87701', 'token': '93796e0d6a854c9aa23b1a0fc4bd004d'},
              {'duid': '20181207-6b1499f6-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'faa2b0eb512040b9a04f1db6721d2f8b'},
              {'duid': '20181207-6bce83c0-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'df4cba11157f4330a2376c4aeaca3c25'},
              {'duid': '20181207-6c7a6f8c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '956854092cf94c2cbfd111bafca6fd39'},
              {'duid': '20181207-6d265cb6-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ec69f01cedc04b62aa4b0ac50a8a26e7'},
              {'duid': '20181207-6de1d5cc-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a02f09e1e3e94da6963edd20f4a3e38d'},
              {'duid': '20181207-6e9d75ca-f9cf-11e8-bf1c-ea00e4d87701', 'token': '60c1a2762b874ce19b5f98d40ed31699'},
              {'duid': '20181207-6f3965ac-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1fbb75afc8914c1e8c60952f5c60e090'},
              {'duid': '20181207-6fe57bb2-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'de08aef5c19e449aa87dc976d6d5695d'},
              {'duid': '20181207-70a0a608-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9c7b38c356924ec5b0e7e669222f5b03'},
              {'duid': '20181207-713d14de-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ec66dc12289d44bd8e8c2ff713255ed4'},
              {'duid': '20181207-71e8cb12-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a0cf51cdfc1f4683869b34ad905ebf5f'},
              {'duid': '20181207-72a3ba94-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3142695639e3444fbac9d7dec04ec5e9'},
              {'duid': '20181207-735ff092-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ef1ad6b9b46a4594bce83a2ca32de7eb'},
              {'duid': '20181207-7403f160-f9cf-11e8-bf1c-ea00e4d87701', 'token': '0d208075d2be4ca1a84d49499d153f44'},
              {'duid': '20181207-74afeae2-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7afb5fa33d154312b61bb5b667137f4c'},
              {'duid': '20181207-7563a5f0-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b528547d703d409384de172df7490454'},
              {'duid': '20181207-760f3460-f9cf-11e8-bf1c-ea00e4d87701', 'token': '13589efaccbb47d081ad3112dd8081eb'},
              {'duid': '20181207-76cb3c28-f9cf-11e8-bf1c-ea00e4d87701', 'token': '5a8c340c598a4b86b58358d9986c0503'},
              {'duid': '20181207-7776f69e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'eca203abcb27407998806234521b445c'},
              {'duid': '20181207-7832754a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '507d98c0db5d4d789adb48086c5c9b64'},
              {'duid': '20181207-78edae0a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '8a48af652cac493894711f94f7537358'},
              {'duid': '20181207-79a9430e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '5b86c2a84e984b399f10be2509d4ee31'},
              {'duid': '20181207-7a558272-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e3b38806410e489491a1139ae19274ec'},
              {'duid': '20181207-7b10f408-f9cf-11e8-bf1c-ea00e4d87701', 'token': '703fd463067d4a7686f3d7353fd49d49'},
              {'duid': '20181207-7bc4e436-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd00c05ff64c24b51b95e8b316c89ffa1'},
              {'duid': '20181207-7c7851f6-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9fe281977a9a457688acb001a67a4c2c'},
              {'duid': '20181207-7d33fc6c-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b5c180fb0a254c40bdf3acc55e3e7a23'},
              {'duid': '20181207-7ddfa792-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'daf9dd835d83478d91a19ea62889c5ac'},
              {'duid': '20181207-7e8b8cec-f9cf-11e8-bf1c-ea00e4d87701', 'token': '26011078e3f84f18add3ee1e35e14f85'},
              {'duid': '20181207-7f38d618-f9cf-11e8-bf1c-ea00e4d87701', 'token': '610d5c5a92d740d88b37ddb1d07357e3'},
              {'duid': '20181207-7fdf5790-f9cf-11e8-bf1c-ea00e4d87701', 'token': '742f49f30d9443d589bc78d223917bd1'},
              {'duid': '20181207-809eaee2-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'eb3b968de6a64ff09e965b41159cfa22'},
              {'duid': '20181207-813b18a4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '72be26405d014b11a74cda6af3d25273'},
              {'duid': '20181207-81d748c8-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a7c6b7be9a2a482e80873c67c3990c00'},
              {'duid': '20181207-8273999e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b834e25c5c634eadb601fe19e8f18df7'},
              {'duid': '20181207-830e4ee4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '218a2f24183145cf9fc7c6a196b064b1'},
              {'duid': '20181207-83cb13da-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd1453d414bd14b3fb4e419d71c5b6168'},
              {'duid': '20181207-84773b6a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '2492e2cecca44e3b96e9d86bc9f6765f'},
              {'duid': '20181207-85137dd6-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ea387eb363eb471db590d7bfa0af921f'},
              {'duid': '20181207-85ce9a26-f9cf-11e8-bf1c-ea00e4d87701', 'token': '668f23cbdd1d4fd6b61bcd58756f2876'},
              {'duid': '20181207-86739288-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f1fc5a11b17b49188e8b078ca8884be2'},
              {'duid': '20181207-870f43d6-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e20cebdd72c64992aeab8ea314d981da'},
              {'duid': '20181207-87c30560-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4025de62360c4864a0d90be915d343c5'},
              {'duid': '20181207-886eed4e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'adc1115d16e64ca3925ed5a55bf5f143'},
              {'duid': '20181207-890fa626-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e9b0b37983054564bf0e83e76593bd7d'},
              {'duid': '20181207-89b2de22-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'bc5c479ab89343efbff2268a3fdbbe03'},
              {'duid': '20181207-8a62d71e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '516f9254047b4a9fb94d15449d81cc42'},
              {'duid': '20181207-8b07380e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '57df60823fed4de49398e639ed41a1b3'},
              {'duid': '20181207-8ba360d0-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a14c0429b8d84f32b25474ab3e588ec1'},
              {'duid': '20181207-8c471626-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9a6d6d4a114e4ab6b825984573a348e3'},
              {'duid': '20181207-8cf2f5fe-f9cf-11e8-bf1c-ea00e4d87701', 'token': '708de4ee38d14e72935292f37c05ffe3'},
              {'duid': '20181207-8da77d80-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'cacfed96ae0847459e16f1f984e7c9f9'},
              {'duid': '20181207-8e42c98e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '2940d55d8e584fecb76c8dcd051868a0'},
              {'duid': '20181207-8ef6c060-f9cf-11e8-bf1c-ea00e4d87701', 'token': '154b6e4d0af5415e97566651c40e518b'},
              {'duid': '20181207-8fae6bde-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e4b855944d6f4dffac2f90200a68fcc8'},
              {'duid': '20181207-905e0468-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'bdc00f79d0304107b2b439950d92c37a'},
              {'duid': '20181207-90fa1394-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd9bd1b2ae9c94c48a201c27ed808f51d'},
              {'duid': '20181207-919657f4-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b8cf86f48696477289df5338da63c33d'},
              {'duid': '20181207-922f7fc4-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'fb381e17cc4c43169ef5973ef6957b0a'},
              {'duid': '20181207-92ceec9e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '0cac6dcf5ce147db98e61959ccde9054'},
              {'duid': '20181207-936b6b1e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'c05a9311f47a48ad9a6a84fc5d18aab0'},
              {'duid': '20181207-94073936-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f0508da685d64accaa17a394b6acd3a6'},
              {'duid': '20181207-94a3ed8a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7e12f4f9287e43579f2ee83347078546'},
              {'duid': '20181207-953fe58c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '84ab73c0ff5041b9bfe20130558f3421'},
              {'duid': '20181207-963821c0-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'add26b47333a4702a0d0a5a0c8e818ba'},
              {'duid': '20181207-96e60e20-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'adb48a591fbf4b4f9512dd1a9717ca8b'},
              {'duid': '20181207-97927e9e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'eeef8e0b162b4c858736a88dc9bc5480'},
              {'duid': '20181207-983d9b80-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd50ab459e7bf4b649b2935989c441263'},
              {'duid': '20181207-98da0e20-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'afeb892eeeb74ce48bdefbd12e3fb22b'},
              {'duid': '20181207-99a4db00-f9cf-11e8-bf1c-ea00e4d87701', 'token': '741d7303846e4ccbb87a56e1f91ab9de'},
              {'duid': '20181207-9a605c5e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '03397cb17d844d1899ad9cdf79bfc2a7'},
              {'duid': '20181207-9b0c833a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '763c8f4cceaa46e284d87fdc9d61ac24'},
              {'duid': '20181207-9bb8a566-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9958982ac272485489eb7201aad92d66'},
              {'duid': '20181207-9c656a30-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b1fbf7921e554a3daa33951194866954'},
              {'duid': '20181207-9cfe2ee6-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'fdc00271ffdf4d45a6cfc485b9723caa'},
              {'duid': '20181207-9dac6934-f9cf-11e8-bf1c-ea00e4d87701', 'token': '86ebb891adc54ab38044a6ad8a959d0d'},
              {'duid': '20181207-9e43b9ec-f9cf-11e8-bf1c-ea00e4d87701', 'token': '85fc3368cd524920ac28e478f6131424'},
              {'duid': '20181207-9edb4564-f9cf-11e8-bf1c-ea00e4d87701', 'token': '278e12667f8b4c1b817926b4dbe362f5'},
              {'duid': '20181207-9f7f193c-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b38891cb60d3467ba7b4563d934eedee'},
              {'duid': '20181207-a03c71e4-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ad1c919815794cb3b41f951489d8b9b1'},
              {'duid': '20181207-a0f7e0fa-f9cf-11e8-bf1c-ea00e4d87701', 'token': '102ae1d9ebae4ec09cd9de5ca7e32999'},
              {'duid': '20181207-a1e0428c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '78b026d8d57e461280d05eafb90f6eb0'},
              {'duid': '20181207-a27df5ae-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7d2451cddb80427f9d9c32067fad90a5'},
              {'duid': '20181207-a339ff92-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'caef3276670c4730b075a0edc802e584'},
              {'duid': '20181207-a3edf43e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '47a96f882c314403a99fe3b96db36df8'},
              {'duid': '20181207-a4a18dbe-f9cf-11e8-bf1c-ea00e4d87701', 'token': '54e0fcbf3c2d497d80045ab3775b43d0'},
              {'duid': '20181207-a55d314a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '6b8ac7903efa4fb291cd28eb9abb836d'},
              {'duid': '20181207-a60903c6-f9cf-11e8-bf1c-ea00e4d87701', 'token': '59a695d3b11647318037f763d447017c'},
              {'duid': '20181207-a6c46c60-f9cf-11e8-bf1c-ea00e4d87701', 'token': '8371511f96eb48e49a4dcc0ca1a51f87'},
              {'duid': '20181207-a7704706-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b27cc15f4fa64934aed62b681b93b7bc'},
              {'duid': '20181207-a82bc864-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ad5eed4a25a44d55b7a79963eaf7f6d6'},
              {'duid': '20181207-a8d7e7d4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '64d7540f832c4303bf9457f905a741d0'},
              {'duid': '20181207-a9934858-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4ea5bbfa6814446c8cd66f81d0f49fed'},
              {'duid': '20181207-aa475c94-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9f933c0ecae54ad882bd863baeb9ba1f'},
              {'duid': '20181207-aafa7414-f9cf-11e8-bf1c-ea00e4d87701', 'token': '317d6cf32f7346d2bbeb48cf3f379e00'},
              {'duid': '20181207-aba7162e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9434f897040d4b93b4325b945b9c430f'},
              {'duid': '20181207-ac620f74-f9cf-11e8-bf1c-ea00e4d87701', 'token': '2f4facc26af0406c88ba322c04038100'},
              {'duid': '20181207-ad0e0ad6-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f157838e87f84f2c912adcc7ad1e35e7'},
              {'duid': '20181207-adb9ca92-f9cf-11e8-bf1c-ea00e4d87701', 'token': '705b42d04f8b47df916ef1a3deedd66d'},
              {'duid': '20181207-ae5f86f8-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'fbee7d94f1b1484898de739836895f65'},
              {'duid': '20181207-af09e756-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e2bedffaa0554609b5187c0201c78d17'},
              {'duid': '20181207-afad9f36-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f10d8fb35fae4230a1e995cafd8891d6'},
              {'duid': '20181207-b057b8a4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9a47e6f238d84574bcd74925cce059f0'},
              {'duid': '20181207-b0f5c404-f9cf-11e8-bf1c-ea00e4d87701', 'token': '01e7909b5f2f4aeabd5cbd42dcf55f54'},
              {'duid': '20181207-b1a9f726-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'fd57510c9a6b4722aa0286a4369b0b87'},
              {'duid': '20181207-b24dc310-f9cf-11e8-bf1c-ea00e4d87701', 'token': '122f0dc4bc244d90b7d25931fef1fc10'},
              {'duid': '20181207-b2f9abda-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'c9bc49e554164be8bbffd5272e821a8d'},
              {'duid': '20181207-b3b52e0a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '6309b3a4f0a44036924e6995f1ad47ec'},
              {'duid': '20181207-b468e76a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '34862839d8724f2f84a48f099a0cb45e'},
              {'duid': '20181207-b51c8126-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'fbbf24d1be894702ba0d78006a4553d1'},
              {'duid': '20181207-b5c81590-f9cf-11e8-bf1c-ea00e4d87701', 'token': '73180689926d4860907f2b040fbd1309'},
              {'duid': '20181207-b674254c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '6d2999f398e1415da0903417466fc056'},
              {'duid': '20181207-b718a450-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9491dd8023674be0b6997021967d2fd8'},
              {'duid': '20181207-b7bc71de-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1f29ccb1583f465697514f8690522bd6'},
              {'duid': '20181207-b869e3fa-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e604576da5c44649b6f57f87b0c9d59c'},
              {'duid': '20181207-b9059a84-f9cf-11e8-bf1c-ea00e4d87701', 'token': '00e346c4a0354aca960c28e86d938f8d'},
              {'duid': '20181207-b9b06324-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ecc653b3cffc41019b93f489eb951b0f'},
              {'duid': '20181207-ba641e32-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1d8df8b31e89442993d80c2ce1ea04eb'},
              {'duid': '20181207-bb17c7b6-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a548cbf5009a479a871aef6c1630e359'},
              {'duid': '20181207-bbd2f7d4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '0cde4e6063f8457b993444d3417368e6'},
              {'duid': '20181207-bc7ef0e8-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9ddb52ba3eb44105acee099cf6266ad3'},
              {'duid': '20181207-bd3acd86-f9cf-11e8-bf1c-ea00e4d87701', 'token': '8bb1e007b8584e34af13382f1fa281fe'},
              {'duid': '20181207-bdf628f6-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ec27958f3ecd4f64880ac4399aa1d977'},
              {'duid': '20181207-bf1f89de-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e39e8cc5b3cd46f8b2d125ba6344c9f6'},
              {'duid': '20181207-c0118108-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f8cd4fa82efa4447a76a625cd2a6ea0d'},
              {'duid': '20181207-c0d8a990-f9cf-11e8-bf1c-ea00e4d87701', 'token': '8d896b000f7e40d7b89b01374bab71a9'},
              {'duid': '20181207-c1bf0fac-f9cf-11e8-bf1c-ea00e4d87701', 'token': '5abe439527e94275ab4edf255ab84684'},
              {'duid': '20181207-c299b7ce-f9cf-11e8-bf1c-ea00e4d87701', 'token': '6077fd3d8ec74e6bb0a43f582ba9ba0a'},
              {'duid': '20181207-c3759384-f9cf-11e8-bf1c-ea00e4d87701', 'token': '06153b8a1a9f4817ae9e02889ff6b951'},
              {'duid': '20181207-c45ebde8-f9cf-11e8-bf1c-ea00e4d87701', 'token': '05165c4a02b74420afd73a85750eac03'},
              {'duid': '20181207-c5438e50-f9cf-11e8-bf1c-ea00e4d87701', 'token': '289fbd590c804120907aa46b5faf5bf5'},
              {'duid': '20181207-c623fdb4-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'c4bad2f595a8465aa7e7f19d2815046b'},
              {'duid': '20181207-c6ff682c-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'c587aed6cb6f45839d9a44e9afda7e63'},
              {'duid': '20181207-c7c9b9e2-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'cd66bdb2be58431a840c286609afbb55'},
              {'duid': '20181207-c8c3bf46-f9cf-11e8-bf1c-ea00e4d87701', 'token': '972de2c4b0e349d89500a77cc5fd9618'},
              {'duid': '20181207-c99fc86a-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f1e216caedea48a59fd2432219bf7f54'},
              {'duid': '20181207-ca5de502-f9cf-11e8-bf1c-ea00e4d87701', 'token': '26e51803406341cdaf3a3739c8f0af42'},
              {'duid': '20181207-cb35e06a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7eb14ed8f6864c15a389e922491f2d58'},
              {'duid': '20181207-cc0f6088-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7a2b0dbc3759429c99d0a331a0f9f973'},
              {'duid': '20181207-ccdc08fe-f9cf-11e8-bf1c-ea00e4d87701', 'token': '2a882288341a4b08bba05832ce174f67'},
              {'duid': '20181207-cdbcb322-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd0950111233e4b71a2c746361103c524'},
              {'duid': '20181207-ce999e5e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '2624f750feac46c3ba9068eeaf857f29'},
              {'duid': '20181207-cf6ceab6-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1358ab0beaac46ad960308e77c98aab6'},
              {'duid': '20181207-d035e7fe-f9cf-11e8-bf1c-ea00e4d87701', 'token': '6d21861c72024c99956ef9282dcd14c5'},
              {'duid': '20181207-d100f93a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '06c94dadfc4647eeb614886d80557cd2'},
              {'duid': '20181207-d1bca572-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'c1f66f8407514939a95cd81f58b4241f'},
              {'duid': '20181207-d25904d0-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f8fcc152968842809445d2de26cc05d0'},
              {'duid': '20181207-d308e936-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b459541c7c794eda9bc70e15fec8d5c5'},
              {'duid': '20181207-d3b8e0e8-f9cf-11e8-bf1c-ea00e4d87701', 'token': '12391610da6a4ecfa9ec815cc50244d8'},
              {'duid': '20181207-d4549218-f9cf-11e8-bf1c-ea00e4d87701', 'token': '8cf27e7d16b64149b6d73785fe23508b'},
              {'duid': '20181207-d4f16d7c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '04d3221fdd27481bb6b5f14d4eacb1b1'},
              {'duid': '20181207-d594ef42-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a1a6b34983c14dec8f8b555dbf2a4278'},
              {'duid': '20181207-d650a296-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7412a3d5d5234ec4a7c435a61d61510d'},
              {'duid': '20181207-d703dc26-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4a1ffd05279444eb9859c09c76ce0d11'},
              {'duid': '20181207-d7b7ee96-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a30fd6d7b23348c6968a4ec8f2c2c8c7'},
              {'duid': '20181207-d8616e80-f9cf-11e8-bf1c-ea00e4d87701', 'token': '2afcbbac0de54f019e5a900e25d4de98'},
              {'duid': '20181207-d91f210a-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd922ad66af834460b3448f82d279a462'},
              {'duid': '20181207-d9cb11f4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '90c2d77bf10c40379277b3b30df31346'},
              {'duid': '20181207-da6fc01e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9739ff0ab0fc452dabf78a7e64151315'},
              {'duid': '20181207-db111748-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e078c0754f3e496c937d091189a148b1'},
              {'duid': '20181207-dbb841ee-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'c7e622dda87a4835830ae31bf834bcbe'},
              {'duid': '20181207-dc737568-f9cf-11e8-bf1c-ea00e4d87701', 'token': '2c59b88d4bb8405084c0497e8655c1ea'},
              {'duid': '20181207-dd14e77c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '2ee5877cbc374bc68fbe1d6fe581c18c'},
              {'duid': '20181207-ddb09b40-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'bd0f25a19b40462396e4a430d4f2d489'},
              {'duid': '20181207-de493df0-f9cf-11e8-bf1c-ea00e4d87701', 'token': '948abfb1bfb84b33a31698bdac7c1acc'},
              {'duid': '20181207-dee17eee-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b0581185ba15417889fa95c70469e26b'},
              {'duid': '20181207-df78da6e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e0d50d07c0a849a8aef31bfaed998e06'},
              {'duid': '20181207-e013263c-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e3731460158646d7ae2f072ccb9f255a'},
              {'duid': '20181207-e0b5432c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '976de89147d54015b2d1b4c483a9edde'},
              {'duid': '20181207-e15a5128-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4ca7d61e7b2b491a9ca17691561e0a6b'},
              {'duid': '20181207-e1f2145e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '42f22900e8eb41979daaf3605c59617f'},
              {'duid': '20181207-e28afa98-f9cf-11e8-bf1c-ea00e4d87701', 'token': '489aed443b1042609a5a55a8474f05a2'},
              {'duid': '20181207-e330e2d2-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1b4ae7de7a5d4bef852099db85e18917'},
              {'duid': '20181207-e3d5d620-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ae5c72dd7a6d4a2884d71b342ab29082'},
              {'duid': '20181207-e476e132-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'fc56598d700d4021aa18bd8a3bdb09d7'},
              {'duid': '20181207-e50e3ee2-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f263c225d0834622830769cf5cd96e5d'},
              {'duid': '20181207-e5a54986-f9cf-11e8-bf1c-ea00e4d87701', 'token': '8f4c522a7863451aafdef6bfa84e4bb2'},
              {'duid': '20181207-e63c7112-f9cf-11e8-bf1c-ea00e4d87701', 'token': '041daf8755214d198a3e0d3d411a1149'},
              {'duid': '20181207-e6d471ba-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4b0f85be8e864178b66297b6f380f9aa'},
              {'duid': '20181207-e77d41be-f9cf-11e8-bf1c-ea00e4d87701', 'token': '42b3b3e3b48b4c7cad15784d5063ee61'},
              {'duid': '20181207-e81b378e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '2431a816052e425290ec0ae4c98c53bf'},
              {'duid': '20181207-e8b34934-f9cf-11e8-bf1c-ea00e4d87701', 'token': '87b99c43b9c744f7a94e550b94582ef8'},
              {'duid': '20181207-e960413e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '86601d65660044f681cf2d169991cd50'},
              {'duid': '20181207-e9f94884-f9cf-11e8-bf1c-ea00e4d87701', 'token': '5e30f7f9ef4a40b78375d558fa176ba6'},
              {'duid': '20181207-ea900fc6-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ec8cde617de8426c8d9516df0b5e8a53'},
              {'duid': '20181207-eb2e1dd8-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'fcf6da145c5e47dfb9a7e908857388ba'},
              {'duid': '20181207-ebe431fe-f9cf-11e8-bf1c-ea00e4d87701', 'token': '6f97a3c47b9f4952a06b22e4c4e005c8'},
              {'duid': '20181207-ec882ade-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a516b3a9b1c244fe971973c2468d4910'},
              {'duid': '20181207-ed33d6fe-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'c80e054c18f1481daec03a30c47ec258'},
              {'duid': '20181207-edeaea1a-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b68c82c119304eea8db94f10a4a18ece'},
              {'duid': '20181207-ee842d88-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'bb898da18ac546a3a887713476e81dec'},
              {'duid': '20181207-ef280eb2-f9cf-11e8-bf1c-ea00e4d87701', 'token': '8cc3f3215d094b95815e6c6bbac8af52'},
              {'duid': '20181207-efc42e96-f9cf-11e8-bf1c-ea00e4d87701', 'token': '911d0968d6b04be6a0265df10c1b7d25'},
              {'duid': '20181207-f05c5824-f9cf-11e8-bf1c-ea00e4d87701', 'token': '95c7a472aa0648e9b4cf3ea41b0369fb'},
              {'duid': '20181207-f10175d4-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e2ae5795b4164376bdcd3254d609c6df'},
              {'duid': '20181207-f199bd76-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'aebd74598a114393810a59ed3a0fd251'},
              {'duid': '20181207-f241ab6c-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'abc69c3ee2784dfcb8fe4807297f86f3'},
              {'duid': '20181207-f2d85788-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'aedae6fdeb894e1daa0b621a5c62fce4'},
              {'duid': '20181207-f36dc2b4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1dd4b39692b04ebea80649ec567fa491'},
              {'duid': '20181207-f40718c4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '91e18e9e0b5e40759d6450b0c242da80'},
              {'duid': '20181207-f49fe2f2-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'afa4371ca92148238411065fc594cc9c'},
              {'duid': '20181207-f53889a8-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4c2216dcc08a4137b5cb3a53ef9126b2'},
              {'duid': '20181207-f5d7511e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '21d0b136d1574ae2bec5bb2f6fcbed7f'},
              {'duid': '20181207-f68234da-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e967b49bc9d04c88ab7d79a7c2a9debc'},
              {'duid': '20181207-f7176dd4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '13afc27aeb194c81a8a83cb2e1903313'},
              {'duid': '20181207-f7b31914-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4d2c77c1fba74a92a6de8a0bde92a65e'},
              {'duid': '20181207-f85223e2-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'dbccc4ecd640405c895e0704f4e55a55'},
              {'duid': '20181207-f8ef4672-f9cf-11e8-bf1c-ea00e4d87701', 'token': '40c544c3630c4630a22693f656142c13'},
              {'duid': '20181207-f98777e4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '68711681bd5f4ad28755e02d8cfef993'},
              {'duid': '20181207-fa247fee-f9cf-11e8-bf1c-ea00e4d87701', 'token': '951f96f4495e4a378164c333ca41d92c'},
              {'duid': '20181207-fabb2c46-f9cf-11e8-bf1c-ea00e4d87701', 'token': '52d5da148824439c816111c67730630b'},
              {'duid': '20181207-fb6cb150-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9fcb14ef30964ddf930f94bd78f89d6f'},
              {'duid': '20181207-fc0cda0e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '523da5b0503146d293596f79068b09e5'},
              {'duid': '20181207-fcb50526-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a762e0f05ab84006aa42f9d09f5f48b5'},
              {'duid': '20181207-fd605c50-f9cf-11e8-bf1c-ea00e4d87701', 'token': '176f70bf12784f74aeff728aeda1f67d'},
              {'duid': '20181207-fe046660-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'aed7b7827eda408f80b30ab7d491d157'},
              {'duid': '20181207-fe9d9984-f9cf-11e8-bf1c-ea00e4d87701', 'token': '458356d4543b41cca2eabf929589c92f'},
              {'duid': '20181207-ff347dfe-f9cf-11e8-bf1c-ea00e4d87701', 'token': '6319db60ecc841399d129d06bcb63dc2'},
              {'duid': '20181207-ffc9cc2e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'fd248968369a472e9152ea226c77cb76'},
              {'duid': '20181207-00624742-f9d0-11e8-bf1c-ea00e4d87701', 'token': '6512ac94a14341338d924bf83688bc0f'},
              {'duid': '20181207-0101e554-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'cbad65997df44e1c9b10f2c2d3ba10cf'},
              {'duid': '20181207-019e1fe6-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'a0e13fcc4a3140e2a2ad10bbdb4d4acb'},
              {'duid': '20181207-0234e9a8-f9d0-11e8-bf1c-ea00e4d87701', 'token': '0d6fd6697e6e4a10a9bbee4086c39e13'},
              {'duid': '20181207-02ca1cf8-f9d0-11e8-bf1c-ea00e4d87701', 'token': '41441c5ae70b40e980258fa3c2c3d09e'},
              {'duid': '20181207-03600f56-f9d0-11e8-bf1c-ea00e4d87701', 'token': '770314ad98704cd78a8fbc8841c9940f'},
              {'duid': '20181207-03fa163c-f9d0-11e8-bf1c-ea00e4d87701', 'token': '5a63aed3b34d44b4910633cf43456c30'},
              {'duid': '20181207-049281a6-f9d0-11e8-bf1c-ea00e4d87701', 'token': '6709715789ae449ea9fd9d6b7891829a'},
              {'duid': '20181207-052b381a-f9d0-11e8-bf1c-ea00e4d87701', 'token': '4d8551d4353f428a9869bee0652c7a34'},
              {'duid': '20181207-05c4311e-f9d0-11e8-bf1c-ea00e4d87701', 'token': '5bf4658a34054f57b941e2cf0a45a472'},
              {'duid': '20181207-065b9b8a-f9d0-11e8-bf1c-ea00e4d87701', 'token': '89e0220bfa35489f9ae2410d866a1290'},
              {'duid': '20181207-06f4ae1a-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'd917bfac7541473c8fc9337f63f7c30b'},
              {'duid': '20181207-078c3e10-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'f7e754c88b854b6b9f77314d373ecff1'},
              {'duid': '20181207-082e2cb6-f9d0-11e8-bf1c-ea00e4d87701', 'token': '60a0eccffe12486a852c4c79f08399bf'},
              {'duid': '20181207-08da10b2-f9d0-11e8-bf1c-ea00e4d87701', 'token': '26294578dbdc4c29abb2ec01eed0a5d4'},
              {'duid': '20181207-097b0292-f9d0-11e8-bf1c-ea00e4d87701', 'token': '4fcb347e2bb44497a29524c2b3b8cde6'},
              {'duid': '20181207-0a1fc20a-f9d0-11e8-bf1c-ea00e4d87701', 'token': '8c8c7381566043659523cb898dccb89f'},
              {'duid': '20181207-0ada90b2-f9d0-11e8-bf1c-ea00e4d87701', 'token': '34ca16f08675432aaed6b4e5f496f071'},
              {'duid': '20181207-0b992fe0-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'a2e9c117007a4345b185d900dac1396b'},
              {'duid': '20181207-0c3b11fc-f9d0-11e8-bf1c-ea00e4d87701', 'token': '8498087305894bc29246ad84da12306e'},
              {'duid': '20181207-0cd2a288-f9d0-11e8-bf1c-ea00e4d87701', 'token': '28710d47230b47d4b29ffe9dd588f165'},
              {'duid': '20181207-0d694c9c-f9d0-11e8-bf1c-ea00e4d87701', 'token': '5a53c39920b44bb889d13cce786048a1'},
              {'duid': '20181207-0e00f9de-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'e3c580bd5ce74527bc1ecd3bb977c6b2'},
              {'duid': '20181207-0eab4b64-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'dbfe17b176a34db09e9a21903d1a6a3c'},
              {'duid': '20181207-0f4af308-f9d0-11e8-bf1c-ea00e4d87701', 'token': '5eb64e8835454b1894e7547f064e5ab7'},
              {'duid': '20181207-0feed1d0-f9d0-11e8-bf1c-ea00e4d87701', 'token': '56c58a534df44101b29197c56a8f0d7a'},
              {'duid': '20181207-113f3f52-f9d0-11e8-bf1c-ea00e4d87701', 'token': '22c51258adc8471e858d6fd8f6659589'},
              {'duid': '20181207-11eaf284-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'e57be0cbbb384f3396d7e00381590f78'},
              {'duid': '20181207-12969440-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'd85521757d7a438ab866708e7e02e3ed'},
              {'duid': '20181207-13420c6c-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'b5ae2911c3474e5f88c24344b45ab292'},
              {'duid': '20181207-13e3fdec-f9d0-11e8-bf1c-ea00e4d87701', 'token': '81a4e7139bfb418d8a27d6b86746cf23'},
              {'duid': '20181207-149255fe-f9d0-11e8-bf1c-ea00e4d87701', 'token': '6b3c470134ec4e36a6ff44b3233aff4b'},
              {'duid': '20181207-153bc5f8-f9d0-11e8-bf1c-ea00e4d87701', 'token': '24b057e6857745cda882288aed6d0c3e'},
              {'duid': '20181207-15df10f0-f9d0-11e8-bf1c-ea00e4d87701', 'token': '62d007bde233404a882c3aa15bb7c4d7'},
              {'duid': '20181207-167823a8-f9d0-11e8-bf1c-ea00e4d87701', 'token': '8af5c49750e043be846c4e809b6c0720'},
              {'duid': '20181207-171afc0e-f9d0-11e8-bf1c-ea00e4d87701', 'token': '6c7c5a1f9b064ee88e4c616aac5a8f0f'},
              {'duid': '20181207-17b72dcc-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'ed07f40fbd874e97bf5423c834470350'},
              {'duid': '20181207-185e5fde-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'f53bb5692d9044c38fd473baf3f43637'},
              {'duid': '20181207-1906ed2a-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'b5aa81c424be4782b16d256b49f02917'},
              {'duid': '20181207-19a39328-f9d0-11e8-bf1c-ea00e4d87701', 'token': '77bf178dc2d447b186f27ed68c0d09e5'},
              {'duid': '20181207-1a4f1ea0-f9d0-11e8-bf1c-ea00e4d87701', 'token': '6c54ae1620ee48a2a1a6a588692b85ed'}]

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
