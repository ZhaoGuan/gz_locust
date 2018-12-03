# -*- coding: utf-8 -*-
# __author__ = 'Gz'
import copy
import os
import random
import threading
from basics_function.golable_function import config_reader, config_data_path, list_duplicate_removal
from basics_function.wuren_request import FiveNut
from basics_function.kika_base_request import Kika_base_request

kika = Kika_base_request("")


class HttpTest:
    def __init__(self, config, source="online"):
        self._value_lock = threading.Lock()
        self.source = source
        self.config = config["data"]
        print(self.config)
        try:
            self.the_flowing = self.config["THE_FLOWING"]
        except:
            self.the_flowing = None
        try:
            self.the_above_data = self.config["THE_ABOVE"]["DATA"]
        except:
            self.the_above_data = None
        try:
            self.the_above_type = self.config["THE_ABOVE"]["TYPE"]
        except:
            self.the_above_type = None
        try:
            self.the_above_key = self.config["THE_ABOVE"]["KEY"]
        except:
            self.the_above_key = None
        self.url = self.config["SOURCE"][source]["URL"]
        self.headers = self.config["SOURCE"][source]["HEADERS"]
        self.params = self.config["SOURCE"][source]["PARAMS"]
        self.mode = self.config["SOURCE"][source]["MODE"]
        self.body = self.config["SOURCE"][source]["BODY"]
        self.fail_list = []
        self.fail_count = 0
        self.all_list = []
        # 伍仁
        self.fivenut = FiveNut(self.fail_list)
        self.fivenut.sign = None
        self.fivenut.token = None

    def url_headers_data(self):
        all_header_data = []
        url_headers_keys = list(self.headers["DATA"].keys())
        for i in url_headers_keys:
            if len(all_header_data) == 0:
                for f in self.headers["DATA"][i]:
                    all_header_data.append({i: f})
            else:
                temp_all = []
                for e in self.headers["DATA"][i]:
                    temp = copy.deepcopy(all_header_data)
                    [f.update({i: e}) for f in temp]
                    [temp_all.append(g) for g in temp]
                    all_header_data = temp_all
        return all_header_data

    def parameters_data(self):
        all_data = []
        params_keys = list(self.params["DATA"].keys())
        for i in params_keys:
            if len(all_data) == 0:
                for f in self.params["DATA"][i]:
                    all_data.append({i: f})
            else:
                temp_all = []
                for e in self.params["DATA"][i]:
                    temp = copy.deepcopy(all_data)
                    [f.update({i: e}) for f in temp]
                    [temp_all.append(g) for g in temp]
                all_data = temp_all
        return all_data

    def body_data(self):
        all_data = []
        if self.body["DATA"] is not None:
            data_keys = list(self.body["DATA"].keys())
            for i in data_keys:
                if len(all_data) == 0:
                    for f in self.body["DATA"][i]:
                        all_data.append({i: f})
                else:
                    temp_all = []
                    for e in self.body["DATA"][i]:
                        temp = copy.deepcopy(all_data)
                        [f.update({i: e}) for f in temp]
                        [temp_all.append(g) for g in temp]
                    all_data = temp_all
        else:
            all_data = None
        try:
            body_function = self.body["FUNCTION"]
            if body_function is None:
                body_function = "NORMAL"
        except:
            body_function = "NORMAL"

        result = {"data": all_data, "type": self.body["TYPE"], "function": body_function}
        return result

    def confirm_body(self, data, headers):
        function = data["body"]["function"]
        body = data["body"]["data"]
        if function == "5NUT":
            if body is None:
                body = {"sign": self.fivenut.get_sign(data),
                        "token": self.fivenut.get_token(data, headers, self.source)}
            else:
                body.update(
                    {"sign": self.fivenut.get_sign(data)})
                if "token" not in list(body.keys()):
                    body["token"] = self.fivenut.get_token(data, headers, self.source)
            return body
        elif function == "5NUT_sigin":
            if body is None:
                body = {"sign": self.fivenut.get_sign(data)}
            else:
                body.update({"sign": self.fivenut.get_sign(data)})
            return body
        else:
            if body is None:
                assert False, "body内容为空"

    # url key 数据整理
    def url_parameters(self):
        if self.params["DATA"] is not None:
            all_data = self.parameters_data()
        else:
            all_data = None
        return all_data

    # url带有参数且会影响header中内容的时候
    def normal_parameters_case_data(self, url_parameters_data):
        result_data = []
        for i in url_parameters_data:
            if self.headers["DATA"] is not None:
                header = self.url_headers_data()
            else:
                header = None
            if isinstance(header, list):
                for e in header:
                    result_data.append({"parameters": i, "headers": e})
            else:
                result_data.append({"parameters": i, "headers": header})
        return result_data

    # url不带有参数的时候,切所有数据都根据header中内容
    def none_parameters_case_data(self):
        if self.headers["DATA"] is not None:
            header = self.url_headers_data()
        else:
            header = None
        # header 是多个的时候
        if isinstance(header, list):
            result = []
            for i in header:
                result.append({"parameters": None, "headers": i})
            return result
        else:
            return [{"parameters": None, "headers": header}]

    def no_body_case_data(self):
        url_parameters_data = self.url_parameters()
        if url_parameters_data is not None:
            return self.normal_parameters_case_data(url_parameters_data)
        else:
            return self.none_parameters_case_data()

    def body_case_data(self):
        data = self.no_body_case_data()
        body = self.body_data()
        body_data = body["data"]
        body_type = body["type"]
        body_function = body["function"]
        result = []
        for i in data:
            if body_data is not None:
                for e in body_data:
                    temp = copy.deepcopy(i)
                    temp.update({"body": {"data": e, "type": body_type, "function": body_function}})
                    result.append(temp)
            else:
                temp = copy.deepcopy(i)
                temp.update({"body": {"data": None, "type": body_type, "function": body_function}})
                result.append(temp)
        return result

    def case_data(self):
        if self.body is not None:
            cases = self.body_case_data()
        else:
            cases = self.no_body_case_data()
        return list_duplicate_removal(cases)

    # url 重新拼接
    """
    JOINT拼接
    NORMAL直接返回URL

    """

    def url_mosaic_type(self, data):
        url = self.url
        parameters = copy.deepcopy(data["parameters"])
        headers = data["headers"]
        if self.params["TYPE"] == "JOINT" and self.params["DATA"] is not None:
            for key, value in parameters.items():
                url += str(key) + "=" + str(value) + "&"
            result_url = url[:-1]
        elif self.params["TYPE"] == "KIKA" and self.params["DATA"] is not None:
            sign = kika.get_sign(headers["app"], headers["version"], parameters["duid"])
            parameters.update({"sign": sign})
            parameters.pop("duid")
            for key, value in parameters.items():
                url += str(key) + "=" + str(value) + "&"
            result_url = url[:-1]
        else:
            assert False, "不存在的TYPE值选项" + self.params["TYPE"]
        return result_url

    def url_mosaic(self, data):
        if self.params["TYPE"] != "NORMAL" and (self.url[-1] == "?" or self.url[-1] == "&"):
            # 根据TYPE类型去添加新的参数
            result_url = self.url_mosaic_type(data)
        else:
            if (self.url[-1] == "?" and self.url[-1] == "&") and self.params["DATA"] is None:
                assert False, "URL为非?和&结尾,但是没有添加参数值"
            else:
                result_url = self.url
        return result_url

    # header 处理
    def confirm_headers(self, data):
        # """
        # if TYPE value is "local" will return DATA value
        # if TYPE value is "config" will return DATA value corresponding config file name data
        # if TYPE value is "function"
        # :return:
        # """
        headers_type = self.headers["TYPE"]
        headers_data = data["headers"]
        parameters_data = data["parameters"]
        if headers_data is not None:
            if headers_type == "local":
                headers = headers_data
            elif headers_type == "config":
                headers = config_reader("./config/%s.yml" % headers_data)
            elif headers_type == "KIKA":
                if self.params["DATA"] is not None:
                    headers = kika.set_header(duid=parameters_data["duid"], lang=parameters_data["kb_lang"],
                                              app=headers_data["app"], version=headers_data["version"])
                else:
                    headers = None
            elif headers_type == "5NUT":
                headers = self.fivenut.set_header(data)
            # NORMAL默认为None
            else:
                headers = None
        #
        else:
            headers = None
        return headers

    # 真发送
    def true_url_reuqest(self, request_mode, request_header, url, data, ):
        if request_mode == "GET" and request_header is None:
            return {"url": url, "request_header": request_header, "request_type": "get"}
        else:
            body = self.confirm_body(data, request_header)
            print("发送body:" + str(body))
            if data["body"]["type"] == "JSON":
                return {"url": url, "request_header": request_header, "body": body, "request_type": "post"}
            elif data["body"]["type"] == "FILE":
                try:
                    file_path = body["file_path"]
                    body.pop("file_path")
                except:
                    assert False, "未发现file_path"
                # files = {"file": open(PATH + "/case/" + file_path, "rb").read()}
                # response = :self.client.post(url, json=body, files=files)
                # return {"url": url, "request_header": request_header, "files": files, "body": body,
                #         "request_type": "post"}
            # else:
            #     return {"url": url, "request_header": request_header, "body": body, "request_type": "post"}

    # 发送请求
    def url_request_data(self, data):
        # url 和 headers统一处理
        url = self.url_mosaic(data)
        print("发送URL:" + str(url))
        request_header = self.confirm_headers(data)
        print("发送header:" + str(request_header))
        # 类型选择
        request_mode = self.mode["TYPE"]
        with self._value_lock:
            data = self.true_url_reuqest(request_mode, request_header, url, data)
        return data
