# -*- coding: utf-8 -*-
# __author__ = 'Gz'
import yaml
import sys, getopt
import hashlib


def config_reader(yaml_file):
    yf = open(yaml_file)
    yx = yaml.load(yf)
    yf.close()
    return yx


def config_data_path(yaml_file):
    yf = open(yaml_file)
    yx = yaml.load(yf)
    yf.close()
    return {"data": yx, "path": yaml_file}


def source_input():
    argv = sys.argv[1:]
    source = None
    try:
        opts, args = getopt.getopt(argv, "h:s:", ["source="])
    except getopt.GetoptError:
        print('xxx.py  -s <source>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('xx.py -s <source>')
            sys.exit()
        elif opt in ("-s", "--source"):
            source = arg
        else:
            print('失败,未填写source')
    return source


def MD5(data):
    m = hashlib.md5()
    m.update(data.encode('utf-8'))
    MD5 = m.hexdigest()
    return MD5


def list_duplicate_removal(data):
    result = []
    for i in data:
        if i not in result:
            result.append(i)
    return result
