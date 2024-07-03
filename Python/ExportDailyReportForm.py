import ScheduleCount
import Utility
import json
import os
import datetime
import unittest
import openpyxl
from openpyxl.drawing.image import Image
from openpyxl.drawing.xdr import XDRPoint2D, XDRPositiveSize2D
from openpyxl.utils.units import pixels_to_EMU, cm_to_EMU
from openpyxl.drawing.spreadsheet_drawing import OneCellAnchor, AnchorMarker

def func_fill_in_day_each_month(worksheet, input_year):
    first_day = str(input_year) + '-01-01'
    date_obj = datetime.datetime.strptime(first_day, "%Y-%m-%d")  
    is_leap_year = ( input_year % 4 == 0 )

    if is_leap_year:
        days_a_year = 366
    else:
        days_a_year = 365

    for i in range(days_a_year):
        day = date_obj.day
        str_date = date_obj.strftime("%Y-%m-%d")

        cell_num = func_get_cell_num(str_date)
        column = cell_num['ColumnNum']
        row = cell_num['RowNum']+1
        cell = Utility.number_to_string(column)+str(row)
        worksheet[cell] = day
        date_obj += datetime.timedelta(days=1)

def func_get_cell_num( date ):
    date_obj = datetime.datetime.strptime(date, "%Y-%m-%d")
    month = date_obj.month
    day = date_obj.day
    weekday = ( date_obj.weekday() + 2 ) % 7 
    if weekday == 0:
        weekday += 7
    row_num = 6 + month * 2
    week_num = func_get_week_num( date )
    column_num = 1 + ( week_num - 1 ) * 7 + weekday


    returnValue = {}
    returnValue['WeekNum'] = week_num
    returnValue['RowNum'] = row_num
    returnValue['ColumnNum'] = column_num
    returnValue['ColumnString'] = Utility.number_to_string( column_num )
    return returnValue

def func_get_week_num( date ):
    date_obj = datetime.datetime.strptime(date, "%Y-%m-%d")
    day = date_obj.day

    weekday = ( date_obj.weekday() + 2 ) % 7 
    if weekday == 0:
        weekday += 7
    week_num = (day - 1) // 7 + 1
    rest = day % 7
    if rest == 0:
        rest += 7
    if weekday - rest < 0:
        week_num += 1
    
    return week_num

def func_create_weather_report_form(eCountType, start_day, current_day):
    arr_const_holiday = []
    arr_const_workday = []
    ScheduleCount.func_load_json_holiday_data(arr_const_holiday,arr_const_workday)

    json_file_path = os.path.join( Utility.current_dir, 'ExternalData\\DailyReport.json')
    input_excel =  os.path.join( Utility.current_dir, 'ExternalData\\DailyReportTemplate.xlsx')
    output_excel = os.path.join( Utility.parent_dir, 'DailyReportFinal.xlsx') 


    c2e = cm_to_EMU
    # Calculated number of cells width or height from cm into EMUs
    cellh = lambda x: c2e((x * 49.77)/99)
    cellw = lambda x: c2e((x * (18.65-1.71))/10)

    col_offset = cellw(0.1) #60984
    row_up_offset = cellh(0.25) #45245
    row_down_offset = cellh(1) #180981

    p2e = pixels_to_EMU

    whole_size = XDRPositiveSize2D(p2e(30), p2e(30))
    half_size = XDRPositiveSize2D(p2e(30), p2e(15))

    workbook = openpyxl.load_workbook(input_excel)
    worksheet = workbook.active


    with open(json_file_path,'r', encoding='utf-8') as f:
        data = json.load(f)

    #先看有多少年的資料，建立所需worksheet
    lastyear = 0
    for item in data:
        date_obj = datetime.datetime.strptime(item["date"], "%Y-%m-%d")

        start_date_obj = datetime.datetime.strptime(start_day, "%Y-%m-%d")
        current_date_obj = datetime.datetime.strptime(current_day, "%Y-%m-%d")

        if date_obj < start_date_obj:
            continue

        if date_obj > current_date_obj:
            break

        year = date_obj.year
        
        if year != lastyear:
            if lastyear != 0:
                worksheet = workbook.copy_worksheet(worksheet)
            worksheet.title = str(year) + '年'
            worksheet['B4'] = str(year) + '年(' + str(year-1911) + '年)' 

            lastyear = year

    worksheet_index = 0
    lastyear = 0

    for item in data:
        date_obj = datetime.datetime.strptime(item["date"], "%Y-%m-%d")
        start_date_obj = datetime.datetime.strptime(start_day, "%Y-%m-%d")
        current_date_obj = datetime.datetime.strptime(current_day, "%Y-%m-%d")
        if date_obj < start_date_obj:
            continue

        if date_obj > current_date_obj:
            break

        nWeekday = date_obj.weekday()
        year = date_obj.year
        cell_num = func_get_cell_num(item["date"])
        column = cell_num['ColumnNum']-1
        row = cell_num['RowNum']-1
        up_marker = AnchorMarker(col=column, colOff=col_offset, row=row, rowOff=row_up_offset)
        down_marker = AnchorMarker(col=column, colOff=col_offset, row=row, rowOff=row_down_offset)

        if year != lastyear:
            worksheet = workbook.worksheets[worksheet_index]
            func_fill_in_day_each_month(worksheet, year)
            lastyear = year
            worksheet_index += 1
    
        print( item["date"])
        if item["morning_weather"] == 0:#晴天
            Utility.insert_image( worksheet, Utility.image_path_sun_up, up_marker, half_size)
        elif item["morning_weather"] == 1:#雨天
            Utility.insert_image( worksheet, Utility.image_path_rain_up, up_marker, half_size)
        elif item["morning_weather"] == 2:#豪雨
            Utility.insert_image( worksheet, Utility.image_path_heavyrain_up, up_marker, half_size)
        elif item["morning_weather"] == 3:#颱風
            Utility.insert_image( worksheet, Utility.image_path_typhoon_up, up_marker, half_size)
        elif item["morning_weather"] == 4:#酷熱
            Utility.insert_image( worksheet, Utility.image_path_hot_up, up_marker, half_size)

        if item["afternoon_weather"] == 0:#晴天
            Utility.insert_image( worksheet, Utility.image_path_sun_down, down_marker, half_size)
        elif item["afternoon_weather"] == 1:#雨天
            Utility.insert_image( worksheet, Utility.image_path_rain_down, down_marker, half_size)
        elif item["afternoon_weather"] == 2:#豪雨
            Utility.insert_image( worksheet, Utility.image_path_heavyrain_down, down_marker, half_size)
        elif item["afternoon_weather"] == 3:#颱風
            Utility.insert_image( worksheet, Utility.image_path_typhoon_down, down_marker, half_size)
        elif item["afternoon_weather"] == 4:#酷熱
            Utility.insert_image( worksheet, Utility.image_path_hot_down, down_marker, half_size)


        if eCountType == ScheduleCount.WorkDay.ONE_DAY_OFF:
            if nWeekday == 6:#Sunday
                if item["date"] in arr_const_workday:
                    Utility.insert_image( worksheet, Utility.image_path_workday, up_marker, whole_size)
                else:
                    Utility.insert_image( worksheet, Utility.image_path_holiday, up_marker, whole_size)
            else:
                if item["date"] in arr_const_holiday:
                    Utility.insert_image( worksheet, Utility.image_path_holiday, up_marker, whole_size)
        elif eCountType == ScheduleCount.WorkDay.TWO_DAY_OFF:
            if nWeekday == 6 or nWeekday == 5:#Sunday Saturday
                if item["date"] in arr_const_workday:
                    Utility.insert_image( worksheet, Utility.image_path_workday, up_marker, whole_size)
                else:
                    Utility.insert_image( worksheet, Utility.image_path_holiday, up_marker, whole_size)
            else:
                if item["date"] in arr_const_holiday:
                    Utility.insert_image( worksheet, Utility.image_path_holiday, up_marker, whole_size)
        elif eCountType == ScheduleCount.WorkDay.NO_DAY_OFF:
            if item["date"] in arr_const_holiday:
                    Utility.insert_image( worksheet, Utility.image_path_holiday, up_marker, whole_size)


    worksheet = workbook.worksheets[0]
    cell_num = func_get_cell_num(start_day)
    column = cell_num['ColumnNum']-1
    row = cell_num['RowNum']-1
    up_marker = AnchorMarker(col=column, colOff=col_offset, row=row, rowOff=row_up_offset)
    Utility.insert_image( worksheet, Utility.image_path_start_day, up_marker, whole_size)

    any_serial_num = False
    serial_number = 1
    filename, extension = os.path.splitext(output_excel)
    while os.path.exists(output_excel):
        # 如果文件已经存在，则添加流水号并重新检查
        output_excel = f"{filename}_{serial_number}{extension}"
        serial_number += 1
        any_serial_num = True

    # serial_number = 1
    # filename, extension = os.path.splitext(output_pdf)
    # while os.path.exists(output_pdf):
    #     # 如果文件已经存在，则添加流水号并重新检查
    #     output_pdf = f"{filename}_{serial_number}{extension}"
    #     serial_number += 1
    if any_serial_num:
        serial_number -= 1
        output_pdf = f"{filename}_{serial_number}{'.pdf'}"
    else:
        output_pdf = f"{filename}{'.pdf'}"
    workbook.save( output_excel )
    Utility.excel_to_pdf( output_excel, output_pdf )
    print('finish')
    pass





# func_create_weather_report_form(ScheduleCount.WorkDay.TWO_DAY_OFF, '2023-02-10', '2023-04-16' )

class TestFunction(unittest.TestCase):
    def test_week_number_1(self):
        returnValue = func_get_cell_num('2024-02-14')
        self.assertEqual(returnValue['WeekNum'], 3)
        self.assertEqual(returnValue['RowNum'], 10)
        self.assertEqual(returnValue['ColumnNum'], 19)
        self.assertEqual(returnValue['ColumnString'], 'S')

        returnValue = func_get_cell_num('2024-03-09')
        self.assertEqual(returnValue['WeekNum'], 2)
        self.assertEqual(returnValue['RowNum'], 12)
        self.assertEqual(returnValue['ColumnNum'], 15)
        self.assertEqual(returnValue['ColumnString'], 'O')

        returnValue = func_get_cell_num('2024-03-10')
        self.assertEqual(returnValue['WeekNum'], 3)
        self.assertEqual(returnValue['RowNum'], 12)
        self.assertEqual(returnValue['ColumnNum'], 16)
        self.assertEqual(returnValue['ColumnString'], 'P')

        returnValue = func_get_cell_num('2024-03-31')
        self.assertEqual(returnValue['WeekNum'], 6)
        self.assertEqual(returnValue['RowNum'], 12)
        self.assertEqual(returnValue['ColumnNum'], 37)
        self.assertEqual(returnValue['ColumnString'], 'AK')

        returnValue = func_get_cell_num('2024-04-06')
        self.assertEqual(returnValue['WeekNum'], 1)
        self.assertEqual(returnValue['RowNum'], 14)
        self.assertEqual(returnValue['ColumnNum'], 8)
        self.assertEqual(returnValue['ColumnString'], 'H')

        returnValue = func_get_cell_num('2024-04-07')
        self.assertEqual(returnValue['WeekNum'], 2)
        self.assertEqual(returnValue['RowNum'], 14)
        self.assertEqual(returnValue['ColumnNum'], 9)
        self.assertEqual(returnValue['ColumnString'], 'I')

        returnValue = func_get_cell_num('2024-06-30')
        self.assertEqual(returnValue['WeekNum'], 6)
        self.assertEqual(returnValue['RowNum'], 18)
        self.assertEqual(returnValue['ColumnNum'], 37)
        self.assertEqual(returnValue['ColumnString'], 'AK')

        returnValue = func_get_cell_num('2024-09-07')
        self.assertEqual(returnValue['WeekNum'], 1)
        self.assertEqual(returnValue['RowNum'], 24)
        self.assertEqual(returnValue['ColumnNum'], 8)
        self.assertEqual(returnValue['ColumnString'], 'H')
        
        returnValue = func_get_cell_num('2024-09-14')
        self.assertEqual(returnValue['WeekNum'], 2)
        self.assertEqual(returnValue['RowNum'], 24)
        self.assertEqual(returnValue['ColumnNum'], 15)
        self.assertEqual(returnValue['ColumnString'], 'O')

# if __name__ == '__main__':
#     unittest.main()