#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2021/10/6 0:07

from openpyxl import load_workbook

wb = load_workbook(filename= 'empty_book1.xlsx')
sheet_ranges = wb['range names']
print(sheet_ranges['D18'].value)


