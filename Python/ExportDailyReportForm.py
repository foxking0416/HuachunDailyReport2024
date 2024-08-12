import ScheduleCount
import Utility
import LunarCalendar
import json
import os
import datetime
import openpyxl
from openpyxl.drawing.spreadsheet_drawing import AnchorMarker

g_DailyReportType = Utility.DailyReportType.TYPE_A

g_project_no = "Avenger001" #案號
g_project_name = "鋼鐵人的基地興建工程" #工程名稱
g_project_owner = "神盾局" #業主
g_project_supervisor = "復仇者聯盟" #監造單位
g_project_designer = "東尼史塔克" #設計單位
g_project_contractor = "賈維斯" #承攬廠商 


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

        obj_cell_num = func_get_cell_num( date_obj )
        column = obj_cell_num['ColumnNum']
        if g_DailyReportType == Utility.DailyReportType.TYPE_A:
            n_column_for_image = obj_cell_num['ColumnNum']-1
            n_row_for_image = obj_cell_num['RowNum']-1
            up_marker = AnchorMarker( col=n_column_for_image, colOff=Utility.col_offset, row=n_row_for_image, rowOff=Utility.row_up_offset )
            if day == 1:
                Utility.insert_image( worksheet, Utility.image_path_day_01, up_marker, Utility.whole_size )
            elif day == 2:
                Utility.insert_image( worksheet, Utility.image_path_day_02, up_marker, Utility.whole_size )
            elif day == 3:
                Utility.insert_image( worksheet, Utility.image_path_day_03, up_marker, Utility.whole_size )
            elif day == 4:
                Utility.insert_image( worksheet, Utility.image_path_day_04, up_marker, Utility.whole_size )
            elif day == 5:
                Utility.insert_image( worksheet, Utility.image_path_day_05, up_marker, Utility.whole_size )
            elif day == 6:
                Utility.insert_image( worksheet, Utility.image_path_day_06, up_marker, Utility.whole_size )
            elif day == 7:
                Utility.insert_image( worksheet, Utility.image_path_day_07, up_marker, Utility.whole_size )
            elif day == 8:
                Utility.insert_image( worksheet, Utility.image_path_day_08, up_marker, Utility.whole_size )
            elif day == 9:
                Utility.insert_image( worksheet, Utility.image_path_day_09, up_marker, Utility.whole_size )
            elif day == 10:
                Utility.insert_image( worksheet, Utility.image_path_day_10, up_marker, Utility.whole_size )
            elif day == 11:
                Utility.insert_image( worksheet, Utility.image_path_day_11, up_marker, Utility.whole_size )
            elif day == 12:
                Utility.insert_image( worksheet, Utility.image_path_day_12, up_marker, Utility.whole_size )
            elif day == 13:
                Utility.insert_image( worksheet, Utility.image_path_day_13, up_marker, Utility.whole_size )
            elif day == 14:
                Utility.insert_image( worksheet, Utility.image_path_day_14, up_marker, Utility.whole_size )
            elif day == 15:
                Utility.insert_image( worksheet, Utility.image_path_day_15, up_marker, Utility.whole_size )
            elif day == 16:
                Utility.insert_image( worksheet, Utility.image_path_day_16, up_marker, Utility.whole_size )
            elif day == 17:
                Utility.insert_image( worksheet, Utility.image_path_day_17, up_marker, Utility.whole_size )
            elif day == 18:
                Utility.insert_image( worksheet, Utility.image_path_day_18, up_marker, Utility.whole_size )
            elif day == 19:
                Utility.insert_image( worksheet, Utility.image_path_day_19, up_marker, Utility.whole_size )
            elif day == 20:
                Utility.insert_image( worksheet, Utility.image_path_day_20, up_marker, Utility.whole_size )
            elif day == 21:
                Utility.insert_image( worksheet, Utility.image_path_day_21, up_marker, Utility.whole_size )
            elif day == 22:
                Utility.insert_image( worksheet, Utility.image_path_day_22, up_marker, Utility.whole_size )
            elif day == 23:
                Utility.insert_image( worksheet, Utility.image_path_day_23, up_marker, Utility.whole_size )
            elif day == 24:
                Utility.insert_image( worksheet, Utility.image_path_day_24, up_marker, Utility.whole_size )
            elif day == 25:
                Utility.insert_image( worksheet, Utility.image_path_day_25, up_marker, Utility.whole_size )
            elif day == 26:
                Utility.insert_image( worksheet, Utility.image_path_day_26, up_marker, Utility.whole_size )
            elif day == 27:
                Utility.insert_image( worksheet, Utility.image_path_day_27, up_marker, Utility.whole_size )            
            elif day == 28:
                Utility.insert_image( worksheet, Utility.image_path_day_28, up_marker, Utility.whole_size )
            elif day == 29:
                Utility.insert_image( worksheet, Utility.image_path_day_29, up_marker, Utility.whole_size )
            elif day == 30:
                Utility.insert_image( worksheet, Utility.image_path_day_30, up_marker, Utility.whole_size )
            elif day == 31:
                Utility.insert_image( worksheet, Utility.image_path_day_31, up_marker, Utility.whole_size )        
        elif g_DailyReportType == Utility.DailyReportType.TYPE_B:
            row = obj_cell_num['RowNum'] + 1
            cell = Utility.number_to_string(column)+str(row)
            worksheet[cell] = day

        date_obj += datetime.timedelta(days=1)

def func_get_cell_num( obj_date ):
    month = obj_date.month
    weekday = ( obj_date.weekday() + 2 ) % 7 
    if weekday == 0:
        weekday += 7

    row_num = None
    if g_DailyReportType == Utility.DailyReportType.TYPE_A:
        row_num = 5 + month * 3
    elif g_DailyReportType == Utility.DailyReportType.TYPE_B:
        row_num = 4 + month * 4
    
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
    LunarCalendar.func_load_lunar_holiday_data()
    json_file_path = os.path.join( Utility.current_dir, 'ExternalData\\DailyReport.json')
    input_excel =  None
    if g_DailyReportType == Utility.DailyReportType.TYPE_A:
        input_excel =  os.path.join( Utility.current_dir, 'ExternalData\\DailyReportTemplateWithLunar_A.xlsx')
    elif g_DailyReportType == Utility.DailyReportType.TYPE_B:
        input_excel =  os.path.join( Utility.current_dir, 'ExternalData\\DailyReportTemplateWithLunar_B.xlsx')
    output_excel = os.path.join( Utility.parent_dir, 'DailyReportFinal.xlsx') 

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
        worksheet['D2'] = g_project_no
        worksheet['AP2'] = g_project_no
        worksheet['D3'] = g_project_name
        worksheet['AP3'] = g_project_name
        worksheet['V2'] = g_project_owner
        worksheet['BD2'] = g_project_owner
        worksheet['V3'] = g_project_supervisor
        worksheet['BD3'] = g_project_supervisor
        worksheet['AF2'] = g_project_designer
        worksheet['BM2'] = g_project_designer
        worksheet['AF3'] = g_project_contractor
        worksheet['BM3'] = g_project_contractor

    with open(json_file_path,'r', encoding='utf-8') as f:
        data = json.load(f)
    #TODO 可以把json檔案做排序

    obj_date = obj_start_date
    n_workdays_from_start = 0

    n_calendar_days_each_month = 0
    n_calendar_days_accumulate = 0
    last_month = 0
    last_year = 0
    worksheet_index = -1


    while( True ):
        weather_data = func_find_weather_data_by_date( data, obj_date )
        n_Weekday = obj_date.weekday()
        year = obj_date.year
        if year != last_year:
            worksheet_index += 1
            last_year = year
        worksheet = workbook.worksheets[ worksheet_index ]
        month = obj_date.month

        str_cell_calendar_days_each_month = None
        str_cell_calendar_days_accumulate = None
        if g_DailyReportType == Utility.DailyReportType.TYPE_A:
            str_cell_calendar_days_each_month = 'AM' + str( 5 + month * 3 )
            str_cell_calendar_days_accumulate = 'AM' + str( 6 + month * 3 )
        elif g_DailyReportType == Utility.DailyReportType.TYPE_B:
            str_cell_calendar_days_each_month = 'AM' + str( 4 + month * 4 )
            str_cell_calendar_days_accumulate = 'AM' + str( 5 + month * 4 )

        obj_date_add_1 = obj_date + datetime.timedelta(days=1)
        n_calendar_days_each_month += 1
        n_calendar_days_accumulate += 1
        if obj_date.month != obj_date_add_1.month:
            worksheet[ str_cell_calendar_days_each_month ] = n_calendar_days_each_month
            worksheet[ str_cell_calendar_days_accumulate ] = n_calendar_days_accumulate
            n_calendar_days_each_month = 0

        obj_cell_num = func_get_cell_num( obj_date )
        n_column_for_image = obj_cell_num['ColumnNum']-1
        n_row_for_image = obj_cell_num['RowNum']-1
        up_marker = AnchorMarker( col=n_column_for_image, colOff=Utility.col_offset, row=n_row_for_image, rowOff=Utility.row_up_offset )
        down_marker = AnchorMarker( col=n_column_for_image, colOff=Utility.col_offset, row=n_row_for_image, rowOff=Utility.row_down_offset )

        n_column_for_text = obj_cell_num['ColumnNum']#跟上面的 obj_cell_num['ColumnNum']-1 其實是指向同一個column，只是因為一個是貼圖的AnchorMarker，一個是cell要使用的，兩個api的基準值不一樣

        str_lunar_reason = LunarCalendar.func_get_lunar_reason( obj_date )
        if str_lunar_reason != None:
            if g_DailyReportType == Utility.DailyReportType.TYPE_A:
                n_row_for_note = obj_cell_num['RowNum'] + 1
            elif  g_DailyReportType == Utility.DailyReportType.TYPE_B:
                n_row_for_note = obj_cell_num['RowNum'] + 2
            cell_note = Utility.number_to_string( n_column_for_text ) + str( n_row_for_note )
            worksheet[ cell_note ] = str_lunar_reason

        if g_DailyReportType == Utility.DailyReportType.TYPE_A:
            n_row_workdays_from_start = obj_cell_num['RowNum'] + 2
        elif  g_DailyReportType == Utility.DailyReportType.TYPE_B:
            n_row_workdays_from_start = obj_cell_num['RowNum'] + 3

        cell_workdays_from_start = Utility.number_to_string( n_column_for_text ) + str( n_row_workdays_from_start )

        if ScheduleCount.func_check_is_work_day( arr_const_holiday, arr_const_workday, obj_date, n_Weekday, e_count_type ):
            if weather_data and obj_date <= obj_current_date:
                if obj_date in dict_weather_related_holiday:
                    if dict_weather_related_holiday[ obj_date ] == ScheduleCount.CountWorkingDay.NO_COUNT:
                        pass
                    elif dict_weather_related_holiday[ obj_date ] == ScheduleCount.CountWorkingDay.COUNT_HALF_DAY:
                        n_workdays_from_start += 0.5
                    else:
                        n_workdays_from_start += 1
                else:
                    n_workdays_from_start += 1
            else:
                n_workdays_from_start += 1

        worksheet[ cell_workdays_from_start ] = n_workdays_from_start

        if weather_data and obj_date <= obj_current_date:
            if weather_data["morning_weather"] == 0:#晴天
                Utility.insert_image( worksheet, Utility.image_path_sun_up, up_marker, Utility.half_size )
            elif weather_data["morning_weather"] == 1:#雨天
                Utility.insert_image( worksheet, Utility.image_path_rain_up, up_marker, Utility.half_size )
            elif weather_data["morning_weather"] == 2:#豪雨
                Utility.insert_image( worksheet, Utility.image_path_heavyrain_up, up_marker, Utility.half_size )
            elif weather_data["morning_weather"] == 3:#颱風
                Utility.insert_image( worksheet, Utility.image_path_typhoon_up, up_marker, Utility.half_size )
            elif weather_data["morning_weather"] == 4:#酷熱
                Utility.insert_image( worksheet, Utility.image_path_hot_up, up_marker, Utility.half_size )

            if weather_data["afternoon_weather"] == 0:#晴天
                Utility.insert_image( worksheet, Utility.image_path_sun_down, down_marker, Utility.half_size )
            elif weather_data["afternoon_weather"] == 1:#雨天
                Utility.insert_image( worksheet, Utility.image_path_rain_down, down_marker, Utility.half_size )
            elif weather_data["afternoon_weather"] == 2:#豪雨
                Utility.insert_image( worksheet, Utility.image_path_heavyrain_down, down_marker, Utility.half_size )
            elif weather_data["afternoon_weather"] == 3:#颱風
                Utility.insert_image( worksheet, Utility.image_path_typhoon_down, down_marker, Utility.half_size )
            elif weather_data["afternoon_weather"] == 4:#酷熱
                Utility.insert_image( worksheet, Utility.image_path_hot_down, down_marker, Utility.half_size )

        if e_count_type == ScheduleCount.WorkDay.ONE_DAY_OFF:
            if n_Weekday == 6:#Sunday
                if obj_date in arr_const_workday:
                    Utility.insert_image( worksheet, Utility.image_path_workday, up_marker, Utility.whole_size )
                else:
                    Utility.insert_image( worksheet, Utility.image_path_holiday, up_marker, Utility.whole_size )
            else:
                if obj_date in arr_const_holiday:
                    Utility.insert_image( worksheet, Utility.image_path_holiday, up_marker, Utility.whole_size )
        elif e_count_type == ScheduleCount.WorkDay.TWO_DAY_OFF:
            if n_Weekday == 6 or n_Weekday == 5:#Sunday Saturday
                if obj_date in arr_const_workday:
                    Utility.insert_image( worksheet, Utility.image_path_workday, up_marker, Utility.whole_size )
                else:
                    Utility.insert_image( worksheet, Utility.image_path_holiday, up_marker, Utility.whole_size )
            else:
                if obj_date in arr_const_holiday:
                    Utility.insert_image( worksheet, Utility.image_path_holiday, up_marker, Utility.whole_size )
        elif e_count_type == ScheduleCount.WorkDay.NO_DAY_OFF:
            if obj_date in arr_const_holiday:
                    Utility.insert_image( worksheet, Utility.image_path_holiday, up_marker, Utility.whole_size )

        if obj_date == obj_real_finish_date['ExpectFinishDate']:
            Utility.insert_image( worksheet, Utility.image_path_expect_finish_day, up_marker, Utility.whole_size )

        if obj_date == obj_real_finish_date['RealFinishDate']:
            Utility.insert_image( worksheet, Utility.image_path_real_finish_day, up_marker, Utility.whole_size )
            if n_calendar_days_each_month != 0:
                worksheet[ str_cell_calendar_days_each_month ] = n_calendar_days_each_month
            worksheet[ str_cell_calendar_days_accumulate ] = n_calendar_days_accumulate
            break

        obj_date += datetime.timedelta(days=1)


    worksheet = workbook.worksheets[0]
    obj_cell_num = func_get_cell_num( obj_start_date )
    column = obj_cell_num['ColumnNum']-1
    row = obj_cell_num['RowNum']-1
    up_marker = AnchorMarker(col=column, colOff=Utility.col_offset, row=row, rowOff=Utility.row_up_offset)
    Utility.insert_image( worksheet, Utility.image_path_start_day, up_marker, Utility.whole_size)

    worksheet_index = 0
    for n_year in range( n_start_year, n_end_year + 1 ):
        worksheet = workbook.worksheets[ worksheet_index ]
        func_fill_in_day_each_month( worksheet, n_year )
        worksheet_index += 1

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


# func_create_weather_report_form(ScheduleCount.WorkDay.TWO_DAY_OFF, 60, datetime.datetime.strptime('2023-01-03', "%Y-%m-%d"), datetime.datetime.strptime('2023-01-16', "%Y-%m-%d") )
