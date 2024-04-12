import json
import os
import datetime
import unittest
from enum import Enum

class WorkDay(Enum):
    ONE_DAY_OFF = 0
    TWO_DAY_OFF = 1
    NO_DAY_OFF = 2

class Weekday(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

class CountWorkingDay(Enum):
    COUNT_ALL_DAY = 0
    COUNT_HALF_DAY = 1
    NO_COUNT = 2

arrGlobalConstHoliday = []
arrGlobalConstWorkday = []
dictGlobalVariableHoliday = {}

# 從 Holiday.json 的檔案讀取補班或放假的資料
def LoadJsonHolidayData(arrConstHoliday, arrConstWorkday):
    # 取得目前工作目錄
    current_dir = os.path.dirname(__file__)
    # 組合JSON檔案的路徑
    json_file_path = os.path.join(current_dir, 'Holiday.json')

    with open(json_file_path,'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        if(item["holiday"]):
            arrConstHoliday.append(item["date"])
        if(not item["holiday"]):
            arrConstWorkday.append(item["date"])
    # print(arrWorkday)


# 從 DailyReport.json 的檔案讀取美日資料
def LoadJsonDailyReportData(dictVariableHoliday):
    current_dir = os.path.dirname(__file__)
    json_file_path = os.path.join(current_dir, 'DailyReport.json')

    with open(json_file_path,'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        date = item["date"]
        if(item["morning_weather"] != 0 or item["morning_other"] != 0 ):
            dictVariableHoliday[date] = CountWorkingDay.NO_COUNT
        elif(item["afternoon_weather"] != 0 or item["afternoon_other"] != 0 ):
            dictVariableHoliday[date] = CountWorkingDay.COUNT_HALF_DAY
    

def CheckIsWorkDay(arrConstHoliday, arrConstWorkday, strDate, nWeekday, nCountType):
    if strDate in arrConstHoliday :
        return False
    elif strDate in arrConstWorkday:
        return True
    else:
        #周休一日
        if nCountType == WorkDay.ONE_DAY_OFF and nWeekday != Weekday.SUNDAY.value:
            return True
        #周休二日
        elif nCountType == WorkDay.TWO_DAY_OFF and nWeekday != Weekday.SATURDAY.value and nWeekday != Weekday.SUNDAY.value:
            return True
        #沒周休
        elif nCountType == WorkDay.NO_DAY_OFF:
            return True

def CountExpectFinishDate(strStart, nCountType, nTotalDay, arrConstHoliday, arrConstWorkday):
    kEndDate = datetime.datetime.strptime(strStart, "%Y-%m-%d")

    while(True):
        nWeekday = kEndDate.weekday()
        strEndDate = kEndDate.strftime("%Y-%m-%d")

        if CheckIsWorkDay(arrConstHoliday, arrConstWorkday, strEndDate, nWeekday, nCountType):
            nTotalDay -= 1

        if(nTotalDay <= 0):
            break

        kEndDate += datetime.timedelta(days=1)
    # print('End Date : ' + kEndDate.strftime("%Y-%m-%d"))
    return kEndDate.strftime("%Y-%m-%d")
    

# kStartDate 開工日字串，如 '2023-01-01'
# nCountType 工期計算方式 0:周休一日  1:周休二日  2:日曆天
# nTotalDay 工期天數
# arrConstHoliday 固定因素放假日
# arrConstWorkday 固定因素補班日
def CountRealFinishDate(strStart, nCountType, nTotalDay, arrConstHoliday, arrConstWorkday, dictVariableHoliday, strToday ):
    kEndDate = datetime.datetime.strptime(strStart, "%Y-%m-%d")
    kTodayDate = datetime.datetime.strptime(strToday, "%Y-%m-%d")
    
    #契約工期
    #契約天數
    #開工迄今天數
    #今日開始追加工期
    #累計追加工期
    #工期總計
    #契約完工日
    #變動完工日


    while(True):
        nWeekday = kEndDate.weekday()
        strEndDate = kEndDate.strftime("%Y-%m-%d")

        if CheckIsWorkDay(arrConstHoliday, arrConstWorkday, strEndDate, nWeekday, nCountType):
            if kEndDate <= kTodayDate:
                if strEndDate in dictVariableHoliday:
                    if dictVariableHoliday[strEndDate] == CountWorkingDay.NO_COUNT:
                        pass
                    elif dictVariableHoliday[strEndDate] == CountWorkingDay.COUNT_HALF_DAY:
                        nTotalDay -= 0.5
                    else:
                        nTotalDay -= 1
                else:
                    nTotalDay -= 1#沒填日報表就當作一般晴天
            else:
                nTotalDay -= 1#未來的日子還沒有日報表

        if(nTotalDay <= 0):
            break

        kEndDate += datetime.timedelta(days=1)
    # print('End Date : ' + kEndDate.strftime("%Y-%m-%d"))
    return kEndDate.strftime("%Y-%m-%d")


class TestFunction(unittest.TestCase):
    
    # 測試函數的測試用例
    def test_OneDayOffExpectFinishDate1(self):
        LoadJsonHolidayData(arrGlobalConstHoliday,arrGlobalConstWorkday)
        endDate = CountExpectFinishDate('2023-01-01', WorkDay.ONE_DAY_OFF, 1, arrGlobalConstHoliday, arrGlobalConstWorkday)
        self.assertEqual(endDate, '2023-01-03')

    def test_OneDayOffExpectFinishDate2(self):
        LoadJsonHolidayData(arrGlobalConstHoliday,arrGlobalConstWorkday)
        endDate = CountExpectFinishDate('2023-01-01', WorkDay.ONE_DAY_OFF, 60, arrGlobalConstHoliday, arrGlobalConstWorkday)
        self.assertEqual(endDate, '2023-03-25')
        
    def test_TwoDayOffExpectFinishDate(self):
        LoadJsonHolidayData(arrGlobalConstHoliday,arrGlobalConstWorkday)
        endDate = CountExpectFinishDate('2023-01-01', WorkDay.TWO_DAY_OFF, 60, arrGlobalConstHoliday, arrGlobalConstWorkday)
        self.assertEqual(endDate, '2023-03-31')

    def test_TwoDayOffRealFinishDate(self):
        LoadJsonHolidayData(arrGlobalConstHoliday,arrGlobalConstWorkday)
        LoadJsonDailyReportData(dictGlobalVariableHoliday)
        endDate = CountRealFinishDate('2023-01-01', WorkDay.TWO_DAY_OFF, 60, arrGlobalConstHoliday, arrGlobalConstWorkday, dictGlobalVariableHoliday, '2023-01-17')
        self.assertEqual(endDate, '2023-04-06')

    def test_TwoDayOffRealFinishDate2(self):
        LoadJsonHolidayData(arrGlobalConstHoliday,arrGlobalConstWorkday)
        LoadJsonDailyReportData(dictGlobalVariableHoliday)
        endDate = CountRealFinishDate('2023-01-01', WorkDay.TWO_DAY_OFF, 60, arrGlobalConstHoliday, arrGlobalConstWorkday, dictGlobalVariableHoliday, '2023-01-18')
        self.assertEqual(endDate, '2023-04-07')

if __name__ == '__main__':
    unittest.main()

# LoadJsonHolidayData(arrGlobalConstHoliday,arrGlobalConstWorkday)
# endDate = CountExpectFinishDate('2023-01-01',0,60,arrGlobalConstHoliday,arrGlobalConstWorkday)

# LoadJsonDailyReportData(dictGlobalVariableHoliday)
# CountFinishDate('2023-01-01',1,60,arrGlobalConstHoliday,arrGlobalConstWorkday,dictGlobalVariableHoliday, '2023-01-17')

# print(jsonGlobalVariableHoliday)