# -*- coding: utf-8 -*-
# __author__ = 'Gz'
import binascii
import hashlib
import random
import yaml
import copy
from multiprocessing import Process, Pipe, Manager, Queue
import threading
import requests
import json
import time


def config_reader(Yaml_file):
    yf = open(Yaml_file)
    yx = yaml.load(yf)
    yf.close()
    return yx


# 随机udid值
def random_duid():
    all_world = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
    world = random.sample(all_world, 5)
    result_world = ''
    for i in world:
        result_world += i
    m = hashlib.md5()
    m.update(result_world.encode('utf-8'))
    MD5 = m.hexdigest()
    # print(MD5)
    return MD5


# popup分组计算
def sum_duid(duid):
    sum_result = 0
    a_ = []
    for i in duid:
        # print(i)
        d = int(i, 16)
        # print(d)
        a_.append(d)
        sum_result += int(d)
        # print(sum_result)
    return sum_result


# 根据取模数确认分组
def which_group(way, duid):
    duid_value = sum_duid(duid)
    group = duid_value % int(way)
    # print('取模结果：')
    # print(group)
    return group


# 获取对应取模值的duid
def get_duid_in_way(way, result):
    while True:
        duid = random_duid()
        if which_group(way, duid) == result:
            break
    return duid


class Http_Test:
    def __init__(self, config):
        self.config = config
        self.url = self.config['url']
        try:
            self.keys = self.config['keys']
        except:
            self.keys = None
        try:
            self.data = self.config['data']
        except:
            self.data = None
        try:
            self.other = self.config['other']
        except:
            self.version = 2043
            self.way = 'online'
            self.host = 'api.kikakeyboard.com'
        try:
            self.other = self.config['other']
            self.version = self.other['version']
            if self.version == None:
                self.version = 2043
        except:
            self.version = 2043
        try:
            self.other = self.config['other']
            self.way = self.other['way']
            if self.way == None:
                self.way = 'online'
        except:
            self.way = 'online'
        try:
            self.other = self.config['other']
            self.host = self.other['host']
        except:
            self.host = None
        try:
            self.Assert = self.config['assert']
        except:
            self.Assert = None

    # 根据udid获取sign
    def get_sign(self, app, version, duid):
        if app == None or version == None or duid == None:
            sign = False
        else:
            if 'pro' == app:
                app_key = '4e5ab3a6d2140457e0423a28a094b1fd'
                security_key = '58d71c3fd1b5b17db9e0be0acc1b8048'
                # package_name =

            elif 'ikey' == app:
                app_key = 'e2934742f9d3b8ef2b59806a041ab389'
                security_key = '2c7cd6555d6486c2844afa0870aac5d6'
                # package_name =
            else:
                app_key = '78472ddd7528bcacc15725a16aeec190'
                security_key = '6f43e445f47073c4272603990e9adf54'
                # package_name =
            base = 'app_key' + app_key + 'app_version' + str(version) + 'duid' + str(duid)
            m = hashlib.md5()
            m.update(base.encode('utf-8'))
            sign = m.hexdigest()
        # print(sign)
        return sign

    # 设定header
    def set_header(self, duid, lang='en_AU', app='kika', version=2043, way='online'):
        lange_en = ['en_AU', 'AU', 'en']
        lange_pt = ['pt_BR', 'BR', 'pt']
        lange_es = ['es_AR', 'AR', 'es']
        lange_in = ['in_ID', 'ID', 'in']
        lange_us = ['en_US', 'US', 'en']
        lange_ca = ['en_CA', 'CA', 'en']
        lange_e_in = ['en_IN', 'IN', 'en']
        lange_nz = ['en_NZ', 'NZ', 'en']
        lange_ph = ['en_PH', 'PH', 'en']
        lange_uk = ['en_UK', 'UK', 'en']
        if lang == 'en_AU':
            use_lang = lange_en
        elif lang == 'en_US':
            use_lang = lange_us
        elif lang == 'en_CA':
            use_lang = lange_ca
        elif lang == 'en_IN':
            use_lang = lange_e_in
        elif lang == 'en_NZ':
            use_lang = lange_nz
        elif lang == 'en_PH':
            use_lang = lange_ph
        elif lang == 'en_UK':
            use_lang = lange_uk
        elif lang == 'pt_BR':
            use_lang = lange_pt
        elif lang == 'es_AR':
            use_lang = lange_es
        else:
            use_lang = lange_in
        # print('@@@@@@@@')
        # print(use_lang)
        if 'pro' == app:
            app_key = '4e5ab3a6d2140457e0423a28a094b1fd'
            security_key = '58d71c3fd1b5b17db9e0be0acc1b8048'
            # 这个错误的
            package_name = 'com.emoji.coolkeyboard'

        elif 'ikey' == app:
            app_key = 'e2934742f9d3b8ef2b59806a041ab389'
            security_key = '2c7cd6555d6486c2844afa0870aac5d6'
            # 这个错误的
            package_name = 'com.emoji.ikeyboard'
        else:
            app_key = '78472ddd7528bcacc15725a16aeec190'
            security_key = '6f43e445f47073c4272603990e9adf54'
            package_name = 'com.qisiemoji.inputmethod'
        if way == 'online':
            # 线上
            # User-Agent package_name/app_version (udif/app_key)
            header = {'Accept-Charset': 'UTF-8',
                      'Kika-Install-Time': '1505198889124',
                      'Connection': 'Keep-Alive',
                      'Host': self.host,
                      'Accept-Language': '%s' % use_lang[0],
                      'User-Agent': '%s/%s (%s/%s) Country/%s Language/%s System/android Version/23 Screen/480' % (
                          package_name, version, duid, app_key, use_lang[1], use_lang[2]),
                      'X-Model': 'D6603', 'Accept-Encoding': 'gzip'}
            # header = {
            #     'User-Agent': '%s/%s (%s/%s) Country/%s Language/%s System/android Version/23 Screen/480' % (
            #         package_name, version, duid, app_key, use_lang[1], use_lang[2])}
        else:
            # 测试
            header = {'Accept-Charset': 'UTF-8',
                      'Kika-Install-Time': '1505198889124',
                      'Connection': 'Keep-Alive',
                      'Host': self.host,
                      'Accept-Language': '%s' % use_lang[0],
                      'User-Agent': '%s/%s (%s/%s) Country/%s Language/%s System/android Version/23 Screen/480' % (
                          package_name, version, duid, app_key, use_lang[1], use_lang[2]),
                      'X-Model': 'D6603', 'Accept-Encoding': 'gzip'}

        return header

    # url key 数据整理
    def url_keys_data(self):
        all_data = []
        config_data = self.data
        data_keys = self.data.keys()
        for i in data_keys:
            if len(all_data) == 0:
                for f in config_data[i]:
                    all_data.append({i: f})
            else:
                temp_all = []
                for e in config_data[i]:
                    temp = copy.deepcopy(all_data)
                    for f in temp:
                        f.update({i: e})
                    for g in temp:
                        try:
                            if isinstance(g['duid'], list):
                                g['duid'] = get_duid_in_way(g['duid'][0], g['duid'][1])
                        except:
                            pass
                        temp_all.append(g)
                all_data = temp_all
        # print(all_data)
        # print(len(all_data))

        return all_data

    # url 重新拼接
    def url_mosaic(self, data):
        url = self.url
        keys = self.keys
        for i in keys:
            if i != keys[-1]:
                url = url + i + '=' + data[i] + '&'
            else:
                url = url + i + '=' + data[i]
        if 'duid' in url:
            sign = self.get_sign(version=self.version, duid=data['duid'], app=data['app'])
            re_sign = 'sign=' + sign
            duid = 'duid=' + data['duid']
            url = url.replace(duid, re_sign)
        # print(url)
        return url

    # http资源验证
    def Http_Resources(self, url):
        # resources = request.
        resources = requests.request('get', url)
        # print(resources.status_code)
        if resources.status_code == 200:
            resources_result = True
        else:
            resources_result = False
        return resources_result

    # 返回数据校验
    def response_data_check(self, case, response):
        if case == '&&&':
            print('有值进行了忽略')
            result = True
        else:
            if case == 'HTTP':
                if self.Http_Resources(response) == True:
                    result = True
                else:
                    result = False
            elif case == 'Bool':
                result = isinstance(response, bool)
            elif case == 'Str':
                # 判断字符串是否为空字符串
                result = isinstance(response, str) and response != ''
            elif case == 'Int':
                result = isinstance(response, int)
            else:
                # None处理
                if response == None:
                    response = '$$$'
                else:
                    # print('存在非None的值')
                    pass
                if case == response:
                    result = True
                else:
                    result = False
                    # print(result)
        return result

    # 返回不同检查数据处理
    # 遇到list不检查list的数量去case中的第一个模板跟response中的内容最对比
    def response_diff_list(self, case, response):
        diff_result = True
        diff = []
        if isinstance(case, list):
            model = case[0]
            for i in case:
                for e in response:
                    if isinstance(i, str):
                        diff.append(self.response_data_check(model, e))
                    else:
                        self.response_diff_list(i, e)
        if isinstance(case, dict):
            if case.keys() == response.keys():
                for key in case.keys():
                    # 值得类型是list进行忽略检查
                    if isinstance(case[key], list):
                        # dict value检查有&&&忽略(强制转化了下期中的内容），这里是对list数量不对称的处理
                        if '&&&' in str(case[key]):
                            continue
                        else:
                            self.response_diff_list(case[key], response[key])
                    else:
                        if isinstance(case[key], str):
                            diff.append(self.response_data_check(case[key], response[key]))
                        else:
                            self.response_diff_list(case[key], response[key])
            else:
                diff.append(self.response_data_check(case, response))
        if False in diff:
            diff_result = False
        return diff_result

    # 对应字段返回对应值
    def data_content(self, data, Assert_data_content, response):
        data_content_result = True
        for i in list(Assert_data_content.keys()):
            if '&' in i:
                i_ = i.split('&')
                keys = [f for f in i_]
                data_list = list(data.values())
                key_result = [g for g in keys if g in str(data_list)]
                if len(key_result) == len(keys):
                    # try:
                    #     check = json.loads('Assert_data_content[i]')
                    #     print('&&&&&&&&&&&&&&&&')
                    #     data_content_result = self.response_diff_list(check, response)
                    # except:
                    #     print(check)
                    #     print(response)
                    check = Assert_data_content[i]
                    if check in str(response):
                        data_content_result = True
                    else:
                        print(str(check))
                        print(str(response))
                        data_content_result = False
            else:
                for e in data.values():
                    if i in e:
                        if Assert_data_content[i] in str(response):
                            data_content_result = True
                        else:
                            data_content_result = False
        return data_content_result

    # 检查(returen True or False,and add reason in fail)
    def asser_api(self, data, response, fail):
        Assert = self.Assert
        try:
            Assert_code = Assert['code']
        except:
            Assert_code = None
        try:
            Assert_data_format = Assert['data_format']
        except:
            Assert_data_format = None
        try:
            Assert_data_content = Assert['data_content']
        except:
            Assert_data_content = None
        fail_data = {}
        reason = []
        if response.status_code != 200:
            reason.append('接口返回值不等于200')
        try:
            response_data = json.loads(response.text)
            if Assert_code != None:
                code = response_data[Assert['code']['key']]
                if code != int(Assert['code']['value']):
                    reason.append('接口对应code' + Assert['code']['key'] + '值错误,返回内容为' + str(code))
            if Assert_data_format != None:
                case = Assert['data_format']
                data_format_result = self.response_diff_list(case, response_data)
                if data_format_result == False:
                    reason.append('接口数据格式错误,返回格式为:' + response.text)
            if Assert_data_content != None:
                data_content_result = self.data_content(data, Assert_data_content, response_data)
                if data_content_result == False:
                    reason.append('接口数据错误,返回数据为:' + response.text)
        except:
            # print('非JSON')
            pass
        if len(reason) > 0:
            fail_data.update({'data': data, 'reason': reason})
            fail.append(fail_data)
            return False
        else:
            return True

    # 发送请求
    def url_request(self, data, fail):
        if self.data == None or self.keys == None:
            url = self.url
            response = requests.request('get', url)
        else:
            lang = data['kb_lang']
            duid = data['duid']
            if isinstance(duid, list):
                duid = get_duid_in_way(duid[0], duid[1])
            else:
                pass
            app = data['app']
            header = self.set_header(duid, app=app, version=self.version, lang=lang, way=self.way)
            url = self.url_mosaic(data)
            response = requests.request('get', url, headers=header)
        self.asser_api(data, response, fail)


if __name__ == "__main__":
    test = config_reader('./test_case')
    a = Http_Test(test)
    data = a.url_keys_data()
    for i in data:
        print(i)
        # print(a.url_mosaic(i))
