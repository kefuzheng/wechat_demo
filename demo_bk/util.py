#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     util.py
   Description :   常用工具方法
   Author :        kefuz
   date：          10:20 10/31/2019
-------------------------------------------------
   Change Activity:
                   10:20 10/31/2019
-------------------------------------------------
"""
import json
import uuid
from datetime import datetime


def model_list_to_json(model_list):
    """ model list 转换为json """
    new_list = []
    for model in model_list:
        model_dict = model.__dict__
        model_dict.pop('_sa_instance_state')
        created_date = model_dict.get('created_date').strftime('%b %d %H:%M')
        model_dict['created_date'] = created_date
        updated_date = model_dict.get('updated_date').strftime('%b %d %H:%M')
        model_dict['updated_date'] = updated_date
        new_list.append(model_dict)
    # json.dumps序列化时对中文默认使用的ascii编码.想输出真正的中文需要指定ensure_ascii = False
    return json.dumps(new_list)


def generate_unique_id():
    """ 生成唯一ID """
    str_id = str(uuid.uuid1())
    first_id = str_id.split("-")[0]
    return int(first_id, 16)


def generate_now_date():
    """ 生成当前时间，并转为timestamp """
    now = datetime.now()
    return now


print(generate_now_date())
