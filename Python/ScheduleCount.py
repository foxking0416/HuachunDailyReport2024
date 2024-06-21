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
def func_load_json_holiday_data(arrConstHoliday, arrConstWorkday):
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
def func_load_json_daily_report_data(dictWeatherRelatedHoliday):
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
def func_load_json_extend_data(dictExtendData):
    current_dir = os.path.dirname(__file__)
    json_file_path = os.path.join(current_dir, 'ExtendData.json')

    with open(json_file_path,'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        dictExtendData[item["extend_start_date"]] = item["extend_days"]



#根據固定因素判斷是否為工作日
def func_check_is_work_day(arrConstHoliday, arrConstWorkday, strDate, nWeekday, eCountType):
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

def func_count_expect_finish_date(eCountType, nExpectTotalWorkdays, strStart, arrConstHoliday, arrConstWorkday):
    kStartDate = datetime.datetime.strptime(strStart, "%Y-%m-%d")
    kExpectEndDate = datetime.datetime.strptime(strStart, "%Y-%m-%d")

    while(True):
        nWeekday = kExpectEndDate.weekday()
        strEndDate = kExpectEndDate.strftime("%Y-%m-%d")

        if func_check_is_work_day(arrConstHoliday, arrConstWorkday, strEndDate, nWeekday, eCountType):
            nExpectTotalWorkdays -= 1

        if(nExpectTotalWorkdays <= 0):
            break

        kExpectEndDate += datetime.timedelta(days=1)

    returnValue = {}
    returnValue['ExpectFinishDate'] = kExpectEndDate.strftime("%Y-%m-%d")
    returnValue['ExpectTotalCalendarDays'] = (kExpectEndDate - kStartDate).days + 1

    return returnValue
    

# kStartDate 開工日字串，如 '2023-01-01'
# eCountType 工期計算方式 0:周休一日  1:周休二日  2:日曆天
# nTotalWorkdays 工期天數
# arrConstHoliday 固定因素放假日
# arrConstWorkday 固定因素補班日
def func_count_real_finish_date(eCountType, nExpectTotalWorkdays, strStart, strToday, arrConstHoliday, arrConstWorkday, dictWeatherRelatedHoliday, dictExtendData):
    kStartDate = datetime.datetime.strptime(strStart, "%Y-%m-%d")#開工日期
    kTodayDate = datetime.datetime.strptime(strToday, "%Y-%m-%d")
    kRealEndDate = kStartDate 
    kExpectEndDate = kStartDate
    nRealRestWorkdays = nExpectTotalWorkdays
    nExpectRestWorkdays = nExpectTotalWorkdays

    nPastWorkdays = 0
    nTotalExtendDays = 0

    for key, value in dictExtendData.items():
        kExtendStartDate = datetime.datetime.strptime(key, "%Y-%m-%d")
        if kTodayDate >= kExtendStartDate:
            nTotalExtendDays += value

    nRealRestWorkdays += nTotalExtendDays

    #契約工期         合約給定
    #契約完工日       ExpectFinishDate
    #契約天數         ExpectTotalCalendarDays

    #開工迄今工作天數  FromStartWorkDays
    #開工迄今日曆天數  FromStartCalendarDays
    #變動完工日       RealFinishDate
    #變動完工天數     RealTotalCalendarDays
    #預計剩餘工期     ExpectRestWorkDays
    #預計剩餘天數     ExpectRestCalendarkDays
    #實際剩餘工期     RealRestWorkDays
    #實際剩餘天數     RealRestCalendarkDays
    
    #今日開始追加工期
    #累計追加工期
    #工期總計

    

    while(True):
        nWeekday = kRealEndDate.weekday()
        strEndDate = kRealEndDate.strftime("%Y-%m-%d")

        if func_check_is_work_day(arrConstHoliday, arrConstWorkday, strEndDate, nWeekday, eCountType):
            if kRealEndDate <= kTodayDate:
                if strEndDate in dictWeatherRelatedHoliday:
                    if dictWeatherRelatedHoliday[strEndDate] == CountWorkingDay.NO_COUNT:
                        pass
                    elif dictWeatherRelatedHoliday[strEndDate] == CountWorkingDay.COUNT_HALF_DAY:
                        nPastWorkdays += 0.5
                        nRealRestWorkdays -= 0.5
                    else:
                        nPastWorkdays += 1
                        nRealRestWorkdays -= 1
                else:
                    nPastWorkdays += 1
                    nRealRestWorkdays -= 1#沒填日報表就當作一般晴天
            else:
                nRealRestWorkdays -= 1#未來的日子還沒有日報表
            nExpectRestWorkdays -= 1

        if(nRealRestWorkdays <= 0):
            break

        if nExpectRestWorkdays > 0:
            kExpectEndDate += datetime.timedelta(days=1)

        kRealEndDate += datetime.timedelta(days=1)


    # print('End Date : ' + kEndDate.strftime("%Y-%m-%d"))
    returnValue = {}
    returnValue['ExpectFinishDate'] = kExpectEndDate.strftime("%Y-%m-%d")
    returnValue['ExpectTotalCalendarDays'] = (kExpectEndDate - kStartDate).days + 1
    returnValue['RealFinishDate'] = kRealEndDate.strftime("%Y-%m-%d")
    returnValue['RealTotalCalendarDays'] = (kRealEndDate - kStartDate).days + 1
    returnValue['FromStartCalendarDays'] = (kTodayDate - kStartDate).days + 1
    returnValue['FromStartWorkDays'] = nPastWorkdays
    returnValue['ExpectRestWorkDays'] = nExpectTotalWorkdays - nPastWorkdays
    returnValue['ExpectRestCalendarkDays'] = (kExpectEndDate - kTodayDate).days
    returnValue['RealRestWorkDays'] = nExpectTotalWorkdays + nTotalExtendDays - nPastWorkdays
    returnValue['RealRestCalendarkDays'] = (kRealEndDate - kTodayDate).days 

    return returnValue


class TestFunction(unittest.TestCase):
    
    # 測試函數的測試用例
    def test_OneDayOffExpectFinishDate1(self):
        func_load_json_holiday_data(arrGlobalConstHoliday,arrGlobalConstWorkday)
        returnValue = func_count_expect_finish_date(WorkDay.ONE_DAY_OFF, 1, '2023-01-01', arrGlobalConstHoliday, arrGlobalConstWorkday)
        self.assertEqual(returnValue['ExpectFinishDate'], '2023-01-03')
        self.assertEqual(returnValue['ExpectTotalCalendarDays'], 3)

    def test_OneDayOffExpectFinishDate2(self):
        func_load_json_holiday_data(arrGlobalConstHoliday,arrGlobalConstWorkday)
        returnValue = func_count_expect_finish_date(WorkDay.ONE_DAY_OFF, 60, '2023-01-01', arrGlobalConstHoliday, arrGlobalConstWorkday)
        self.assertEqual(returnValue['ExpectFinishDate'], '2023-03-25')
        self.assertEqual(returnValue['ExpectTotalCalendarDays'], 84)
        
    def test_TwoDayOffExpectFinishDate(self):
        func_load_json_holiday_data(arrGlobalConstHoliday,arrGlobalConstWorkday)
        returnValue = func_count_expect_finish_date(WorkDay.TWO_DAY_OFF, 60, '2023-01-01', arrGlobalConstHoliday, arrGlobalConstWorkday)
        self.assertEqual(returnValue['ExpectFinishDate'], '2023-03-31')
        self.assertEqual(returnValue['ExpectTotalCalendarDays'], 90)

    def test_OneDayOffRealFinishDate(self):
        func_load_json_holiday_data(arrGlobalConstHoliday,arrGlobalConstWorkday)
        func_load_json_daily_report_data(dictGlobalWeatherRelatedHoliday)
        func_load_json_extend_data(dictGlobalExtendData)
        returnValue = func_count_real_finish_date(WorkDay.ONE_DAY_OFF, 60, '2023-01-01', '2023-01-17', arrGlobalConstHoliday, arrGlobalConstWorkday, dictGlobalWeatherRelatedHoliday, dictGlobalExtendData)
        self.assertEqual(returnValue['ExpectFinishDate'], '2023-03-25')
        self.assertEqual(returnValue['ExpectTotalCalendarDays'], 84)
        self.assertEqual(returnValue['RealFinishDate'], '2023-03-27')
        self.assertEqual(returnValue['RealTotalCalendarDays'], 86)
        self.assertEqual(returnValue['FromStartCalendarDays'], 17)
        self.assertEqual(returnValue['FromStartWorkDays'], 12.5)
        self.assertEqual(returnValue['ExpectRestWorkDays'], 47.5)
        self.assertEqual(returnValue['ExpectRestCalendarkDays'], 67)#14+28+25
        self.assertEqual(returnValue['RealRestWorkDays'], 47.5)
        self.assertEqual(returnValue['RealRestCalendarkDays'], 69)#14+28+27

    def test_TwoDayOffRealFinishDate(self):
        func_load_json_holiday_data(arrGlobalConstHoliday,arrGlobalConstWorkday)
        func_load_json_daily_report_data(dictGlobalWeatherRelatedHoliday)
        func_load_json_extend_data(dictGlobalExtendData)
        returnValue = func_count_real_finish_date(WorkDay.TWO_DAY_OFF, 60, '2023-01-01', '2023-01-17', arrGlobalConstHoliday, arrGlobalConstWorkday, dictGlobalWeatherRelatedHoliday, dictGlobalExtendData)
        self.assertEqual(returnValue['ExpectFinishDate'], '2023-03-31')
        self.assertEqual(returnValue['ExpectTotalCalendarDays'], 90)#31+28+31
        self.assertEqual(returnValue['RealFinishDate'], '2023-04-06')
        self.assertEqual(returnValue['RealTotalCalendarDays'], 96)#31+28+31+6
        self.assertEqual(returnValue['FromStartCalendarDays'], 17)
        self.assertEqual(returnValue['FromStartWorkDays'], 11.5)
        self.assertEqual(returnValue['ExpectRestWorkDays'], 48.5)#60-11.5
        self.assertEqual(returnValue['ExpectRestCalendarkDays'], 73)#14+28+31
        self.assertEqual(returnValue['RealRestWorkDays'], 48.5)#60-11.5
        self.assertEqual(returnValue['RealRestCalendarkDays'], 79)#14+28+31+6
        
    def test_TwoDayOffRealFinishDate2(self):
        func_load_json_holiday_data(arrGlobalConstHoliday,arrGlobalConstWorkday)
        func_load_json_daily_report_data(dictGlobalWeatherRelatedHoliday)
        func_load_json_extend_data(dictGlobalExtendData)
        returnValue = func_count_real_finish_date(WorkDay.TWO_DAY_OFF, 60, '2023-01-01', '2023-01-18', arrGlobalConstHoliday, arrGlobalConstWorkday, dictGlobalWeatherRelatedHoliday, dictGlobalExtendData)
        self.assertEqual(returnValue['ExpectFinishDate'], '2023-03-31')
        self.assertEqual(returnValue['ExpectTotalCalendarDays'], 90)#31+28+31
        self.assertEqual(returnValue['RealFinishDate'], '2023-04-07')
        self.assertEqual(returnValue['RealTotalCalendarDays'], 97)#31+28+31+7
        self.assertEqual(returnValue['FromStartCalendarDays'], 18)
        self.assertEqual(returnValue['FromStartWorkDays'], 11.5)
        self.assertEqual(returnValue['ExpectRestWorkDays'], 48.5)#60-11.5
        self.assertEqual(returnValue['ExpectRestCalendarkDays'], 72)#13+28+31
        self.assertEqual(returnValue['RealRestWorkDays'], 48.5)#60-11.5
        self.assertEqual(returnValue['RealRestCalendarkDays'], 79)#13+28+31+7

    def test_TwoDayOffRealFinishDate3(self):
        func_load_json_holiday_data(arrGlobalConstHoliday,arrGlobalConstWorkday)
        func_load_json_daily_report_data(dictGlobalWeatherRelatedHoliday)
        func_load_json_extend_data(dictGlobalExtendData)
        returnValue = func_count_real_finish_date(WorkDay.TWO_DAY_OFF, 60, '2023-01-01', '2023-03-13', arrGlobalConstHoliday, arrGlobalConstWorkday, dictGlobalWeatherRelatedHoliday, dictGlobalExtendData)
        self.assertEqual(returnValue['ExpectFinishDate'], '2023-03-31')
        self.assertEqual(returnValue['ExpectTotalCalendarDays'], 90)#31+28+31
        self.assertEqual(returnValue['RealFinishDate'], '2023-04-12')
        self.assertEqual(returnValue['RealTotalCalendarDays'], 102)#31+28+31+12
        self.assertEqual(returnValue['FromStartCalendarDays'], 72)#31+28+13
        self.assertEqual(returnValue['FromStartWorkDays'], 40)
        self.assertEqual(returnValue['ExpectRestWorkDays'], 20)#60-40
        self.assertEqual(returnValue['ExpectRestCalendarkDays'], 18)# 0313~0331 
        self.assertEqual(returnValue['RealRestWorkDays'], 20)#60-40
        self.assertEqual(returnValue['RealRestCalendarkDays'], 30)#18+12

    def test_TwoDayOffRealFinishDate4(self):
        func_load_json_holiday_data(arrGlobalConstHoliday,arrGlobalConstWorkday)
        func_load_json_daily_report_data(dictGlobalWeatherRelatedHoliday)
        func_load_json_extend_data(dictGlobalExtendData)
        returnValue = func_count_real_finish_date(WorkDay.TWO_DAY_OFF, 60, '2023-01-01', '2023-03-14', arrGlobalConstHoliday, arrGlobalConstWorkday, dictGlobalWeatherRelatedHoliday, dictGlobalExtendData)
        self.assertEqual(returnValue['ExpectFinishDate'], '2023-03-31')
        self.assertEqual(returnValue['ExpectTotalCalendarDays'], 90)
        self.assertEqual(returnValue['RealFinishDate'], '2023-05-03')
        self.assertEqual(returnValue['RealTotalCalendarDays'], 123)
        self.assertEqual(returnValue['FromStartCalendarDays'], 73)#31+28+14
        self.assertEqual(returnValue['FromStartWorkDays'], 41)
        self.assertEqual(returnValue['ExpectRestWorkDays'], 19)#60-41
        self.assertEqual(returnValue['ExpectRestCalendarkDays'], 17)#0314~0331
        self.assertEqual(returnValue['RealRestWorkDays'], 34)#60+15-41
        self.assertEqual(returnValue['RealRestCalendarkDays'], 50)#0314~0503=17+30+3

if __name__ == '__main__':
    unittest.main()

# func_load_json_holiday_data(arrGlobalConstHoliday,arrGlobalConstWorkday)
# endDate = func_count_expect_finish_date('2023-01-01',0,60,arrGlobalConstHoliday,arrGlobalConstWorkday)

# func_load_json_daily_report_data(dictGlobalWeatherRelatedHoliday)
# CountFinishDate('2023-01-01',1,60,arrGlobalConstHoliday,arrGlobalConstWorkday,dictGlobalWeatherRelatedHoliday, '2023-01-17')

# print(jsonGlobalVariableHoliday)