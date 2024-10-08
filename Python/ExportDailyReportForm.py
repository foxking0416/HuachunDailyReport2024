import ScheduleCount
import Utility
import LunarCalendar
import json
import os
import datetime
import openpyxl
from openpyxl.drawing.spreadsheet_drawing import AnchorMarker

g_daily_report_type = Utility.DailyReportType.TYPE_A
g_draw_triangle_for_weekend = True

g_project_no = "Avenger001" #案號
g_project_name = "鋼鐵人的基地興建工程" #工程名稱
g_project_owner = "神盾局" #業主
g_project_supervisor = "復仇者聯盟" #監造單位
g_project_designer = "東尼史塔克" #設計單位
g_project_contractor = "賈維斯" #承攬廠商 


def func_set_info( str_project_no, str_project_name, str_project_owner, str_project_supervisor, str_project_designer, str_project_contractor ):
    global g_project_no
    global g_project_name
    global g_project_owner
    global g_project_supervisor
    global g_project_designer
    global g_project_contractor
    
    g_project_no = str_project_no
    g_project_name = str_project_name
    g_project_owner = str_project_owner
    g_project_supervisor = str_project_supervisor
    g_project_designer = str_project_designer
    g_project_contractor = str_project_contractor

def func_set_form_type( str_form_type, str_triangle_for_weekend ):
    global g_daily_report_type
    global g_draw_triangle_for_weekend
    if str_form_type == 'TypeA':
        g_daily_report_type = Utility.DailyReportType.TYPE_A
    elif str_form_type == 'TypeB':
        g_daily_report_type = Utility.DailyReportType.TYPE_B

    if str_triangle_for_weekend == 'true':
        g_draw_triangle_for_weekend = True
    else:
        g_draw_triangle_for_weekend = False

def func_fill_in_day_each_month( worksheet, input_year ):
    str_first_day = str( input_year ) + '-01-01'
    date_obj = datetime.datetime.strptime( str_first_day, "%Y-%m-%d" )  
    b_is_leap_year = ( input_year % 4 == 0 )

    if b_is_leap_year:
        n_days_a_year = 366
    else:
        n_days_a_year = 365

    for i in range( n_days_a_year ):
        n_day = date_obj.day

        obj_cell_num = func_get_cell_num( date_obj )
        
        if g_daily_report_type == Utility.DailyReportType.TYPE_A:
            n_column_for_image = obj_cell_num['ColumnNum']-1
            n_row_for_image = obj_cell_num['RowNum']-1
            up_marker = AnchorMarker( col=n_column_for_image, colOff=Utility.col_offset, row=n_row_for_image, rowOff=Utility.row_up_offset )
            if n_day == 1:
                Utility.insert_image( worksheet, Utility.image_path_day_01, up_marker, Utility.whole_size )
            elif n_day == 2:
                Utility.insert_image( worksheet, Utility.image_path_day_02, up_marker, Utility.whole_size )
            elif n_day == 3:
                Utility.insert_image( worksheet, Utility.image_path_day_03, up_marker, Utility.whole_size )
            elif n_day == 4:
                Utility.insert_image( worksheet, Utility.image_path_day_04, up_marker, Utility.whole_size )
            elif n_day == 5:
                Utility.insert_image( worksheet, Utility.image_path_day_05, up_marker, Utility.whole_size )
            elif n_day == 6:
                Utility.insert_image( worksheet, Utility.image_path_day_06, up_marker, Utility.whole_size )
            elif n_day == 7:
                Utility.insert_image( worksheet, Utility.image_path_day_07, up_marker, Utility.whole_size )
            elif n_day == 8:
                Utility.insert_image( worksheet, Utility.image_path_day_08, up_marker, Utility.whole_size )
            elif n_day == 9:
                Utility.insert_image( worksheet, Utility.image_path_day_09, up_marker, Utility.whole_size )
            elif n_day == 10:
                Utility.insert_image( worksheet, Utility.image_path_day_10, up_marker, Utility.whole_size )
            elif n_day == 11:
                Utility.insert_image( worksheet, Utility.image_path_day_11, up_marker, Utility.whole_size )
            elif n_day == 12:
                Utility.insert_image( worksheet, Utility.image_path_day_12, up_marker, Utility.whole_size )
            elif n_day == 13:
                Utility.insert_image( worksheet, Utility.image_path_day_13, up_marker, Utility.whole_size )
            elif n_day == 14:
                Utility.insert_image( worksheet, Utility.image_path_day_14, up_marker, Utility.whole_size )
            elif n_day == 15:
                Utility.insert_image( worksheet, Utility.image_path_day_15, up_marker, Utility.whole_size )
            elif n_day == 16:
                Utility.insert_image( worksheet, Utility.image_path_day_16, up_marker, Utility.whole_size )
            elif n_day == 17:
                Utility.insert_image( worksheet, Utility.image_path_day_17, up_marker, Utility.whole_size )
            elif n_day == 18:
                Utility.insert_image( worksheet, Utility.image_path_day_18, up_marker, Utility.whole_size )
            elif n_day == 19:
                Utility.insert_image( worksheet, Utility.image_path_day_19, up_marker, Utility.whole_size )
            elif n_day == 20:
                Utility.insert_image( worksheet, Utility.image_path_day_20, up_marker, Utility.whole_size )
            elif n_day == 21:
                Utility.insert_image( worksheet, Utility.image_path_day_21, up_marker, Utility.whole_size )
            elif n_day == 22:
                Utility.insert_image( worksheet, Utility.image_path_day_22, up_marker, Utility.whole_size )
            elif n_day == 23:
                Utility.insert_image( worksheet, Utility.image_path_day_23, up_marker, Utility.whole_size )
            elif n_day == 24:
                Utility.insert_image( worksheet, Utility.image_path_day_24, up_marker, Utility.whole_size )
            elif n_day == 25:
                Utility.insert_image( worksheet, Utility.image_path_day_25, up_marker, Utility.whole_size )
            elif n_day == 26:
                Utility.insert_image( worksheet, Utility.image_path_day_26, up_marker, Utility.whole_size )
            elif n_day == 27:
                Utility.insert_image( worksheet, Utility.image_path_day_27, up_marker, Utility.whole_size )            
            elif n_day == 28:
                Utility.insert_image( worksheet, Utility.image_path_day_28, up_marker, Utility.whole_size )
            elif n_day == 29:
                Utility.insert_image( worksheet, Utility.image_path_day_29, up_marker, Utility.whole_size )
            elif n_day == 30:
                Utility.insert_image( worksheet, Utility.image_path_day_30, up_marker, Utility.whole_size )
            elif n_day == 31:
                Utility.insert_image( worksheet, Utility.image_path_day_31, up_marker, Utility.whole_size )        
        elif g_daily_report_type == Utility.DailyReportType.TYPE_B:
            n_column = obj_cell_num['ColumnNum']
            n_row = obj_cell_num['RowNum'] + 1
            str_cell = Utility.number_to_string( n_column )+str( n_row )
            worksheet[str_cell] = n_day

        date_obj += datetime.timedelta(days=1)

def func_get_cell_num( obj_date ):
    month = obj_date.month
    weekday = ( obj_date.weekday() + 2 ) % 7 
    if weekday == 0:
        weekday += 7

    row_num = None
    if g_daily_report_type == Utility.DailyReportType.TYPE_A:
        row_num = 5 + month * 3
    elif g_daily_report_type == Utility.DailyReportType.TYPE_B:
        row_num = 4 + month * 4
    
    week_num = func_get_week_num( obj_date )
    column_num = 1 + ( week_num - 1 ) * 7 + weekday


    return_value = {}
    return_value['WeekNum'] = week_num
    return_value['RowNum'] = row_num
    return_value['ColumnNum'] = column_num
    return_value['ColumnString'] = Utility.number_to_string( column_num )
    return return_value

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

def func_find_daily_data_by_date( daily_report_date, obj_date ):        
    for entry in daily_report_date:
        if entry["date"] == obj_date.strftime("%Y-%m-%d"):
            return entry
    return None

def func_create_weather_report_form( e_count_type, n_expect_total_workdays, obj_start_date, obj_current_date ):
    LunarCalendar.func_load_lunar_holiday_data()
    LunarCalendar.func_load_solar_holiday_data()
    input_excel =  None
    if g_daily_report_type == Utility.DailyReportType.TYPE_A:
        input_excel =  os.path.join( Utility.current_dir, 'ExternalData\\DailyReportTemplateWithLunar_A.xlsx')
    elif g_daily_report_type == Utility.DailyReportType.TYPE_B:
        input_excel =  os.path.join( Utility.current_dir, 'ExternalData\\DailyReportTemplateWithLunar_B.xlsx')
    output_excel = os.path.join( Utility.parent_dir, 'DailyReportFinal.xlsx') 

    workbook = openpyxl.load_workbook(input_excel)
    worksheet = workbook.active

    arr_const_holiday = []
    arr_const_workday = []
    dict_holiday_reason = {}
    ScheduleCount.func_load_json_holiday_data( arr_const_holiday,arr_const_workday, dict_holiday_reason )

    dict_weather_and_human_related_holiday = {}
    daily_report_data = ScheduleCount.func_load_json_daily_report_data( dict_weather_and_human_related_holiday )
    dict_extend_data = {}
    ScheduleCount.func_load_json_extend_data( dict_extend_data )
    obj_real_finish_date = ScheduleCount.func_count_real_finish_date( e_count_type, n_expect_total_workdays, obj_start_date, obj_current_date, arr_const_holiday, arr_const_workday, dict_weather_and_human_related_holiday, dict_extend_data )

    dict_morning_weather_condition_setting = {}
    dict_afternoon_weather_condition_setting = {}
    dict_morning_human_condition_setting = {}
    dict_afternoon_human_condition_setting = {}
    ScheduleCount.func_load_json_condition_setting_data( dict_morning_weather_condition_setting, dict_afternoon_weather_condition_setting,
                                                         dict_morning_human_condition_setting, dict_afternoon_human_condition_setting )

    n_start_year = obj_start_date.year
    n_end_year = obj_real_finish_date['RealFinishDate'].year
    #先看有多少年的資料，建立所需worksheet，並且做填色
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
        if e_count_type == e_count_type == ScheduleCount.WorkDay.NO_DAY_OFF:
            worksheet['C44'] = '工期計算方式為日曆天，無周休、無國定假日'
        elif e_count_type == ScheduleCount.WorkDay.ONE_DAY_OFF:
            worksheet['C44'] = '工期計算方式為工作天，週休一日，國定假日不施工'
        elif e_count_type == ScheduleCount.WorkDay.TWO_DAY_OFF:
            worksheet['C44'] = '工期計算方式為工作天，週休二日，國定假日不施工'

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

        #將追加工期資料寫進表裡
        n_extend_times = 0
        for key, value in dict_extend_data.items():
            # if n_extend_times > 6:
                # worksheet.insert_rows(52)
                # worksheet.row_dimensions[53].height = 27.75
            n_row_index = 0
            if g_daily_report_type == Utility.DailyReportType.TYPE_A:
                n_row_index = 47
            elif g_daily_report_type == Utility.DailyReportType.TYPE_B:
                n_row_index = 59

            str_border_cell_1 = 'AX' + str( n_row_index + n_extend_times )
            str_border_cell_2 = 'AY' + str( n_row_index + n_extend_times )
            str_border_cell_3 = 'AZ' + str( n_row_index + n_extend_times )
            str_border_cell_4 = 'BA' + str( n_row_index + n_extend_times )
            worksheet[str_border_cell_1].border = Utility.border
            worksheet[str_border_cell_2].border = Utility.border       
            worksheet[str_border_cell_3].border = Utility.border
            worksheet[str_border_cell_4].border = Utility.border

            str_merge_cell = 'AX' + str( n_row_index + n_extend_times ) + ':BA' + str( n_row_index + n_extend_times )
            worksheet.merge_cells( str_merge_cell )
            obj_extend_start_date = key
            n_extend_days = value
            str_extend = key.strftime("%Y/%m/%d") + ': ' + str( n_extend_days ) + '天'
            cell_extend_data = 'AX' + str( n_row_index + n_extend_times )
            worksheet[cell_extend_data] = str_extend
            n_extend_times += 1

    # region 定義計算各種天數的參數
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
    f_sun_days_each_month = 0
    f_sun_days_accumulate = 0
    f_rain_days_each_month = 0
    f_rain_days_accumulate = 0
    f_rain_days_no_count_each_month = 0
    f_rain_days_no_count_accumulate = 0
    f_heavy_rain_days_each_month = 0
    f_heavy_rain_days_accumulate = 0
    f_heavy_rain_days_no_count_each_month = 0
    f_heavy_rain_days_no_count_accumulate = 0
    f_typhoon_days_each_month = 0
    f_typhoon_days_accumulate = 0
    f_typhoon_days_no_count_each_month = 0
    f_typhoon_days_no_count_accumulate = 0
    f_hot_days_each_month = 0
    f_hot_days_accumulate = 0
    f_hot_days_no_count_each_month = 0
    f_hot_days_no_count_accumulate = 0
    f_muddy_days_each_month = 0
    f_muddy_days_accumulate = 0
    f_muddy_days_no_count_each_month = 0
    f_muddy_days_no_count_accumulate = 0
    f_weather_other_days_each_month = 0
    f_weather_other_days_accumulate = 0
    f_weather_other_days_no_count_each_month = 0
    f_weather_other_days_no_count_accumulate = 0
    f_weather_no_count_days_each_month = 0
    f_weather_no_count_days_accumulate = 0

    f_suspend_work_days_each_month = 0
    f_suspend_work_days_accumulate = 0
    f_suspend_work_days_no_count_each_month = 0
    f_suspend_work_days_no_count_accumulate = 0
    f_power_off_days_each_month = 0
    f_power_off_days_accumulate = 0
    f_power_off_days_no_count_each_month = 0
    f_power_off_days_no_count_accumulate = 0
    f_human_other_days_each_month = 0
    f_human_other_days_accumulate = 0
    f_human_other_days_no_count_each_month = 0
    f_human_other_days_no_count_accumulate = 0
    f_human_no_count_days_each_month = 0
    f_human_no_count_days_accumulate = 0

    n_total_work_days = 0 #F1
    f_work_days_no_count_each_month = 0 #F0
    f_work_days_no_count_accumulate = 0 #F0
    f_work_days_used_each_month = 0 #F2
    f_work_days_used_accumulate = 0 #F2
    f_rest_work_days = 0 #F3

    f_calendar_days_used_each_month = 0 #G2
    f_calendar_days_used_accumulate = 0 #G2

    

    n_last_year = 0
    n_worksheet_index = 0
    # endregion

    while( True ):
        daily_data = func_find_daily_data_by_date( daily_report_data, obj_date )
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
        up_marker = AnchorMarker( col=n_column_for_image, colOff=Utility.col_offset, row=n_row_for_image, rowOff=Utility.row_up_offset )
        down_marker = AnchorMarker( col=n_column_for_image, colOff=Utility.col_offset, row=n_row_for_image, rowOff=Utility.row_down_offset )
        up_marker_human = AnchorMarker( col=n_column_for_image, colOff=Utility.col_offset_human, row=n_row_for_image, rowOff=Utility.row_up_offset )
        down_marker_human = AnchorMarker( col=n_column_for_image, colOff=Utility.col_offset_human, row=n_row_for_image, rowOff=Utility.row_down_offset )

        n_column_for_text = obj_cell_num['ColumnNum']#跟上面的 obj_cell_num['ColumnNum']-1 其實是指向同一個column，只是因為一個是貼圖的AnchorMarker，一個是cell要使用的，兩個api的基準值不一樣

        str_lunar_reason = LunarCalendar.func_get_lunar_reason( obj_date )
        str_solar_reason = LunarCalendar.func_get_solar_reason( obj_date, dict_holiday_reason )
        if str_lunar_reason != None or str_solar_reason != None:
            if g_daily_report_type == Utility.DailyReportType.TYPE_A:
                n_row_for_note = obj_cell_num['RowNum'] + 1
            elif  g_daily_report_type == Utility.DailyReportType.TYPE_B:
                n_row_for_note = obj_cell_num['RowNum'] + 2
            cell_note = Utility.number_to_string( n_column_for_text ) + str( n_row_for_note )
            if str_solar_reason:
                worksheet[ cell_note ] = str_solar_reason
            elif str_lunar_reason:
                worksheet[ cell_note ] = str_lunar_reason

        if g_daily_report_type == Utility.DailyReportType.TYPE_A:
            n_row_workdays_from_start = obj_cell_num['RowNum'] + 2
        elif  g_daily_report_type == Utility.DailyReportType.TYPE_B:
            n_row_workdays_from_start = obj_cell_num['RowNum'] + 3

        cell_workdays_from_start = Utility.number_to_string( n_column_for_text ) + str( n_row_workdays_from_start )

        b_is_weekend = [False]
        b_is_holiday = [False]
        b_is_make_up_workday = [False]
        b_is_work_day = ScheduleCount.func_check_is_work_day( arr_const_holiday, arr_const_workday, obj_date, n_weekday, e_count_type, b_is_weekend, b_is_holiday, b_is_make_up_workday )
        if b_is_work_day:
            if daily_data and obj_date <= obj_current_date:
                if obj_date in dict_weather_and_human_related_holiday:
                    if dict_weather_and_human_related_holiday[ obj_date ] == ScheduleCount.CountWorkingDay.NO_COUNT:
                        pass
                    elif dict_weather_and_human_related_holiday[ obj_date ] == ScheduleCount.CountWorkingDay.COUNT_HALF_DAY:
                        n_workdays_from_start += 0.5
                    else:
                        n_workdays_from_start += 1
                else:
                    n_workdays_from_start += 1
            else:
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

        if obj_date <= obj_current_date:
            if not daily_data:
                Utility.insert_image( worksheet, Utility.image_path_no_data, up_marker, Utility.whole_size )
            else:
                if daily_data["morning_weather"] == ScheduleCount.Weather.SUN:#晴天
                    Utility.insert_image( worksheet, Utility.image_path_sun_up,           up_marker, Utility.half_size )
                    f_sun_days_each_month += 0.5
                    f_sun_days_accumulate += 0.5
                elif daily_data["morning_weather"] == ScheduleCount.Weather.RAIN:#雨天
                    Utility.insert_image( worksheet, Utility.image_path_rain_up,          up_marker, Utility.half_size )
                    f_rain_days_each_month += 0.5
                    f_rain_days_accumulate += 0.5
                elif daily_data["morning_weather"] == ScheduleCount.Weather.HEAVY_RAIN:#豪雨
                    Utility.insert_image( worksheet, Utility.image_path_heavyrain_up,     up_marker, Utility.half_size )
                    f_heavy_rain_days_each_month += 0.5
                    f_heavy_rain_days_accumulate += 0.5
                elif daily_data["morning_weather"] == ScheduleCount.Weather.TYPHOON:#颱風
                    Utility.insert_image( worksheet, Utility.image_path_typhoon_up,       up_marker, Utility.half_size )
                    f_typhoon_days_each_month += 0.5
                    f_typhoon_days_accumulate += 0.5
                elif daily_data["morning_weather"] == ScheduleCount.Weather.HOT:#酷熱
                    Utility.insert_image( worksheet, Utility.image_path_hot_up,           up_marker, Utility.half_size )
                    f_hot_days_each_month += 0.5
                    f_hot_days_accumulate += 0.5
                elif daily_data["morning_weather"] == ScheduleCount.Weather.MUDDY:#雨後泥濘
                    Utility.insert_image( worksheet, Utility.image_path_muddy_up,         up_marker, Utility.half_size )
                    f_muddy_days_each_month += 0.5
                    f_muddy_days_accumulate += 0.5
                elif daily_data["morning_weather"] == ScheduleCount.Weather.OTHER:#其他
                    Utility.insert_image( worksheet, Utility.image_path_weather_other_up, up_marker, Utility.half_size )
                    f_weather_other_days_each_month += 0.5
                    f_weather_other_days_accumulate += 0.5

                if daily_data["afternoon_weather"] == ScheduleCount.Weather.SUN:#晴天
                    Utility.insert_image( worksheet, Utility.image_path_sun_down,         down_marker, Utility.half_size )
                    f_sun_days_each_month += 0.5
                    f_sun_days_accumulate += 0.5
                elif daily_data["afternoon_weather"] == ScheduleCount.Weather.RAIN:#雨天
                    Utility.insert_image( worksheet, Utility.image_path_rain_down,        down_marker, Utility.half_size )
                    f_rain_days_each_month += 0.5
                    f_rain_days_accumulate += 0.5
                elif daily_data["afternoon_weather"] == ScheduleCount.Weather.HEAVY_RAIN:#豪雨
                    Utility.insert_image( worksheet, Utility.image_path_heavyrain_down,   down_marker, Utility.half_size )
                    f_heavy_rain_days_each_month += 0.5
                    f_heavy_rain_days_accumulate += 0.5
                elif daily_data["afternoon_weather"] == ScheduleCount.Weather.TYPHOON:#颱風
                    Utility.insert_image( worksheet, Utility.image_path_typhoon_down,     down_marker, Utility.half_size )
                    f_typhoon_days_each_month += 0.5
                    f_typhoon_days_accumulate += 0.5
                elif daily_data["afternoon_weather"] == ScheduleCount.Weather.HOT:#酷熱
                    Utility.insert_image( worksheet, Utility.image_path_hot_down,         down_marker, Utility.half_size )
                    f_hot_days_each_month += 0.5
                    f_hot_days_accumulate += 0.5
                elif daily_data["afternoon_weather"] == ScheduleCount.Weather.MUDDY:#雨後泥濘
                    Utility.insert_image( worksheet, Utility.image_path_muddy_down,       down_marker, Utility.half_size )
                    f_muddy_days_each_month += 0.5
                    f_muddy_days_accumulate += 0.5
                elif daily_data["afternoon_weather"] == ScheduleCount.Weather.OTHER:#其他
                    Utility.insert_image( worksheet, Utility.image_path_weather_other_down, down_marker, Utility.half_size )
                    f_weather_other_days_each_month += 0.5
                    f_weather_other_days_accumulate += 0.5
                
                # 不能搬到天氣前面，不然image會被蓋掉
                if daily_data["suspend_work"] == ScheduleCount.SyspendWork.SUSPEND_WORK:#停工
                    Utility.insert_image( worksheet, Utility.image_path_suspend_work_up,   up_marker_human, Utility.quarter_size )
                    f_suspend_work_days_each_month += 1
                    f_suspend_work_days_accumulate += 1

                if daily_data["morning_human"] == ScheduleCount.Human.POWER_OFF:#停電
                    Utility.insert_image( worksheet, Utility.image_path_power_off_up,      up_marker_human, Utility.quarter_size )
                    f_power_off_days_each_month += 0.5
                    f_power_off_days_accumulate += 0.5
                elif daily_data["morning_human"] == ScheduleCount.Human.OTHER:#其他
                    Utility.insert_image( worksheet, Utility.image_path_human_other_up,    up_marker_human, Utility.quarter_size )
                    f_human_other_days_each_month += 0.5
                    f_human_other_days_accumulate += 0.5

                if daily_data["afternoon_human"] == ScheduleCount.Human.POWER_OFF:#停電
                    Utility.insert_image( worksheet, Utility.image_path_power_off_down,    down_marker_human, Utility.quarter_size )
                    f_power_off_days_each_month += 0.5
                    f_power_off_days_accumulate += 0.5
                elif daily_data["afternoon_human"] == ScheduleCount.Human.OTHER:#其他
                    Utility.insert_image( worksheet, Utility.image_path_human_other_down,  down_marker_human, Utility.quarter_size )
                    f_human_other_days_each_month += 0.5
                    f_human_other_days_accumulate += 0.5

                dict_return_suspend_work = {}
                dict_return_weather = {}
                dict_return_human = {}
                ScheduleCount.func_condition_no_count( b_is_work_day,
                                                       dict_morning_weather_condition_setting,
                                                       dict_afternoon_weather_condition_setting,
                                                       dict_morning_human_condition_setting,
                                                       dict_afternoon_human_condition_setting,
                                                       daily_data["suspend_work"],
                                                       daily_data["morning_weather"],
                                                       daily_data["afternoon_weather"],
                                                       daily_data["morning_human"],
                                                       daily_data["afternoon_human"],
                                                       dict_return_suspend_work,
                                                       dict_return_weather,
                                                       dict_return_human )
                #計算C1
                f_suspend_work_days_no_count_each_month += dict_return_suspend_work[ ScheduleCount.SyspendWork.SUSPEND_WORK ]
                f_suspend_work_days_no_count_accumulate += dict_return_suspend_work[ ScheduleCount.SyspendWork.SUSPEND_WORK ]

                #計算D1到D7的不計欄位
                f_rain_days_no_count_each_month += dict_return_weather[ ScheduleCount.Weather.RAIN ]
                f_rain_days_no_count_accumulate += dict_return_weather[ ScheduleCount.Weather.RAIN ]
                f_heavy_rain_days_no_count_each_month += dict_return_weather[ ScheduleCount.Weather.HEAVY_RAIN ]
                f_heavy_rain_days_no_count_accumulate += dict_return_weather[ ScheduleCount.Weather.HEAVY_RAIN ]
                f_typhoon_days_no_count_each_month += dict_return_weather[ ScheduleCount.Weather.TYPHOON ]
                f_typhoon_days_no_count_accumulate += dict_return_weather[ ScheduleCount.Weather.TYPHOON ]
                f_hot_days_no_count_each_month += dict_return_weather[ ScheduleCount.Weather.HOT ]
                f_hot_days_no_count_accumulate += dict_return_weather[ ScheduleCount.Weather.HOT ]
                f_muddy_days_no_count_each_month += dict_return_weather[ ScheduleCount.Weather.MUDDY ]
                f_muddy_days_no_count_accumulate += dict_return_weather[ ScheduleCount.Weather.MUDDY ]
                f_weather_other_days_no_count_each_month += dict_return_weather[ ScheduleCount.Weather.OTHER ]
                f_weather_other_days_no_count_accumulate += dict_return_weather[ ScheduleCount.Weather.OTHER ]
                #計算D0
                f_weather_no_count_days_each_month += dict_return_weather[ ScheduleCount.Weather.TOTAL ]
                f_weather_no_count_days_accumulate += dict_return_weather[ ScheduleCount.Weather.TOTAL ]

                #計算E1到E2的不計欄位
                f_power_off_days_no_count_each_month += dict_return_human[ ScheduleCount.Human.POWER_OFF ]
                f_power_off_days_no_count_accumulate += dict_return_human[ ScheduleCount.Human.POWER_OFF ]
                f_human_other_days_no_count_each_month += dict_return_human[ ScheduleCount.Human.OTHER ]
                f_human_other_days_no_count_accumulate += dict_return_human[ ScheduleCount.Human.OTHER ]
                #計算E0
                f_human_no_count_days_each_month += dict_return_human[ ScheduleCount.Human.TOTAL ]
                f_human_no_count_days_accumulate += dict_return_human[ ScheduleCount.Human.TOTAL ]

        n_total_work_days = n_expect_total_workdays

        if obj_date <= obj_current_date:
            for key, value in dict_extend_data.items():
                obj_extend_start_date = key
                if obj_date >= obj_extend_start_date:
                    n_total_work_days += value


            if b_is_work_day:
                if obj_date in dict_weather_and_human_related_holiday:
                    if dict_weather_and_human_related_holiday[ obj_date ] == ScheduleCount.CountWorkingDay.NO_COUNT:
                        f_work_days_no_count_each_month += 1
                        f_work_days_no_count_accumulate += 1
                    elif dict_weather_and_human_related_holiday[ obj_date ] == ScheduleCount.CountWorkingDay.COUNT_HALF_DAY:
                        f_work_days_no_count_each_month += 0.5
                        f_work_days_no_count_accumulate += 0.5
                        f_work_days_used_each_month += 0.5
                        f_work_days_used_accumulate += 0.5
                    else:
                        f_work_days_used_each_month += 1
                        f_work_days_used_accumulate += 1
                        pass
                else:
                    f_work_days_used_each_month += 1
                    f_work_days_used_accumulate += 1
            else:
                f_work_days_no_count_each_month += 1
                f_work_days_no_count_accumulate += 1

            f_rest_work_days = n_total_work_days - f_work_days_used_accumulate

            f_calendar_days_used_each_month += 1
            f_calendar_days_used_accumulate += 1

        if b_is_weekend[0]:
            if g_draw_triangle_for_weekend:
                Utility.insert_image( worksheet, Utility.image_path_holiday, up_marker, Utility.whole_size )
        elif b_is_holiday[0]:
            Utility.insert_image( worksheet, Utility.image_path_holiday, up_marker, Utility.whole_size )
        elif b_is_make_up_workday[0]:
            Utility.insert_image( worksheet, Utility.image_path_workday, up_marker, Utility.whole_size )

        if obj_date == obj_real_finish_date['ExpectFinishDate']:
            Utility.insert_image( worksheet, Utility.image_path_expect_finish_day, up_marker, Utility.whole_size )

        # region 定義要填入的欄位
        str_cell_calendar_days_each_month = None                     #天數(每月) A 欄位"AM"
        str_cell_calendar_days_accumulate = None                     #天數(累計) A 欄位"AM"
        str_cell_calendar_days_accumulate_final = None               #天數(年總計) A 欄位"AM"
        str_cell_weekend_days_each_month = None                      #星期例假(每月) B1 欄位"AN"
        str_cell_weekend_days_accumulate = None                      #星期例假(累計) B1 欄位"AN"
        str_cell_weekend_days_accumulate_final = None                #星期例假(年總計) B1 欄位"AN"
        str_cell_holiday_days_each_month = None                      #國定例假(每月) B2 欄位"AO"
        str_cell_holiday_days_accumulate = None                      #國定例假(累計) B2 欄位"AO"
        str_cell_holiday_days_accumulate_final = None                #國定例假(年總計) B2 欄位"AO"
        str_cell_no_count_days_each_month = None                     #不計工期(每月) B0 欄位"AP"
        str_cell_no_count_days_accumulate = None                     #不計工期(累計) B0 欄位"AP"
        str_cell_no_count_days_accumulate_final = None               #不計工期(年總計) B0 欄位"AP"

        str_cell_suspend_work_days_each_month = None                 #停工(每月) C1 欄位"AQ"
        str_cell_suspend_work_days_accumulate = None                 #停工(累計) C1 欄位"AQ"
        str_cell_suspend_work_days_accumulate_final = None           #停工(年總計) C1 欄位"AQ"
        str_cell_suspend_work_days_no_count_each_month = None        #停工且不計工期(每月) C1 欄位"AR"
        str_cell_suspend_work_days_no_count_accumulate = None        #停工且不計工期(累計) C1 欄位"AR"
        str_cell_suspend_work_days_no_count_accumulate_final = None  #停工且不計工期(年總計) C1 欄位"AR"

        str_cell_sun_days_each_month = None                          #晴天(每月) D1 欄位"AS"
        str_cell_sun_days_accumulate = None                          #晴天(累計) D1 欄位"AS"
        str_cell_sun_days_accumulate_final = None                    #晴天(年總計) D1 欄位"AS"
        str_cell_rain_days_each_month = None                         #雨天(每月) D2 欄位"AT"
        str_cell_rain_days_accumulate = None                         #雨天(累計) D2 欄位"AT"
        str_cell_rain_days_accumulate_final = None                   #雨天(年總計) D2 欄位"AT"
        str_cell_rain_days_no_count_each_month = None                #雨天且不計工期(每月) D2 欄位"AU"
        str_cell_rain_days_no_count_accumulate = None                #雨天且不計工期(累計) D2 欄位"AU"
        str_cell_rain_days_no_count_accumulate_final = None          #雨天且不計工期(年總計) D2 欄位"AU"
        str_cell_heavy_rain_days_each_month = None                   #豪雨(每月) D3 欄位"AV"
        str_cell_heavy_rain_days_accumulate = None                   #豪雨(累計) D3 欄位"AV"
        str_cell_heavy_rain_days_accumulate_final = None             #豪雨(年總計) D3 欄位"AV"
        str_cell_heavy_rain_days_no_count_each_month = None          #豪雨且不計工期(每月) D3 欄位"AW"
        str_cell_heavy_rain_days_no_count_accumulate = None          #豪雨且不計工期(累計) D3 欄位"AW"
        str_cell_heavy_rain_days_no_count_accumulate_final = None    #豪雨且不計工期(年總計) D3 欄位"AW"
        str_cell_typhoon_days_each_month = None                      #颱風(每月) D4 欄位"AX"
        str_cell_typhoon_days_accumulate = None                      #颱風(累計) D4 欄位"AX"
        str_cell_typhoon_days_accumulate_final = None                #颱風(年總計) D4 欄位"AX"
        str_cell_typhoon_days_no_count_each_month = None             #颱風且不計工期(每月) D4 欄位"AY"
        str_cell_typhoon_days_no_count_accumulate = None             #颱風且不計工期(累計) D4 欄位"AY"
        str_cell_typhoon_days_no_count_accumulate_final = None       #颱風且不計工期(年總計) D4 欄位"AY"
        str_cell_hot_days_each_month = None                          #酷熱(每月) D5 欄位"AZ"
        str_cell_hot_days_accumulate = None                          #酷熱(累計) D5 欄位"AZ"
        str_cell_hot_days_accumulate_final = None                    #酷熱(年總計) D5 欄位"AZ"
        str_cell_hot_days_no_count_each_month = None                 #酷熱且不計工期(每月) D5 欄位"BA"
        str_cell_hot_days_no_count_accumulate = None                 #酷熱且不計工期(累計) D5 欄位"BA"
        str_cell_hot_days_no_count_accumulate_final = None           #酷熱且不計工期(年總計) D5 欄位"BA"
        str_cell_muddy_days_each_month = None                        #雨後泥濘(每月) D6 欄位"BB"
        str_cell_muddy_days_accumulate = None                        #雨後泥濘(累計) D6 欄位"BB"
        str_cell_muddy_days_accumulate_final = None                  #雨後泥濘(年總計) D6 欄位"BB"
        str_cell_muddy_days_no_count_each_month = None               #雨後泥濘且不計工期(每月) D6 欄位"BC"
        str_cell_muddy_days_no_count_accumulate = None               #雨後泥濘且不計工期(累計) D6 欄位"BC"
        str_cell_muddy_days_no_count_accumulate_final = None         #雨後泥濘且不計工期(年總計) D6 欄位"BC"
        str_cell_weather_other_days_each_month = None                #天候其他因素(每月) D7 欄位"BD"
        str_cell_weather_other_days_accumulate = None                #天候其他因素(累計) D7 欄位"BD"
        str_cell_weather_other_days_accumulate_final = None          #天候其他因素(年總計) D7 欄位"BD"
        str_cell_weather_other_days_no_count_each_month = None       #天候其他因素且不計工期(每月) D7 欄位"BE"
        str_cell_weather_other_days_no_count_accumulate = None       #天候其他因素且不計工期(累計) D7 欄位"BE"
        str_cell_weather_other_days_no_count_accumulate_final = None #天候其他因素且不計工期(年總計) D7 欄位"BE"
        str_cell_weather_no_count_days_each_month = None             #天候不計工期(每月) D0 欄位"BF"
        str_cell_weather_no_count_days_accumulate = None             #天候不計工期(累計) D0 欄位"BF"
        str_cell_weather_no_count_days_accumulate_final = None       #天候不計工期(年總計) D0 欄位"BF"

        str_cell_power_off_days_each_month = None                    #停電(每月) E1 欄位"BG"
        str_cell_power_off_days_accumulate = None                    #停電(累計) E1 欄位"BG"
        str_cell_power_off_days_accumulate_final = None              #停電(年總計) E1 欄位"BG"
        str_cell_power_off_days_no_count_each_month = None           #停電且不計工期(每月) E1 欄位"BH"
        str_cell_power_off_days_no_count_accumulate = None           #停電且不計工期(累計) E1 欄位"BH"
        str_cell_power_off_days_no_count_accumulate_final = None     #停電且不計工期(年總計) E1 欄位"BH"
        str_cell_human_other_days_each_month = None                  #人為其他因素(每月) E2 欄位"BI"
        str_cell_human_other_days_accumulate = None                  #人為其他因素(累計) E2 欄位"BI"
        str_cell_human_other_days_accumulate_final = None            #人為其他因素(年總計) E2 欄位"BI"
        str_cell_human_other_days_no_count_each_month = None         #人為其他因素且不計工期(每月) E2 欄位"BJ"
        str_cell_human_other_days_no_count_accumulate = None         #人為其他因素且不計工期(累計) E2 欄位"BJ"
        str_cell_human_other_days_no_count_accumulate_final = None   #人為其他因素且不計工期(年總計) E2 欄位"BJ"
        str_cell_human_no_count_days_each_month = None               #人為不計工期(每月) E0 欄位"BK"
        str_cell_human_no_count_days_accumulate = None               #人為不計工期(累計) E0 欄位"BK" 
        str_cell_human_no_count_days_accumulate_final = None         #人為不計工期(年總計) E0 欄位"BK"

        str_cell_total_work_days_days = None                         #合約工期 F1 欄位"BL"
        str_cell_work_days_no_count_each_month = None                #不計工期(每月) F0 欄位"BM"
        str_cell_work_days_no_count_accumulate = None                #不計工期(累計) F0 欄位"BM"
        str_cell_work_days_no_count_accumulate_final = None          #不計工期(年總計) F0 欄位"BM"
        str_cell_work_days_used_each_month = None                    #使用工期(每月) F2 欄位"BN"
        str_cell_work_days_used_accumulate = None                    #使用工期(累計) F2 欄位"BN"
        str_cell_work_days_used_accumulate_final = None              #使用工期(年總計) F2 欄位"BN"
        str_cell_rest_work_days = None                               #剩餘工期 F3 欄位"BO"
    
        str_cell_total_calendar_days = None                          #總天數 G1 欄位"BP"
        str_cell_calendar_days_used_each_month = None                #使用天數(每月) G2 欄位"BQ"
        str_cell_calendar_days_used_accumulate = None                #使用天數(累計) G2 欄位"BQ"
        str_cell_calendar_days_used_accumulate_final = None          #使用天數(年總計) G2 欄位"BQ"
        str_cell_rest_calendar_days = None                           #剩餘天數 G3 欄位"BR"
        # endregion

        n_each_month_row_count = 0
        n_accumulate_row_count = 0
        n_row_stride = 0
        str_accumulate_final = None
        if g_daily_report_type == Utility.DailyReportType.TYPE_A:
            n_each_month_row_count = 5
            n_accumulate_row_count = 6
            n_row_stride = 3
            str_accumulate_final = '45'
        elif g_daily_report_type == Utility.DailyReportType.TYPE_B:
            n_each_month_row_count = 4
            n_accumulate_row_count = 5
            n_row_stride = 4
            str_accumulate_final = '57'

        # 固定因素(固定例假日)
        str_cell_calendar_days_each_month                     = 'AM' + str( n_each_month_row_count + month * n_row_stride )
        str_cell_calendar_days_accumulate                     = 'AM' + str( n_accumulate_row_count + month * n_row_stride )
        str_cell_calendar_days_accumulate_final               = 'AM' + str_accumulate_final
        str_cell_weekend_days_each_month                      = 'AN' + str( n_each_month_row_count + month * n_row_stride )
        str_cell_weekend_days_accumulate                      = 'AN' + str( n_accumulate_row_count + month * n_row_stride )
        str_cell_weekend_days_accumulate_final                = 'AN' + str_accumulate_final
        str_cell_holiday_days_each_month                      = 'AO' + str( n_each_month_row_count + month * n_row_stride )
        str_cell_holiday_days_accumulate                      = 'AO' + str( n_accumulate_row_count + month * n_row_stride )
        str_cell_holiday_days_accumulate_final                = 'AO' + str_accumulate_final
        str_cell_no_count_days_each_month                     = 'AP' + str( n_each_month_row_count + month * n_row_stride )
        str_cell_no_count_days_accumulate                     = 'AP' + str( n_accumulate_row_count + month * n_row_stride )
        str_cell_no_count_days_accumulate_final               = 'AP' + str_accumulate_final

        # 變動因素(停工)
        str_cell_suspend_work_days_each_month                 = 'AQ' + str( n_each_month_row_count + month * n_row_stride )
        str_cell_suspend_work_days_accumulate                 = 'AQ' + str( n_accumulate_row_count + month * n_row_stride )
        str_cell_suspend_work_days_accumulate_final           = 'AQ' + str_accumulate_final
        str_cell_suspend_work_days_no_count_each_month        = 'AR' + str( n_each_month_row_count + month * n_row_stride )
        str_cell_suspend_work_days_no_count_accumulate        = 'AR' + str( n_accumulate_row_count + month * n_row_stride )
        str_cell_suspend_work_days_no_count_accumulate_final  = 'AR' + str_accumulate_final

        # 變動因素(天候)
        str_cell_sun_days_each_month                          = 'AS' + str( n_each_month_row_count + month * n_row_stride )
        str_cell_sun_days_accumulate                          = 'AS' + str( n_accumulate_row_count + month * n_row_stride )
        str_cell_sun_days_accumulate_final                    = 'AS' + str_accumulate_final
        str_cell_rain_days_each_month                         = 'AT' + str( n_each_month_row_count + month * n_row_stride )
        str_cell_rain_days_accumulate                         = 'AT' + str( n_accumulate_row_count + month * n_row_stride )
        str_cell_rain_days_accumulate_final                   = 'AT' + str_accumulate_final
        str_cell_rain_days_no_count_each_month                = 'AU' + str( n_each_month_row_count + month * n_row_stride )
        str_cell_rain_days_no_count_accumulate                = 'AU' + str( n_accumulate_row_count + month * n_row_stride )
        str_cell_rain_days_no_count_accumulate_final          = 'AU' + str_accumulate_final
        str_cell_heavy_rain_days_each_month                   = 'AV' + str( n_each_month_row_count + month * n_row_stride )
        str_cell_heavy_rain_days_accumulate                   = 'AV' + str( n_accumulate_row_count + month * n_row_stride )
        str_cell_heavy_rain_days_accumulate_final             = 'AV' + str_accumulate_final
        str_cell_heavy_rain_days_no_count_each_month          = 'AW' + str( n_each_month_row_count + month * n_row_stride )
        str_cell_heavy_rain_days_no_count_accumulate          = 'AW' + str( n_accumulate_row_count + month * n_row_stride )
        str_cell_heavy_rain_days_no_count_accumulate_final    = 'AW' + str_accumulate_final
        str_cell_typhoon_days_each_month                      = 'AX' + str( n_each_month_row_count + month * n_row_stride )
        str_cell_typhoon_days_accumulate                      = 'AX' + str( n_accumulate_row_count + month * n_row_stride )
        str_cell_typhoon_days_accumulate_final                = 'AX' + str_accumulate_final
        str_cell_typhoon_days_no_count_each_month             = 'AY' + str( n_each_month_row_count + month * n_row_stride )
        str_cell_typhoon_days_no_count_accumulate             = 'AY' + str( n_accumulate_row_count + month * n_row_stride )
        str_cell_typhoon_days_no_count_accumulate_final       = 'AY' + str_accumulate_final
        str_cell_hot_days_each_month                          = 'AZ' + str( n_each_month_row_count + month * n_row_stride )
        str_cell_hot_days_accumulate                          = 'AZ' + str( n_accumulate_row_count + month * n_row_stride )
        str_cell_hot_days_accumulate_final                    = 'AZ' + str_accumulate_final
        str_cell_hot_days_no_count_each_month                 = 'BA' + str( n_each_month_row_count + month * n_row_stride )
        str_cell_hot_days_no_count_accumulate                 = 'BA' + str( n_accumulate_row_count + month * n_row_stride )
        str_cell_hot_days_no_count_accumulate_final           = 'BA' + str_accumulate_final
        str_cell_muddy_days_each_month                        = 'BB' + str( n_each_month_row_count + month * n_row_stride )
        str_cell_muddy_days_accumulate                        = 'BB' + str( n_accumulate_row_count + month * n_row_stride )
        str_cell_muddy_days_accumulate_final                  = 'BB' + str_accumulate_final
        str_cell_muddy_days_no_count_each_month               = 'BC' + str( n_each_month_row_count + month * n_row_stride )
        str_cell_muddy_days_no_count_accumulate               = 'BC' + str( n_accumulate_row_count + month * n_row_stride )
        str_cell_muddy_days_no_count_accumulate_final         = 'BC' + str_accumulate_final
        str_cell_weather_other_days_each_month                = 'BD' + str( n_each_month_row_count + month * n_row_stride )
        str_cell_weather_other_days_accumulate                = 'BD' + str( n_accumulate_row_count + month * n_row_stride )
        str_cell_weather_other_days_accumulate_final          = 'BD' + str_accumulate_final
        str_cell_weather_other_days_no_count_each_month       = 'BE' + str( n_each_month_row_count + month * n_row_stride )
        str_cell_weather_other_days_no_count_accumulate       = 'BE' + str( n_accumulate_row_count + month * n_row_stride )
        str_cell_weather_other_days_no_count_accumulate_final = 'BE' + str_accumulate_final
        str_cell_weather_no_count_days_each_month             = 'BF' + str( n_each_month_row_count + month * n_row_stride )
        str_cell_weather_no_count_days_accumulate             = 'BF' + str( n_accumulate_row_count + month * n_row_stride )
        str_cell_weather_no_count_days_accumulate_final       = 'BF' + str_accumulate_final

        # 變動因素(停電…等)
        str_cell_power_off_days_each_month                    = 'BG' + str( n_each_month_row_count + month * n_row_stride )
        str_cell_power_off_days_accumulate                    = 'BG' + str( n_accumulate_row_count + month * n_row_stride )
        str_cell_power_off_days_accumulate_final              = 'BG' + str_accumulate_final
        str_cell_power_off_days_no_count_each_month           = 'BH' + str( n_each_month_row_count + month * n_row_stride )
        str_cell_power_off_days_no_count_accumulate           = 'BH' + str( n_accumulate_row_count + month * n_row_stride )
        str_cell_power_off_days_no_count_accumulate_final     = 'BH' + str_accumulate_final
        str_cell_human_other_days_each_month                  = 'BI' + str( n_each_month_row_count + month * n_row_stride )
        str_cell_human_other_days_accumulate                  = 'BI' + str( n_accumulate_row_count + month * n_row_stride )
        str_cell_human_other_days_accumulate_final            = 'BI' + str_accumulate_final
        str_cell_human_other_days_no_count_each_month         = 'BJ' + str( n_each_month_row_count + month * n_row_stride )
        str_cell_human_other_days_no_count_accumulate         = 'BJ' + str( n_accumulate_row_count + month * n_row_stride )
        str_cell_human_other_days_no_count_accumulate_final   = 'BJ' + str_accumulate_final
        str_cell_human_no_count_days_each_month               = 'BK' + str( n_each_month_row_count + month * n_row_stride )
        str_cell_human_no_count_days_accumulate               = 'BK' + str( n_accumulate_row_count + month * n_row_stride )
        str_cell_human_no_count_days_accumulate_final         = 'BK' + str_accumulate_final
        
        # 工期
        str_cell_total_work_days_days                         = 'BL' + str( n_each_month_row_count + month * n_row_stride )
        str_cell_work_days_no_count_each_month                = 'BM' + str( n_each_month_row_count + month * n_row_stride )
        str_cell_work_days_no_count_accumulate                = 'BM' + str( n_accumulate_row_count + month * n_row_stride )
        str_cell_work_days_no_count_accumulate_final          = 'BM' + str_accumulate_final
        str_cell_work_days_used_each_month                    = 'BN' + str( n_each_month_row_count + month * n_row_stride )
        str_cell_work_days_used_accumulate                    = 'BN' + str( n_accumulate_row_count + month * n_row_stride )
        str_cell_work_days_used_accumulate_final              = 'BN' + str_accumulate_final
        str_cell_rest_work_days                               = 'BO' + str( n_each_month_row_count + month * n_row_stride )
        
        # 天數
        str_cell_total_calendar_days                          = 'BP' + str( n_each_month_row_count + month * n_row_stride )
        str_cell_calendar_days_used_each_month                = 'BQ' + str( n_each_month_row_count + month * n_row_stride )
        str_cell_calendar_days_used_accumulate                = 'BQ' + str( n_accumulate_row_count + month * n_row_stride )
        str_cell_calendar_days_used_accumulate_final          = 'BQ' + str_accumulate_final
        str_cell_rest_calendar_days                           = 'BR' + str( n_each_month_row_count + month * n_row_stride )


        obj_date_add_1 = obj_date + datetime.timedelta(days=1)

        if obj_date.year != obj_date_add_1.year:
            worksheet[ str_cell_calendar_days_accumulate_final ] = n_calendar_days_accumulate
            worksheet[ str_cell_weekend_days_accumulate_final ] = n_weekend_days_accumulate
            worksheet[ str_cell_holiday_days_accumulate_final ] = n_holiday_days_accumulate
            worksheet[ str_cell_no_count_days_accumulate_final ] = n_no_count_days_accumulate

            worksheet[ str_cell_sun_days_accumulate_final ] = f_sun_days_accumulate
            worksheet[ str_cell_rain_days_accumulate_final ] = f_rain_days_accumulate
            worksheet[ str_cell_rain_days_no_count_accumulate_final ] = f_rain_days_no_count_accumulate
            worksheet[ str_cell_rain_days_accumulate_final ] = f_rain_days_accumulate
            worksheet[ str_cell_heavy_rain_days_accumulate_final ] = f_heavy_rain_days_accumulate
            worksheet[ str_cell_heavy_rain_days_no_count_accumulate_final ] = f_heavy_rain_days_no_count_accumulate
            worksheet[ str_cell_typhoon_days_accumulate_final ] = f_typhoon_days_accumulate
            worksheet[ str_cell_typhoon_days_no_count_accumulate_final ] = f_typhoon_days_no_count_accumulate
            worksheet[ str_cell_hot_days_accumulate_final ] = f_hot_days_accumulate
            worksheet[ str_cell_hot_days_no_count_accumulate_final ] = f_hot_days_no_count_accumulate
            worksheet[ str_cell_muddy_days_accumulate_final ] = f_muddy_days_accumulate
            worksheet[ str_cell_muddy_days_no_count_accumulate_final ] = f_muddy_days_no_count_accumulate
            worksheet[ str_cell_weather_other_days_accumulate_final ] = f_weather_other_days_accumulate
            worksheet[ str_cell_weather_other_days_no_count_accumulate_final ] = f_weather_other_days_no_count_accumulate
            worksheet[ str_cell_weather_no_count_days_accumulate_final ] = f_weather_no_count_days_accumulate

            worksheet[ str_cell_suspend_work_days_accumulate_final ] = f_suspend_work_days_accumulate
            worksheet[ str_cell_suspend_work_days_no_count_accumulate_final ] = f_suspend_work_days_no_count_accumulate
            worksheet[ str_cell_power_off_days_accumulate_final ] = f_power_off_days_accumulate
            worksheet[ str_cell_power_off_days_no_count_accumulate_final ] = f_power_off_days_no_count_accumulate
            worksheet[ str_cell_human_other_days_accumulate_final ] = f_human_other_days_accumulate
            worksheet[ str_cell_human_other_days_no_count_accumulate_final ] = f_human_other_days_no_count_accumulate
            worksheet[ str_cell_human_no_count_days_accumulate_final ] = f_human_no_count_days_accumulate

            worksheet[ str_cell_work_days_no_count_accumulate_final ] = f_work_days_no_count_accumulate
            worksheet[ str_cell_work_days_used_accumulate_final ] = f_work_days_used_accumulate
            worksheet[ str_cell_calendar_days_used_accumulate_final ] = f_calendar_days_used_accumulate

        #填入晴天/雨天/...停工/停電等欄位數值
        if obj_date.month != obj_date_add_1.month:
            #固定因素
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

        if ( obj_date.month != obj_date_add_1.month and obj_date <= obj_current_date ) or obj_date == obj_current_date:
            #變動因素(天候)
            worksheet[ str_cell_sun_days_each_month ]                    = f_sun_days_each_month
            worksheet[ str_cell_sun_days_accumulate ]                    = f_sun_days_accumulate
            worksheet[ str_cell_rain_days_each_month ]                   = f_rain_days_each_month
            worksheet[ str_cell_rain_days_accumulate ]                   = f_rain_days_accumulate
            worksheet[ str_cell_rain_days_no_count_each_month ]          = f_rain_days_no_count_each_month
            worksheet[ str_cell_rain_days_no_count_accumulate ]          = f_rain_days_no_count_accumulate
            worksheet[ str_cell_heavy_rain_days_each_month ]             = f_heavy_rain_days_each_month
            worksheet[ str_cell_heavy_rain_days_accumulate ]             = f_heavy_rain_days_accumulate
            worksheet[ str_cell_heavy_rain_days_no_count_each_month ]    = f_heavy_rain_days_no_count_each_month
            worksheet[ str_cell_heavy_rain_days_no_count_accumulate ]    = f_heavy_rain_days_no_count_accumulate
            worksheet[ str_cell_typhoon_days_each_month ]                = f_typhoon_days_each_month
            worksheet[ str_cell_typhoon_days_accumulate ]                = f_typhoon_days_accumulate
            worksheet[ str_cell_typhoon_days_no_count_each_month ]       = f_typhoon_days_no_count_each_month
            worksheet[ str_cell_typhoon_days_no_count_accumulate ]       = f_typhoon_days_no_count_accumulate
            worksheet[ str_cell_hot_days_each_month ]                    = f_hot_days_each_month
            worksheet[ str_cell_hot_days_accumulate ]                    = f_hot_days_accumulate
            worksheet[ str_cell_hot_days_no_count_each_month ]           = f_hot_days_no_count_each_month
            worksheet[ str_cell_hot_days_no_count_accumulate ]           = f_hot_days_no_count_accumulate
            worksheet[ str_cell_muddy_days_each_month ]                  = f_muddy_days_each_month
            worksheet[ str_cell_muddy_days_accumulate ]                  = f_muddy_days_accumulate
            worksheet[ str_cell_muddy_days_no_count_each_month ]         = f_muddy_days_no_count_each_month
            worksheet[ str_cell_muddy_days_no_count_accumulate ]         = f_muddy_days_no_count_accumulate
            worksheet[ str_cell_weather_other_days_each_month ]          = f_weather_other_days_each_month
            worksheet[ str_cell_weather_other_days_accumulate ]          = f_weather_other_days_accumulate
            worksheet[ str_cell_weather_other_days_no_count_each_month ] = f_weather_other_days_no_count_each_month
            worksheet[ str_cell_weather_other_days_no_count_accumulate ] = f_weather_other_days_no_count_accumulate
            worksheet[ str_cell_weather_no_count_days_each_month ]       = f_weather_no_count_days_each_month
            worksheet[ str_cell_weather_no_count_days_accumulate ]       = f_weather_no_count_days_accumulate
            #變動因素(人為)
            worksheet[ str_cell_suspend_work_days_each_month ]           = f_suspend_work_days_each_month
            worksheet[ str_cell_suspend_work_days_accumulate ]           = f_suspend_work_days_accumulate
            worksheet[ str_cell_suspend_work_days_no_count_each_month ]  = f_suspend_work_days_no_count_each_month
            worksheet[ str_cell_suspend_work_days_no_count_accumulate ]  = f_suspend_work_days_no_count_accumulate
            worksheet[ str_cell_power_off_days_each_month ]              = f_power_off_days_each_month
            worksheet[ str_cell_power_off_days_accumulate ]              = f_power_off_days_accumulate
            worksheet[ str_cell_power_off_days_no_count_each_month ]     = f_power_off_days_no_count_each_month
            worksheet[ str_cell_power_off_days_no_count_accumulate ]     = f_power_off_days_no_count_accumulate
            worksheet[ str_cell_human_other_days_each_month ]            = f_human_other_days_each_month
            worksheet[ str_cell_human_other_days_accumulate ]            = f_human_other_days_accumulate
            worksheet[ str_cell_human_other_days_no_count_each_month ]   = f_human_other_days_no_count_each_month
            worksheet[ str_cell_human_other_days_no_count_accumulate ]   = f_human_other_days_no_count_accumulate
            worksheet[ str_cell_human_no_count_days_each_month ]         = f_human_no_count_days_each_month
            worksheet[ str_cell_human_no_count_days_accumulate ]         = f_human_no_count_days_accumulate

            worksheet[ str_cell_total_work_days_days ]                   = n_total_work_days #合約工期 F1
            worksheet[ str_cell_work_days_no_count_each_month ]          = f_work_days_no_count_each_month #不計工期(每月) F0
            worksheet[ str_cell_work_days_no_count_accumulate ]          = f_work_days_no_count_accumulate #不計工期(累計) F0
            worksheet[ str_cell_work_days_used_each_month ]              = f_work_days_used_each_month #使用工期(每月) F2
            worksheet[ str_cell_work_days_used_accumulate ]              = f_work_days_used_accumulate #使用工期(累計) F2
            worksheet[ str_cell_rest_work_days ]                         = f_rest_work_days #剩餘工期 F3
        
            temp_real_finish_date = ScheduleCount.func_count_real_finish_date( e_count_type, n_expect_total_workdays, obj_start_date, obj_date, arr_const_holiday, arr_const_workday, dict_weather_and_human_related_holiday, dict_extend_data )
            worksheet[ str_cell_total_calendar_days ]                    = temp_real_finish_date['RealTotalCalendarDays'] #總天數 G1
            worksheet[ str_cell_calendar_days_used_each_month ]          = f_calendar_days_used_each_month #使用天數(每月) G2
            worksheet[ str_cell_calendar_days_used_accumulate ]          = f_calendar_days_used_accumulate #使用天數(累計) G2
            worksheet[ str_cell_rest_calendar_days ]                     = temp_real_finish_date['RealTotalCalendarDays'] - f_calendar_days_used_accumulate #剩餘天數 F3 

            f_sun_days_each_month = 0
            f_rain_days_each_month = 0
            f_rain_days_no_count_each_month = 0
            f_heavy_rain_days_each_month = 0
            f_heavy_rain_days_no_count_each_month = 0
            f_typhoon_days_each_month = 0
            f_typhoon_days_no_count_each_month = 0
            f_hot_days_each_month = 0
            f_hot_days_no_count_each_month = 0
            f_muddy_days_each_month = 0
            f_muddy_days_no_count_each_month = 0
            f_weather_other_days_each_month = 0
            f_weather_other_days_no_count_each_month = 0
            f_weather_no_count_days_each_month = 0

            f_suspend_work_days_each_month = 0
            f_suspend_work_days_no_count_each_month = 0
            f_power_off_days_each_month = 0
            f_power_off_days_no_count_each_month = 0
            f_human_other_days_each_month = 0
            f_human_other_days_no_count_each_month = 0
            f_human_no_count_days_each_month = 0

            f_work_days_no_count_each_month = 0
            f_work_days_used_each_month = 0
            f_calendar_days_used_each_month = 0


        if obj_date == obj_real_finish_date['RealFinishDate']:
            Utility.insert_image( worksheet, Utility.image_path_real_finish_day, up_marker, Utility.whole_size )
            if n_calendar_days_each_month != 0:
                #固定因素
                worksheet[ str_cell_calendar_days_each_month ] = n_calendar_days_each_month #A
                worksheet[ str_cell_calendar_days_accumulate ] = n_calendar_days_accumulate
                worksheet[ str_cell_weekend_days_each_month ]  = n_weekend_days_each_month #B1
                worksheet[ str_cell_weekend_days_accumulate ]  = n_weekend_days_accumulate
                worksheet[ str_cell_holiday_days_each_month ]  = n_holiday_days_each_month #B2
                worksheet[ str_cell_holiday_days_accumulate ]  = n_holiday_days_accumulate
                worksheet[ str_cell_no_count_days_each_month ] = n_no_count_days_each_month #B0
                worksheet[ str_cell_no_count_days_accumulate ] = n_no_count_days_accumulate

                worksheet[ str_cell_calendar_days_accumulate_final ] = n_calendar_days_accumulate
                worksheet[ str_cell_weekend_days_accumulate_final ] = n_weekend_days_accumulate
                worksheet[ str_cell_holiday_days_accumulate_final ] = n_holiday_days_accumulate
                worksheet[ str_cell_no_count_days_accumulate_final ] = n_no_count_days_accumulate

                worksheet[ str_cell_sun_days_accumulate_final ] = f_sun_days_accumulate
                worksheet[ str_cell_rain_days_accumulate_final ] = f_rain_days_accumulate
                worksheet[ str_cell_rain_days_no_count_accumulate_final ] = f_rain_days_no_count_accumulate
                worksheet[ str_cell_rain_days_accumulate_final ] = f_rain_days_accumulate
                worksheet[ str_cell_heavy_rain_days_accumulate_final ] = f_heavy_rain_days_accumulate
                worksheet[ str_cell_heavy_rain_days_no_count_accumulate_final ] = f_heavy_rain_days_no_count_accumulate
                worksheet[ str_cell_typhoon_days_accumulate_final ] = f_typhoon_days_accumulate
                worksheet[ str_cell_typhoon_days_no_count_accumulate_final ] = f_typhoon_days_no_count_accumulate
                worksheet[ str_cell_hot_days_accumulate_final ] = f_hot_days_accumulate
                worksheet[ str_cell_hot_days_no_count_accumulate_final ] = f_hot_days_no_count_accumulate
                worksheet[ str_cell_muddy_days_accumulate_final ] = f_muddy_days_accumulate
                worksheet[ str_cell_muddy_days_no_count_accumulate_final ] = f_muddy_days_no_count_accumulate
                worksheet[ str_cell_weather_other_days_accumulate_final ] = f_weather_other_days_accumulate
                worksheet[ str_cell_weather_other_days_no_count_accumulate_final ] = f_weather_other_days_no_count_accumulate
                worksheet[ str_cell_weather_no_count_days_accumulate_final ] = f_weather_no_count_days_accumulate

                worksheet[ str_cell_suspend_work_days_accumulate_final ] = f_suspend_work_days_accumulate
                worksheet[ str_cell_suspend_work_days_no_count_accumulate_final ] = f_suspend_work_days_no_count_accumulate
                worksheet[ str_cell_power_off_days_accumulate_final ] = f_power_off_days_accumulate
                worksheet[ str_cell_power_off_days_no_count_accumulate_final ] = f_power_off_days_no_count_accumulate
                worksheet[ str_cell_human_other_days_accumulate_final ] = f_human_other_days_accumulate
                worksheet[ str_cell_human_other_days_no_count_accumulate_final ] = f_human_other_days_no_count_accumulate
                worksheet[ str_cell_human_no_count_days_accumulate_final ] = f_human_no_count_days_accumulate

                worksheet[ str_cell_work_days_no_count_accumulate_final ] = f_work_days_no_count_accumulate
                worksheet[ str_cell_work_days_used_accumulate_final ] = f_work_days_used_accumulate
                worksheet[ str_cell_calendar_days_used_accumulate_final ] = f_calendar_days_used_accumulate
            break

        obj_date += datetime.timedelta(days=1)


    worksheet = workbook.worksheets[0]
    obj_cell_num = func_get_cell_num( obj_start_date )
    column = obj_cell_num['ColumnNum']-1
    row = obj_cell_num['RowNum']-1
    up_marker = AnchorMarker(col=column, colOff=Utility.col_offset, row=row, rowOff=Utility.row_up_offset)
    Utility.insert_image( worksheet, Utility.image_path_start_day, up_marker, Utility.whole_size)

    n_worksheet_index = 0
    for n_year in range( n_start_year, n_end_year + 1 ):
        worksheet = workbook.worksheets[ n_worksheet_index ]
        func_fill_in_day_each_month( worksheet, n_year )
        n_worksheet_index += 1

    #填入當月天數及固定因素



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


# func_create_weather_report_form(ScheduleCount.WorkDay.TWO_DAY_OFF, 411, datetime.datetime.strptime('2023-01-06', "%Y-%m-%d"), datetime.datetime.strptime('2023-11-16', "%Y-%m-%d") )
