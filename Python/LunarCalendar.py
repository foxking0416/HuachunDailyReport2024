import lunarcalendar
import datetime
import json
import os
from lunarcalendar.converter import Converter, Solar, Lunar

global_dict_lunar_holiday = {}

def func_load_lunar_holiday_data():
    current_dir = os.path.dirname(__file__)
    json_file_path = os.path.join( current_dir, 'ExternalData\\LunarHoliday.json' )

    with open( json_file_path,'r', encoding='utf-8' ) as f:
        data = json.load( f )

    for item in data:
        global_dict_lunar_holiday[ item[ "date" ] ] = item[ "reason" ]


def func_get_lunar_reason( solar_datetime ):
    lunar_date = Converter.Solar2Lunar( solar_datetime )

    for item in global_dict_lunar_holiday:
        parts = item.split('-')
        month = int( parts[0] )
        day = int( parts[1] )
        if lunar_date.month == month and lunar_date.day == day:
            return global_dict_lunar_holiday[ item ]

    return None


# func_load_lunar_holiday_data()
# print( func_convert_solar_to_lunar(datetime.datetime.strptime( '2024-02-24', "%Y-%m-%d" )) )