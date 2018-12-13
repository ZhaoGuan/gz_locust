# -*- coding: utf-8 -*-
# __author__ = 'Gz'
import requests
import json
import csv
import os


class ZabbixData:
    def __init__(self):
        self.zabbix_api_url = "http://zabbix.ci.wuren.com/zabbix/api_jsonrpc.php"
        self.user_data = {
            "user": "guanzhao",
            "password": "gz19891020"
        }
        self.login_data = {
            # API使用的JSON-RPC协议的版本
            "jsonrpc": "2.0",
            # api 调用方法≈
            "method": "user.login",
            "params": {
                "user": self.user_data["user"],
                "password": self.user_data["password"]
            },
            "id": 1,
            "auth": None
        }
        self.token = None

    def login_token(self):
        response = requests.post(url=self.zabbix_api_url, json=self.login_data)
        # print(response.text)
        return json.loads(response.text)["result"]

    def get_token(self):
        if self.token is None:
            self.token = self.login_token()
        return self.token

    def get_host_id(self, host_name):
        host_group = {
            "jsonrpc": "2.0",
            "method": "host.get",
            "params": {
                "output": "extend",
                "filter": {
                    "name": [
                        host_name
                    ]
                }
            },
            "auth": self.get_token(),
            "id": 1
        }
        response = requests.post(url=self.zabbix_api_url, json=host_group)
        # print(response.text)
        return json.loads(response.text)["result"][0]["hostid"]

    def get_server_item_data(self, host_id, key):
        # 监控内容
        # 每分钟cpu load 每核
        # system.cpu.load[percpu,avg1]
        # 每分钟cpu load 全核
        # system.cpu.load[all,avg1]
        # 可用内存
        # vm.memory.size[available]
        # cpu io wait tiime
        # system.cpu.util[,iowait]
        item_data = {
            "jsonrpc": "2.0",
            "method": "item.get",
            "params": {
                "output": "extend",
                "hostids": host_id,
                "search": {
                    "key_": key,

                },
                "sortfield": "name"
            },
            "auth": self.get_token(),
            "id": 1
        }
        response = requests.post(url=self.zabbix_api_url, json=item_data)
        # print(response.text)
        return json.loads(response.text)

    def get_server_data(self, host_id):
        data_list = {
            "Load": "system.cpu.load[percpu,avg1]",
            "Available_Memory": "vm.memory.size[available]",
            "IOWait": "system.cpu.util[,iowait]"
        }
        result = {}
        for key, value in data_list.items():
            value_data = self.get_server_item_data(host_id, value)["result"][0]["lastvalue"]
            result.update({key: value_data})
        # print(result)
        return result

    def save_data_to_csv(self, count, host_name, path):
        file_path = path + "/server_" + host_name + "_" + str(count) + ".csv"
        host_id = self.get_host_id(host_name)
        result = self.get_server_data(host_id)
        first_line = ["Count", "Load", "Available_Memory", "IOWait"]
        result.update({"Count": count})
        print(result)
        with open(file_path, "w") as f:
            dw = csv.DictWriter(f, first_line)
            dw.writeheader()
            for items in [result]:
                dw.writerow(items)

    def all_report_to_csv(self, host_name, path):
        result_file_list = []
        file_list = os.listdir(path)
        all_data = [["Count", "Load", "Available_Memory", "IOWait"]]
        for file in file_list:
            if "server" in file and "all" not in file:
                result_file_list.append(file)
        for server_file in result_file_list:
            with open(path + "/" + server_file) as f:
                # print([i for i in csv.reader(f)])
                data = [i for i in csv.reader(f)]
                all_data.append(data[1])
        with open(path + "/server_" + host_name + "_all.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerows(all_data)


if __name__ == "__main__":
    ZD = ZabbixData()
    host_id = ZD.get_host_id("wuren-backend-burger-web0")
    # print(host_id)
    load = ZD.get_server_item_data(host_id, "load")
    # load = ZD.get_server_data(host_id)
    print(load)
