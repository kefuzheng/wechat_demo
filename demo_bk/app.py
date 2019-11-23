#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, request, redirect, url_for
import config
from models import *
import json
import util
import exts

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/delete/<id>', methods=['GET'])
def delete_by_id(id):
    user = User.query.filter(User.id == id).first()
    user.delete()
    exts.db_commit(user)
    return 'success'


@app.route('/list', methods=['GET'])
def get_list():
    users = User.query.filter(User.deleted_flag==False).order_by(User.created_date).all()
    users_list = util.model_list_to_json(users)
    print(users_list)
    return json.dumps(users_list)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/form', methods=['POST', 'GET'])
def form():
    data_dict = {}
    if request.method == 'GET':
        data_dict = request.args.to_dict()
    else:
        data_dict = request.get_data()
        # get_data 为byte类型，需要转为json
        data_dict = json.loads(data_dict)

    name = data_dict.get('user_name')
    age = data_dict.get('user_age')
    job = data_dict.get('user_job')
    address = data_dict.get('user_address')
    sex = data_dict.get('user_sex')

    address_model = Address(address)
    user = User(name, age, job, sex, address_model.id)
    exts.db_commit_all(address_model, user)
    # return redirect(url_for('get_list'))
    return 'success'


@app.route('/login/<nick_name>', methods=['POST', 'GET'])
def login(nick_name):
    print(nick_name)
    return "Hello %s" % nick_name


if __name__ == '__main__':
    app.run(debug=True)
