# -*- coding: utf-8 -*-

from base import base_request, get_followeds
from excel_adapter import excel_data_getter_for_xlsx
from excel_adapter import save_data
import click
import os.path as osp


def get_followeds_data(uid, path, page_size=50, number_of_follow=50, en=False):
    """
    :param uid:
    :param path:
    :param page_size: 每页调用数量
    :param number_of_follow: 最多拉取数量
    :param en: 使用英文表头
    :return:
    """
    body_data = []
    if en:
        header = ["nickname", "userId", "followeds", "gender", "avatarUrl", "vipType", "userPage"]
    else:
        header = ["用户昵称", "用户id", "粉丝数量", "性别", "头像", "VIP等级", "主页"]
    flag = True
    page_count = 0
    while flag:
        this = get_followeds(uid, limit=page_size, offset=page_count*page_size)
        body_data += this
        print(f"page_count={page_count}, page_size={page_size}, len(this)={len(this)}")
        page_count += 1
        if len(this) == 0:
            flag = False

        if len(body_data) >= number_of_follow > 0:
            flag = False

    final_body = [header] + body_data
    base_data = excel_data_getter_for_xlsx("sheet1", final_body)
    save_data(path, base_data)


help_c = """Get Netease Cloud Music Follow Users"""
help_output = "Excel输出路径, like: ~/Desktop"
help_uid = "网易云音乐用户id, like: 46304650"
help_number = "最多拉取用户数量, 如果填`-1`则代表不限制数量, like: 100"


@click.command()
@click.help_option("-h", "--help", help=help_c)
@click.option("-o", "--output-dir", "output_dir", help=help_output, type=str, default=".")
@click.option("-u", "--uid", "uid", help=help_uid, type=int, required=True)
@click.option("-n", "--number-of-follow", "number_of_follow", help=help_number, type=int, default=50)
def main(uid, output_dir, number_of_follow):
    output_path = osp.join(output_dir, "music163_followeds_users.xlsx")
    get_followeds_data(uid, output_path, number_of_follow=number_of_follow)


if __name__ == '__main__':
    # _uid = 46304650
    # _output_path = "./follow_users.xlsx"
    main()
