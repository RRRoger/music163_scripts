# -*- coding: utf-8 -*-
from io import BytesIO
import xlsxwriter
import base64


def excel_data_getter_for_xlsx(name, excel_data):
    """
    :param name: sheet1 名
    :param excel_data: excel  数据
    :return: 返回二进制的数据
    """
    xls = BytesIO()
    xls_workbook = xlsxwriter.Workbook(xls)
    head_cell_format = xls_workbook.add_format({
        'font_size': 12,
        'bg_color': "#bbbbbb",
        'font_name': "Source Han Sans CN",
        'bold': 1,
    })

    body_cell_format = xls_workbook.add_format({
        'font_size': 12,
        'font_name': "Source Han Sans CN",
    })

    data_sheet = xls_workbook.add_worksheet(name)
    for x_index, x_data in enumerate(excel_data):
        for y_index, y_data in enumerate(x_data):
            if x_index == 0:
                data_sheet.write(x_index, y_index, y_data, head_cell_format)
            else:
                data_sheet.write(x_index, y_index, y_data, body_cell_format)

    xls_workbook.close()
    xls.seek(0)
    data = xls.getvalue()
    return data


def save_data(path, base_data):
    with open(path, "wb") as f:
        f.write(base_data)
    return


if __name__ == '__main__':
    _path = "./test.xlsx"
    _sheet1_name = "sheet"
    _excel_data = [
        ["col1", "col2"],
        ["123", "1234"],
        ["123", "1234"],
        ["123", "1234"],

    ]
    base_data = excel_data_getter_for_xlsx(_sheet1_name, _excel_data)
    save_data(_path, base_data)
