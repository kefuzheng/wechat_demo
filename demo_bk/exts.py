#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     exts.py
   Description :   实例化db
   Author :        kefuz
   date：          16:30 10/18/2019
-------------------------------------------------
   Change Activity:
                   16:30 10/18/2019
-------------------------------------------------
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def db_commit(obj):
    """ 提交单个数据 """
    db.session.add(obj)
    db.session.commit()


def db_commit_all(*objs):
    """ 提交多个数据 list"""
    db.session.add_all(objs)
    db.session.commit()

"""
    级联查询
    model = db.session.query(Class.name,Class.id, User.id).join(User, Class.user_id == User.id).all()

"""