from database.db import *
from flask import Flask, render_template, request, jsonify
from controllers.admin_s3 import *

def func_home_func():
    return render_template("home.html")

def func_register_page_func():
    return render_template("register.html")

def func_register_render_func():
    data = request.form
    file = request.files
    id = data["id"]
    name = data["name"]
    lastname = data["lastname"]
    birthday = data["birthday"]
    photo = file["photo"]
    add_user(id, name, lastname, birthday)
    upload_file_s3(photo, id)
    return "The user was added"

def func_consult_page_func():
    return render_template("consult.html")

def func_consult_render_func():   
    id = request.get_json()
    result = consult_user(id)
    obj_resp = {
        'name': result[0][1],
        'lastname': result[0][2]
    }
    return jsonify(obj_resp)