#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     manage.py
   Description :   管理数据库
   Author :        kefuz
   date：          16:36 10/18/2019
-------------------------------------------------
   Change Activity:
                   16:36 10/18/2019
-------------------------------------------------
"""
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app
from models import *

migrate = Migrate(app, db)
manage = Manager(app)
manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manage.run()
