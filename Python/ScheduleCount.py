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
dictGlobalWeatherRelatedHoliday = {}
dictGlobalExtendData = {}

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
def LoadJsonDailyReportData(dictWeatherRelatedHoliday):
    current_dir = os.path.dirname(__file__)
    json_file_path = os.path.join(current_dir, 'DailyReport.json')

    with open(json_file_path,'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        date = item["date"]
        if(item["morning_weather"] != 0 or item["morning_other"] != 0 ):
            dictWeatherRelatedHoliday[date] = CountWorkingDay.NO_COUNT
        elif(item["afternoon_weather"] != 0 or item["afternoon_other"] != 0 ):
            dictWeatherRelatedHoliday[date] = CountWorkingDay.COUNT_HALF_DAY
    

# 從 ExtendData.json 的檔案讀取美日資料
def LoadJsonExtendData(dictExtendData):
    current_dir = os.path.dirname(__file__)
    json_file_path = os.path.join(current_dir, 'ExtendData.json')

    with open(json_file_path,'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        dictExtendData[item["extend_start_date"]] = item["extend_days"]



#根據固定因素判斷是否為工作日
def CheckIsWorkDay(arrConstHoliday, arrConstWorkday, strDate, nWeekday, eCountType):
    if strDate in arrConstHoliday :
        return False
    elif strDate in arrConstWorkday:
        return True
    else:
        #周休一日
        if eCountType == WorkDay.ONE_DAY_OFF and nWeekday != Weekday.SUNDAY.value:
            return True
        #周休二日
        elif eCountType == WorkDay.TWO_DAY_OFF and nWeekday != Weekday.SATURDAY.value and nWeekday != Weekday.SUNDAY.value:
            return True
        #沒周休
        elif eCountType == WorkDay.NO_DAY_OFF:
            return True

def CountExpectFinishDate(eCountType, nTotalWorkdays, strStart, arrConstHoliday, arrConstWorkday):
    kStartDate = datetime.datetime.strptime(strStart, "%Y-%m-%d")
    kEndDate = datetime.datetime.strptime(strStart, "%Y-%m-%d")

    while(True):
        nWeekday = kEndDate.weekday()
        strEndDate = kEndDate.strftime("%Y-%m-%d")

        if CheckIsWorkDay(arrConstHoliday, arrConstWorkday, strEndDate, nWeekday, eCountType):
            nTotalWorkdays -= 1

        if(nTotalWorkdays <= 0):
            break

        kEndDate += datetime.timedelta(days=1)

    returnValue = {}
    returnValue['ExpectFinishDate'] = kEndDate.strftime("%Y-%m-%d")
    returnValue['ExpectTotalCalendarDays'] = (kEndDate - kStartDate).days - 1

    return returnValue
    

# kStartDate 開工日字串，如 '2023-01-01'
# eCountType 工期計算方式 0:周休一日  1:周休二日  2:日曆天
# nTotalWorkdays 工期天數
# arrConstHoliday 固定因素放假日
# arrConstWorkday 固定因素補班日
def CountRealFinishDate(eCountType, nTotalWorkdays, strStart, strToday, arrConstHoliday, arrConstWorkday, dictWeatherRelatedHoliday, dictExtendData):
    kStartDate = datetime.datetime.strptime(strStart, "%Y-%m-%d")
    kEndDate = datetime.datetime.strptime(strStart, "%Y-%m-%d")
    kTodayDate = datetime.datetime.strptime(strToday, "%Y-%m-%d")
    
    for key, value in dictExtendData.items():
        kExtendStartDate = datetime.datetime.strptime(key, "%Y-%m-%d")
        if kTodayDate >= kExtendStartDate:
            nTotalWorkdays += value

    #契約工期         合約給定
    #契約天數         ExpectTotalCalendarDays
    #契約完工日       ExpectFinishDate
    #開工迄今工作天數  WorkDaysFromStart
    #開工迄今日曆天數  CalendarDaysFromStart
    #今日開始追加工期
    #累計追加工期
    #工期總計
    #變動完工日        RealFinishDate
    #變動完工天數      RealTotalCalendarDays


    while(True):
        nWeekday = kEndDate.weekday()
        strEndDate = kEndDate.strftime("%Y-%m-%d")

        if CheckIsWorkDay(arrConstHoliday, arrConstWorkday, strEndDate, nWeekday, eCountType):
            if kEndDate <= kTodayDate:
                if strEndDate in dictWeatherRelatedHoliday:
                    if dictWeatherRelatedHoliday[strEndDate] == CountWorkingDay.NO_COUNT:
                        pass
                    elif dictWeatherRelatedHoliday[strEndDate] == CountWorkingDay.COUNT_HALF_DAY:
                        nTotalWorkdays -= 0.5
                    else:
                        nTotalWorkdays -= 1
                else:
                    nTotalWorkdays -= 1#沒填日報表就當作一般晴天
            else:
                nTotalWorkdays -= 1#未來的日子還沒有日報表

        if(nTotalWorkdays <= 0):
            break

        kEndDate += datetime.timedelta(days=1)
    # print('End Date : ' + kEndDate.strftime("%Y-%m-%d"))
    returnValue = {}
    returnValue['RealFinishDate'] = kEndDate.strftime("%Y-%m-%d")
    returnValue['RealTotalCalendarDays'] = (kEndDate - kStartDate).days + 1
    # returnValue['WorkDaysFromStart']
    # returnValue['CalendarDaysFromStart']

    return returnValue


class TestFunction(unittest.TestCase):
    
    # 測試函數的測試用例
    def test_OneDayOffExpectFinishDate1(self):
        LoadJsonHolidayData(arrGlobalConstHoliday,arrGlobalConstWorkday)
        returnValue = CountExpectFinishDate(WorkDay.ONE_DAY_OFF, 1, '2023-01-01', arrGlobalConstHoliday, arrGlobalConstWorkday)
        self.assertEqual(returnValue['ExpectFinishDate'], '2023-01-03')

    def test_OneDayOffExpectFinishDate2(self):
        LoadJsonHolidayData(arrGlobalConstHoliday,arrGlobalConstWorkday)
        returnValue = CountExpectFinishDate(WorkDay.ONE_DAY_OFF, 60, '2023-01-01', arrGlobalConstHoliday, arrGlobalConstWorkday)
        self.assertEqual(returnValue['ExpectFinishDate'], '2023-03-25')
        
    def test_TwoDayOffExpectFinishDate(self):
        LoadJsonHolidayData(arrGlobalConstHoliday,arrGlobalConstWorkday)
        returnValue = CountExpectFinishDate(WorkDay.TWO_DAY_OFF, 60, '2023-01-01', arrGlobalConstHoliday, arrGlobalConstWorkday)
        self.assertEqual(returnValue['ExpectFinishDate'], '2023-03-31')

    def test_TwoDayOffRealFinishDate(self):
        LoadJsonHolidayData(arrGlobalConstHoliday,arrGlobalConstWorkday)
        LoadJsonDailyReportData(dictGlobalWeatherRelatedHoliday)
        LoadJsonExtendData(dictGlobalExtendData)
        returnValue = CountRealFinishDate(WorkDay.TWO_DAY_OFF, 60, '2023-01-01', '2023-01-17', arrGlobalConstHoliday, arrGlobalConstWorkday, dictGlobalWeatherRelatedHoliday, dictGlobalExtendData)
        # self.assertEqual(returnValue['ExpectFinishDate'], '2023-03-31')
        self.assertEqual(returnValue['RealFinishDate'], '2023-04-06')
        self.assertEqual(returnValue['RealTotalCalendarDays'], 96)

    def test_TwoDayOffRealFinishDate2(self):
        LoadJsonHolidayData(arrGlobalConstHoliday,arrGlobalConstWorkday)
        LoadJsonDailyReportData(dictGlobalWeatherRelatedHoliday)
        LoadJsonExtendData(dictGlobalExtendData)
        returnValue = CountRealFinishDate(WorkDay.TWO_DAY_OFF, 60, '2023-01-01', '2023-01-18', arrGlobalConstHoliday, arrGlobalConstWorkday, dictGlobalWeatherRelatedHoliday, dictGlobalExtendData)
        self.assertEqual(returnValue['RealFinishDate'], '2023-04-07')
        self.assertEqual(returnValue['RealTotalCalendarDays'], 97)

if __name__ == '__main__':
    unittest.main()

# LoadJsonHolidayData(arrGlobalConstHoliday,arrGlobalConstWorkday)
# endDate = CountExpectFinishDate('2023-01-01',0,60,arrGlobalConstHoliday,arrGlobalConstWorkday)

# LoadJsonDailyReportData(dictGlobalWeatherRelatedHoliday)
# CountFinishDate('2023-01-01',1,60,arrGlobalConstHoliday,arrGlobalConstWorkday,dictGlobalWeatherRelatedHoliday, '2023-01-17')

# print(jsonGlobalVariableHoliday)