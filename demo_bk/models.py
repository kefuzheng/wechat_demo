#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     models.py
   Description :   数据库model模型
   Author :        kefuz
   date：          16:38 10/18/2019
-------------------------------------------------
   Change Activity:
                   16:38 10/18/2019
-------------------------------------------------
"""
import util
from exts import db


class BaseModel(db.Model):
    """ base model """
    __abstract__ = True
    id = db.Column(db.BigInteger, primary_key=True)
    created_date = db.Column(db.DateTime, nullable=False)
    updated_date = db.Column(db.DateTime, nullable=False)
    deleted_flag = db.Column(db.Integer)

    def __init__(self):
        self.id = util.generate_unique_id()
        self.created_date = util.generate_now_date()
        self.updated_date = util.generate_now_date()
        self.deleted_flag = int(False)

    def delete(self):
        """ 删除此条数据（假删除） """
        self.deleted_flag = int(True)
        self.updated_date = util.generate_now_date()


class User(BaseModel):
    __tablename__ = 'user'
    name = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    job = db.Column(db.String(20), nullable=False)
    sex = db.Column(db.String(5), nullable=False)
    address_id = db.Column(db.BigInteger, nullable=False)

    def __init__(self, name, age, job, sex, address_id):
        super(self.__class__, self).__init__()
        self.name = name
        self.age = age
        self.job = job
        self.sex = sex
        self.address_id = address_id


class Address(BaseModel):
    __tablename__ = 'address'
    address = db.Column(db.String(20), nullable=False)

    def __init__(self, address):
        super(self.__class__, self).__init__()
        self.address = address
