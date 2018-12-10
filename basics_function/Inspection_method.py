# -*- coding: utf-8 -*-
# __author__ = "Gz"
import requests
import json
import io
from PIL import Image

"""
相关语法的定义:
| 表示或
null 表示 None 关键是这个Json直接就是了
$$$ 表示忽略
"""


class InspectionMethod:
    def __init__(self):
        self.request_time_out = 30
        self.extra = {"LIST_REPEATED": True,
                      "LIST_EMPTY": True,
                      "URL_FROM": None
                      }
        # http资源验证

    def get_pic_size(self, pic):
        img = Image.open(pic)
        size = list(img.size)
        height = size[0]
        width = size[1]
        return {"height": height, "width": width}

    def get_url_stream(self, url):
        if self.extra["URL_FROM"] is not None and self.extra["URL_FROM"] not in url:
            print(url)
            print("资源来源不是" + str(self.extra["URL_FROM"]))
        response = requests.get(url, timeout=self.request_time_out)
        if response.status_code == 200:
            return io.BytesIO(response.content)
        else:
            return False

    def http_resource(self, url):
        url = str(url)
        print(url)
        if self.extra["URL_FROM"] is not None and self.extra["URL_FROM"] not in url:
            print(url)
            print("资源来源不是" + str(self.extra["URL_FROM"]))
        resources = requests.request("head", url)
        if resources.status_code == 200:
            return True
        else:
            return False

    # 返回数据详细校验
    # 检查字段类型 null HTTP Bool Str Int Float 或者 值相等
    def response_data_check_(self, case, response):
        # None处理
        if case == "HTTP":
            return self.http_resource(response)
        elif case == "Bool":
            return isinstance(response, bool)
        elif case == "Str":
            # 判断字符串是否为空字符串
            if response != "":
                return isinstance(response, str)
            else:
                return False
        elif case == "Int":
            return isinstance(response, int)
        elif case == "Float":
            return isinstance(response, float)
        else:
            if (case != response and case != "$$$") and (case == "null" and response is not None):
                return False
            else:
                return True

    # 返回数据校验
    # 多个可能有一个可以那么就通过
    def response_data_check(self, case, response):
        result = []
        if "|" in case:
            case_ = case.split("|")
            for i in case_:
                result.append(self.response_data_check_(i, response))
        else:
            result.append(self.response_data_check_(case, response))
        if True in result:
            return True
        else:
            print(result)
            print("返回数据校验错误,错误内容:")
            print("case:" + str(case))
            print(type(case))
            print("response:" + str(response))
            print(type(response))
            return False

    # response字段获取
    def get_key_vaule(self, keys, data):
        if "/" in str(keys):
            keys = keys.split("/")
        if isinstance(keys, list):
            for i in keys:
                # 遇到list进行处理
                try:
                    i = int(i)
                except:
                    pass
                # 对层级错误进行报错
                try:
                    data = data[i]
                except Exception as e:
                    print("不存在字段，内容报错:")
                    print(i)
                    print(data)
                    data = False
        else:
            try:
                data = data[keys]
            except Exception as e:
                print("不存在字段，内容报错:")
                print(keys)
                print(data)
                data = False
        return data

    # key value 条件判断
    """
    case 的格式为k/k/k=v
    """

    def key_value_check(self, case, data):
        case = case.split("=")
        keys = case[0]
        value = case[1]
        data_value = self.get_key_vaule(keys, data)
        if value == data_value:
            return True
        else:
            return False

    def list_repeated_examination(self, response, diff=[]):
        new_response = []
        repeated = []
        for i in response:
            if i not in new_response:
                new_response.append(i)
            else:
                repeated.append(i)
        if len(repeated) > 0:
            diff.append(False)
            print("$$$$$$$$$$$$$$$$$$$")
            print("list中有重复内容")
            print("response:" + str(response))
            print("重复的内容为:" + str(repeated))
            print("$$$$$$$$$$$$$$$$$$$$")

    def list_empty_check(self, case, response, diff=[]):
        if len(response) == 0:
            diff.append(False)
            print("$$$$$$$$$$$$$$$$$$$")
            print("response list内容为空:")
            print("case:" + str(case))
            print("response:" + str(response))
            print("$$$$$$$$$$$$$$$$$$$")

    # response检查list类型
    # 默认进行重复检查
    def format_list(self, case, response, diff=[]):
        model = case[0]
        if self.extra["LIST_REPEATED"] is True:
            self.list_repeated_examination(response=response, diff=diff)
        if self.extra["LIST_EMPTY"] is True:
            self.list_empty_check(case, response, diff)
        for i in case:
            for e in response:
                if isinstance(i, str):
                    diff.append(self.response_data_check(model, e))
                else:
                    self.format_diff(i, e, diff)

    def pic_case_data(self, case, response):
        if 'width' in list(case.keys()) and 'height' in list(case.keys()) and (
                'url' in list(case.keys()) or 'pic_url' in list(case.keys())):
            if "url" in list(case.keys()):
                url_stream = self.get_url_stream(response["url"])
            else:
                url_stream = self.get_url_stream(response["pic"])
            if url_stream is not False:
                pic_size = self.get_pic_size(url_stream)
                case["width"] = str(pic_size["width"])
                case["height"] = str(pic_size["height"])
                case["url"] = "$$$"
                if "size" in list(case.keys()):
                    case["size"] = str(url_stream.getvalue())
        return {"case": case, "response": response}

    # response检查dict类型
    def format_dict(self, case, response, diff=[]):
        if case.keys() == response.keys():
            self.pic_case_data(case, response)
            for key in case.keys():
                # 值得类型是list进行忽略检查
                if isinstance(case[key], list):
                    if (isinstance(case[key][0], dict) and ("$$$" not in case[key])) or (
                            isinstance(case[key], str) and (case[key] != response[key])):
                        self.format_diff(case[key], response[key], diff)
                    else:
                        self.format_list(case[key], response[key], diff)
                elif isinstance(case[key], str):
                    diff.append(self.response_data_check(case[key], response[key]))
                else:
                    self.format_diff(case[key], response[key], diff)
        else:
            print("错误内容:")
            print("字典型key不匹配")
            print(case.keys())
            print(response.keys())
            print("case:" + str(case))
            print("response:" + str(response))
            diff.append(False)

    # response检查格式
    def format_diff(self, case, response, diff=[]):
        try:
            # case为list
            if isinstance(case, list):
                self.format_list(case, response, diff=diff)
            # case 为dict
            elif isinstance(case, dict):
                self.format_dict(case, response, diff=diff)
            # case 为str
            else:
                if case is None:
                    case = "null"
                if response is None:
                    response = "null"
                diff.append(self.response_data_check(case, response))
        except Exception as e:
            diff.append(False)
            print(e)
            print("错误内容:")
            print("case:" + str(case))
            print("response:" + str(response))
        if False in diff:
            return False
        else:
            return True

    # 检查格式条件判断
    def qualification_format_diff(self, case, response):
        format_type = case["TYPE"]
        format_data = case["DATA"]
        result_list = []
        diff = []
        if format_type == "ONLY":
            return self.format_diff(format_data, response, diff=diff)
        else:
            # 多个可能时case
            for content, single_case in format_data.items():
                if self.key_value_check(content, response):
                    result_list.append(self.format_diff(single_case, response, diff=diff))
                else:
                    print('未发现对应DATA_FORMAT条件')
                    print('条件为:' + str(content))
        if True in result_list:
            return True
        else:
            return False

    # 条件确认

    # 发现不对就不对了,字典强匹配
    """
        case格式a=1&b=2
        data 为一个字典
        """

    def qualification_check(self, qualification, data):
        result = True
        truth_qualification = qualification.split("@")[0]
        case_list = truth_qualification.split("&")
        for i in case_list:
            case_ = i.split("=")
            keys = case_[0].split("/")
            value = case_[1]
            if self.get_key_vaule(keys, data) != value:
                result = False
                break
        return result

    # 具体值得检查
    def content_check(self, case_keys, case_value, response):
        response = self.get_key_vaule(case_keys, response)
        # # 表示检查格式
        # case中因为转换所有都为str,所以强制装换response
        if (case_value == "#" and response is not False) or (response is not False and str(response) == case_value):
            return True
        else:
            return False

    # 单一条件判断
    """
    单一判断判断的值中有/那么会按照一个list去处理
    """

    def sigle_data_content_check(self, qualification, case, data, response):
        if self.qualification_check(qualification, response) or qualification == "~all":
            case = case.split("=")
            case_value = case[1]
            case_keys = case[0]
            if "|" in case_value:
                result_list = []
                # 循环检查有正确就是正确
                for case_value_ in case_value.split("|"):
                    result_list.append(self.content_check(case_keys, case_value_, response))
                if True in result_list:
                    return True
                else:
                    return False
            else:
                return self.content_check(case_keys, case_value, response)
        else:
            print("未满足条件:" + qualification)
            return True

    # 具体数据的判断 有判断没有不判断
    def data_content_check(self, case, data, response):
        result_list = []
        for qualification, case_ in case.items():
            result_list.append(self.sigle_data_content_check(qualification, case_, data, response))
        if False in result_list:
            return False
        else:
            return True

    def header_check_(self, case, value, response_header):
        response_header_value = self.get_key_vaule(case, response_header)
        if "|" in value and response_header_value is not False:
            if response_header[case] in list(value.split("|")):
                return True
            else:
                return False
        elif response_header_value is not False:
            if response_header[case] == value:
                return True
            else:
                return False
        else:
            return False

    def header_check(self, case, response_header):
        for key, value in case.items():
            if key != "~all":
                if isinstance(value, dict) and self.qualification_check(key, response_header):
                    return self.header_check_(list(value.keys())[0], list(value.values())[0], response_header)
                elif isinstance(value, str):
                    return self.header_check_(key, value, response_header)
                else:
                    return False
            else:
                if isinstance(value, dict):
                    return self.header_check_(list(value.keys())[0], list(value.values())[0], response_header)
                elif isinstance(value, str):
                    return self.header_check_(key, value, response_header)
                else:
                    return False
