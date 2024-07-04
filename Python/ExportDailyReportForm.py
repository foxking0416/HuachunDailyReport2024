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

def func_fill_in_day_each_month( worksheet, input_year ):
    first_day = str( input_year ) + '-01-01'
    date_obj = datetime.datetime.strptime( first_day, "%Y-%m-%d" )  
    b_is_leap_year = ( input_year % 4 == 0 )

    if b_is_leap_year:
        days_a_year = 366
    else:
        days_a_year = 365

    for i in range( days_a_year ):
        day = date_obj.day

        cell_num = func_get_cell_num(date_obj)
        column = cell_num['ColumnNum']
        row = cell_num['RowNum']+1
        cell = Utility.number_to_string(column)+str(row)
        worksheet[cell] = day
        date_obj += datetime.timedelta(days=1)

def func_get_cell_num( obj_date ):
    month = obj_date.month
    weekday = ( obj_date.weekday() + 2 ) % 7 
    if weekday == 0:
        weekday += 7
    row_num = 6 + month * 2
    week_num = func_get_week_num( obj_date )
    column_num = 1 + ( week_num - 1 ) * 7 + weekday


    returnValue = {}
    returnValue['WeekNum'] = week_num
    returnValue['RowNum'] = row_num
    returnValue['ColumnNum'] = column_num
    returnValue['ColumnString'] = Utility.number_to_string( column_num )
    return returnValue

def func_get_week_num( obj_date ):
    day = obj_date.day

    weekday = ( obj_date.weekday() + 2 ) % 7 
    if weekday == 0:
        weekday += 7
    week_num = (day - 1) // 7 + 1
    rest = day % 7
    if rest == 0:
        rest += 7
    if weekday - rest < 0:
        week_num += 1
    
    return week_num

def func_find_weather_data_by_date( weather_report_date, obj_date ):        
    for entry in weather_report_date:
        if entry["date"] == obj_date.strftime("%Y-%m-%d"):
            return entry
    return None

def func_create_weather_report_form( e_count_type, n_expect_total_workdays, obj_start_date, obj_current_date ):
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

    arr_const_holiday = []
    arr_const_workday = []
    ScheduleCount.func_load_json_holiday_data( arr_const_holiday,arr_const_workday )

    dict_weather_related_holiday = {}
    ScheduleCount.func_load_json_daily_report_data( dict_weather_related_holiday )
    dict_extend_data = {}
    ScheduleCount.func_load_json_extend_data( dict_extend_data )
    obj_real_finish_date = ScheduleCount.func_count_real_finish_date( e_count_type, n_expect_total_workdays, obj_start_date, obj_current_date, arr_const_holiday, arr_const_workday, dict_weather_related_holiday, dict_extend_data )

    n_start_year = obj_start_date.year
    n_end_year = obj_real_finish_date['RealFinishDate'].year
    #先看有多少年的資料，建立所需worksheet
    for n_year in range( n_start_year, n_end_year + 1 ):
        if n_year != n_start_year:
            worksheet = workbook.copy_worksheet( worksheet )
        worksheet.title = str(n_year) + '年'
        worksheet['B4'] = str(n_year) + '年(' + str( n_year - 1911 ) + '年)' 

    with open(json_file_path,'r', encoding='utf-8') as f:
        data = json.load(f)

    n_lastyear = 0
    worksheet_index = 0

    obj_date = obj_start_date
    while( True ):
        weather_data = func_find_weather_data_by_date( data, obj_date )
        nWeekday = obj_date.weekday()
        year = obj_date.year
        cell_num = func_get_cell_num( obj_date )
        column = cell_num['ColumnNum']-1
        row = cell_num['RowNum']-1
        up_marker = AnchorMarker( col=column, colOff=col_offset, row=row, rowOff=row_up_offset )
        down_marker = AnchorMarker( col=column, colOff=col_offset, row=row, rowOff=row_down_offset )

        if year != n_lastyear:
            worksheet = workbook.worksheets[ worksheet_index ]
            func_fill_in_day_each_month( worksheet, year )
            n_lastyear = year
            worksheet_index += 1

        if weather_data and obj_date <= obj_current_date:
            if weather_data["morning_weather"] == 0:#晴天
                Utility.insert_image( worksheet, Utility.image_path_sun_up, up_marker, half_size )
            elif weather_data["morning_weather"] == 1:#雨天
                Utility.insert_image( worksheet, Utility.image_path_rain_up, up_marker, half_size )
            elif weather_data["morning_weather"] == 2:#豪雨
                Utility.insert_image( worksheet, Utility.image_path_heavyrain_up, up_marker, half_size )
            elif weather_data["morning_weather"] == 3:#颱風
                Utility.insert_image( worksheet, Utility.image_path_typhoon_up, up_marker, half_size )
            elif weather_data["morning_weather"] == 4:#酷熱
                Utility.insert_image( worksheet, Utility.image_path_hot_up, up_marker, half_size )

            if weather_data["afternoon_weather"] == 0:#晴天
                Utility.insert_image( worksheet, Utility.image_path_sun_down, down_marker, half_size )
            elif weather_data["afternoon_weather"] == 1:#雨天
                Utility.insert_image( worksheet, Utility.image_path_rain_down, down_marker, half_size )
            elif weather_data["afternoon_weather"] == 2:#豪雨
                Utility.insert_image( worksheet, Utility.image_path_heavyrain_down, down_marker, half_size )
            elif weather_data["afternoon_weather"] == 3:#颱風
                Utility.insert_image( worksheet, Utility.image_path_typhoon_down, down_marker, half_size )
            elif weather_data["afternoon_weather"] == 4:#酷熱
                Utility.insert_image( worksheet, Utility.image_path_hot_down, down_marker, half_size )

        if e_count_type == ScheduleCount.WorkDay.ONE_DAY_OFF:
            if nWeekday == 6:#Sunday
                if obj_date in arr_const_workday:
                    Utility.insert_image( worksheet, Utility.image_path_workday, up_marker, whole_size )
                else:
                    Utility.insert_image( worksheet, Utility.image_path_holiday, up_marker, whole_size )
            else:
                if obj_date in arr_const_holiday:
                    Utility.insert_image( worksheet, Utility.image_path_holiday, up_marker, whole_size )
        elif e_count_type == ScheduleCount.WorkDay.TWO_DAY_OFF:
            if nWeekday == 6 or nWeekday == 5:#Sunday Saturday
                if obj_date in arr_const_workday:
                    Utility.insert_image( worksheet, Utility.image_path_workday, up_marker, whole_size )
                else:
                    Utility.insert_image( worksheet, Utility.image_path_holiday, up_marker, whole_size )
            else:
                if obj_date in arr_const_holiday:
                    Utility.insert_image( worksheet, Utility.image_path_holiday, up_marker, whole_size )
        elif e_count_type == ScheduleCount.WorkDay.NO_DAY_OFF:
            if obj_date in arr_const_holiday:
                    Utility.insert_image( worksheet, Utility.image_path_holiday, up_marker, whole_size )

        if obj_date == obj_real_finish_date['ExpectFinishDate']:
            Utility.insert_image( worksheet, Utility.image_path_expect_finish_day, up_marker, whole_size )

        if obj_date == obj_real_finish_date['RealFinishDate']:
            Utility.insert_image( worksheet, Utility.image_path_real_finish_day, up_marker, whole_size )
            break

        obj_date += datetime.timedelta(days=1)

    worksheet = workbook.worksheets[0]
    cell_num = func_get_cell_num( obj_start_date )
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


# func_create_weather_report_form(ScheduleCount.WorkDay.TWO_DAY_OFF, 30, datetime.datetime.strptime('2023-01-03', "%Y-%m-%d"), datetime.datetime.strptime('2023-01-16', "%Y-%m-%d") )
