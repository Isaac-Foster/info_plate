from datetime import datetime, timedelta, timezone
from json import dumps


from flask import Blueprint, request, Response, session
from flask import make_response


from models.user import UserLogin


blue: Blueprint = Blueprint("login", __name__, url_prefix="/user")


def fields_required(fields: list[str]) -> tuple:
    data = dict(request.form or request.json)

    if not all([data.get(x) for x in fields]):
        return {"error": "fields not found"}, False

    return data, True


def get_data(data) -> tuple:
    user = UserLogin(**data)
    return user.verify()


def login_required(function):
    def inner(*args, **kwargs):
        # TODO
        user_login = UserLogin(
            session.get('login'),
            session.get('passwd')
        )
        print(session)
        print(user_login)

        if not user_login.verify()[1]:
            return 'Não está logado'
        return function(*args, *kwargs)
    return inner


@blue.route('/')
@login_required
def home():
    return 'acessado'


@blue.route("/login", methods=["POST"])
def login():
    data, all_fields = fields_required(["login", "passwd"])
    print(data)

    if all_fields:
        user = UserLogin(**data)
        hr = user.auth()

        if hr.status:

            session['login'] = user.login
            session['passwd'] = user.passwd
            print(session)

            return hr.message
        else:
            session.clear()

        return hr.message
    
    return data


@blue.route("/create", methods=["POST"])
def create():
    data, all_fields = fields_required(["login", "passwd"])
    print(data)
    user = UserLogin(**data)

    if not all_fields:
        return data
    
    hr = user.insert()

    return  hr.message


@blue.route("/update", methods=["UPDATE"])
def update_pass():
    data, all_fields = fields_required(["login", "passwd"])

    if not all_fields:
        return data
    
    return data


@blue.route("/delete", methods=["DELETE"])
def delete():
    data, all_fields = fields_required(["login", "passwd"])

    if not all_fields:
        return data
    
    return data