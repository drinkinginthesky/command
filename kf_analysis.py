import pyodbc
from datetime import datetime

cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=localhost;"
                      "Database=shifenzheng;"
                      "Trusted_Connection=yes;")
cursor = cnxn.cursor()

BASE_CONDITION = 'select Ctfid, Version from cdsgus'
BASE_CONDITION_ID = 'len(Ctfid) = 18'
BASE_CONDITION_TIME = 'version <> \'\''
BASE_CONDITION_NAME = 'name is not null'


def get_birth_year(id):
    return int(id[6: 10])

def get_birth_month(id):
    return int(id[10: 12])

def get_birth_day(id):
    return int(id[12: 14])

"""
根据出生月份，日期生成星座
"""
def getConstellation(month, day):
    constellation_list = [
            {
                "name": "baiyang",
                "start_month": 3,
                "start_day": 21,
                "end_month": 4,
                "end_day": 19
            },
            {
                "name": "jinniu",
                "start_month": 4,
                "start_day": 20,
                "end_month": 5,
                "end_day": 20
            },
            {
                "name": "shuangzi",
                "start_month": 5,
                "start_day": 21,
                "end_month": 6,
                "end_day": 21
            },
            {
                "name": "juxie",
                "start_month": 6,
                "start_day": 22,
                "end_month": 7,
                "end_day": 22
            },
            {
                "name": "shizi",
                "start_month": 7,
                "start_day": 23,
                "end_month": 8,
                "end_day": 22
            },
            {
                "name": "chunv",
                "start_month": 8,
                "start_day": 23,
                "end_month": 9,
                "end_day": 22
            },
            {
                "name": "tiancheng",
                "start_month": 9,
                "start_day": 23,
                "end_month": 10,
                "end_day": 23
            },
            {
                "name": "tianxie",
                "start_month": 10,
                "start_day": 24,
                "end_month": 11,
                "end_day": 22
            },
            {
                "name": "sheshou",
                "start_month": 11,
                "start_day": 23,
                "end_month": 12,
                "end_day": 21
            },
            {
                "name": "mojie",
                "start_month": 12,
                "start_day": 22,
                "end_month": 1,
                "end_day": 19
            },
            {
                "name": "shuiping",
                "start_month": 1,
                "start_day": 20,
                "end_month": 2,
                "end_day": 18
            },
            {
                "name": "shuangyu",
                "start_month": 2,
                "start_day": 19,
                "end_month": 3,
                "end_day": 20
            }
        ]
    for item in constellation_list:
        if month == item['start_month'] and day > item['start_day']:
            return item['name']
        elif month == item['end_month'] and day < item['end_day']:
            return item['name']

"""
省份分析
"""
def analysisAddress(cursor):
    result = {
        '50': 0,
        '31': 0,
        '11': 0,
        '12': 0,
        '13': 0,
        '14': 0,
        '21': 0,
        '22': 0,
        '23': 0,
        '32': 0,
        '33': 0,
        '34': 0,
        '35': 0,
        '36': 0,
        '37': 0,
        '41': 0,
        '42': 0,
        '43': 0,
        '44': 0,
        '46': 0,
        '51': 0,
        '52': 0,
        '53': 0,
        '61': 0,
        '62': 0,
        '63': 0,
        '64': 0,
        '65': 0,
        '15': 0,
        '45': 0,
        '54': 0
    }
    sql = BASE_CONDITION + ' where ' + BASE_CONDITION_ID
    cursor.execute(sql)
    for info in cursor:
        if info.Ctfid[0: 2] in result:
            result[info.Ctfid[0: 2]] += 1
    print('address: ------------')
    print(result)
    print('address: ------------')

"""
年龄分析
"""
def analysisAge(cursor):
    result = {}
    sql = BASE_CONDITION + ' where ' + BASE_CONDITION_ID + ' and ' + BASE_CONDITION_TIME
    cursor.execute(sql)
    for info in cursor:
        try:
            birth = get_birth_year(info.Ctfid)
            check_in_time = datetime.strptime(info.Version, '%Y-%m-%d %H:%M:%S')
        except:
            continue
        age = check_in_time.year - birth
        if age < 16 or age > 80:
            continue
        if age in result:
            result[age] += 1
        else:
            result[age] = 1
    print('age: ------------')
    print(result)
    print('age: ------------')

"""
星座分析
"""
def analysisConstellation(cursor):
    sql = BASE_CONDITION + ' where ' + BASE_CONDITION_ID
    result = {}
    cursor.execute(sql)
    for info in cursor:
        try:
            birth_month = get_birth_month(info.Ctfid)
            birth_day = get_birth_day(info.Ctfid)
        except:
            continue
        constellation = getConstellation(birth_month, birth_day)
        if constellation in result:
            result[constellation] += 1
        else:
            result[constellation] = 1
    print('constellation: ------------')
    print(result)
    print('constellation: ------------')

"""
时间分析
"""
def analysisCheckInTime(cursor):
    day_result = {}
    year_result = {}
    sql = BASE_CONDITION + ' where ' + BASE_CONDITION_TIME
    cursor.execute(sql)
    for info in cursor:
        try:
            check_in_time = datetime.strptime(info.Version, '%Y-%m-%d %H:%M:%S')
        except:
            continue
        year = str(check_in_time.year)
        month = check_in_time.month
        day = check_in_time.day
        if month < 10:
            month = '0' + str(month)
        else:
            month = str(month)
        if day < 10:
            day = '0' + str(day)
        else:
            day = str(day)
        year_month_day = year + month + day
        hour = check_in_time.hour
        if hour in day_result:
            day_result[hour] += 1
        else:
            day_result[hour] = 1
        if year_month_day in year_result:
            year_result[year_month_day] += 1
        else:
            year_result[year_month_day] = 1

    print('check in time : ------------')
    # print(day_result)
    print(year_result)
    print('check in time : ------------')
analysisCheckInTime(cursor)

