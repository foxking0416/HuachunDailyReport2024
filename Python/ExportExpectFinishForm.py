import ScheduleCount
import Utility
import LunarCalendar
import os
import datetime
import openpyxl
from openpyxl.drawing.image import Image
from openpyxl.drawing.xdr import XDRPoint2D, XDRPositiveSize2D
from openpyxl.utils.units import pixels_to_EMU, cm_to_EMU
from openpyxl.drawing.spreadsheet_drawing import OneCellAnchor, AnchorMarker


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
        n_column = obj_cell_num['ColumnNum']
        n_row = obj_cell_num['RowNum']
        str_cell = Utility.number_to_string( n_column ) + str( n_row )
        obj_worksheet[str_cell] = n_day
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

    obj_date = obj_start_date
    n_lastyear = 0
    n_worksheet_index = 0
    n_workdays_from_start = 0
    b_insert_start_day_icon = False

    while( True ):
        n_weekday = obj_date.weekday()
        n_year = obj_date.year

        if n_year != n_lastyear:
            worksheet = workbook.worksheets[ n_worksheet_index ]
            func_fill_in_day_each_month( worksheet, n_year )
            n_lastyear = n_year
            n_worksheet_index += 1

        obj_cell_num = func_get_cell_num( obj_date )
        n_column_for_image = obj_cell_num['ColumnNum']-1
        n_row_for_image = obj_cell_num['RowNum']-1
        up_marker   = AnchorMarker( col = n_column_for_image, colOff = col_offset, row = n_row_for_image, rowOff = row_up_offset )

        #插入開工日icon
        if not b_insert_start_day_icon:
            Utility.insert_image( worksheet, Utility.image_path_start_day, up_marker, whole_size )
            b_insert_start_day_icon = True

        n_column_for_text = obj_cell_num['ColumnNum']#跟上面的 obj_cell_num['ColumnNum']-1 其實是指向同一個column，只是因為一個是貼圖的AnchorMarker，一個是cell要使用的，兩個api的基準值不一樣
        n_row_workdays_from_start = obj_cell_num['RowNum']+1
        cell_workdays_from_start = Utility.number_to_string( n_column_for_text ) + str( n_row_workdays_from_start )

        str_lunar_reason = LunarCalendar.func_get_lunar_reason( obj_date )
        if str_lunar_reason != None:
            n_row_for_note = obj_cell_num['RowNum']+2
            cell_note = Utility.number_to_string( n_column_for_text ) + str( n_row_for_note )
            worksheet[ cell_note ] = str_lunar_reason

        if e_count_type == ScheduleCount.WorkDay.ONE_DAY_OFF:
            if n_weekday == 6:#Sunday
                if obj_date in arr_const_workday:
                    Utility.insert_image( worksheet, Utility.image_path_workday, up_marker, whole_size )
                else:
                    Utility.insert_image( worksheet, Utility.image_path_holiday, up_marker, whole_size )
            else:
                if obj_date in arr_const_holiday:
                    Utility.insert_image( worksheet, Utility.image_path_holiday, up_marker, whole_size )
        elif e_count_type == ScheduleCount.WorkDay.TWO_DAY_OFF:
            if n_weekday == 6 or n_weekday == 5:#Sunday Saturday
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

        if ScheduleCount.func_check_is_work_day( arr_const_holiday, arr_const_workday, obj_date, n_weekday, e_count_type ):
            n_expect_total_workdays -= 1
            n_workdays_from_start += 1

        worksheet[ cell_workdays_from_start ] = n_workdays_from_start
        
        if(n_expect_total_workdays <= 0):
            Utility.insert_image( worksheet, Utility.image_path_expect_finish_day, up_marker, whole_size )
            break

        obj_date += datetime.timedelta( days = 1 )

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

# func_create_expect_finish_form(ScheduleCount.WorkDay.TWO_DAY_OFF, 60, datetime.datetime.strptisme('2023-01-01', "%Y-%m-%d") )