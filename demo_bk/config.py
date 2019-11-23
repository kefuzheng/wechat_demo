#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     config.py
   Description :   数据库配置信息
   Author :        kefuz
   date：          16:30 10/18/2019
-------------------------------------------------
   Change Activity:
                   16:30 10/18/2019
-------------------------------------------------
"""
from datetime import timedelta

SECRET_KEY = 'secret'
WTF_CSRF_SECRET_KEY = 'key'
DIALECT = 'mysql+pymysql'
USERNAME = 'root'
PASSWORD = '123456'
HOST = 'localhost'
PORT = '3306'
DATABASE = 'demo_db'

cons = '%s://%s:%s@%s:%s/%s' % (DIALECT, USERNAME, PASSWORD, HOST, PORT, DATABASE)

SQLALCHEMY_DATABASE_URI = cons
SQLALCHEMY_TRACK_MODIFICATIONS = False
PERMANENT_SESSION_LIFETIME = timedelta(days=7)
