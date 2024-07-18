import json
import os
import datetime
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

# 從 Holiday.json 的檔案讀取補班或放假的資料
def func_load_json_holiday_data( arr_const_holiday, arr_const_workday ):
    # 取得目前工作目錄
    current_dir = os.path.dirname( __file__ )
    # 組合JSON檔案的路徑
    json_file_path = os.path.join( current_dir, 'ExternalData\\Holiday.json' )

    with open( json_file_path,'r', encoding='utf-8' ) as f:
        data = json.load( f )

    for item in data:
        if( item[ "holiday" ] ):
            arr_const_holiday.append( datetime.datetime.strptime( item[ "date" ], "%Y-%m-%d") )
        if(not item[ "holiday" ]):
            arr_const_workday.append( datetime.datetime.strptime( item[ "date" ], "%Y-%m-%d") )


# 從 ConditionSetting.json 的檔案讀取每日資料
def func_load_json_condition_setting_data( dict_morning_weather_condition_setting, dict_afternoon_weather_condition_setting ):
    current_dir = os.path.dirname( __file__ )
    json_file_path = os.path.join( current_dir, 'ExternalData\\ConditionSetting.json' )
    with open( json_file_path,'r', encoding='utf-8' ) as f:
        data = json.load( f )

    for item in data:
        weather_condition = item[ "weather_condition" ]
        dict_morning_weather_condition_setting[ weather_condition ] = item[ "morning_nocount" ]
        dict_afternoon_weather_condition_setting[ weather_condition ] = item[ "afternoon_nocount" ]

# 從 DailyReport.json 的檔案讀取每日資料
def func_load_json_daily_report_data( dict_weather_related_holiday ):

    dict_morning_weather_condition_setting = {}
    dict_afternoon_weather_condition_setting = {}
    func_load_json_condition_setting_data( dict_morning_weather_condition_setting, dict_afternoon_weather_condition_setting )

    current_dir = os.path.dirname( __file__ )
    json_file_path = os.path.join( current_dir, 'ExternalData\\DailyReport.json' )

    with open( json_file_path,'r', encoding='utf-8' ) as f:
        data = json.load( f )

    for item in data:
        obj_date = datetime.datetime.strptime( item[ "date" ], "%Y-%m-%d")

        n_morning_weather = item["morning_weather"]
        n_morning_other = item["morning_other"]
        n_afternoon_weather = item["afternoon_weather"]
        n_afternoon_other = item["afternoon_other"]
        f_nocount = 0
        if( n_morning_weather != 0 or n_morning_other != 0 ):
            if n_morning_weather in dict_morning_weather_condition_setting:
                f_morning_nocount = dict_morning_weather_condition_setting[ n_morning_weather ]

                if f_morning_nocount == 1:
                    dict_weather_related_holiday[ obj_date ] = CountWorkingDay.NO_COUNT
                    continue
                elif f_morning_nocount == 0.5:
                    f_nocount = 0.5

        if( n_afternoon_weather != 0 or n_afternoon_other != 0 ):
            if n_afternoon_weather in dict_afternoon_weather_condition_setting:
                f_afternoon_nocount = dict_afternoon_weather_condition_setting[ n_afternoon_weather ]

                if f_afternoon_nocount == 1:
                    dict_weather_related_holiday[ obj_date ] = CountWorkingDay.NO_COUNT
                    continue
                elif f_afternoon_nocount == 0.5:
                    f_nocount += 0.5

        if f_nocount == 0.5:
            dict_weather_related_holiday[ obj_date ] = CountWorkingDay.COUNT_HALF_DAY
        elif f_nocount == 1:
            dict_weather_related_holiday[ obj_date ] = CountWorkingDay.NO_COUNT

# 從 ExtendData.json 的檔案讀取每日資料
def func_load_json_extend_data(dict_extend_data):
    current_dir = os.path.dirname(__file__)
    json_file_path = os.path.join(current_dir, 'ExternalData\\ExtendData.json')

    with open(json_file_path,'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        dict_extend_data[ datetime.datetime.strptime( item[ "extend_start_date" ], "%Y-%m-%d") ] = item[ "extend_days" ]


#根據固定因素判斷是否為工作日
def func_check_is_work_day( arr_const_holiday, arr_const_workday, obj_date, n_weekday, e_count_type ):
    if obj_date in arr_const_holiday :
        return False
    elif obj_date in arr_const_workday:
        return True
    else:
        #周休一日
        if e_count_type == WorkDay.ONE_DAY_OFF and n_weekday != Weekday.SUNDAY.value:
            return True
        #周休二日
        elif e_count_type == WorkDay.TWO_DAY_OFF and n_weekday != Weekday.SATURDAY.value and n_weekday != Weekday.SUNDAY.value:
            return True
        #沒周休
        elif e_count_type == WorkDay.NO_DAY_OFF:
            return True

def func_count_expect_finish_date( e_count_type, n_expect_total_workdays, obj_start_date, arr_const_holiday, arr_const_workday ):
    obj_expect_end_date = obj_start_date

    while( True ):
        n_weekday = obj_expect_end_date.weekday()

        if func_check_is_work_day( arr_const_holiday, arr_const_workday, obj_expect_end_date, n_weekday, e_count_type ):
            n_expect_total_workdays -= 1

        if( n_expect_total_workdays <= 0 ):
            break

        obj_expect_end_date += datetime.timedelta( days = 1 )

    obj_return_value = {}
    obj_return_value[ 'ExpectFinishDate' ] = obj_expect_end_date
    obj_return_value[ 'ExpectTotalCalendarDays' ] = ( obj_expect_end_date - obj_start_date ).days + 1

    return obj_return_value
    

# e_count_type 工期計算方式 0:周休一日  1:周休二日  2:日曆天
# n_expect_total_workdays 工期天數
# obj_start_date 開工日，如 '2023-01-01'
# obj_today_date 今天日期，如 '2023-01-01'
# arr_const_holiday 固定因素放假日
# arr_const_workday 固定因素補班日
# dict_weather_related_holiday 因為天氣停工資料
# dict_extend_data 追加工期資料
def func_count_real_finish_date( e_count_type, n_expect_total_workdays, obj_start_date, obj_today_date, arr_const_holiday, arr_const_workday, dict_weather_related_holiday, dict_extend_data ):
    obj_real_end_date = obj_start_date 
    obj_expect_end_date = obj_start_date
    n_real_rest_workdays = n_expect_total_workdays
    n_expect_rest_workdays = n_expect_total_workdays

    n_past_workdays = 0
    n_total_extend_days = 0

    #讀入追加工期資料
    for key, value in dict_extend_data.items():
        obj_extend_start_date = key
        if obj_today_date >= obj_extend_start_date:
            n_total_extend_days += value

    n_real_rest_workdays += n_total_extend_days

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

    

    while( True ):
        n_weekday = obj_real_end_date.weekday()

        if func_check_is_work_day( arr_const_holiday, arr_const_workday, obj_real_end_date, n_weekday, e_count_type ):
            if obj_real_end_date <= obj_today_date:
                if obj_real_end_date in dict_weather_related_holiday:
                    if dict_weather_related_holiday[ obj_real_end_date ] == CountWorkingDay.NO_COUNT:
                        pass
                    elif dict_weather_related_holiday[ obj_real_end_date ] == CountWorkingDay.COUNT_HALF_DAY:
                        n_past_workdays += 0.5
                        n_real_rest_workdays -= 0.5
                    else:
                        n_past_workdays += 1
                        n_real_rest_workdays -= 1
                else:
                    n_past_workdays += 1
                    n_real_rest_workdays -= 1#沒填日報表就當作一般晴天
            else:
                n_real_rest_workdays -= 1#未來的日子還沒有日報表
            n_expect_rest_workdays -= 1

        if n_real_rest_workdays <= 0:
            break

        if n_expect_rest_workdays > 0:
            obj_expect_end_date += datetime.timedelta( days = 1 )

        obj_real_end_date += datetime.timedelta( days = 1 )


    # print('End Date : ' + kEndDate.strftime("%Y-%m-%d"))
    obj_return_value = {}
    obj_return_value['ExpectFinishDate']        = obj_expect_end_date
    obj_return_value['ExpectTotalCalendarDays'] = ( obj_expect_end_date - obj_start_date ).days + 1
    obj_return_value['RealFinishDate']          = obj_real_end_date
    obj_return_value['RealTotalCalendarDays']   = ( obj_real_end_date - obj_start_date ).days + 1
    obj_return_value['FromStartCalendarDays']   = ( obj_today_date - obj_start_date ).days + 1
    obj_return_value['FromStartWorkDays']       = n_past_workdays
    obj_return_value['ExpectRestWorkDays']      = n_expect_total_workdays - n_past_workdays
    obj_return_value['ExpectRestCalendarkDays'] = ( obj_expect_end_date - obj_today_date ).days
    obj_return_value['RealRestWorkDays']        = n_expect_total_workdays + n_total_extend_days - n_past_workdays
    obj_return_value['RealRestCalendarkDays']   = ( obj_real_end_date - obj_today_date ).days 

    return obj_return_value
