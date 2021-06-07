# -*- coding: utf-8 -*-
from base import login, base_request
import time


def del_follow(uid):
    """
        取消关注
    :param uid: 用户id
    :return:
    """
    follow(uid, t=0)


def add_follow(uid):
    """
        添加关注
    :param uid: 用户id
    :return:
    """
    follow(uid, t=1)


def follow(uid, t=1):
    """
    :param uid: 用户id
    :param t: 1为关注,其他为取消关注
    :return:
    """
    with open("./cookie.txt", 'r') as f:
        cookie = f.read()
    rest = f"/follow?id={uid}&t={t}&cookie={cookie}"
    data = base_request(rest)
    code = data.get('code')
    msg = data.get('msg')
    if code == 301 and msg == '需要登录':
        print(f"开始登录, 等待1s...")
        time.sleep(1)
        login()
        follow(uid, t=t)
    elif code == 200:
        print(f"{uid}: 操作成功")
        return True
    else:
        print(f"操作失败: {msg}")
        return False


def main():
    # add_follow(629015034)
    del_follow(629015034)


if __name__ == '__main__':
    main()
