# encoding=utf-8
import uuid

import xlrd
import pymysql

#数据库配置
host = "127.0.0.1"
user = "root"
password = "root"
database = "work_record"


config_attribute = {
    '帐号' : 'account',
    '工号' : 'number',
    '姓名' : 'name',
    '部门' : 'dept',
    '职位' : 'position',
    '日期' : 'date',
    '星期' : 'day',
    '日期类型' : 'date_type',
    '班次' : 'shift',
    '上班时间' : 'on_work',
    '下班时间' : 'off_work',
    '签到打卡' : 'on_punch',
    '签退打卡' : 'off_punch',
    '工作时间(小时)' : 'work_hour',
    '计薪时间(小时)' : 'salary_hour',
    '迟到' : 'late',
    '早退' : 'early',
    '旷工(小时)' : 'neglect',
    '调休(小时)' : 'exchange',
    '外出(小时)' : 'go_out',
    '出差(小时)' : 'business',
    '加班(小时)' : 'overtime',
    '请假类型' : 'leave_type',
    '请假(小时)' : 'leave_hour'
}

config_attribute_arr = ['account',
                    'number',
                    'name',
                    'dept',
                    'position',
                    'date',
                    'day',
                    'date_type',
                    'shift',
                    'on_work',
                    'off_work',
                    'on_punch',
                    'off_punch',
                    'work_hour',
                    'salary_hour',
                    'late',
                    'early',
                    'neglect',
                    'exchange',
                    'go_out',
                    'business',
                    'overtime',
                    'leave_type',
                    'leave_hour']

def insert_by_sql(sql):
    print("execute sql:"+sql)
    conn = pymysql.connect(host, user, password, database,charset='utf8')
    cursor = conn.cursor()
    cursor.execute(sql)

    conn.commit()
    # data = cursor.fetchone()
    # print("Database version : %s " % data)
    conn.close()

open_workbook=xlrd.open_workbook(r'D:/project-python/export/Downloads/考勤日报-2020年07月04日至2020年07月04日-1593915601513.xls');

print(open_workbook);

table = open_workbook.sheets()[0]
print(table.nrows)
row = table.row_values(0)
col = table.col_values(0)
print(table.row_values(1));

for index in range(0,table.nrows):

    excelRow = table.row_values(index)

    if(index == 1):
        continue
    print(excelRow)

    if(index > 1):
        obj = {}
        sql = "insert into work_check ({}) values ({})";
        obj["id"] = ''.join(str(uuid.uuid1()).split('-'))
        for i in range(0,len(excelRow)):
            obj[config_attribute_arr[i]] = excelRow[i]

        sql1 = ""
        sql2 = ""
        for key in obj:
            sql1 += key + ","
            sql2 += "'" + obj[key] + "'" +","

        sql1 = sql1[:-1]
        sql2 = sql2[:-1]

        sql = sql.format(sql1,sql2)

        insert_by_sql(sql)






