# -*- coding:utf-8 -*-
import xlrd
import xlwt
from datetime import date,datetime
#连接数据库
import os
import MySQLdb
import sys
reload(sys)

sys.setdefaultencoding('utf-8')

conn=MySQLdb.connect(host="localhost",port=3306,user="root",passwd="mao123456",db="testdb",charset="utf8")
cursor=conn.cursor()
#def read_excel():
    #打开文件
workbook = xlrd.open_workbook(r'D:\TestExcel\ReportCase.xlsx')
sheet = workbook.sheet_by_index(1)
sheet = workbook.sheet_by_name('MXJ')
print sheet.name,sheet.nrows,sheet.ncols

rows = sheet.row_values(3)
cols = sheet.col_values(4)
print rows
print cols
sqli = "insert into student values(%s,%s,%s,%s)"
for i in range(sheet.nrows):
    print sheet.col_values(2)[i]
    cursor.execute(sqli,('sheet.col_values(2)[i]','sheet.col_values(0)[i]','sheet.col_values(1)[i]','sheet.col_values(3)[i]'))

