# -*- coding: utf-8 -*-

from base import base_request
from excel_adapter import excel_data_getter_for_xlsx
from excel_adapter import save_data
import click
import os.path as osp

USER_PAGE_URL = "https://music.163.com/#/user/home"
GENDER_DICT = {
    1: "男",
    2: "女",
    0: "未知",
}


def get_follows(uid, limit=30, offset=0):
    """
        获取关注用户的数据
    :param uid: 查询用户的uid
    :param limit:
    :param offset:
    :return:
    """
    # print("call `get_follows`...")
    rest = f"/user/follows?uid={uid}&limit={limit}&offset={offset}"
    data = base_request(rest)
    follow = data.get("follow", [])
    result = []
    for follower in follow:
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


def get_follows_data(uid, path, page_size=50, en=False):
    """
    :param uid:
    :param path:
    :param page_size: 每页调用数量
    :param en: 使用英文表头
    :return:
    """
    body_data = []
    if en:
        header = ["nickname", "userId", "followeds", "gender", "avatarUrl", "vipType", "user_page"]
    else:
        header = ["用户昵称", "用户id", "粉丝数量", "性别", "头像", "VIP等级", "主页"]
    flag = True
    page_count = 0
    while flag:
        this = get_follows(uid, limit=page_size, offset=page_count*page_size)
        body_data += this
        print(f"page_count={page_count}, page_size={page_size}, len(this)={len(this)}")
        page_count += 1
        if len(this) == 0:
            flag = False

        # to comment
        if page_count == 1:
            flag = False

    final_body = [header] + body_data
    base_data = excel_data_getter_for_xlsx("sheet1", final_body)
    save_data(path, base_data)


help_c = """Get Cloud Music Follow Users"""
help_output = "Excel输出路径"
help_uid = "网易云音乐用户id"


@click.command()
@click.help_option("-h", "--help", help=help_c)
@click.option("-o", "--output-dir", "output_dir", help=help_output, type=str, default="./follow_users.xlsx")
@click.option("-u", "--uid", "uid", help=help_uid, type=int, default=46304650)
def main(uid, output_dir):
    output_path = osp.join(output_dir, "music163_follow_users.xlsx")
    get_follows_data(uid, output_path)


if __name__ == '__main__':
    # _uid = 46304650
    # _output_path = "./follow_users.xlsx"
    main()
