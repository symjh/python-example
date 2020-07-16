# encoding=utf-8
import time
import uuid

import xlrd
import pymysql
import os

#数据库配置
host = ""
user = "apps"
password = "lnmN4tA8n"
database = "femsuat"
path = "D:/project-python/export/Downloads/"

config_attribute = {
    '模具编号' : 'MODEL_CODE',
    '模具名称' : 'MODEL_NAME',
    '模具管理状态' : 'STATE'
}

config_attribute_arr = {
    '204360,204420,200268,200581':'1',
    '200591,200595':'2',
    '200804,200806,200810':'3',
    '200590,200592,204367':'4',
    '204364,200274,204363,204362':'5',
    '200270,200269,200201':'6',
    '200585':'7',
    '200583':'8',
    '200582':'9',
    '':'10',
    '205083':'11',
    '200789,200124':'12',
    '205040,200788':'13',
    '201204':'14',
    '':'15',
    '201211':'16',
    '200783':'17',
    '200127':'18',
    '200786':'19',
    '200135,200116':'20',
    '201207':'21',
    '201203':'22',
    '201206':'23',
    '201201,201202':'24',
    '201210':'25',
    '203780':'26',
    '201208':'27',
    '':'28',
    '':'29',
    '':'30',
}

def get_org_id(short_org):
    long_org = str(200000+int(short_org))
    for a in config_attribute_arr:
        if(a.find(long_org) >= 0):
            return config_attribute_arr[a]


def insert_by_sql(sql):
    print("execute sql:"+sql)
    conn = pymysql.connect(host, user, password, database,charset='utf8')
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    # data = cursor.fetchone()
    # print("Database version : %s " % data)
    conn.close()

def run_read():
    open_workbook=xlrd.open_workbook(r'D:/MyData/huangjh54/Downloads/模具主表数据.xls');
    print(open_workbook);
    table = open_workbook.sheets()[0]
    print(table.nrows)
    row = table.row_values(0)
    col = table.col_values(0)
    print(table.row_values(1));
    for index in range(0,table.nrows):
        excelRow = table.row_values(index)
        print(excelRow)
        if(index >= 1):
            obj = {}
            sql = "insert into model ({}) values ({})";
            # obj["id"] = ''.join(str(uuid.uuid1()).split('-'))
            obj["DATETIME_CREATED"] = "2020-07-15 18:00:00"
            obj["USER_CREATED"] = "sys"
            obj["DATETIME_MODIFIED"] = "2020-07-15 18:00:00"
            obj["USER_MODIFIED"] = "sys"
            obj["MODEL_CODE"] = excelRow[1]
            obj["MODEL_NAME"] = excelRow[2]
            obj["STATE"] = excelRow[3]
            if(excelRow[4] == ''):
                continue
            obj["ORG_ID"] = get_org_id(excelRow[4])
            sql1 = ""
            sql2 = ""
            for key in obj:
                sql1 += key + ","
                sql2 += "'" + str(obj[key]) + "'" +","
            sql1 = sql1[:-1]
            sql2 = sql2[:-1]
            sql = sql.format(sql1,sql2)
            try:
                insert_by_sql(sql)
            except Exception as ex:
                print("Exception:%s"%ex)
            else:
                print("正常")

if __name__ == '__main__':
    run_read()








