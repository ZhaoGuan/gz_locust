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
time_stamp = int(round(time.time() * 1000))
version = "1"
salt = "3*y4f569#tunt$le!i5o"

source = "test"


class GetToken:
    def __init__(self):
        self.duid = None

    def header(self):
        return {'User-Agent': self.duid + "#&#" + language + "#&#" + str(time_stamp) + "#&#" + str(version)}

    def get_sing(self):
        data = self.duid + "_" + language + "_" + str(time_stamp) + "_" + str(version) + "_" + salt
        print(data)
        result = MD5(data)
        print(result)
        return result

    def random_duid(self):
        duid = str(today) + "-" + str(uuid.uuid1())
        return duid

    def login_token(self, duid):
        self.duid = duid
        if source == "test":
            token_url = "http://api.dev.wuren.com:8080/v1/identity/login"
        else:
            token_url = "http://api.wuren.com:8080/v1/identity/login"
        print(self.header())
        response = requests.post(token_url, json={"sign": self.get_sing()}, headers=self.header())
        if response.status_code == 200:
            try:
                token = json.loads(response.text)["info"]["token"]
            except:
                print(response.text)
                assert False, "获取token错误"
        else:
            print(response.text)
        return {"duid": self.duid, "token": token}

    def registry(self):
        self.duid = self.random_duid()
        if source == "test":
            token_url = "http://api.dev.wuren.com:8080/v1/identity/registry"
        else:
            token_url = "http://api.wuren.com:8080/v1/identity/registry"
        print(self.header())
        response = requests.post(token_url, json={"sign": self.get_sing()}, headers=self.header())
        if response.status_code == 200:
            try:
                token = json.loads(response.text)["info"]["token"]
                print("！！！！！！！1")
            except:
                print(response.text)
                assert False, "获取token错误"
        else:
            print(response.text)
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
    for i in data:
        duid = i["duid"]
        duid_token = GT.login_token(duid)
        result.append(duid_token)
    with open("./duid_token.yaml", "w") as f:
        yaml.dump(result, f, default_flow_style=False)


if __name__ == "__main__":
    # registry_duid_tokens(2)
    reflash_token()
