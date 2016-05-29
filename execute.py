# -*- coding: utf-8 -*-
from datetime import datetime

import xlwings as xw

import url_check as uc


def execute():
    wb = xw.Workbook.caller()
    set_execute_time()
    check()


def set_execute_time():
    xw.Range('B1').value = datetime.now().strftime("%Y/%m/%d %H:%M:%S")


def check():
    # get target url list
    targets = xw.Range('A3').table.value

    # check each url
    for target in targets:
        if target[0] == "No":
            continue
        else:
            result = uc.url_check(target[1])
            target[2] = result[0]
            target[3] = result[1]

    # set the result
    xw.Range('A3').value = targets


if __name__ == "__main__":
    # ready xls file
    file_name = "URLCheckTool.xlsm"
    wb = xw.Workbook(file_name)
    set_execute_time()
    check()
