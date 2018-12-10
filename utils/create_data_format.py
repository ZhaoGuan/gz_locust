# -*- coding: utf-8 -*-
# __author__ = "Gz"
import json


# 根据数据类型生成校验参数
def data_type_case(data):
    if isinstance(data, str) and "http" in data:
        data_type = "HTTP"
    elif isinstance(data, bool):
        data_type = "Bool"
    elif isinstance(data, str):
        data_type = "Str"
    elif isinstance(data, int):
        data_type = "Int"
    elif isinstance(data, float):
        data_type = "Float"
    else:
        # 处理了None
        data_type = None
    return data_type


# content数据清洗
# 把接口中的值清理了
# 如果遇到的是一个LIST那么默认其中所有的内容都是一致的只保留一个模板内容
def ergodic_list(data):
    for i in range(len(data)):
        if i == 0:
            if isinstance(data[i], str) or isinstance(data[i], int) or \
                    isinstance(data[i], bool) or isinstance(data[i], float) or data[i] is None:
                data[i] = data_type_case(data[i])
                print("list中存放的不是dict")
            else:
                ergodic(data[i])
        else:
            data[i] = None


def ergodic_dict(data):
    for key in data.keys():
        if isinstance(data[key], str) or isinstance(data[key], int) or \
                isinstance(data[key], bool) or isinstance(data[key], float) or data[key] is None:
            data[key] = data_type_case(data[key])
        else:
            ergodic(data[key])


def ergodic(data):
    if isinstance(data, list):
        ergodic_list(data)
    elif isinstance(data, dict):
        ergodic_dict(data)
    return data


# 异常数据处理
# 需要根据具体情况添加主要解决不识别问题
def data_clear(data):
    if isinstance(data, bytes):
        data = data.decode("utf-8")
    data = json.loads(data)
    data = ergodic(data)
    return data


if __name__ == "__main__":
    # data内容为response返回内容
    response = {
        "errorCode": "0",
        "errorMsg": "ok",
        "info": {
            "search_list": [
                {
                    "hot_word": "hoooooot"
                }
            ]
        }
    }
    data = json.dumps(response)
    print(data_clear(data))
