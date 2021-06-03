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


USER_PAGE_URL = "https://music.163.com/#/user/home"
GENDER_DICT = {
    1: "男",
    2: "女",
    0: "未知",
}


def base_request(rest, cookie=None):
    data = {}
    try:
        response = requests.get(api_host + rest)
        data = response.json()
    except Exception as e:
        print("An error occurred...")
        print(e)
    return data


def get_fos(uid, key="followeds", limit=30, offset=0):
    """
        获取粉丝数据
    :param uid: 查询用户的uid
    :param key: followeds 粉丝; follow 关注的人
    :param limit:
    :param offset:
    :return:
    """
    if key == "followeds":
        rest = f"/user/followeds?uid={uid}&limit={limit}&offset={offset}"
        field = "followeds"
    elif key == "follows":
        rest = f"/user/follows?uid={uid}&limit={limit}&offset={offset}"
        field = "follow"
    else:
        raise Exception("An error occurred...")

    data = base_request(rest)
    followeds = data.get(field, [])
    result = []
    for follower in followeds:
        nickname = follower['nickname']
        follower_id = follower['userId']
        followeds = follower['followeds']
        avatar_url = follower['avatarUrl']
        gender = GENDER_DICT.get(follower['gender'])
        vip_type = follower['vipType']
        user_page = f"{USER_PAGE_URL}?id={follower_id}"
        result.append([
            nickname, follower_id, followeds, gender, avatar_url, vip_type, user_page
        ])
    return result


def get_followeds(uid, limit=30, offset=0):
    return get_fos(uid, key="followeds", limit=limit, offset=offset)


def get_follows(uid, limit=30, offset=0):
    return get_fos(uid, key="follows", limit=limit, offset=offset)

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
