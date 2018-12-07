# -*- coding: utf-8 -*-
# __author__ = 'Gz'
import datetime
import time
import uuid
import requests
import json
import yaml
from basics_function.golable_function import MD5, config_reader

today = datetime.date.today().strftime("%Y%m%d")
language = "en_US"
version = "1"
salt = "3*y4f569#tunt$le!i5o"

source = "online"


class GetToken:
    def __init__(self):
        self.duid = None

    def header(self):
        time_stamp = str(int(round(time.time() * 1000)))
        return {"header": {
            'User-Agent': self.duid + "#&#" + language + "#&#" + time_stamp + "#&#" + str(
                version)}, "time_stamp": time_stamp}

    def get_sign(self, time_stamp):
        data = self.duid + "_" + language + "_" + time_stamp + "_" + str(version) + "_" + salt
        result = MD5(data)
        return result

    def random_duid(self):
        duid = str(today) + "-" + str(uuid.uuid1())
        return duid

    def login_token(self, duid):
        self.duid = duid
        if source == "test":
            token_url = "http://api.dev.wuren.com:8080/v1/identity/login"
        else:
            token_url = "https://api.5nuthost.com/v1/identity/login"
        print(self.header())
        header = self.header()["header"]
        time_stamp = self.header()["time_stamp"]
        response = requests.post(token_url, json={"sign": self.get_sign(time_stamp)}, headers=header)
        if response.status_code == 200:
            try:
                token = json.loads(response.text)["info"]["token"]
            except:
                print(response.text)
                print(duid)
                assert False, "获取token错误"
        else:
            print(response.text)
        return {"duid": self.duid, "token": token}

    def registry(self):
        self.duid = self.random_duid()
        if source == "test":
            token_url = "http://api.dev.wuren.com:8080/v1/identity/registry"
        else:
            token_url = "https://api.5nuthost.com/v1/identity/registry"
        # print(self.header())
        header = self.header()["header"]
        time_stamp = self.header()["time_stamp"]
        response = requests.post(token_url, json={"sign": self.get_sign(time_stamp), "identity": "meme-app"},
                                 headers=header)
        if response.status_code == 200:
            try:
                token = json.loads(response.text)["info"]["token"]
                print("！！！！！！！")
            except:
                print(response.text)
                assert False, "获取token错误"
        else:
            pass
        # print(response.text)
        return {"duid": self.duid, "token": token}


def registry_duid_tokens(no):
    GT = GetToken()
    result = []
    while True:
        data = GT.registry()
        result.append(data)
        if len(result) == no:
            with open("./duid_token.yaml", "w") as f:
                yaml.dump(result, f, default_flow_style=False)
            break


def reflash_token():
    GT = GetToken()
    path = "./duid_token.yaml"
    data = config_reader(path)
    result = []
    count = 0
    for i in data:
        duid = i["duid"]
        duid_token = GT.login_token(duid)
        result.append(duid_token)
        print(result)
        count += 1
        print(count)
    with open("./duid_token.yaml", "w") as f:
        yaml.dump(result, f, default_flow_style=False)


if __name__ == "__main__":
    # registry_duid_tokens(1000)
    reflash_token()
    result = [
        {'duid': '20181207-6a06f180-f9cf-11e8-bf1c-ea00e4d87701', 'token': '86cca4af224b4f32bf4a6ae62929de09'},
        {'duid': '20181207-6b1499f6-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'fcda3c3b3bea43fda42c809e3a000403'},
        {'duid': '20181207-6bce83c0-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3ea017009e754b87ada9fb3abba199a1'},
        {'duid': '20181207-6c7a6f8c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '306ad494922f4b2080782c0bb8ab55d7'},
        {'duid': '20181207-6d265cb6-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'df06333ed1b44f36a79a5e6a4fe3af4d'},
        {'duid': '20181207-6de1d5cc-f9cf-11e8-bf1c-ea00e4d87701', 'token': '39a0cbbe9ce04c65b6e37d32b3819845'},
        {'duid': '20181207-6e9d75ca-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'fe7e59ec538f4598b83f185b9e6ca25c'},
        {'duid': '20181207-6f3965ac-f9cf-11e8-bf1c-ea00e4d87701', 'token': '68bc8c15e26b46a8b230b2db64882076'},
        {'duid': '20181207-6fe57bb2-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f0ebc57283b541bf861b0a103825c699'},
        {'duid': '20181207-70a0a608-f9cf-11e8-bf1c-ea00e4d87701', 'token': '31d6281874c64ea19ce16f2b02c1074c'},
        {'duid': '20181207-713d14de-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b169a0a1b7e746ae8f7b0465e7970231'},
        {'duid': '20181207-71e8cb12-f9cf-11e8-bf1c-ea00e4d87701', 'token': '417215f010be47f5931e070333516e21'},
        {'duid': '20181207-72a3ba94-f9cf-11e8-bf1c-ea00e4d87701', 'token': '769d5bc404074c5cb516926902e99085'},
        {'duid': '20181207-735ff092-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b90824f243d04f208622c94ee344256d'},
        {'duid': '20181207-7403f160-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3d007970e285465c9b69c1b56131a53e'},
        {'duid': '20181207-74afeae2-f9cf-11e8-bf1c-ea00e4d87701', 'token': '22c4234f17d74775ba735c573aae5d82'},
        {'duid': '20181207-7563a5f0-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3c5b1e10efd14a4b92534bd4c38af007'},
        {'duid': '20181207-760f3460-f9cf-11e8-bf1c-ea00e4d87701', 'token': '84c2cacdee6e4614b08ccdc2ee09bcb7'},
        {'duid': '20181207-76cb3c28-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3c72b28621624926a9490c2afd734c9e'},
        {'duid': '20181207-7776f69e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '586ab00173cf458b9fe04a04fe1d5362'},
        {'duid': '20181207-7832754a-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'c784395ebd254551a9e04ca38c4040f7'},
        {'duid': '20181207-78edae0a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '5152b60fc42e4f0baa1cf6613b7b6700'},
        {'duid': '20181207-79a9430e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9a00ffed2b9e48fa9c8e87bafb5882f9'},
        {'duid': '20181207-7a558272-f9cf-11e8-bf1c-ea00e4d87701', 'token': '385d4ea58bff4145a43c49b7e3800727'},
        {'duid': '20181207-7b10f408-f9cf-11e8-bf1c-ea00e4d87701', 'token': '2132d4e7253149eb877098eb34d29cc5'},
        {'duid': '20181207-7bc4e436-f9cf-11e8-bf1c-ea00e4d87701', 'token': '0b5983135b454b45b5f8daa4a85a5450'},
        {'duid': '20181207-7c7851f6-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f104ebffab9b4082a6809a780bc0beca'},
        {'duid': '20181207-7d33fc6c-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'dd814fb6f30a41ccacb2e1a6078fde1b'},
        {'duid': '20181207-7ddfa792-f9cf-11e8-bf1c-ea00e4d87701', 'token': '6a23553abf964b92a354c46e46d834e8'},
        {'duid': '20181207-7e8b8cec-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4ea706d5bd494f8fa56d53ff282a9f55'},
        {'duid': '20181207-7f38d618-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a60bfe9cae7d4394bc26da14de7420cf'},
        {'duid': '20181207-7fdf5790-f9cf-11e8-bf1c-ea00e4d87701', 'token': '497096395d5d4bf496e9b6ddbbaff4ac'},
        {'duid': '20181207-809eaee2-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'aacb40b1d2154d92866816191f47c375'},
        {'duid': '20181207-813b18a4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '5a41441cb493492da6eb773071ed800c'},
        {'duid': '20181207-81d748c8-f9cf-11e8-bf1c-ea00e4d87701', 'token': '58c53fe6fb884e7cb8f84f99acdac343'},
        {'duid': '20181207-8273999e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'bb3d0fb1e7ef40a3b3fb07b33ab1898a'},
        {'duid': '20181207-830e4ee4-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ccf9c788e16e44b2aefe185da76697ee'},
        {'duid': '20181207-83cb13da-f9cf-11e8-bf1c-ea00e4d87701', 'token': '2df58d9ad4254ba69cdda9854e903858'},
        {'duid': '20181207-84773b6a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '5c12eafb6ea54e61954380ab1f27815a'},
        {'duid': '20181207-85137dd6-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b5700e5eb7894f479d46c2e67cb4c527'},
        {'duid': '20181207-85ce9a26-f9cf-11e8-bf1c-ea00e4d87701', 'token': '00a92069435f4cbd83f0569fee74d4e1'},
        {'duid': '20181207-86739288-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9ead3eea9d08453185b7fb9423e9a230'},
        {'duid': '20181207-870f43d6-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e77a66f3dfda4b4f91c2651d1dfeda00'},
        {'duid': '20181207-87c30560-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9ee37ce5863844a0a6a9d18256ac4510'},
        {'duid': '20181207-886eed4e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '5cb95eb743bd490cb3c7adecba2d99a1'},
        {'duid': '20181207-890fa626-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f94a4e6f1e6d4d70a85e144bf9d47375'},
        {'duid': '20181207-89b2de22-f9cf-11e8-bf1c-ea00e4d87701', 'token': '86110ffd923c4716a1c23ba6f88dc486'},
        {'duid': '20181207-8a62d71e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '70833b58faff457c809447c7f449ab67'},
        {'duid': '20181207-8b07380e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1a15f66d45dd43beb42dd3b809e6b185'},
        {'duid': '20181207-8ba360d0-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'bfacdda651ec4370ad1546d4f092ab06'},
        {'duid': '20181207-8c471626-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'cdcec6ff51d9428cbbf7855fa16687e8'},
        {'duid': '20181207-8cf2f5fe-f9cf-11e8-bf1c-ea00e4d87701', 'token': '950f362e55fc4ea59adcf7092e8a5411'},
        {'duid': '20181207-8da77d80-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd1669e44882a4b01a7cffc96b939817c'},
        {'duid': '20181207-8e42c98e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '6857db9f25544c3ca3415fdeb4b7850f'},
        {'duid': '20181207-8ef6c060-f9cf-11e8-bf1c-ea00e4d87701', 'token': '51e931125a8841f3a094d540ac51fd73'},
        {'duid': '20181207-8fae6bde-f9cf-11e8-bf1c-ea00e4d87701', 'token': '8a5eb61335d0439f8b4f5d40465035ed'},
        {'duid': '20181207-905e0468-f9cf-11e8-bf1c-ea00e4d87701', 'token': '078f9b86624d4e5ead7c62e143939853'},
        {'duid': '20181207-90fa1394-f9cf-11e8-bf1c-ea00e4d87701', 'token': '879cad0873ae48df80b8bab550fd9c47'},
        {'duid': '20181207-919657f4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '0caf5990f2f14053a3ea118480067c42'},
        {'duid': '20181207-922f7fc4-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'fd4ba3124c2848cb9fe2329cb03f85f4'},
        {'duid': '20181207-92ceec9e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '41cee87801144c419b080c7fd66d5eed'},
        {'duid': '20181207-936b6b1e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ca1cdd63452e49788cf9c35ee366c553'},
        {'duid': '20181207-94073936-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'c68bb6f5a29f4df9a432079c3c329c23'},
        {'duid': '20181207-94a3ed8a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1f4c84c65b5d4effa11b5cc36bed31eb'},
        {'duid': '20181207-953fe58c-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'fd12bfc47efe4facbca6a1b130eed2e3'},
        {'duid': '20181207-963821c0-f9cf-11e8-bf1c-ea00e4d87701', 'token': '8daef57e857940e89aa1605147c6a699'},
        {'duid': '20181207-96e60e20-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b78abcf519904b38a8b945647750f5ed'},
        {'duid': '20181207-97927e9e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '8a37ac7b39364c45ad5604202f4b2958'},
        {'duid': '20181207-983d9b80-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3d81140ec13d4c11ad08dcd7c68200a9'},
        {'duid': '20181207-98da0e20-f9cf-11e8-bf1c-ea00e4d87701', 'token': '2db441fb01dc4811909bcf6b2c0f8c21'},
        {'duid': '20181207-99a4db00-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b45d3117b42242e69b603797a2a419eb'},
        {'duid': '20181207-9a605c5e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9a9c0072a5a44e9194838109810b821c'},
        {'duid': '20181207-9b0c833a-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'c008686356894318ae1d52f0b3e61b14'},
        {'duid': '20181207-9bb8a566-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'bcba45d7498d42ccaa62472ad1c3eb37'},
        {'duid': '20181207-9c656a30-f9cf-11e8-bf1c-ea00e4d87701', 'token': '54cfdf8c5886400baf34c8c276d61d6b'},
        {'duid': '20181207-9cfe2ee6-f9cf-11e8-bf1c-ea00e4d87701', 'token': '92edb0a0096e4f4b96f6dfef524fc5a5'},
        {'duid': '20181207-9dac6934-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f9b0d6761fe844fdbc210501824d9708'},
        {'duid': '20181207-9e43b9ec-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'c1d770d15315443ea108884c474bd777'},
        {'duid': '20181207-9edb4564-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'feac85542e7842818e80e8ff25672b5c'},
        {'duid': '20181207-9f7f193c-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f82e7fc5f97540d8ba2db525cb433516'},
        {'duid': '20181207-a03c71e4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4c876c56a2fd4ef798ceeab5e2b7b611'},
        {'duid': '20181207-a0f7e0fa-f9cf-11e8-bf1c-ea00e4d87701', 'token': '980d51a1a2874d21ad54cf6d620a4d5d'},
        {'duid': '20181207-a1e0428c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '0fdd3efa3a6e4a4984132170538e3d85'},
        {'duid': '20181207-a27df5ae-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'e5ccaad3024b4b08991941372838428e'},
        {'duid': '20181207-a339ff92-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f7d5a0cebab1480ebbcf5c7682ba14c5'},
        {'duid': '20181207-a3edf43e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'aacece2da7314d058cd2f13fe5539b8b'},
        {'duid': '20181207-a4a18dbe-f9cf-11e8-bf1c-ea00e4d87701', 'token': '86603be485ea4cb28660830245edaab6'},
        {'duid': '20181207-a55d314a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '5f39cb7abb054d0cadc849159d2c5e86'},
        {'duid': '20181207-a60903c6-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4801828fb3af424fa9cec488e027b7d7'},
        {'duid': '20181207-a6c46c60-f9cf-11e8-bf1c-ea00e4d87701', 'token': '2e0a82adbbeb4a5996f3c455941dcd33'},
        {'duid': '20181207-a7704706-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'fd3f89b67e2c451386e91294f418b8c4'},
        {'duid': '20181207-a82bc864-f9cf-11e8-bf1c-ea00e4d87701', 'token': '406295c3d7864ca18c755e9c0291d035'},
        {'duid': '20181207-a8d7e7d4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '6507af1075c941a7864eb40ddcbf8760'},
        {'duid': '20181207-a9934858-f9cf-11e8-bf1c-ea00e4d87701', 'token': '2890ac8f0d6b4108af5a065c22e51172'},
        {'duid': '20181207-aa475c94-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'eb17f439195649bd8417bc137510c43c'},
        {'duid': '20181207-aafa7414-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'bdcb2335031d4fcd95e45f91551dbf48'},
        {'duid': '20181207-aba7162e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '5e2a37713005479a9c64d127b315f503'},
        {'duid': '20181207-ac620f74-f9cf-11e8-bf1c-ea00e4d87701', 'token': '21a349fcc5b54fb4a859a7ce08bbca5e'},
        {'duid': '20181207-ad0e0ad6-f9cf-11e8-bf1c-ea00e4d87701', 'token': '5d35dfbfa78849c88ef09870ab3d2093'},
        {'duid': '20181207-adb9ca92-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ab27e8726e354e899cf0e253ec6314b6'},
        {'duid': '20181207-ae5f86f8-f9cf-11e8-bf1c-ea00e4d87701', 'token': '820d63010ee148589d94f5ca4a81362e'},
        {'duid': '20181207-af09e756-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1602c977a4de44daaa80f273c8e8b1a7'},
        {'duid': '20181207-afad9f36-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f82477b0ccf2473bb0d2383055682cb1'},
        {'duid': '20181207-b057b8a4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3039713d47264589b767de863df1a12e'},
        {'duid': '20181207-b0f5c404-f9cf-11e8-bf1c-ea00e4d87701', 'token': '0a87d978fc5f435b955768ee7edd0076'},
        {'duid': '20181207-b1a9f726-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b72f979da72c45368ff7e4dd6b5b23b5'},
        {'duid': '20181207-b24dc310-f9cf-11e8-bf1c-ea00e4d87701', 'token': '648084e1e3c8451198667942e3aba7b6'},
        {'duid': '20181207-b2f9abda-f9cf-11e8-bf1c-ea00e4d87701', 'token': '52222610c55e42c0b5a4df7c32a0402c'},
        {'duid': '20181207-b3b52e0a-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f3827b9c5d5047889ae07b2655bf5bf2'},
        {'duid': '20181207-b468e76a-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a333fb89c16a49a9aa79aeafb6c97c19'},
        {'duid': '20181207-b51c8126-f9cf-11e8-bf1c-ea00e4d87701', 'token': '451785ce51994d358255c8d440cacea8'},
        {'duid': '20181207-b5c81590-f9cf-11e8-bf1c-ea00e4d87701', 'token': '213bea92c3fb4935838cc8610a8b8fde'},
        {'duid': '20181207-b674254c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7447311d4954472b8a922826685d5a16'},
        {'duid': '20181207-b718a450-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'cc8d86b614ac406da2b770feb03b84e8'},
        {'duid': '20181207-b7bc71de-f9cf-11e8-bf1c-ea00e4d87701', 'token': '414a4a70768c40a49fd18ea4d85067d2'},
        {'duid': '20181207-b869e3fa-f9cf-11e8-bf1c-ea00e4d87701', 'token': '86863aaa3ea74481acd53258305b5891'},
        {'duid': '20181207-b9059a84-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'bb6ccee6dd6e48ac870cdebc1934a27a'},
        {'duid': '20181207-b9b06324-f9cf-11e8-bf1c-ea00e4d87701', 'token': '434126539953436dbce87b53fe03a519'},
        {'duid': '20181207-ba641e32-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b21182d6ed7146e1ba8c229f67c4698a'},
        {'duid': '20181207-bb17c7b6-f9cf-11e8-bf1c-ea00e4d87701', 'token': '0624a77072ad49efa0b39b8fd2599a74'},
        {'duid': '20181207-bbd2f7d4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7bcdbc5f410a4291bbc694a0a9af0f89'},
        {'duid': '20181207-bc7ef0e8-f9cf-11e8-bf1c-ea00e4d87701', 'token': '30843bf8146840e68fd8d9f529848e30'},
        {'duid': '20181207-bd3acd86-f9cf-11e8-bf1c-ea00e4d87701', 'token': '173acc0849d447f8b50716cefcafdcd9'},
        {'duid': '20181207-bdf628f6-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd5f5ceb4c4e340c2a8cc56185d7b3f7c'},
        {'duid': '20181207-bf1f89de-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b065261c97c54ce788b74afb64f117e1'},
        {'duid': '20181207-c0118108-f9cf-11e8-bf1c-ea00e4d87701', 'token': '743bcc298c894a96a3de291836388d22'},
        {'duid': '20181207-c0d8a990-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1818695fb56a4e37b55621d2aa92f2df'},
        {'duid': '20181207-c1bf0fac-f9cf-11e8-bf1c-ea00e4d87701', 'token': '723467b80aaa4c08a026efe03b2bd7a4'},
        {'duid': '20181207-c299b7ce-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1b579f5edb7b410b97a5782b4b68aa32'},
        {'duid': '20181207-c3759384-f9cf-11e8-bf1c-ea00e4d87701', 'token': '2f7a530b3e4445a3b9b4599f220ddb2e'},
        {'duid': '20181207-c45ebde8-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a84b5bbea3fc4039a1c0f3cfadf7ce76'},
        {'duid': '20181207-c5438e50-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'edbcf37b3bcb4cc28802f03589b2699e'},
        {'duid': '20181207-c623fdb4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '87768498dd4c4cf3adefebf03dc2fcbc'},
        {'duid': '20181207-c6ff682c-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f730a81dac6040c38f2177befdfecdfb'},
        {'duid': '20181207-c7c9b9e2-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a337210a443042899e6588f912a4a991'},
        {'duid': '20181207-c8c3bf46-f9cf-11e8-bf1c-ea00e4d87701', 'token': '5865ec0d71bf4d578f3a2e15682a2cb7'},
        {'duid': '20181207-c99fc86a-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'db245ec1e2ed4419a171ba11f0e3b762'},
        {'duid': '20181207-ca5de502-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b9d1017494a74de891f91778bbbfc9b3'},
        {'duid': '20181207-cb35e06a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '807a3bc6f7e54c80baf65a3a8d664b3f'},
        {'duid': '20181207-cc0f6088-f9cf-11e8-bf1c-ea00e4d87701', 'token': '618b05e75b674dec828ecd5485cf6729'},
        {'duid': '20181207-ccdc08fe-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'c471e08ea37b487f83f899f9a496549c'},
        {'duid': '20181207-cdbcb322-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'eb2ff651d9a64eeb92db5ff87d4b02c7'},
        {'duid': '20181207-ce999e5e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a9423ef6a13548ecb97eae821936d764'},
        {'duid': '20181207-cf6ceab6-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ae687383430d4fe79e36d6bdd7dbd2f8'},
        {'duid': '20181207-d035e7fe-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f29ff99de0684100a38b43e771878997'},
        {'duid': '20181207-d100f93a-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'bfff95065b544d84aa9cd684e16a5959'},
        {'duid': '20181207-d1bca572-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3d83e6f4cb5d43d79dcecef1d10a4f0d'},
        {'duid': '20181207-d25904d0-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd5b63fc513464c20a9ff10e585d9594f'},
        {'duid': '20181207-d308e936-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f10f9800025140bfb34a9b3087dbaa67'},
        {'duid': '20181207-d3b8e0e8-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1cad250e208d443c87d1d6a2941e898f'},
        {'duid': '20181207-d4549218-f9cf-11e8-bf1c-ea00e4d87701', 'token': '994ac5cf685c4538aba7d25fade1b199'},
        {'duid': '20181207-d4f16d7c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '46259f3581b74f6d9265cf8356d72c1a'},
        {'duid': '20181207-d594ef42-f9cf-11e8-bf1c-ea00e4d87701', 'token': '9cf580c2c7b646db8c21061df6195895'},
        {'duid': '20181207-d650a296-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a9eb625fc27e4cf983eed362dd07a3e7'},
        {'duid': '20181207-d703dc26-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a836f1d90a9b41e2b568a306e5ebb607'},
        {'duid': '20181207-d7b7ee96-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4cde1dcd359f4f01ad6832f35b831243'},
        {'duid': '20181207-d8616e80-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a0fb4327df734c60bbca1ce88d601988'},
        {'duid': '20181207-d91f210a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7340b31abfac408792584cac58470ea2'},
        {'duid': '20181207-d9cb11f4-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd59c7fc7edcd4475a0e279f9b51e5b81'},
        {'duid': '20181207-da6fc01e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b24f9e39a553463184e42c81958d813e'},
        {'duid': '20181207-db111748-f9cf-11e8-bf1c-ea00e4d87701', 'token': '6e813a7451d240c1b92de9409f785305'},
        {'duid': '20181207-dbb841ee-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd516eef31a334ed0b9639f8f29534838'},
        {'duid': '20181207-dc737568-f9cf-11e8-bf1c-ea00e4d87701', 'token': '01f290d1f95a466d9e57abeb65061e04'},
        {'duid': '20181207-dd14e77c-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a94c10facc454af88e59386884a5e24d'},
        {'duid': '20181207-ddb09b40-f9cf-11e8-bf1c-ea00e4d87701', 'token': '0dd7e8c1f5f94e95a38fc1f7ca26191b'},
        {'duid': '20181207-de493df0-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b9cdefe7ca87445985754ba1a4d110c9'},
        {'duid': '20181207-dee17eee-f9cf-11e8-bf1c-ea00e4d87701', 'token': '7198a0a094054040948527dc5ab2cc09'},
        {'duid': '20181207-df78da6e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '02be332ab189498481a5d919f6980754'},
        {'duid': '20181207-e013263c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '69e1bceead1b44a79f2cff6f9a260c4e'},
        {'duid': '20181207-e0b5432c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '55930692100f47a08f82286dd87cb864'},
        {'duid': '20181207-e15a5128-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'fdba762702c34025863f7f81fe8e5c15'},
        {'duid': '20181207-e1f2145e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'dacca96ae66e42028f583047453eed4c'},
        {'duid': '20181207-e28afa98-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4ae554a6d6c5426389699f04a0e8729b'},
        {'duid': '20181207-e330e2d2-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'edf32740c4384b1b9f9cb3fa2a9579d3'},
        {'duid': '20181207-e3d5d620-f9cf-11e8-bf1c-ea00e4d87701', 'token': '6500dd74dba447babd55f9b4351b2c76'},
        {'duid': '20181207-e476e132-f9cf-11e8-bf1c-ea00e4d87701', 'token': '5e8ca4e331674c9a991fc636da7b3fce'},
        {'duid': '20181207-e50e3ee2-f9cf-11e8-bf1c-ea00e4d87701', 'token': '2cd6e1c013bf4ef4aa39815db8ebf0d7'},
        {'duid': '20181207-e5a54986-f9cf-11e8-bf1c-ea00e4d87701', 'token': '67208e963c174443817cff8846cd4c03'},
        {'duid': '20181207-e63c7112-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4c6276eea6dd45ff860593cee0766919'},
        {'duid': '20181207-e6d471ba-f9cf-11e8-bf1c-ea00e4d87701', 'token': '8a46490cb18e4626a1940e8800600fdf'},
        {'duid': '20181207-e77d41be-f9cf-11e8-bf1c-ea00e4d87701', 'token': '0f26930826a24b51b3ad3fd3600d4041'},
        {'duid': '20181207-e81b378e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '249d8e6970c64144a8f4e7bf618417e1'},
        {'duid': '20181207-e8b34934-f9cf-11e8-bf1c-ea00e4d87701', 'token': '082f259a74844c6f9691c003629795da'},
        {'duid': '20181207-e960413e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '338a250c7cbe4632af368c4aad9f025f'},
        {'duid': '20181207-e9f94884-f9cf-11e8-bf1c-ea00e4d87701', 'token': '5a48c9473b574fcfbeacabc9a0e49503'},
        {'duid': '20181207-ea900fc6-f9cf-11e8-bf1c-ea00e4d87701', 'token': '81214e8e1dc6487abe411fd66ce30a4b'},
        {'duid': '20181207-eb2e1dd8-f9cf-11e8-bf1c-ea00e4d87701', 'token': '51f557d329e840cfbf1cd1af9b15258a'},
        {'duid': '20181207-ebe431fe-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'f363059c798d42379d3fd22eac80ff40'},
        {'duid': '20181207-ec882ade-f9cf-11e8-bf1c-ea00e4d87701', 'token': '6523676aa0564b09aacdce895a99061e'},
        {'duid': '20181207-ed33d6fe-f9cf-11e8-bf1c-ea00e4d87701', 'token': '8496f1598c7c4f71b4de151d2785f0f0'},
        {'duid': '20181207-edeaea1a-f9cf-11e8-bf1c-ea00e4d87701', 'token': '98542cf07b46413e976045d0d1ded8bd'},
        {'duid': '20181207-ee842d88-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'fd974e4f9e764a0f956cc1c79b07cf9b'},
        {'duid': '20181207-ef280eb2-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'ab5b5d6a8dd445f1bfdbc845e997e461'},
        {'duid': '20181207-efc42e96-f9cf-11e8-bf1c-ea00e4d87701', 'token': '99c369309a314acdafe3c1c6ed0f08be'},
        {'duid': '20181207-f05c5824-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'df4d4f65c4dc41aca01dce0c5c309534'},
        {'duid': '20181207-f10175d4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '2bf3be75ce6a4de0b4b7477d37f06b9f'},
        {'duid': '20181207-f199bd76-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1e9982f157704c29b979a458b2ef96d4'},
        {'duid': '20181207-f241ab6c-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1e7908eb943343d98c4ada362ffa8bd6'},
        {'duid': '20181207-f2d85788-f9cf-11e8-bf1c-ea00e4d87701', 'token': '2cc1f6b80fa7480aa22910c46897f8d1'},
        {'duid': '20181207-f36dc2b4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '44bd2dcf1fb04bdda7c9d83fe1ca21cd'},
        {'duid': '20181207-f40718c4-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'c09f0cf3f85b4af681c891b49f124a3a'},
        {'duid': '20181207-f49fe2f2-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'b9ce507d61724a7d9e720fe8bc4e35a7'},
        {'duid': '20181207-f53889a8-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'fde3cf3659254d4392c220c577d95b7a'},
        {'duid': '20181207-f5d7511e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '4f1053762b44479db007468fbe0ec19d'},
        {'duid': '20181207-f68234da-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3fcff91fe6a44ef980c64a2779188b1b'},
        {'duid': '20181207-f7176dd4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '313e9f1033ac4644a66c9b9947b9ed74'},
        {'duid': '20181207-f7b31914-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1fd249cabfb84ce782ca4e8ec82f1ae2'},
        {'duid': '20181207-f85223e2-f9cf-11e8-bf1c-ea00e4d87701', 'token': '0259c4306f394fcd86b645ac801222aa'},
        {'duid': '20181207-f8ef4672-f9cf-11e8-bf1c-ea00e4d87701', 'token': '1342d76bd52d4168ac1fc7d8f5ddadb1'},
        {'duid': '20181207-f98777e4-f9cf-11e8-bf1c-ea00e4d87701', 'token': '14b379172f3847b7bbf5e073455599c6'},
        {'duid': '20181207-fa247fee-f9cf-11e8-bf1c-ea00e4d87701', 'token': '24c1f4d6e7674edc81f7d9c9fa5b7649'},
        {'duid': '20181207-fabb2c46-f9cf-11e8-bf1c-ea00e4d87701', 'token': '398fd8e3731c47748d3ba3266114c520'},
        {'duid': '20181207-fb6cb150-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'cc2292abe73841778cb128019057a8ac'},
        {'duid': '20181207-fc0cda0e-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'd215bef95362483fad746830ddd3a5e1'},
        {'duid': '20181207-fcb50526-f9cf-11e8-bf1c-ea00e4d87701', 'token': '78b4cfa2202747928faca7cb22b6f312'},
        {'duid': '20181207-fd605c50-f9cf-11e8-bf1c-ea00e4d87701', 'token': '0aae792a4c434829bd6951f0f7cc2870'},
        {'duid': '20181207-fe046660-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a5aea482ef40488e82a715581427ba6a'},
        {'duid': '20181207-fe9d9984-f9cf-11e8-bf1c-ea00e4d87701', 'token': '3a0a50dde6324f9bae1399ed2d351857'},
        {'duid': '20181207-ff347dfe-f9cf-11e8-bf1c-ea00e4d87701', 'token': 'a1129838601947a782b61372561559b6'},
        {'duid': '20181207-ffc9cc2e-f9cf-11e8-bf1c-ea00e4d87701', 'token': '03c8552b7b174386a7c2c187c9d1159d'},
        {'duid': '20181207-00624742-f9d0-11e8-bf1c-ea00e4d87701', 'token': '020acd4f77e44992af6016637d8e84d0'},
        {'duid': '20181207-0101e554-f9d0-11e8-bf1c-ea00e4d87701', 'token': '8414e3cb34ff4bf581c120d791595ad0'},
        {'duid': '20181207-019e1fe6-f9d0-11e8-bf1c-ea00e4d87701', 'token': '796c8792c1354781aa9353683ca27948'},
        {'duid': '20181207-0234e9a8-f9d0-11e8-bf1c-ea00e4d87701', 'token': '9602d11c5cda43858d891868bd5ca4d6'},
        {'duid': '20181207-02ca1cf8-f9d0-11e8-bf1c-ea00e4d87701', 'token': '2c703e78c4a645a384380e98fe6d8259'},
        {'duid': '20181207-03600f56-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'e304ef2c21ba4914934321077aab9ada'},
        {'duid': '20181207-03fa163c-f9d0-11e8-bf1c-ea00e4d87701', 'token': '4a6aaa4183fe4b8e8848ff0c1d098c89'},
        {'duid': '20181207-049281a6-f9d0-11e8-bf1c-ea00e4d87701', 'token': '0c55ee717964449b901b80dc83406d2f'},
        {'duid': '20181207-052b381a-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'a89b8ba7a6ee407da99e97f53b9148eb'},
        {'duid': '20181207-05c4311e-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'e12278e2ed3e477ca64c2661e8232888'},
        {'duid': '20181207-065b9b8a-f9d0-11e8-bf1c-ea00e4d87701', 'token': '02329de0177447dc9ede071dd0ad00d8'},
        {'duid': '20181207-06f4ae1a-f9d0-11e8-bf1c-ea00e4d87701', 'token': '6de6ea55871549bb9f213646be015ad9'},
        {'duid': '20181207-078c3e10-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'd03acf6fcc3a44f78d130e23015e50c7'},
        {'duid': '20181207-082e2cb6-f9d0-11e8-bf1c-ea00e4d87701', 'token': '2eb2702de5a44553a4b74c45e90af13b'},
        {'duid': '20181207-08da10b2-f9d0-11e8-bf1c-ea00e4d87701', 'token': '02337b4f57f14bbaa7a69789e9d2dad7'},
        {'duid': '20181207-097b0292-f9d0-11e8-bf1c-ea00e4d87701', 'token': '42dddbc6ac0646fbb43450723169121e'},
        {'duid': '20181207-0a1fc20a-f9d0-11e8-bf1c-ea00e4d87701', 'token': '5e4ab79f86d84211b8cc3573e398e869'},
        {'duid': '20181207-0ada90b2-f9d0-11e8-bf1c-ea00e4d87701', 'token': '3c98df533aaf46e39362adca8d8286a7'},
        {'duid': '20181207-0b992fe0-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'e7bfa4c82de141028eee5310d1d11970'},
        {'duid': '20181207-0c3b11fc-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'be22a243ed7e4cbd9af0fb7eb3f7bc5b'},
        {'duid': '20181207-0cd2a288-f9d0-11e8-bf1c-ea00e4d87701', 'token': '201228b6f8cb455d9adc6d8ee63e0576'},
        {'duid': '20181207-0d694c9c-f9d0-11e8-bf1c-ea00e4d87701', 'token': '6cb61fb565c04e32a1442288d236b9f4'},
        {'duid': '20181207-0e00f9de-f9d0-11e8-bf1c-ea00e4d87701', 'token': '1197f5a4851f4dfcb47d7342f55a5bd1'},
        {'duid': '20181207-0eab4b64-f9d0-11e8-bf1c-ea00e4d87701', 'token': '132f5777a81e45d49c61ca01e7e95880'},
        {'duid': '20181207-0f4af308-f9d0-11e8-bf1c-ea00e4d87701', 'token': '6e6dd40ba6844f8a80871353f06dd2bb'},
        {'duid': '20181207-0feed1d0-f9d0-11e8-bf1c-ea00e4d87701', 'token': '422388465b5c4b81aad4ab259f1dbba3'},
        {'duid': '20181207-113f3f52-f9d0-11e8-bf1c-ea00e4d87701', 'token': '919d4092188446daba32b4091983b782'},
        {'duid': '20181207-11eaf284-f9d0-11e8-bf1c-ea00e4d87701', 'token': '43ef7d7642ef45f486cc2c533d56f3c5'},
        {'duid': '20181207-12969440-f9d0-11e8-bf1c-ea00e4d87701', 'token': '42a756a6563f4672afd1e862369f2520'},
        {'duid': '20181207-13420c6c-f9d0-11e8-bf1c-ea00e4d87701', 'token': '531c808c88b34e219930d94fd2ecf7d8'},
        {'duid': '20181207-13e3fdec-f9d0-11e8-bf1c-ea00e4d87701', 'token': '5300cc3813ae4286b75ed9588d6f1af7'},
        {'duid': '20181207-149255fe-f9d0-11e8-bf1c-ea00e4d87701', 'token': '00bb68808f3a4ce18ae980577e7de03f'},
        {'duid': '20181207-153bc5f8-f9d0-11e8-bf1c-ea00e4d87701', 'token': '9aca6db9398d4e5cbeafafd0b7cd3b6f'},
        {'duid': '20181207-15df10f0-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'a9993462f3de4691933749c80a8b0f3d'},
        {'duid': '20181207-167823a8-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'fc640e2277b342fab72afe347c7b5959'},
        {'duid': '20181207-171afc0e-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'b4ab8a6d77c0418a84e9ba04bfb6fe90'},
        {'duid': '20181207-17b72dcc-f9d0-11e8-bf1c-ea00e4d87701', 'token': '68a308c2460440b7858d0797a5f6233a'},
        {'duid': '20181207-185e5fde-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'ec889b74a16c4f93b552843173b6ce2d'},
        {'duid': '20181207-1906ed2a-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'b7a21d9a43c64fbcb30efa37ed867a33'},
        {'duid': '20181207-19a39328-f9d0-11e8-bf1c-ea00e4d87701', 'token': '15bdabf0f8d3402d8619d98ab280ed20'},
        {'duid': '20181207-1a4f1ea0-f9d0-11e8-bf1c-ea00e4d87701', 'token': 'eb5e2839571c4317a8d6213155b732fe'}]
    # with open("./duid_token.yaml", "w") as f:
    #     yaml.dump(result, f, default_flow_style=False)
