# -*- coding: utf-8 -*-
# __author__ = 'Gz'
import datetime
import time
import uuid
import requests
import json
import yaml
import os
from basics_function.golable_function import MD5, config_reader

today = datetime.date.today().strftime("%Y%m%d")
language = "en_US"
version = "1"
salt = "3*y4f569#tunt$le!i5o"

source = "online"
PATH = os.path.dirname(os.path.abspath(__file__))


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
                print(response.status_code)
                print(response.text)
                print(duid)
                assert False, "获取token错误"
        else:
            print(response.status_code)
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
                print(response.status_code)
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
            with open(PATH + "/duid_token.yaml", "w") as f:
                yaml.dump(result, f, default_flow_style=False)
            break


def reflash_token():
    GT = GetToken()
    path = PATH + "/duid_token.yaml"
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
    with open(PATH + "/duid_token.yaml", "w") as f:
        yaml.dump(result, f, default_flow_style=False)


if __name__ == "__main__":
    # registry_duid_tokens(1000)
    reflash_token()
