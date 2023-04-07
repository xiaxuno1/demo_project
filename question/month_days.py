# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: month_days
# Author: xiaxu
# DATA: 2023/3/24
# Description:
# ---------------------------------------------------
import calendar

def month_range(years,month):
    days = 30 #默认30天
    leap_year = False
    if years %4 ==0 and years %100 !=0 or years %400 ==0:
        leap_year = True
    if month in (4,6,9,11):
        days = 31
    elif leap_year and month ==2:
        days = 29
    elif month ==2:
        days = 28
    return days

if __name__ == '__main__':
    print(calendar.monthrange(2020, 2))
    print(month_range(2020, 2))
