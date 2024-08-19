import lunarcalendar
import datetime
import json
import os
from lunarcalendar.converter import Converter, Solar, Lunar

global_dict_lunar_holiday = {}
global_dict_solar_holiday = {}

def func_load_lunar_holiday_data():
    current_dir = os.path.dirname(__file__)
    json_file_path = os.path.join( current_dir, 'ExternalData\\LunarHoliday.json' )

    with open( json_file_path,'r', encoding='utf-8' ) as f:
        data = json.load( f )

    for item in data:
        global_dict_lunar_holiday[ item[ "date" ] ] = item[ "reason" ]


def func_get_lunar_reason( solar_datetime ):
    lunar_date = Converter.Solar2Lunar( solar_datetime )
    lunar_date_sub_1 = Converter.Solar2Lunar( solar_datetime - datetime.timedelta(days=1) )

    for item in global_dict_lunar_holiday:
        parts = item.split('-')
        month = int( parts[0] )
        day = int( parts[1] )
        if lunar_date.month == month and lunar_date.day == day:
            return global_dict_lunar_holiday[ item ]
        if lunar_date.month != lunar_date_sub_1.month:
            if lunar_date.month == 1:
                return '正月'
            elif lunar_date.month == 2:
                return '二月'
            elif lunar_date.month == 3:
                return '三月'
            elif lunar_date.month == 4:
                return '四月'
            elif lunar_date.month == 5:
                return '五月'
            elif lunar_date.month == 6:
                return '六月'
            elif lunar_date.month == 7:
                return '七月'
            elif lunar_date.month == 8:
                return '八月'
            elif lunar_date.month == 9:
                return '九月'
            elif lunar_date.month == 10:
                return '十月'
            elif lunar_date.month == 11:
                return '十一月'
            elif lunar_date.month == 12:
                return '十二月'
        elif lunar_date.day == 15:
            return '十五'

    return None


def func_load_solar_holiday_data():
    current_dir = os.path.dirname(__file__)
    json_file_path = os.path.join( current_dir, 'ExternalData\\SolarHoliday.json' )

    with open( json_file_path,'r', encoding='utf-8' ) as f:
        data = json.load( f )

    for item in data:
        global_dict_solar_holiday[ item[ "date" ] ] = item[ "reason" ]


def func_get_solar_reason( solar_datetime, dict_holiday_reason ):

    for key, value in dict_holiday_reason.items():
        if key == solar_datetime:
            return value

    for item in global_dict_solar_holiday:
        parts = item.split('-')
        month = int( parts[0] )
        day = int( parts[1] )
        if solar_datetime.month == month and solar_datetime.day == day:
            return global_dict_solar_holiday[ item ]

    return None

# func_load_lunar_holiday_data()
# print( func_convert_solar_to_lunar(datetime.datetime.strptime( '2024-02-24', "%Y-%m-%d" )) )