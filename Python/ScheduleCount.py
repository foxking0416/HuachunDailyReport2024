import json
import os
import datetime

arrGlobalConstHoliday = []
arrGlobalConstWorkday = []


# 從 Holiday.json 的檔案讀取補班或放假的資料
def LoadPythonHolidayData(arrConstHoliday, arrConstWorkday):
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




# kStartDate 開工日字串，如 '2023-01-01'
# nCountType 工期計算方式 0:周休一日  1:周休二日  2:日曆天
# nTotalDay 工期天數
# arrConstHoliday 固定因素放假日
# arrConstWorkday 固定因素補班日
def CountFinishDate(strStart, nCountType, nTotalDay, arrConstHoliday, arrConstWorkday):
    print('Start Date : ' + strStart)
    kEndDate = datetime.datetime.strptime(strStart, "%Y-%m-%d")
    
    while(nTotalDay > 1):
        kWeekday = kEndDate.weekday()
        strEndDate = kEndDate.strftime("%Y-%m-%d")

        if(strEndDate in arrConstHoliday):
            # print(strEndDate + ' 是放假日' )
            pass
        elif(strEndDate in arrConstWorkday):
            # print(strEndDate + ' 是補班日' )
            nTotalDay -= 1
        else:
            if nCountType == 0 and kWeekday != 6:
                nTotalDay -= 1
            elif nCountType == 1 and kWeekday != 5 and kWeekday != 6:
                nTotalDay -= 1
            elif nCountType == 2:
                nTotalDay -= 1

        kEndDate += datetime.timedelta(days=1)
    print('End Date : ' + kEndDate.strftime("%Y-%m-%d"))


LoadPythonHolidayData(arrGlobalConstHoliday,arrGlobalConstWorkday)
CountFinishDate('2023-01-01',0,60,arrGlobalConstHoliday,arrGlobalConstWorkday)
CountFinishDate('2023-01-01',1,60,arrGlobalConstHoliday,arrGlobalConstWorkday)