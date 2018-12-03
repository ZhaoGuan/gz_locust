# -*- coding: utf-8 -*-
# __author__ = 'Gz'
from basics_function.golable_function import MD5

import time
import copy
import requests
import json
import threading


class FiveNut:
    def __init__(self, fail_list):
        self.salt = "3*y4f569#tunt$le!i5o"
        self.fail_list = fail_list
        self.time_stamp = int(round(time.time() * 1000))
        self.token = None
        self.sign = None
        self._value_lock = threading.Lock()
        self.duid = None

    # def get_sign(self, data):
    #     with self._value_lock:
    #         if self.duid != data["headers"]["duid"]:
    #             self.sign = self.get_sign_value(data)
    #         return self.sign

    def get_sign(self, data):
        header_data = data["headers"]
        try:
            duid = header_data["duid"]
        except:
            assert False, "header 中没有duid"
        try:
            language = header_data["lang"]
        except:
            assert False, "header 中没有lang"
        try:
            version = header_data["version"]
        except:
            assert False, "header 中没有version"
        data = duid + "_" + language + "_" + str(self.time_stamp) + "_" + str(version) + "_" + self.salt
        result = MD5(data)
        return result

    def set_header(self, data):
        header_data = data["headers"]
        try:
            duid = header_data["duid"]
        except:
            assert False, "header 中没有duid"
        try:
            language = header_data["lang"]
        except:
            assert False, "header 中没有lang"
        try:
            version = header_data["version"]
        except:
            assert False, "header 中没有version"
        new_header_data = copy.deepcopy(header_data)
        new_header_data.pop("duid")
        new_header_data.pop("lang")
        new_header_data.pop("version")
        new_header_data.update(
            {"User-Agent": duid + "#&#" + language + "#&#" + str(self.time_stamp) + "#&#" + str(version)})
        return new_header_data

    # def get_token(self, data, headers, source):
    #     with self._value_lock:
    #         if self.token is None:
    #             self.token = self.get_token_value(data, headers, source)
    #         return self.token

    def get_token(self, data, headers, source):
        if self.sign is None or self.duid != data["headers"]["duid"]:
            sign = self.get_sign(data)
        else:
            sign = self.sign
        if source == "test":
            token_url = "http://api.dev.wuren.com:8080/v1/identity/login"
        else:
            token_url = "http://api.wuren.com:8080/v1/identity/login"
        try:
            response = requests.post(token_url, json={"sign": sign}, headers=headers)
            token = json.loads(response.text)["info"]["token"]
        except:
            print(response.text)
            assert False, "获取token错误"
        return token
