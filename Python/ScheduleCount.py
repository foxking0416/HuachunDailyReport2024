import json
import os
import datetime
import unittest

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
            dictVariableHoliday[date] = 2
        elif(item["afternoon_weather"] != 0 or item["afternoon_other"] != 0 ):
            dictVariableHoliday[date] = 1
    

# kStartDate 開工日字串，如 '2023-01-01'
# nCountType 工期計算方式 0:周休一日  1:周休二日  2:日曆天
# nTotalRestDay 工期天數
# arrConstHoliday 固定因素放假日
# arrConstWorkday 固定因素補班日
def CountFinishDate(strStart, nCountType, nTotalRestDay, arrConstHoliday, arrConstWorkday, dictVariableHoliday, strToday):
    kEndDate = datetime.datetime.strptime(strStart, "%Y-%m-%d")
    kTodayDate = datetime.datetime.strptime(strToday, "%Y-%m-%d")
    
    while(True):
        kWeekday = kEndDate.weekday()
        strEndDate = kEndDate.strftime("%Y-%m-%d")

        isWorkDay = False
        if strEndDate in arrConstHoliday :
            pass
        elif strEndDate in arrConstWorkday:
            isWorkDay = True
        else:
            if nCountType == 0 and kWeekday != 6:
                isWorkDay = True
            elif nCountType == 1 and kWeekday != 5 and kWeekday != 6:
                isWorkDay = True
            elif nCountType == 2:
                isWorkDay = True

        if isWorkDay:
            if kEndDate <= kTodayDate:
                if strEndDate in dictVariableHoliday:
                    if dictVariableHoliday[strEndDate] == 2:#全日不計工期
                        pass
                    elif dictVariableHoliday[strEndDate] == 1:#下午不計工期
                        nTotalRestDay -= 0.5
                    else:
                        nTotalRestDay -= 1
                else:
                    nTotalRestDay -= 1#沒填日報表就當作一般晴天
            else:
                nTotalRestDay -= 1#未來的日子還沒有日報表

        if(nTotalRestDay <= 0):
            break

        kEndDate += datetime.timedelta(days=1)
    # print('End Date : ' + kEndDate.strftime("%Y-%m-%d"))
    return kEndDate.strftime("%Y-%m-%d")


class TestFunction(unittest.TestCase):
    
    # 測試函數的測試用例
    def test_OneDayOffExpectFinishDate1(self):
        LoadJsonHolidayData(arrGlobalConstHoliday,arrGlobalConstWorkday)
        endDate = CountFinishDate('2023-01-01', 0, 1, arrGlobalConstHoliday, arrGlobalConstWorkday, dictGlobalVariableHoliday, '2023-01-01')
        self.assertEqual(endDate, '2023-01-03')

    def test_OneDayOffExpectFinishDate2(self):
        LoadJsonHolidayData(arrGlobalConstHoliday,arrGlobalConstWorkday)
        endDate = CountFinishDate('2023-01-01', 0, 60, arrGlobalConstHoliday, arrGlobalConstWorkday, dictGlobalVariableHoliday, '2023-01-01')
        self.assertEqual(endDate, '2023-03-25')
        
    def test_TwoDayOffExpectFinishDate(self):
        LoadJsonHolidayData(arrGlobalConstHoliday,arrGlobalConstWorkday)
        endDate = CountFinishDate('2023-01-01', 1, 60, arrGlobalConstHoliday, arrGlobalConstWorkday, dictGlobalVariableHoliday, '2023-01-01')
        self.assertEqual(endDate, '2023-03-31')

    def test_TwoDayOffRealFinishDate(self):
        LoadJsonHolidayData(arrGlobalConstHoliday,arrGlobalConstWorkday)
        LoadJsonDailyReportData(dictGlobalVariableHoliday)
        endDate = CountFinishDate('2023-01-01', 1, 60, arrGlobalConstHoliday, arrGlobalConstWorkday, dictGlobalVariableHoliday, '2023-01-17')
        self.assertEqual(endDate, '2023-04-06')

    def test_TwoDayOffRealFinishDate2(self):
        LoadJsonHolidayData(arrGlobalConstHoliday,arrGlobalConstWorkday)
        LoadJsonDailyReportData(dictGlobalVariableHoliday)
        endDate = CountFinishDate('2023-01-01', 1, 60, arrGlobalConstHoliday, arrGlobalConstWorkday, dictGlobalVariableHoliday, '2023-01-18')
        self.assertEqual(endDate, '2023-04-07')

if __name__ == '__main__':
    unittest.main()

# LoadJsonHolidayData(arrGlobalConstHoliday,arrGlobalConstWorkday)
# endDate = CountExpectFinishDate('2023-01-01',0,60,arrGlobalConstHoliday,arrGlobalConstWorkday)

# LoadJsonDailyReportData(dictGlobalVariableHoliday)
# CountFinishDate('2023-01-01',1,60,arrGlobalConstHoliday,arrGlobalConstWorkday,dictGlobalVariableHoliday, '2023-01-17')

# print(jsonGlobalVariableHoliday)