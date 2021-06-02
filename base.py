# -*- coding: utf-8 -*-

import configparser
import requests
PATH = "./user.conf"

config = configparser.ConfigParser()
config.read(PATH)
options = config['options']

login_way = options['login_way']
account = options['account']
password = options['password']
api_host = options['api_host']


def base_request(rest, cookie=None):
    data = {}
    try:
        response = requests.get(api_host + rest)
        data = response.json()
    except Exception as e:
        print("An error occurred...")
        print(e)
    return data


def login(login_way, account, password):
    if login_way == 'phone':
        rest = f"/login/cellphone?phone={account}&password={password}"
    elif login_way == 'email':
        rest = f'/login?email={account}&password={password}'
    else:
        pass
    data = base_request(rest)
    cookie = data.get("cookie", {}) or ''
    with open("./cookie.txt", "w+") as f:
        f.write(cookie)

    return


if __name__ == '__main__':
    login(login_way, account, password)
