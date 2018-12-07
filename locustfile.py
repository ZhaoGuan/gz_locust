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

user_datas = [{'duid': '20181207-6a06f180-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b6a2f920ba0343138b60c6c1dabee500'},
              {'duid': '20181207-6b1499f6-f9cf-11e8-bf1c-ea00e4d87701', 'token': '18f59f2616ee44039175a67641a362d5'},
              {'duid': '20181207-6bce83c0-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd0dea6acff7448bbae8588f2e222fa5f'},
              {'duid': '20181207-6c7a6f8c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3f43ac65dd6443a09465ca104e64e175'},
              {'duid': '20181207-6d265cb6-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4811cd65dab145b399fa89369ac688ef'},
              {'duid': '20181207-6de1d5cc-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9bb195dc648243abbbb420eb4f3711a3'},
              {'duid': '20181207-6e9d75ca-f9cf-11e8-bf1c-ea00e4d87701', 'token': '470b8e7222044fe58cd03350c06213e9'},
              {'duid': '20181207-6f3965ac-f9cf-11e8-bf1c-ea00e4d87701', 'token': '753ecbda9f434e3da4bbc6e4658c3bd9'},
              {'duid': '20181207-6fe57bb2-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ac13a13d55f64fff964431c948254059'},
              {'duid': '20181207-70a0a608-f9cf-11e8-bf1c-ea00e4d87701', 'token': '2ad0762c8b574bc18c01b8fff7dfeaaf'},
              {'duid': '20181207-713d14de-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f1a62e42c566484dba2538e51c0fe4ef'},
              {'duid': '20181207-71e8cb12-f9cf-11e8-bf1c-ea00e4d87701', 'token': '15e90ca61d61460bbd106f7fe7a5598d'},
              {'duid': '20181207-72a3ba94-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'c296c3fa40ef4085b5ff433863e1f5fe'},
              {'duid': '20181207-735ff092-f9cf-11e8-bf1c-ea00e4d87701', 'token': '5e2a4b11dadf4b40aff43ddf97a4075f'},
              {'duid': '20181207-7403f160-f9cf-11e8-bf1c-ea00e4d87701', 'token': '2077622bf85b492f8547c1d43439d0fc'},
              {'duid': '20181207-74afeae2-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ca135ed6c3a74d34bc5402a9566d831c'},
              {'duid': '20181207-7563a5f0-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a23b1f3e2f9b45399e505480fc4bccea'},
              {'duid': '20181207-760f3460-f9cf-11e8-bf1c-ea00e4d87701', 'token': '0ad958d3e45247889ebf5c60f272e816'},
              {'duid': '20181207-76cb3c28-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9d66eb980ee542659b950b68704b53b8'},
              {'duid': '20181207-7776f69e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'c54d322f9eb54a8fa5da4bf7d282b790'},
              {'duid': '20181207-7832754a-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'edbd51f6a585445c96c88c6e0edca0fb'},
              {'duid': '20181207-78edae0a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '991b6cf42d19422b9dc75b07be4c37cf'},
              {'duid': '20181207-79a9430e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ef37990498024587bdcdf07fbccb96a4'},
              {'duid': '20181207-7a558272-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f3263b46f2a04b3cb6cb19a5ba5a9640'},
              {'duid': '20181207-7b10f408-f9cf-11e8-bf1c-ea00e4d87701', 'token': '8cb85eea40ac415d91f6ddc8c3d27424'},
              {'duid': '20181207-7bc4e436-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'c5186546bda549c5ba066c0215f99e68'},
              {'duid': '20181207-7c7851f6-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7609131f7e4a4ee59ab4abf9520c07c0'},
              {'duid': '20181207-7d33fc6c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '563ec15b7c5d4b008514439ceb8e7e73'},
              {'duid': '20181207-7ddfa792-f9cf-11e8-bf1c-ea00e4d87701', 'token': '226d386b34064193a9cc51289960c65b'},
              {'duid': '20181207-7e8b8cec-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3eb9b071fceb4de4bcd96d0095b0763d'},
              {'duid': '20181207-7f38d618-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3c2b61b15fa046448445cc442f37822f'},
              {'duid': '20181207-7fdf5790-f9cf-11e8-bf1c-ea00e4d87701', 'token': '55f62d6f0721491b9418c8bdfd1f71dc'},
              {'duid': '20181207-809eaee2-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4a4bf551dc8c4ce485e70b9fa2c856bc'},
              {'duid': '20181207-813b18a4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7dfbaff3d8424c21a9be13086e530723'},
              {'duid': '20181207-81d748c8-f9cf-11e8-bf1c-ea00e4d87701', 'token': '15cd671efa9246e48dffde0b9c866328'},
              {'duid': '20181207-8273999e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '47ea5bcde98c4917bca46c616e3b26e4'},
              {'duid': '20181207-830e4ee4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '012223a6be304ebda5705709089dead4'},
              {'duid': '20181207-83cb13da-f9cf-11e8-bf1c-ea00e4d87701', 'token': '8817de07e63b422d89e83f07b48b5512'},
              {'duid': '20181207-84773b6a-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'bd42f1945ed8484eb0519bdb4ec4db1c'},
              {'duid': '20181207-85137dd6-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3ecba8e634c847598fb6e90ece699e9f'},
              {'duid': '20181207-85ce9a26-f9cf-11e8-bf1c-ea00e4d87701', 'token': '42d4942982d048828574c5f02f6de540'},
              {'duid': '20181207-86739288-f9cf-11e8-bf1c-ea00e4d87701', 'token': '21e8f71328264c10839208e15a6b5b4c'},
              {'duid': '20181207-870f43d6-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7d6fd974cacb4d1e981b60e287896e36'},
              {'duid': '20181207-87c30560-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3782809edf5d4c508a16aa41459b74b3'},
              {'duid': '20181207-886eed4e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '5d1070da88764d6d9159dad4a234b78a'},
              {'duid': '20181207-890fa626-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'c2de19a20e294a12a1644ed6e26f5c92'},
              {'duid': '20181207-89b2de22-f9cf-11e8-bf1c-ea00e4d87701', 'token': '8203582c161b4348ba3a7ecd66f62392'},
              {'duid': '20181207-8a62d71e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1c862fca3920427fb1dcb58a0ff54ddc'},
              {'duid': '20181207-8b07380e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e02e1689ad0e481691b1b08210edb35f'},
              {'duid': '20181207-8ba360d0-f9cf-11e8-bf1c-ea00e4d87701', 'token': '6db9f8506bce427bb57ab4f34a266c71'},
              {'duid': '20181207-8c471626-f9cf-11e8-bf1c-ea00e4d87701', 'token': '0b70b147f149477aa71a19acdb6c8435'},
              {'duid': '20181207-8cf2f5fe-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd5ddee05d91848e2be8b3b00549a00bd'},
              {'duid': '20181207-8da77d80-f9cf-11e8-bf1c-ea00e4d87701', 'token': '2d663979c350447d9914cb01ece95102'},
              {'duid': '20181207-8e42c98e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ee5196df7ed74714a082cc585f076188'},
              {'duid': '20181207-8ef6c060-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a55ff982829843329aea2b19ce05d33c'},
              {'duid': '20181207-8fae6bde-f9cf-11e8-bf1c-ea00e4d87701', 'token': '73d5cbd7bda84806be43c2510c83947e'},
              {'duid': '20181207-905e0468-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'dcca78e59eff43fbaf1e1b91332b8367'},
              {'duid': '20181207-90fa1394-f9cf-11e8-bf1c-ea00e4d87701', 'token': '405bed861fcc43bcb263baa77dc36ae6'},
              {'duid': '20181207-919657f4-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'cdd1ce5633804e67b51c847622b9129a'},
              {'duid': '20181207-922f7fc4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '0497d2052e794529806cea9bcadcd24e'},
              {'duid': '20181207-92ceec9e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ca559d3735964cdd9e7b71a10bf70506'},
              {'duid': '20181207-936b6b1e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '6c760a934b0a411d930be48248e98817'},
              {'duid': '20181207-94073936-f9cf-11e8-bf1c-ea00e4d87701', 'token': '29c1e9621ba44a37916d89745f92a40e'},
              {'duid': '20181207-94a3ed8a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1831f432e147452d932018f57bfbfd5f'},
              {'duid': '20181207-953fe58c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9d7dee9206fe4f5a8d045b61a7f8bf38'},
              {'duid': '20181207-963821c0-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a4104e7c3e4d4b9e956742f1c3a0f5b9'},
              {'duid': '20181207-96e60e20-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'dcf4d1e354ef4ad6920e79f2b33d2318'},
              {'duid': '20181207-97927e9e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4f0e78fc9c4a44bda5d22876d2656edd'},
              {'duid': '20181207-983d9b80-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ff2250b51c56413c828fecc9f6cc6288'},
              {'duid': '20181207-98da0e20-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd86632f12de749ff9e516125c19ae73d'},
              {'duid': '20181207-99a4db00-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'fd4ca50e0fb2461dbbefefd946ebaeee'},
              {'duid': '20181207-9a605c5e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b06bc23193d14dcc8dc2b35cdf458dac'},
              {'duid': '20181207-9b0c833a-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a216ac7df60b4a25a114c9cd96a41fd4'},
              {'duid': '20181207-9bb8a566-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a4751bd99c6c4f48b505fb5fc788dc2a'},
              {'duid': '20181207-9c656a30-f9cf-11e8-bf1c-ea00e4d87701', 'token': '6dae2294f5c94ea1961c98e69fd1dda4'},
              {'duid': '20181207-9cfe2ee6-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'fd9c85edb31d4ca09b69f1f887ae69a7'},
              {'duid': '20181207-9dac6934-f9cf-11e8-bf1c-ea00e4d87701', 'token': '67d651b863db4eb3a4343dbe00170a1a'},
              {'duid': '20181207-9e43b9ec-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'c044c5d351a1422dba24507b15ae0c58'},
              {'duid': '20181207-9edb4564-f9cf-11e8-bf1c-ea00e4d87701', 'token': '67dfc91a73ec42bd9d0562d0313700db'},
              {'duid': '20181207-9f7f193c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '74d6a6debd9a4465ac90d11bde7750e0'},
              {'duid': '20181207-a03c71e4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '617fe34844fb43e0bb1f4cf6192534fb'},
              {'duid': '20181207-a0f7e0fa-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd01a39076eab461683ce04a1b51673a4'},
              {'duid': '20181207-a1e0428c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7bd8902174054c4cb73fa99aae1c310f'},
              {'duid': '20181207-a27df5ae-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e766b1ea587c4bd4a7d1fbd70c6bc011'},
              {'duid': '20181207-a339ff92-f9cf-11e8-bf1c-ea00e4d87701', 'token': '28ef408415714f5496f7d2e734350d05'},
              {'duid': '20181207-a3edf43e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4acf99ba9c744679beb118cfd4291c2b'},
              {'duid': '20181207-a4a18dbe-f9cf-11e8-bf1c-ea00e4d87701', 'token': '88ff16d11a974bf091417d29057f217b'},
              {'duid': '20181207-a55d314a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '22cecc6916704369802a42e02c47c2b7'},
              {'duid': '20181207-a60903c6-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4b77714d740c43bfaccaaf74eee9038b'},
              {'duid': '20181207-a6c46c60-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3eae648103974308aa738f8501e28c2c'},
              {'duid': '20181207-a7704706-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'be607a938eb74d97b891a111cf87cecf'},
              {'duid': '20181207-a82bc864-f9cf-11e8-bf1c-ea00e4d87701', 'token': '29bd17bd1bf94a5aa5c8c99085794c12'},
              {'duid': '20181207-a8d7e7d4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '635cd762258a4745b75e8ffc16870a32'},
              {'duid': '20181207-a9934858-f9cf-11e8-bf1c-ea00e4d87701', 'token': '19ff4b9e065847789b7dd97f0a04b028'},
              {'duid': '20181207-aa475c94-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b24f531d6f034d8b9e98548268e45e96'},
              {'duid': '20181207-aafa7414-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1100d17baf564e5d8eab542683fedf58'},
              {'duid': '20181207-aba7162e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '2652053f232e4021948a701d63252d0a'},
              {'duid': '20181207-ac620f74-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7a67036c804d41dcbd19f3bdb11531f7'},
              {'duid': '20181207-ad0e0ad6-f9cf-11e8-bf1c-ea00e4d87701', 'token': '5999ed18e1264bce9991ec9f41385f35'},
              {'duid': '20181207-adb9ca92-f9cf-11e8-bf1c-ea00e4d87701', 'token': '065133eb620744239a7d468f13110817'},
              {'duid': '20181207-ae5f86f8-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ff63345e2e6d4b7f8a84977874af282c'},
              {'duid': '20181207-af09e756-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e60816424a374dbf84622000fabdfa36'},
              {'duid': '20181207-afad9f36-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a01298b0abe4412c89adb8b2c4c03e2c'},
              {'duid': '20181207-b057b8a4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '962dfd38cce34ec19a11b85815f25d70'},
              {'duid': '20181207-b0f5c404-f9cf-11e8-bf1c-ea00e4d87701', 'token': '22015ec5fd81474695daf33e5931391c'},
              {'duid': '20181207-b1a9f726-f9cf-11e8-bf1c-ea00e4d87701', 'token': '5424a59821524dd3845595a3be4aa61d'},
              {'duid': '20181207-b24dc310-f9cf-11e8-bf1c-ea00e4d87701', 'token': '401135681d7d40e8bdf04e5b6cf362e1'},
              {'duid': '20181207-b2f9abda-f9cf-11e8-bf1c-ea00e4d87701', 'token': '45f48dacdbad4fb08cb1e783b3526f5a'},
              {'duid': '20181207-b3b52e0a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '53933013e8ce49498ef2e59b9ca7eb82'},
              {'duid': '20181207-b468e76a-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e132122f47084ef195ad9055b091bbbf'},
              {'duid': '20181207-b51c8126-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'c4e9cc794b4642d286b6e47c631b8514'},
              {'duid': '20181207-b5c81590-f9cf-11e8-bf1c-ea00e4d87701', 'token': '8da25ef7c1764c8caae7fb1e4a32f4bc'},
              {'duid': '20181207-b674254c-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b7dd8590d87f46d3ad15997903a6be9a'},
              {'duid': '20181207-b718a450-f9cf-11e8-bf1c-ea00e4d87701', 'token': '331ce67abc60444b8646ab98cd0c60e4'},
              {'duid': '20181207-b7bc71de-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f98d28bf23b840f4839c2b1c1433c608'},
              {'duid': '20181207-b869e3fa-f9cf-11e8-bf1c-ea00e4d87701', 'token': '88b588bc591440258ecac2c1554f0f04'},
              {'duid': '20181207-b9059a84-f9cf-11e8-bf1c-ea00e4d87701', 'token': '6019a07f5561418a927c1cc2c7160201'},
              {'duid': '20181207-b9b06324-f9cf-11e8-bf1c-ea00e4d87701', 'token': '59bad8b61a31497a85f5a573526ef744'},
              {'duid': '20181207-ba641e32-f9cf-11e8-bf1c-ea00e4d87701', 'token': '0f00f0258d7247b78cb3968862070258'},
              {'duid': '20181207-bb17c7b6-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'fd67801d6f1d425080ca08f9aa73ed23'},
              {'duid': '20181207-bbd2f7d4-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ff42a178d4fe448d9c63fff8e7dfac16'},
              {'duid': '20181207-bc7ef0e8-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ce854c1877924808b7cb0a70366b483f'},
              {'duid': '20181207-bd3acd86-f9cf-11e8-bf1c-ea00e4d87701', 'token': '578c640dcd4f41ffb8a2bc6f145e93ef'},
              {'duid': '20181207-bdf628f6-f9cf-11e8-bf1c-ea00e4d87701', 'token': '627675eb30034bb584fac00db8115ab4'},
              {'duid': '20181207-bf1f89de-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3df5487d4f674dfe83ce78c017c325ae'},
              {'duid': '20181207-c0118108-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a79c1065f3194399a40836894921d7d6'},
              {'duid': '20181207-c0d8a990-f9cf-11e8-bf1c-ea00e4d87701', 'token': '23dd042b9c7e4da3a8499c918cace92a'},
              {'duid': '20181207-c1bf0fac-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'daca465abfd64752a9ad34a0e5cd2cab'},
              {'duid': '20181207-c299b7ce-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'c901f11dc64b47cf9cc5589ddcbd8f6b'},
              {'duid': '20181207-c3759384-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4a94dfc4d5f34c9cab5cf741c2f9e89f'},
              {'duid': '20181207-c45ebde8-f9cf-11e8-bf1c-ea00e4d87701', 'token': '36f40ece1f6d47c7a178b3f49b2383bf'},
              {'duid': '20181207-c5438e50-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4355230e7d1e4ee3ae0027ecb7fbe600'},
              {'duid': '20181207-c623fdb4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1997badcb96f472180d589f18ea1c5c7'},
              {'duid': '20181207-c6ff682c-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'dd7b2a9664e44e2eb720a7442fe08af3'},
              {'duid': '20181207-c7c9b9e2-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e82dca8c49cf4161a027d6d46ca164f3'},
              {'duid': '20181207-c8c3bf46-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a20570b4f0394338801b3672a0cfba36'},
              {'duid': '20181207-c99fc86a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1a7fbdd6705f47c4bebd3833db2e7348'},
              {'duid': '20181207-ca5de502-f9cf-11e8-bf1c-ea00e4d87701', 'token': '942142fde8cd4afca4902a7ed1283dac'},
              {'duid': '20181207-cb35e06a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9f7d716ae6974baa98fa55938bd3890b'},
              {'duid': '20181207-cc0f6088-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1e2741bab9964a8c91c8d4cc5fa3245e'},
              {'duid': '20181207-ccdc08fe-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e95f11d593384ce8abd884a3942012c7'},
              {'duid': '20181207-cdbcb322-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3c3078b926534b478f8de59673048ce6'},
              {'duid': '20181207-ce999e5e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '45722d1ce95d4ea38a6c86961adbe0b1'},
              {'duid': '20181207-cf6ceab6-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'df9574ea8e4c4a49843d17a339d4286f'},
              {'duid': '20181207-d035e7fe-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9123dd95dd4644cb9d81329a5896a599'},
              {'duid': '20181207-d100f93a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7c08f94ed89943cc879d84bd2760e75b'},
              {'duid': '20181207-d1bca572-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9609c650a46f4a7ebcdfa6863597e946'},
              {'duid': '20181207-d25904d0-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f3aee4bea9d045859a143a77c777aa15'},
              {'duid': '20181207-d308e936-f9cf-11e8-bf1c-ea00e4d87701', 'token': '348487add8824ef280f284935982c5a4'},
              {'duid': '20181207-d3b8e0e8-f9cf-11e8-bf1c-ea00e4d87701', 'token': '54426f3afdb14ffd943a5c6b64bead80'},
              {'duid': '20181207-d4549218-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1e3d607685b84cc7a2751db86be04cc1'},
              {'duid': '20181207-d4f16d7c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '60f2b96b727b45549b6615543f75073d'},
              {'duid': '20181207-d594ef42-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7f58132f30434f09af08f97980e87d29'},
              {'duid': '20181207-d650a296-f9cf-11e8-bf1c-ea00e4d87701', 'token': '0bf42674191941dfa1c2530c241c7bb7'},
              {'duid': '20181207-d703dc26-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ea7158cf34f74c2bacf0f61ac67b4dce'},
              {'duid': '20181207-d7b7ee96-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f38ed2fddd6c403391d3cdeacee3f089'},
              {'duid': '20181207-d8616e80-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1685b76e33c449ff8f062d328f2e3fc0'},
              {'duid': '20181207-d91f210a-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a3ff62c9995745e88825b777be5ae52d'},
              {'duid': '20181207-d9cb11f4-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'c0365859e6b14e59b928a572e2086c21'},
              {'duid': '20181207-da6fc01e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '821dd8ff1ae541b5aceaf73d59bf26b7'},
              {'duid': '20181207-db111748-f9cf-11e8-bf1c-ea00e4d87701', 'token': '80377178646b4ac6b94c504414234430'},
              {'duid': '20181207-dbb841ee-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4e63d491e59f4f0680bae1cd14b855ef'},
              {'duid': '20181207-dc737568-f9cf-11e8-bf1c-ea00e4d87701', 'token': '741b8ad7034e46eb93f082d3bfbcb13f'},
              {'duid': '20181207-dd14e77c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '8df5140e772d4bc883124d132582c4b9'},
              {'duid': '20181207-ddb09b40-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1817aa994c8d4e5cb1cad9e49ecc6fee'},
              {'duid': '20181207-de493df0-f9cf-11e8-bf1c-ea00e4d87701', 'token': '490ae54d3a6d45d485f5de14111a0efc'},
              {'duid': '20181207-dee17eee-f9cf-11e8-bf1c-ea00e4d87701', 'token': '82b4448b23b343b69169fae424e131c3'},
              {'duid': '20181207-df78da6e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd9fc78889d26409998fa33ac3f414a1c'},
              {'duid': '20181207-e013263c-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd61ff310f74b461a96b21256ec7d90a2'},
              {'duid': '20181207-e0b5432c-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'dcb49b5609f449b9a033f8437c5827d9'},
              {'duid': '20181207-e15a5128-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd7cfd729cda643ea901ee137606ab222'},
              {'duid': '20181207-e1f2145e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'fa600366bebe4254a28183009790e193'},
              {'duid': '20181207-e28afa98-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e6ac07bbab6e4f1d86a61c4eb58e4b48'},
              {'duid': '20181207-e330e2d2-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3ca8812b54d84de68b4863493fe1a25a'},
              {'duid': '20181207-e3d5d620-f9cf-11e8-bf1c-ea00e4d87701', 'token': '5022d4efde6a438f836dfbc16d3d08a6'},
              {'duid': '20181207-e476e132-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'aef5d444e74a4c16b0038c3343c6a822'},
              {'duid': '20181207-e50e3ee2-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'aa9e492f61924dc5b8f36bd53eda7202'},
              {'duid': '20181207-e5a54986-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ded319c2e4a748ada8e95c9f1c4ce1f2'},
              {'duid': '20181207-e63c7112-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'c14a54c18bad41d79931986b4491abef'},
              {'duid': '20181207-e6d471ba-f9cf-11e8-bf1c-ea00e4d87701', 'token': '54e2bc3effab4c9ba63b9800092df85c'},
              {'duid': '20181207-e77d41be-f9cf-11e8-bf1c-ea00e4d87701', 'token': '2b149dd3bb1145418c2ec01f9d772187'},
              {'duid': '20181207-e81b378e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'fd52e4c9724440108748c3e2c4ace28f'},
              {'duid': '20181207-e8b34934-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9fc37c75763a4ed681e7cc8c88916409'},
              {'duid': '20181207-e960413e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '37e78184b928490c995d01b7ea6c5484'},
              {'duid': '20181207-e9f94884-f9cf-11e8-bf1c-ea00e4d87701', 'token': '2f444b2e2396479db3cd8e051e1ea454'},
              {'duid': '20181207-ea900fc6-f9cf-11e8-bf1c-ea00e4d87701', 'token': '00fe01a8d7614d45acca56c0f4cc54de'},
              {'duid': '20181207-eb2e1dd8-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e594a834e5fe43c4b69cdfc996b1ab69'},
              {'duid': '20181207-ebe431fe-f9cf-11e8-bf1c-ea00e4d87701', 'token': '14745b1983fd4db783b6226ecae6f479'},
              {'duid': '20181207-ec882ade-f9cf-11e8-bf1c-ea00e4d87701', 'token': '23b514165e1a4d98ae47c0bb527801eb'},
              {'duid': '20181207-ed33d6fe-f9cf-11e8-bf1c-ea00e4d87701', 'token': '8c6e51e4a9374e75a5ca4e65b771e366'},
              {'duid': '20181207-edeaea1a-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'cc156cfdbec34a90aad3fd6c3f1939fd'},
              {'duid': '20181207-ee842d88-f9cf-11e8-bf1c-ea00e4d87701', 'token': '08a7fd21e7984e9eb865daf215c2c09e'},
              {'duid': '20181207-ef280eb2-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'eb98f307111f4fc7935cda36d6b40a71'},
              {'duid': '20181207-efc42e96-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e0ecc4aaeb4e40bb9663a7f957bd796f'},
              {'duid': '20181207-f05c5824-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b862f5269978447587c7ba45e0f1b4e7'},
              {'duid': '20181207-f10175d4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '562acc8ad6ca421baa53b01fafd8d86f'},
              {'duid': '20181207-f199bd76-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ea0b83c78af54a6cbb4e9e808bb25a74'},
              {'duid': '20181207-f241ab6c-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'c433b98195014a4e908307e7fd50e3f7'},
              {'duid': '20181207-f2d85788-f9cf-11e8-bf1c-ea00e4d87701', 'token': '83a3736325314f598632f1b6160e39a1'},
              {'duid': '20181207-f36dc2b4-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'c043532bedbb4987a5ad2f4337a12442'},
              {'duid': '20181207-f40718c4-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'bbc1bda939e34ebbbd33a28cee142a23'},
              {'duid': '20181207-f49fe2f2-f9cf-11e8-bf1c-ea00e4d87701', 'token': '95eeab3d7f614efd883d8f50eb980bde'},
              {'duid': '20181207-f53889a8-f9cf-11e8-bf1c-ea00e4d87701', 'token': '0476b6e98b5241ee8d09dde2a6e1b80d'},
              {'duid': '20181207-f5d7511e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ad66c1198998451bab18f70926edbcb0'},
              {'duid': '20181207-f68234da-f9cf-11e8-bf1c-ea00e4d87701', 'token': '77fae6311e6b4273b431631cecfd93ed'},
              {'duid': '20181207-f7176dd4-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a2a259ce1e624575802842f88cb6f471'},
              {'duid': '20181207-f7b31914-f9cf-11e8-bf1c-ea00e4d87701', 'token': '32f3aa3a650c4a3ebb018148d3bbeb52'},
              {'duid': '20181207-f85223e2-f9cf-11e8-bf1c-ea00e4d87701', 'token': '924444e7194844fc893ab86eee5c06f7'},
              {'duid': '20181207-f8ef4672-f9cf-11e8-bf1c-ea00e4d87701', 'token': '90f8318f1a7249e8bfb27621df48f300'},
              {'duid': '20181207-f98777e4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1b8e9c8f93a648ae89c5f57ea1428420'},
              {'duid': '20181207-fa247fee-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ec889a400e2f4fdaa360d0541bfb21c8'},
              {'duid': '20181207-fabb2c46-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9ba3871db22d44bc9d2f5d48c779592a'},
              {'duid': '20181207-fb6cb150-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7ac27b81a0c54f82a39522133db2b087'},
              {'duid': '20181207-fc0cda0e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'c2e72bded9cc4954b0e2535d6d6b1cbe'},
              {'duid': '20181207-fcb50526-f9cf-11e8-bf1c-ea00e4d87701', 'token': '8479b042b1f0421c8c5f76f1c4035a8b'},
              {'duid': '20181207-fd605c50-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b6a942a43c0e4f739a64ce5eaa535b0c'},
              {'duid': '20181207-fe046660-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a569b9bbba014e1bad08ca7596d9f9e1'},
              {'duid': '20181207-fe9d9984-f9cf-11e8-bf1c-ea00e4d87701', 'token': '811ba1eacbcd47b6ac2593a9a707d083'},
              {'duid': '20181207-ff347dfe-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd5c430733ea74948982962ffbac59089'},
              {'duid': '20181207-ffc9cc2e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'dfbc01d46d114ef38f953ccf842e72cb'},
              {'duid': '20181207-00624742-f9d0-11e8-bf1c-ea00e4d87701', 'token': '2705e5ca80364b15a4a89119d6411dcf'},
              {'duid': '20181207-0101e554-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'cead1c1c9f6a4e1d98505593df69c3ec'},
              {'duid': '20181207-019e1fe6-f9d0-11e8-bf1c-ea00e4d87701', 'token': '818ae5d4938e43a298bc1b7852870a7e'},
              {'duid': '20181207-0234e9a8-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'f090222c4b1c4d7fbc3ba8d565a2df3c'},
              {'duid': '20181207-02ca1cf8-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'efedd6e323cf43af8c695f55e312e4c4'},
              {'duid': '20181207-03600f56-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'e6ae932951b24e34a0030b6476575762'},
              {'duid': '20181207-03fa163c-f9d0-11e8-bf1c-ea00e4d87701', 'token': '9a0012b0ada94380ad383c6c823f6897'},
              {'duid': '20181207-049281a6-f9d0-11e8-bf1c-ea00e4d87701', 'token': '77dc62d9339d4e049a8d1cbfa3526e55'},
              {'duid': '20181207-052b381a-f9d0-11e8-bf1c-ea00e4d87701', 'token': '429acb9818cc457c89ec8dc5f0ce6587'},
              {'duid': '20181207-05c4311e-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'bb9ecc1a646d43ab914a2e8feede0acc'},
              {'duid': '20181207-065b9b8a-f9d0-11e8-bf1c-ea00e4d87701', 'token': '2dacfe8fb6c746b5855312f9d62bff78'},
              {'duid': '20181207-06f4ae1a-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'a4de22c9245c488697a05772ea638cff'},
              {'duid': '20181207-078c3e10-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'd2968a0f7b0b453c91912cb392df4ab8'},
              {'duid': '20181207-082e2cb6-f9d0-11e8-bf1c-ea00e4d87701', 'token': '9f6593ccd55e475c9df2a2ff923f137e'},
              {'duid': '20181207-08da10b2-f9d0-11e8-bf1c-ea00e4d87701', 'token': '4d935488aa7248c39b24bfca0b25123f'},
              {'duid': '20181207-097b0292-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'e090b76b73cb413683cd2d4727543de0'},
              {'duid': '20181207-0a1fc20a-f9d0-11e8-bf1c-ea00e4d87701', 'token': '2afac73eee30453c979c53a60ddf1140'},
              {'duid': '20181207-0ada90b2-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'd09ce62d0b094a3f857c785c02cf4dd4'},
              {'duid': '20181207-0b992fe0-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'ed98c0ea8acb488580729620930e04b8'},
              {'duid': '20181207-0c3b11fc-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'f259afc0b6494d128942716b3eb4d1f7'},
              {'duid': '20181207-0cd2a288-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'fa1a20f3f3da430ebaa7c736d8e331a8'},
              {'duid': '20181207-0d694c9c-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'f278c9832a9546d3bff5a34c5220a3ce'},
              {'duid': '20181207-0e00f9de-f9d0-11e8-bf1c-ea00e4d87701', 'token': '7d7b41e5048e4b1ea61bd2cdc5695c2f'},
              {'duid': '20181207-0eab4b64-f9d0-11e8-bf1c-ea00e4d87701', 'token': '92ed68aec84b43d89352cafd6e04a98f'},
              {'duid': '20181207-0f4af308-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'ba3ddfc57dac4c54bf725804038e0935'},
              {'duid': '20181207-0feed1d0-f9d0-11e8-bf1c-ea00e4d87701', 'token': '94c40ff65b93486782e43714531f280d'},
              {'duid': '20181207-113f3f52-f9d0-11e8-bf1c-ea00e4d87701', 'token': '5f18aed70ea844c492db860eeff1aaff'},
              {'duid': '20181207-11eaf284-f9d0-11e8-bf1c-ea00e4d87701', 'token': '1b6335a68ad9421ea7db295d85b4cbb4'},
              {'duid': '20181207-12969440-f9d0-11e8-bf1c-ea00e4d87701', 'token': '1e1428cf7d524b649ad9ff0e7603a27c'},
              {'duid': '20181207-13420c6c-f9d0-11e8-bf1c-ea00e4d87701', 'token': '1836711f0dc5472d8ca3f49d72fb1a2f'},
              {'duid': '20181207-13e3fdec-f9d0-11e8-bf1c-ea00e4d87701', 'token': '696679e651064f3d83ad7d7fa5d254ce'},
              {'duid': '20181207-149255fe-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'bd2ee81abba4465eae66372fba450a59'},
              {'duid': '20181207-153bc5f8-f9d0-11e8-bf1c-ea00e4d87701', 'token': '5182694c8be3432f9f125d7565259646'},
              {'duid': '20181207-15df10f0-f9d0-11e8-bf1c-ea00e4d87701', 'token': '464bff63177d4e689905db7c4563b7bc'},
              {'duid': '20181207-167823a8-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'ae80f39f579c48ac87da5d2bc60efee3'},
              {'duid': '20181207-171afc0e-f9d0-11e8-bf1c-ea00e4d87701', 'token': '16b4d7e45dff4a588315d5e1e88fcc86'},
              {'duid': '20181207-17b72dcc-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'a59f14547dcc494399a3261e3e89483b'},
              {'duid': '20181207-185e5fde-f9d0-11e8-bf1c-ea00e4d87701', 'token': '694d47d8e4c14f5f966150aea5699408'},
              {'duid': '20181207-1906ed2a-f9d0-11e8-bf1c-ea00e4d87701', 'token': '8687a1da3d894caaa2a45854c09d592b'},
              {'duid': '20181207-19a39328-f9d0-11e8-bf1c-ea00e4d87701', 'token': '5ea91b5c2f694bc38d4a0f628fa52872'},
              {'duid': '20181207-1a4f1ea0-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'd80ecaa1d05045fb9aea485808a834ad'}]

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

    @task(10)
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
