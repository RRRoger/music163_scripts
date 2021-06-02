# -*- coding: utf-8 -*-

from base import base_request
from excel_adapter import excel_data_getter_for_xlsx
from excel_adapter import save_data


def get_followers(uid, limit=30, offset=0):

    print("call `get_followers`...")

    rest = f"/user/follows?uid={uid}&limit={limit}&offset={offset}"
    data = base_request(rest)
    follow = data.get("follow", [])
    result = []
    for follower in follow:
        nickname = follower['nickname']
        userId = follower['userId']
        followeds = follower['followeds']
        avatarUrl = follower['avatarUrl']
        gender = follower['gender']
        vipType = follower['vipType']
        user_page = f"https://music.163.com/#/user/home?id={userId}"
        result.append([
            nickname, userId, followeds, gender, avatarUrl, vipType, user_page
        ])
    return result


def get_followers_data(uid, page_size=50):
    body_data = []
    header = ["nickname", "userId", "followeds", "gender", "avatarUrl", "vipType", "user_page"]
    flag = True
    page_count = 0
    while flag:
        this = get_followers(uid, limit=page_size, offset=page_count*page_size)
        body_data += this
        print(f"page_count={page_count}, page_size={page_size}, len(this)={len(this)}")
        page_count += 1
        if len(this) == 0:
            flag = False
        if page_count == 20:
            flag = False

    final_body = [header] + body_data
    base_data = excel_data_getter_for_xlsx("sheet1", final_body)
    save_data("./test4.xlsx", base_data)


if __name__ == '__main__':
    _uid = "46304650"
    get_followers_data(_uid)
