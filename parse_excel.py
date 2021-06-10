# -*- encoding: utf-8 -*-

import requests, xlrd


EXCEL_NAME = '/Users/chenpeng/Desktop/music163_follow_users.xlsx'
# 提取原始数据
def read_xlsx(excel_name, sheet_name):
    workbook = xlrd.open_workbook(excel_name)  
    booksheet = workbook.sheet_by_name(sheet_name)  
    p = list()  
    for row in range(booksheet.nrows):
        row_data = []  
        for col in range(booksheet.ncols):  
            cel = booksheet.cell(row, col)  
            val = cel.value  
            try:  
                val = cel.value  
                val = re.sub(r'\s+', '', val)  
            except:  
                pass  
            if type(val) == float:  
                val = int(val)  
            # else:  
            #     val = str(val)
            row_data.append(val)  
        p.append(row_data)
    return  p


def do():
    res = read_xlsx(EXCEL_NAME, u'sheet1')
    keys = res[0]
    data = []
    for row in res[1:]:
        single_dict = {}
        for i in range(len(row)):
            single_dict[keys[i]] = row[i]
        data.append(single_dict)
    users_data = ''
    for line in data:
        # print(line)
        users_data += """
      <tr>
        <td><img src="{头像}" alt="Girl in a jacket" width="60" height="60"></td>
        <td>{用户昵称}</td>
        <td>{用户id}</td>
        <td>{粉丝数量}</td>
        <td>{性别}</td>
        <td>{VIP等级}</td>
        <td><button type="button" οnclick="unfollow({用户id})">取消关注</button></td>
      </tr>
        """.format(**line)

    with open('./users_template.html', 'r') as f:
        text = f.read()

    with open('./users.html', 'w') as f1:
        f1.write(text.replace("USERS_DATA", users_data))
do()