import ScheduleCount
import Utility
import LunarCalendar
import os
import datetime
import openpyxl
from openpyxl.drawing.spreadsheet_drawing import AnchorMarker

g_draw_triangle_for_weekend = False

g_project_no = "Avenger001" #案號
g_project_name = "鋼鐵人的基地興建工程" #工程名稱
g_project_owner = "神盾局" #業主
g_project_supervisor = "復仇者聯盟" #監造單位
g_project_designer = "東尼史塔克" #設計單位
g_project_contractor = "賈維斯" #承攬廠商 

def func_fill_in_day_each_month( obj_worksheet, n_input_year ):
    str_first_day = str( n_input_year ) + '-01-01'
    obj_date = datetime.datetime.strptime( str_first_day, "%Y-%m-%d" )  
    b_is_leap_year = ( n_input_year % 4 == 0 )

    if b_is_leap_year:
        n_days_a_year = 366
    else:
        n_days_a_year = 365

    for i in range( n_days_a_year ):
        n_day = obj_date.day

        obj_cell_num = func_get_cell_num( obj_date )
        n_column_for_image = obj_cell_num['ColumnNum']-1
        n_row_for_image = obj_cell_num['RowNum']-1
        up_marker = AnchorMarker( col=n_column_for_image, colOff=Utility.col_offset, row=n_row_for_image, rowOff=Utility.row_up_offset )
        if n_day == 1:
            Utility.insert_image( obj_worksheet, Utility.image_path_day_01, up_marker, Utility.whole_size )
        elif n_day == 2:
            Utility.insert_image( obj_worksheet, Utility.image_path_day_02, up_marker, Utility.whole_size )
        elif n_day == 3:
            Utility.insert_image( obj_worksheet, Utility.image_path_day_03, up_marker, Utility.whole_size )
        elif n_day == 4:
            Utility.insert_image( obj_worksheet, Utility.image_path_day_04, up_marker, Utility.whole_size )
        elif n_day == 5:
            Utility.insert_image( obj_worksheet, Utility.image_path_day_05, up_marker, Utility.whole_size )
        elif n_day == 6:
            Utility.insert_image( obj_worksheet, Utility.image_path_day_06, up_marker, Utility.whole_size )
        elif n_day == 7:
            Utility.insert_image( obj_worksheet, Utility.image_path_day_07, up_marker, Utility.whole_size )
        elif n_day == 8:
            Utility.insert_image( obj_worksheet, Utility.image_path_day_08, up_marker, Utility.whole_size )
        elif n_day == 9:
            Utility.insert_image( obj_worksheet, Utility.image_path_day_09, up_marker, Utility.whole_size )
        elif n_day == 10:
            Utility.insert_image( obj_worksheet, Utility.image_path_day_10, up_marker, Utility.whole_size )
        elif n_day == 11:
            Utility.insert_image( obj_worksheet, Utility.image_path_day_11, up_marker, Utility.whole_size )
        elif n_day == 12:
            Utility.insert_image( obj_worksheet, Utility.image_path_day_12, up_marker, Utility.whole_size )
        elif n_day == 13:
            Utility.insert_image( obj_worksheet, Utility.image_path_day_13, up_marker, Utility.whole_size )
        elif n_day == 14:
            Utility.insert_image( obj_worksheet, Utility.image_path_day_14, up_marker, Utility.whole_size )
        elif n_day == 15:
            Utility.insert_image( obj_worksheet, Utility.image_path_day_15, up_marker, Utility.whole_size )
        elif n_day == 16:
            Utility.insert_image( obj_worksheet, Utility.image_path_day_16, up_marker, Utility.whole_size )
        elif n_day == 17:
            Utility.insert_image( obj_worksheet, Utility.image_path_day_17, up_marker, Utility.whole_size )
        elif n_day == 18:
            Utility.insert_image( obj_worksheet, Utility.image_path_day_18, up_marker, Utility.whole_size )
        elif n_day == 19:
            Utility.insert_image( obj_worksheet, Utility.image_path_day_19, up_marker, Utility.whole_size )
        elif n_day == 20:
            Utility.insert_image( obj_worksheet, Utility.image_path_day_20, up_marker, Utility.whole_size )
        elif n_day == 21:
            Utility.insert_image( obj_worksheet, Utility.image_path_day_21, up_marker, Utility.whole_size )
        elif n_day == 22:
            Utility.insert_image( obj_worksheet, Utility.image_path_day_22, up_marker, Utility.whole_size )
        elif n_day == 23:
            Utility.insert_image( obj_worksheet, Utility.image_path_day_23, up_marker, Utility.whole_size )
        elif n_day == 24:
            Utility.insert_image( obj_worksheet, Utility.image_path_day_24, up_marker, Utility.whole_size )
        elif n_day == 25:
            Utility.insert_image( obj_worksheet, Utility.image_path_day_25, up_marker, Utility.whole_size )
        elif n_day == 26:
            Utility.insert_image( obj_worksheet, Utility.image_path_day_26, up_marker, Utility.whole_size )
        elif n_day == 27:
            Utility.insert_image( obj_worksheet, Utility.image_path_day_27, up_marker, Utility.whole_size )            
        elif n_day == 28:
            Utility.insert_image( obj_worksheet, Utility.image_path_day_28, up_marker, Utility.whole_size )
        elif n_day == 29:
            Utility.insert_image( obj_worksheet, Utility.image_path_day_29, up_marker, Utility.whole_size )
        elif n_day == 30:
            Utility.insert_image( obj_worksheet, Utility.image_path_day_30, up_marker, Utility.whole_size )
        elif n_day == 31:
            Utility.insert_image( obj_worksheet, Utility.image_path_day_31, up_marker, Utility.whole_size )      
        # str_cell = Utility.number_to_string( n_column ) + str( n_row )
        # obj_worksheet[str_cell] = n_day
        obj_date += datetime.timedelta( days = 1 )

def func_get_cell_num( obj_date ):
    n_month = obj_date.month
    n_day = obj_date.day
    n_weekday = ( obj_date.weekday() + 2 ) % 7 
    if n_weekday == 0:
        n_weekday += 7
    n_row_num = 5 + n_month * 3
    n_week_num = func_get_week_num( obj_date )
    n_column_num = 1 + ( n_week_num - 1 ) * 7 + n_weekday


    obj_returnValue = {}
    obj_returnValue['WeekNum'] = n_week_num
    obj_returnValue['RowNum'] = n_row_num
    obj_returnValue['ColumnNum'] = n_column_num
    obj_returnValue['ColumnString'] = Utility.number_to_string( n_column_num )
    return obj_returnValue

def func_get_week_num( obj_date ):
    n_day = obj_date.day

    n_weekday = ( obj_date.weekday() + 2 ) % 7 
    if n_weekday == 0:
        n_weekday += 7
    n_week_num = ( n_day - 1 ) // 7 + 1
    n_rest = n_day % 7
    if n_rest == 0:
        n_rest += 7
    if n_weekday - n_rest < 0:
        n_week_num += 1
    
    return n_week_num

def func_create_expect_finish_form( e_count_type, n_expect_total_workdays, obj_start_date ):
    LunarCalendar.func_load_lunar_holiday_data()

    input_excel =  os.path.join(Utility.current_dir, 'ExternalData\\ExpectFinishFormTemplate.xlsx')
    output_excel = os.path.join(Utility.parent_dir, 'ExpectFinishFormFinal.xlsx') 

    workbook = openpyxl.load_workbook(input_excel)
    worksheet = workbook.active

    arr_const_holiday = []
    arr_const_workday = []
    ScheduleCount.func_load_json_holiday_data( arr_const_holiday, arr_const_workday )

    obj_return_value = ScheduleCount.func_count_expect_finish_date( e_count_type, n_expect_total_workdays, obj_start_date, arr_const_holiday, arr_const_workday )
    obj_end_date = obj_return_value['ExpectFinishDate']
    n_start_year = obj_start_date.year
    n_end_year = obj_end_date.year
    
    #先準備足夠年份的sheet
    for n_year in range( n_start_year, n_end_year + 1 ):
        if n_year != n_start_year:
            worksheet = workbook.copy_worksheet( worksheet )
        worksheet.title = str(n_year) + '年'
        worksheet['B4'] = str(n_year) + '年(' + str( n_year - 1911 ) + '年)' 
        worksheet['D2'] = g_project_no
        worksheet['D3'] = g_project_name
        worksheet['V2'] = g_project_owner
        worksheet['V3'] = g_project_supervisor
        worksheet['AH2'] = g_project_designer
        worksheet['AH3'] = g_project_contractor

        #填色
        arr_sunday_column = ['B', 'I', 'P', 'W', 'AD', 'AK']
        arr_saturday_column = ['H', 'O', 'V', 'AC', 'AJ']
        if not g_draw_triangle_for_weekend:
            if e_count_type == ScheduleCount.WorkDay.TWO_DAY_OFF or e_count_type == ScheduleCount.WorkDay.ONE_DAY_OFF:
                for column in arr_sunday_column:
                    str_fill_cell = column + str( 6 )
                    worksheet[str_fill_cell].fill = Utility.fill_green
                    for i in range( 36 ):
                        str_fill_cell = column + str( i + 8 )
                        worksheet[str_fill_cell].fill = Utility.fill_green
                if e_count_type == ScheduleCount.WorkDay.TWO_DAY_OFF:
                    for column in arr_saturday_column:
                        str_fill_cell = column + str( 6 )
                        worksheet[str_fill_cell].fill = Utility.fill_green
                        for i in range( 36 ):
                            str_fill_cell = column + str( i + 8 )
                            worksheet[str_fill_cell].fill = Utility.fill_green
        else:
            for column in arr_sunday_column:
                str_fill_cell = column + str( 6 )
                worksheet[str_fill_cell].fill = Utility.fill_green
            for column in arr_saturday_column:
                str_fill_cell = column + str( 6 )
                worksheet[str_fill_cell].fill = Utility.fill_yellow

    obj_date = obj_start_date
    n_workdays_from_start = 0

    n_calendar_days_each_month = 0
    n_calendar_days_accumulate = 0
    n_weekend_days_each_month = 0
    n_weekend_days_accumulate = 0
    n_holiday_days_each_month = 0
    n_holiday_days_accumulate = 0
    n_no_count_days_each_month = 0
    n_no_count_days_accumulate = 0

    n_last_year = 0
    n_worksheet_index = 0
    b_insert_start_day_icon = False

    while( True ):
        n_weekday = obj_date.weekday()
        n_year = obj_date.year
        if n_year != n_last_year:
            worksheet = workbook.worksheets[ n_worksheet_index ]
            n_worksheet_index += 1
            n_last_year = n_year

        month = obj_date.month

        obj_cell_num = func_get_cell_num( obj_date )
        n_column_for_image = obj_cell_num['ColumnNum']-1
        n_row_for_image = obj_cell_num['RowNum']-1
        up_marker   = AnchorMarker( col = n_column_for_image, colOff = Utility.col_offset, row = n_row_for_image, rowOff = Utility.row_up_offset )

        #插入開工日icon
        if not b_insert_start_day_icon:
            Utility.insert_image( worksheet, Utility.image_path_start_day, up_marker, Utility.whole_size )
            b_insert_start_day_icon = True

        n_column_for_text = obj_cell_num['ColumnNum']#跟上面的 obj_cell_num['ColumnNum']-1 其實是指向同一個column，只是因為一個是貼圖的AnchorMarker，一個是cell要使用的，兩個api的基準值不一樣
        n_row_workdays_from_start = obj_cell_num['RowNum']+1
        cell_workdays_from_start = Utility.number_to_string( n_column_for_text ) + str( n_row_workdays_from_start )

        str_lunar_reason = LunarCalendar.func_get_lunar_reason( obj_date )
        if str_lunar_reason != None:
            n_row_for_note = obj_cell_num['RowNum']+2
            cell_note = Utility.number_to_string( n_column_for_text ) + str( n_row_for_note )
            worksheet[ cell_note ] = str_lunar_reason


        b_is_weekend = [False]
        b_is_holiday = [False]
        b_is_make_up_workday = [False]
        b_is_work_day = ScheduleCount.func_check_is_work_day( arr_const_holiday, arr_const_workday, obj_date, n_weekday, e_count_type, b_is_weekend, b_is_holiday, b_is_make_up_workday )
        if b_is_work_day:
            n_expect_total_workdays -= 1
            n_workdays_from_start += 1

        worksheet[ cell_workdays_from_start ] = n_workdays_from_start
        #計算A欄
        n_calendar_days_each_month += 1
        n_calendar_days_accumulate += 1

        if b_is_weekend[0]:#計算B1欄
            n_weekend_days_each_month += 1
            n_weekend_days_accumulate += 1
        if b_is_holiday[0]:#計算B2欄
            n_holiday_days_each_month += 1
            n_holiday_days_accumulate += 1
        if not b_is_work_day:#計算B0欄
            n_no_count_days_each_month += 1
            n_no_count_days_accumulate += 1
        
        if b_is_weekend[0]:
            if g_draw_triangle_for_weekend:
                Utility.insert_image( worksheet, Utility.image_path_holiday, up_marker, Utility.whole_size )
        elif b_is_holiday[0]:
            Utility.insert_image( worksheet, Utility.image_path_holiday, up_marker, Utility.whole_size )
        elif b_is_make_up_workday[0]:
            Utility.insert_image( worksheet, Utility.image_path_workday, up_marker, Utility.whole_size )

        str_cell_calendar_days_each_month = None #天數(每月) A 欄位"AM"
        str_cell_calendar_days_accumulate = None #天數(累計) A 欄位"AM"
        str_cell_weekend_days_each_month = None #星期例假(每月) B1 欄位"AN"
        str_cell_weekend_days_accumulate = None #星期例假(累計) B1 欄位"AN"
        str_cell_holiday_days_each_month = None #國定例假(每月) B2 欄位"AO"
        str_cell_holiday_days_accumulate = None #國定例假(累計) B2 欄位"AO"
        str_cell_no_count_days_each_month = None #不計工期(每月) B3
        str_cell_no_count_days_accumulate = None #不計工期(累計) B3

        str_cell_calendar_days_each_month = 'AM' + str( 5 + month * 3 )
        str_cell_calendar_days_accumulate = 'AM' + str( 6 + month * 3 )
        str_cell_weekend_days_each_month  = 'AN' + str( 5 + month * 3 )
        str_cell_weekend_days_accumulate  = 'AN' + str( 6 + month * 3 )
        str_cell_holiday_days_each_month  = 'AO' + str( 5 + month * 3 )
        str_cell_holiday_days_accumulate  = 'AO' + str( 6 + month * 3 )
        str_cell_no_count_days_each_month = 'AP' + str( 5 + month * 3 )
        str_cell_no_count_days_accumulate = 'AP' + str( 6 + month * 3 )

        obj_date_add_1 = obj_date + datetime.timedelta(days=1)

        if obj_date.month != obj_date_add_1.month:
            worksheet[ str_cell_calendar_days_each_month ] = n_calendar_days_each_month
            worksheet[ str_cell_calendar_days_accumulate ] = n_calendar_days_accumulate
            worksheet[ str_cell_weekend_days_each_month ]  = n_weekend_days_each_month
            worksheet[ str_cell_weekend_days_accumulate ]  = n_weekend_days_accumulate
            worksheet[ str_cell_holiday_days_each_month ]  = n_holiday_days_each_month
            worksheet[ str_cell_holiday_days_accumulate ]  = n_holiday_days_accumulate
            worksheet[ str_cell_no_count_days_each_month ] = n_no_count_days_each_month
            worksheet[ str_cell_no_count_days_accumulate ] = n_no_count_days_accumulate
            n_calendar_days_each_month = 0
            n_weekend_days_each_month = 0
            n_holiday_days_each_month = 0
            n_no_count_days_each_month = 0

        if(n_expect_total_workdays <= 0):
            Utility.insert_image( worksheet, Utility.image_path_expect_finish_day, up_marker, Utility.whole_size )
            if n_calendar_days_each_month != 0:
                #固定因素
                worksheet[ str_cell_calendar_days_each_month ] = n_calendar_days_each_month #A
                worksheet[ str_cell_calendar_days_accumulate ] = n_calendar_days_accumulate
                worksheet[ str_cell_weekend_days_each_month ] = n_weekend_days_each_month #B1
                worksheet[ str_cell_weekend_days_accumulate ]  = n_weekend_days_accumulate
                worksheet[ str_cell_holiday_days_each_month ] = n_holiday_days_each_month #B2
                worksheet[ str_cell_holiday_days_accumulate ]  = n_holiday_days_accumulate
                worksheet[ str_cell_no_count_days_each_month ] = n_no_count_days_each_month #B0
                worksheet[ str_cell_no_count_days_accumulate ] = n_no_count_days_accumulate
            break

        obj_date += datetime.timedelta( days = 1 )

    n_worksheet_index = 0
    for n_year in range( n_start_year, n_end_year + 1 ):
        worksheet = workbook.worksheets[ n_worksheet_index ]
        func_fill_in_day_each_month( worksheet, n_year )
        n_worksheet_index += 1

    any_serial_num = False
    serial_number = 1
    filename, extension = os.path.splitext(output_excel)
    while os.path.exists(output_excel):
        # 如果文件已经存在，则添加流水号并重新检查
        output_excel = f"{filename}_{serial_number}{extension}"
        serial_number += 1
        any_serial_num = True

    if any_serial_num:
        serial_number -= 1
        output_pdf = f"{filename}_{serial_number}{'.pdf'}"
    else:
        output_pdf = f"{filename}{'.pdf'}"
    workbook.save( output_excel )
    Utility.excel_to_pdf( output_excel, output_pdf )
    print('finish')


    pass

# func_create_expect_finish_form(ScheduleCount.WorkDay.TWO_DAY_OFF, 300, datetime.datetime.strptime('2023-01-01', "%Y-%m-%d") )