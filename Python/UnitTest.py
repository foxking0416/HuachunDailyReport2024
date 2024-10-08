import unittest
import ScheduleCount
import ExportExpectFinishForm
import ExportDailyReportForm
import datetime

arr_global_const_holiday = []
arr_global_const_workday = []
dict_holiday_reason = {}
dict_global_weather_related_holiday = {}
dict_global_extend_data = {}

class TestFunction(unittest.TestCase):
    def test_week_number_1(self):
        returnValue = ExportDailyReportForm.func_get_cell_num( datetime.datetime.strptime( '2024-02-14', "%Y-%m-%d" ) )
        self.assertEqual(returnValue['WeekNum'], 3)
        self.assertEqual(returnValue['RowNum'], 11)
        self.assertEqual(returnValue['ColumnNum'], 19)
        self.assertEqual(returnValue['ColumnString'], 'S')

        returnValue = ExportDailyReportForm.func_get_cell_num( datetime.datetime.strptime( '2024-03-09', "%Y-%m-%d" ) )
        self.assertEqual(returnValue['WeekNum'], 2)
        self.assertEqual(returnValue['RowNum'], 14)
        self.assertEqual(returnValue['ColumnNum'], 15)
        self.assertEqual(returnValue['ColumnString'], 'O')

        returnValue = ExportDailyReportForm.func_get_cell_num( datetime.datetime.strptime( '2024-03-10', "%Y-%m-%d" ) )
        self.assertEqual(returnValue['WeekNum'], 3)
        self.assertEqual(returnValue['RowNum'], 14)
        self.assertEqual(returnValue['ColumnNum'], 16)
        self.assertEqual(returnValue['ColumnString'], 'P')

        returnValue = ExportDailyReportForm.func_get_cell_num( datetime.datetime.strptime( '2024-03-31', "%Y-%m-%d" ) )
        self.assertEqual(returnValue['WeekNum'], 6)
        self.assertEqual(returnValue['RowNum'], 14)
        self.assertEqual(returnValue['ColumnNum'], 37)
        self.assertEqual(returnValue['ColumnString'], 'AK')

        returnValue = ExportDailyReportForm.func_get_cell_num( datetime.datetime.strptime( '2024-04-06', "%Y-%m-%d" ) )
        self.assertEqual(returnValue['WeekNum'], 1)
        self.assertEqual(returnValue['RowNum'], 17)
        self.assertEqual(returnValue['ColumnNum'], 8)
        self.assertEqual(returnValue['ColumnString'], 'H')

        returnValue = ExportDailyReportForm.func_get_cell_num( datetime.datetime.strptime( '2024-04-07', "%Y-%m-%d" ) )
        self.assertEqual(returnValue['WeekNum'], 2)
        self.assertEqual(returnValue['RowNum'], 17)
        self.assertEqual(returnValue['ColumnNum'], 9)
        self.assertEqual(returnValue['ColumnString'], 'I')

        returnValue = ExportDailyReportForm.func_get_cell_num( datetime.datetime.strptime( '2024-06-30', "%Y-%m-%d" ) )
        self.assertEqual(returnValue['WeekNum'], 6)
        self.assertEqual(returnValue['RowNum'], 23)
        self.assertEqual(returnValue['ColumnNum'], 37)
        self.assertEqual(returnValue['ColumnString'], 'AK')

        returnValue = ExportDailyReportForm.func_get_cell_num( datetime.datetime.strptime( '2024-09-07', "%Y-%m-%d" ) )
        self.assertEqual(returnValue['WeekNum'], 1)
        self.assertEqual(returnValue['RowNum'], 32)
        self.assertEqual(returnValue['ColumnNum'], 8)
        self.assertEqual(returnValue['ColumnString'], 'H')
        
        returnValue = ExportDailyReportForm.func_get_cell_num( datetime.datetime.strptime( '2024-09-14', "%Y-%m-%d" ) )
        self.assertEqual(returnValue['WeekNum'], 2)
        self.assertEqual(returnValue['RowNum'], 32)
        self.assertEqual(returnValue['ColumnNum'], 15)
        self.assertEqual(returnValue['ColumnString'], 'O')

    def test_OneDayOffExpectFinishDate1( self ):
        ScheduleCount.func_load_json_holiday_data( arr_global_const_holiday, arr_global_const_workday, dict_holiday_reason )
        returnValue = ScheduleCount.func_count_expect_finish_date( ScheduleCount.WorkDay.ONE_DAY_OFF, 1, datetime.datetime.strptime('2023-01-01', "%Y-%m-%d"), arr_global_const_holiday, arr_global_const_workday )
        self.assertEqual(returnValue['ExpectFinishDate'], datetime.datetime.strptime('2023-01-03', "%Y-%m-%d") )
        self.assertEqual(returnValue['ExpectTotalCalendarDays'], 3)

    def test_OneDayOffExpectFinishDate2( self ):
        ScheduleCount.func_load_json_holiday_data( arr_global_const_holiday,arr_global_const_workday, dict_holiday_reason )
        returnValue = ScheduleCount.func_count_expect_finish_date( ScheduleCount.WorkDay.ONE_DAY_OFF, 60, datetime.datetime.strptime('2023-01-01', "%Y-%m-%d"), arr_global_const_holiday, arr_global_const_workday )
        self.assertEqual(returnValue['ExpectFinishDate'], datetime.datetime.strptime('2023-03-25', "%Y-%m-%d") )
        self.assertEqual(returnValue['ExpectTotalCalendarDays'], 84)
        
    def test_TwoDayOffExpectFinishDate( self ):
        ScheduleCount.func_load_json_holiday_data( arr_global_const_holiday,arr_global_const_workday, dict_holiday_reason )
        returnValue = ScheduleCount.func_count_expect_finish_date( ScheduleCount.WorkDay.TWO_DAY_OFF, 60, datetime.datetime.strptime('2023-01-01', "%Y-%m-%d"), arr_global_const_holiday, arr_global_const_workday )
        self.assertEqual(returnValue['ExpectFinishDate'], datetime.datetime.strptime('2023-03-31', "%Y-%m-%d") )
        self.assertEqual(returnValue['ExpectTotalCalendarDays'], 90)

    def test_OneDayOffRealFinishDate( self ):
        ScheduleCount.func_load_json_holiday_data( arr_global_const_holiday,arr_global_const_workday, dict_holiday_reason )
        ScheduleCount.func_load_json_daily_report_data( dict_global_weather_related_holiday )
        ScheduleCount.func_load_json_extend_data( dict_global_extend_data )
        returnValue = ScheduleCount.func_count_real_finish_date( ScheduleCount.WorkDay.ONE_DAY_OFF, 
                                                                60, 
                                                                datetime.datetime.strptime('2023-01-01', "%Y-%m-%d"), 
                                                                datetime.datetime.strptime('2023-01-17', "%Y-%m-%d"), 
                                                                arr_global_const_holiday, 
                                                                arr_global_const_workday, 
                                                                dict_global_weather_related_holiday, 
                                                                dict_global_extend_data )
        self.assertEqual(returnValue['ExpectFinishDate'], datetime.datetime.strptime('2023-03-25', "%Y-%m-%d") )
        self.assertEqual(returnValue['ExpectTotalCalendarDays'], 84 )
        self.assertEqual(returnValue['RealFinishDate'], datetime.datetime.strptime('2023-03-30', "%Y-%m-%d") )
        self.assertEqual(returnValue['RealTotalCalendarDays'], 89 )
        self.assertEqual(returnValue['FromStartCalendarDays'], 17 )
        self.assertEqual(returnValue['FromStartWorkDays'], 9 )
        self.assertEqual(returnValue['ExpectRestWorkDays'], 51 )
        self.assertEqual(returnValue['ExpectRestCalendarkDays'], 67 )#14+28+25
        self.assertEqual(returnValue['RealRestWorkDays'], 51 )
        self.assertEqual(returnValue['RealRestCalendarkDays'], 72 )#14+28+30

    def test_TwoDayOffRealFinishDate( self ):
        ScheduleCount.func_load_json_holiday_data( arr_global_const_holiday,arr_global_const_workday, dict_holiday_reason )
        ScheduleCount.func_load_json_daily_report_data( dict_global_weather_related_holiday )
        ScheduleCount.func_load_json_extend_data( dict_global_extend_data )
        returnValue = ScheduleCount.func_count_real_finish_date( ScheduleCount.WorkDay.TWO_DAY_OFF, 
                                                                60, 
                                                                datetime.datetime.strptime('2023-01-01', "%Y-%m-%d"), 
                                                                datetime.datetime.strptime('2023-01-17', "%Y-%m-%d"), 
                                                                arr_global_const_holiday, 
                                                                arr_global_const_workday, 
                                                                dict_global_weather_related_holiday, 
                                                                dict_global_extend_data )
        self.assertEqual(returnValue['ExpectFinishDate'], datetime.datetime.strptime('2023-03-31', "%Y-%m-%d") )
        self.assertEqual(returnValue['ExpectTotalCalendarDays'], 90 )#31+28+31
        self.assertEqual(returnValue['RealFinishDate'], datetime.datetime.strptime('2023-04-11', "%Y-%m-%d") )
        self.assertEqual(returnValue['RealTotalCalendarDays'], 101 )#31+28+31+11
        self.assertEqual(returnValue['FromStartCalendarDays'], 17 )
        self.assertEqual(returnValue['FromStartWorkDays'], 8 )
        self.assertEqual(returnValue['ExpectRestWorkDays'], 52 )#60-8
        self.assertEqual(returnValue['ExpectRestCalendarkDays'], 73 )#14+28+31
        self.assertEqual(returnValue['RealRestWorkDays'], 52 )#60-8
        self.assertEqual(returnValue['RealRestCalendarkDays'], 84 )#14+28+31+11
        
    def test_TwoDayOffRealFinishDate2(self):
        ScheduleCount.func_load_json_holiday_data( arr_global_const_holiday,arr_global_const_workday, dict_holiday_reason )
        ScheduleCount.func_load_json_daily_report_data( dict_global_weather_related_holiday )
        ScheduleCount.func_load_json_extend_data( dict_global_extend_data )
        returnValue = ScheduleCount.func_count_real_finish_date( ScheduleCount.WorkDay.TWO_DAY_OFF, 
                                                                60, 
                                                                datetime.datetime.strptime('2023-01-01', "%Y-%m-%d"), 
                                                                datetime.datetime.strptime('2023-01-18', "%Y-%m-%d"),  
                                                                arr_global_const_holiday, 
                                                                arr_global_const_workday, 
                                                                dict_global_weather_related_holiday, 
                                                                dict_global_extend_data )
        self.assertEqual(returnValue['ExpectFinishDate'], datetime.datetime.strptime('2023-03-31', "%Y-%m-%d") )
        self.assertEqual(returnValue['ExpectTotalCalendarDays'], 90)#31+28+31
        self.assertEqual(returnValue['RealFinishDate'], datetime.datetime.strptime('2023-04-12', "%Y-%m-%d") )
        self.assertEqual(returnValue['RealTotalCalendarDays'], 102)#31+28+31+12
        self.assertEqual(returnValue['FromStartCalendarDays'], 18)
        self.assertEqual(returnValue['FromStartWorkDays'], 8.5)
        self.assertEqual(returnValue['ExpectRestWorkDays'], 51.5)#60-8.5
        self.assertEqual(returnValue['ExpectRestCalendarkDays'], 72)#13+28+31
        self.assertEqual(returnValue['RealRestWorkDays'], 51.5)#60-8.5
        self.assertEqual(returnValue['RealRestCalendarkDays'], 84)#13+28+31+12  

    # def test_TwoDayOffRealFinishDate3(self):
        ScheduleCount.func_load_json_holiday_data( arr_global_const_holiday,arr_global_const_workday, dict_holiday_reason )
        ScheduleCount.func_load_json_daily_report_data( dict_global_weather_related_holiday )
        ScheduleCount.func_load_json_extend_data( dict_global_extend_data )
        returnValue = ScheduleCount.func_count_real_finish_date( ScheduleCount.WorkDay.TWO_DAY_OFF, 
                                                                60, 
                                                                datetime.datetime.strptime('2023-01-01', "%Y-%m-%d"),  
                                                                datetime.datetime.strptime('2023-03-13', "%Y-%m-%d"),  
                                                                arr_global_const_holiday, 
                                                                arr_global_const_workday, 
                                                                dict_global_weather_related_holiday, 
                                                                dict_global_extend_data )
        self.assertEqual(returnValue['ExpectFinishDate'], datetime.datetime.strptime('2023-03-31', "%Y-%m-%d") )
        self.assertEqual(returnValue['ExpectTotalCalendarDays'], 90)#31+28+31
        self.assertEqual(returnValue['RealFinishDate'], datetime.datetime.strptime('2023-04-20', "%Y-%m-%d") )
        self.assertEqual(returnValue['RealTotalCalendarDays'], 110)#31+28+31+20
        self.assertEqual(returnValue['FromStartCalendarDays'], 72)#31+28+13
        self.assertEqual(returnValue['FromStartWorkDays'], 34.5)
        self.assertEqual(returnValue['ExpectRestWorkDays'], 25.5)#60-34.5
        self.assertEqual(returnValue['ExpectRestCalendarkDays'], 18)# 0313~0331 
        self.assertEqual(returnValue['RealRestWorkDays'], 25.5)#60-34.5
        self.assertEqual(returnValue['RealRestCalendarkDays'], 38)#18+17

    def test_TwoDayOffRealFinishDate4(self):
        ScheduleCount.func_load_json_holiday_data(arr_global_const_holiday, arr_global_const_workday, dict_holiday_reason)
        ScheduleCount.func_load_json_daily_report_data(dict_global_weather_related_holiday)
        ScheduleCount.func_load_json_extend_data(dict_global_extend_data)
        returnValue = ScheduleCount.func_count_real_finish_date(ScheduleCount.WorkDay.TWO_DAY_OFF, 
                                                                60, 
                                                                datetime.datetime.strptime('2023-01-01', "%Y-%m-%d"),  
                                                                datetime.datetime.strptime('2023-03-14', "%Y-%m-%d"),  
                                                                arr_global_const_holiday, 
                                                                arr_global_const_workday, 
                                                                dict_global_weather_related_holiday, 
                                                                dict_global_extend_data )
        self.assertEqual(returnValue['ExpectFinishDate'], datetime.datetime.strptime('2023-03-31', "%Y-%m-%d") )
        self.assertEqual(returnValue['ExpectTotalCalendarDays'], 90)#31+28+31
        self.assertEqual(returnValue['RealFinishDate'], datetime.datetime.strptime('2023-05-12', "%Y-%m-%d") )
        self.assertEqual(returnValue['RealTotalCalendarDays'], 132)#31+28+31+30+12
        self.assertEqual(returnValue['FromStartCalendarDays'], 73)#31+28+14
        self.assertEqual(returnValue['FromStartWorkDays'], 34.5)
        self.assertEqual(returnValue['ExpectRestWorkDays'], 25.5)#60-34.5
        self.assertEqual(returnValue['ExpectRestCalendarkDays'], 17)#0314~0331
        self.assertEqual(returnValue['RealRestWorkDays'], 40.5)#60+15-34.5
        self.assertEqual(returnValue['RealRestCalendarkDays'], 59)#0314~0508=17+30+12

    def test_func_condition_no_count_1(self):
        dict_morning_weather_condition_setting = { 
            int( ScheduleCount.Weather.RAIN ): 0.5,
            int( ScheduleCount.Weather.HEAVY_RAIN ): 1,
            int( ScheduleCount.Weather.TYPHOON ): 1,
            int( ScheduleCount.Weather.HOT ): 0.5,
            int( ScheduleCount.Weather.MUDDY ): 0,
            int( ScheduleCount.Weather.OTHER ): 0
        }
        dict_afternoon_weather_condition_setting = { 
            int( ScheduleCount.Weather.RAIN ): 0.5,
            int( ScheduleCount.Weather.HEAVY_RAIN ): 1,
            int( ScheduleCount.Weather.TYPHOON ): 0.5,
            int( ScheduleCount.Weather.HOT ): 1,
            int( ScheduleCount.Weather.MUDDY ): 1,
            int( ScheduleCount.Weather.OTHER ): 0
        }

        dict_morning_human_condition_setting = { 
            int( ScheduleCount.Human.POWER_OFF ): 1,
            int( ScheduleCount.Human.OTHER ): 0.5
        }

        dict_afternoon_human_condition_setting = { 
            int( ScheduleCount.Human.POWER_OFF ): 0.5,
            int( ScheduleCount.Human.OTHER ): 0.5
        }
        b_is_work_day = False
        n_suspend_work = 1
        n_morning_weather = int( ScheduleCount.Weather.HEAVY_RAIN )
        n_afternoon_weather = int( ScheduleCount.Weather.HEAVY_RAIN )
        n_morning_human = int( ScheduleCount.Human.POWER_OFF )
        n_afternoon_human = int( ScheduleCount.Human.POWER_OFF )

        dict_return_suspend_work = {}
        dict_return_weather = {}
        dict_return_human = {}

        ScheduleCount.func_condition_no_count( b_is_work_day, 
                                               dict_morning_weather_condition_setting, dict_afternoon_weather_condition_setting,
                                               dict_morning_human_condition_setting, dict_afternoon_human_condition_setting,
                                               n_suspend_work,
                                               n_morning_weather, n_afternoon_weather, 
                                               n_morning_human, n_afternoon_human,
                                               dict_return_suspend_work, dict_return_weather, dict_return_human )
        
        self.assertEqual( dict_return_suspend_work[ ScheduleCount.SyspendWork.SUSPEND_WORK ], 0 )

        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.RAIN ], 0 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.HEAVY_RAIN ], 0 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.TYPHOON ], 0 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.HOT ], 0 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.MUDDY ], 0 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.OTHER ], 0 )

        self.assertEqual( dict_return_human[ ScheduleCount.Human.POWER_OFF ], 0 )
        self.assertEqual( dict_return_human[ ScheduleCount.Human.OTHER ], 0 )

        pass

    def test_func_condition_no_count_2(self):
        dict_morning_weather_condition_setting = { 
            int( ScheduleCount.Weather.RAIN ): 0.5,
            int( ScheduleCount.Weather.HEAVY_RAIN ): 1,
            int( ScheduleCount.Weather.TYPHOON ): 1,
            int( ScheduleCount.Weather.HOT ): 0.5,
            int( ScheduleCount.Weather.MUDDY ): 0,
            int( ScheduleCount.Weather.OTHER ): 0
        }
        dict_afternoon_weather_condition_setting = { 
            int( ScheduleCount.Weather.RAIN ): 0.5,
            int( ScheduleCount.Weather.HEAVY_RAIN ): 1,
            int( ScheduleCount.Weather.TYPHOON ): 0.5,
            int( ScheduleCount.Weather.HOT ): 1,
            int( ScheduleCount.Weather.MUDDY ): 1,
            int( ScheduleCount.Weather.OTHER ): 0
        }

        dict_morning_human_condition_setting = { 
            int( ScheduleCount.Human.POWER_OFF ): 1,
            int( ScheduleCount.Human.OTHER ): 0.5
        }

        dict_afternoon_human_condition_setting = { 
            int( ScheduleCount.Human.POWER_OFF ): 0.5,
            int( ScheduleCount.Human.OTHER ): 0.5
        }
        b_is_work_day = True
        n_suspend_work = 1
        n_morning_weather = int( ScheduleCount.Weather.HEAVY_RAIN )
        n_afternoon_weather = int( ScheduleCount.Weather.HEAVY_RAIN )
        n_morning_human = int( ScheduleCount.Human.POWER_OFF )
        n_afternoon_human = int( ScheduleCount.Human.POWER_OFF )

        dict_return_suspend_work = {}
        dict_return_weather = {}
        dict_return_human = {}

        ScheduleCount.func_condition_no_count( b_is_work_day, 
                                               dict_morning_weather_condition_setting, dict_afternoon_weather_condition_setting,
                                               dict_morning_human_condition_setting, dict_afternoon_human_condition_setting,
                                               n_suspend_work,
                                               n_morning_weather, n_afternoon_weather, 
                                               n_morning_human, n_afternoon_human,
                                               dict_return_suspend_work, dict_return_weather, dict_return_human )
        
        self.assertEqual( dict_return_suspend_work[ ScheduleCount.SyspendWork.SUSPEND_WORK ], 1 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.RAIN ], 0 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.HEAVY_RAIN ], 0 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.TYPHOON ], 0 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.HOT ], 0 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.MUDDY ], 0 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.OTHER ], 0 )
        self.assertEqual( dict_return_human[ ScheduleCount.Human.POWER_OFF ], 0 )
        self.assertEqual( dict_return_human[ ScheduleCount.Human.OTHER ], 0 )

        pass

    def test_func_condition_no_count_3(self):
        dict_morning_weather_condition_setting = { 
            int( ScheduleCount.Weather.RAIN ): 0.5,
            int( ScheduleCount.Weather.HEAVY_RAIN ): 1,
            int( ScheduleCount.Weather.TYPHOON ): 1,
            int( ScheduleCount.Weather.HOT ): 0.5,
            int( ScheduleCount.Weather.MUDDY ): 0,
            int( ScheduleCount.Weather.OTHER ): 0
        }
        dict_afternoon_weather_condition_setting = { 
            int( ScheduleCount.Weather.RAIN ): 0.5,
            int( ScheduleCount.Weather.HEAVY_RAIN ): 1,
            int( ScheduleCount.Weather.TYPHOON ): 0.5,
            int( ScheduleCount.Weather.HOT ): 1,
            int( ScheduleCount.Weather.MUDDY ): 1,
            int( ScheduleCount.Weather.OTHER ): 0
        }

        dict_morning_human_condition_setting = { 
            int( ScheduleCount.Human.POWER_OFF ): 1,
            int( ScheduleCount.Human.OTHER ): 0.5
        }

        dict_afternoon_human_condition_setting = { 
            int( ScheduleCount.Human.POWER_OFF ): 0.5,
            int( ScheduleCount.Human.OTHER ): 0.5
        }
        b_is_work_day = True
        n_suspend_work = 0
        n_morning_weather = int( ScheduleCount.Weather.HEAVY_RAIN ) # 1
        n_afternoon_weather = int( ScheduleCount.Weather.HEAVY_RAIN ) # 1
        n_morning_human = int( ScheduleCount.Human.POWER_OFF ) # 1
        n_afternoon_human = int( ScheduleCount.Human.POWER_OFF ) # 0.5

        dict_return_suspend_work = {}
        dict_return_weather = {}
        dict_return_human = {}

        ScheduleCount.func_condition_no_count( b_is_work_day, 
                                               dict_morning_weather_condition_setting, dict_afternoon_weather_condition_setting,
                                               dict_morning_human_condition_setting, dict_afternoon_human_condition_setting,
                                               n_suspend_work,
                                               n_morning_weather, n_afternoon_weather, 
                                               n_morning_human, n_afternoon_human,
                                               dict_return_suspend_work, dict_return_weather, dict_return_human )
        
        self.assertEqual( dict_return_suspend_work[ ScheduleCount.SyspendWork.SUSPEND_WORK ], 0 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.RAIN ], 0 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.HEAVY_RAIN ], 1 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.TYPHOON ], 0 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.HOT ], 0 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.MUDDY ], 0 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.OTHER ], 0 )
        self.assertEqual( dict_return_human[ ScheduleCount.Human.POWER_OFF ], 0 )
        self.assertEqual( dict_return_human[ ScheduleCount.Human.OTHER ], 0 )

        pass

    def test_func_condition_no_count_4(self):
        dict_morning_weather_condition_setting = { 
            int( ScheduleCount.Weather.RAIN ): 0.5,
            int( ScheduleCount.Weather.HEAVY_RAIN ): 1,
            int( ScheduleCount.Weather.TYPHOON ): 1,
            int( ScheduleCount.Weather.HOT ): 0.5,
            int( ScheduleCount.Weather.MUDDY ): 0,
            int( ScheduleCount.Weather.OTHER ): 0
        }
        dict_afternoon_weather_condition_setting = { 
            int( ScheduleCount.Weather.RAIN ): 0.5,
            int( ScheduleCount.Weather.HEAVY_RAIN ): 1,
            int( ScheduleCount.Weather.TYPHOON ): 0.5,
            int( ScheduleCount.Weather.HOT ): 1,
            int( ScheduleCount.Weather.MUDDY ): 1,
            int( ScheduleCount.Weather.OTHER ): 0
        }

        dict_morning_human_condition_setting = { 
            int( ScheduleCount.Human.POWER_OFF ): 1,
            int( ScheduleCount.Human.OTHER ): 0.5
        }

        dict_afternoon_human_condition_setting = { 
            int( ScheduleCount.Human.POWER_OFF ): 0.5,
            int( ScheduleCount.Human.OTHER ): 0.5
        }
        b_is_work_day = True
        n_suspend_work = 0
        n_morning_weather = int( ScheduleCount.Weather.RAIN )# 0.5
        n_afternoon_weather = int( ScheduleCount.Weather.HEAVY_RAIN )# 1
        n_morning_human = int( ScheduleCount.Human.POWER_OFF )# 1
        n_afternoon_human = int( ScheduleCount.Human.OTHER )# 0.5

        dict_return_suspend_work = {}
        dict_return_weather = {}
        dict_return_human = {}

        ScheduleCount.func_condition_no_count( b_is_work_day, 
                                               dict_morning_weather_condition_setting, dict_afternoon_weather_condition_setting,
                                               dict_morning_human_condition_setting, dict_afternoon_human_condition_setting,
                                               n_suspend_work,
                                               n_morning_weather, n_afternoon_weather, 
                                               n_morning_human, n_afternoon_human,
                                               dict_return_suspend_work, dict_return_weather, dict_return_human )
        
        self.assertEqual( dict_return_suspend_work[ ScheduleCount.SyspendWork.SUSPEND_WORK ], 0 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.RAIN ], 0.5 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.HEAVY_RAIN ], 0.5 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.TYPHOON ], 0 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.HOT ], 0 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.MUDDY ], 0 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.OTHER ], 0 )
        self.assertEqual( dict_return_human[ ScheduleCount.Human.POWER_OFF ], 0 )
        self.assertEqual( dict_return_human[ ScheduleCount.Human.OTHER ], 0 )

        pass

    def test_func_condition_no_count_5(self):
        dict_morning_weather_condition_setting = { 
            int( ScheduleCount.Weather.RAIN ): 0.5,
            int( ScheduleCount.Weather.HEAVY_RAIN ): 1,
            int( ScheduleCount.Weather.TYPHOON ): 1,
            int( ScheduleCount.Weather.HOT ): 0.5,
            int( ScheduleCount.Weather.MUDDY ): 0,
            int( ScheduleCount.Weather.OTHER ): 0
        }
        dict_afternoon_weather_condition_setting = { 
            int( ScheduleCount.Weather.RAIN ): 0.5,
            int( ScheduleCount.Weather.HEAVY_RAIN ): 1,
            int( ScheduleCount.Weather.TYPHOON ): 0.5,
            int( ScheduleCount.Weather.HOT ): 1,
            int( ScheduleCount.Weather.MUDDY ): 1,
            int( ScheduleCount.Weather.OTHER ): 0
        }

        dict_morning_human_condition_setting = { 
            int( ScheduleCount.Human.POWER_OFF ): 1,
            int( ScheduleCount.Human.OTHER ): 0.5
        }

        dict_afternoon_human_condition_setting = { 
            int( ScheduleCount.Human.POWER_OFF ): 0.5,
            int( ScheduleCount.Human.OTHER ): 0.5
        }
        b_is_work_day = True
        n_suspend_work = 0
        n_morning_weather = int( ScheduleCount.Weather.OTHER ) # 0
        n_afternoon_weather = int( ScheduleCount.Weather.HEAVY_RAIN ) # 1
        n_morning_human = int( ScheduleCount.Human.POWER_OFF ) # 1
        n_afternoon_human = int( ScheduleCount.Human.OTHER ) # 0.5

        dict_return_suspend_work = {}
        dict_return_weather = {}
        dict_return_human = {}

        ScheduleCount.func_condition_no_count( b_is_work_day, 
                                               dict_morning_weather_condition_setting, dict_afternoon_weather_condition_setting,
                                               dict_morning_human_condition_setting, dict_afternoon_human_condition_setting,
                                               n_suspend_work,
                                               n_morning_weather, n_afternoon_weather, 
                                               n_morning_human, n_afternoon_human,
                                               dict_return_suspend_work, dict_return_weather, dict_return_human )
        
        self.assertEqual( dict_return_suspend_work[ ScheduleCount.SyspendWork.SUSPEND_WORK ], 0 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.RAIN ], 0 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.HEAVY_RAIN ], 1 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.TYPHOON ], 0 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.HOT ], 0 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.MUDDY ], 0 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.OTHER ], 0 )
        self.assertEqual( dict_return_human[ ScheduleCount.Human.POWER_OFF ], 0 )
        self.assertEqual( dict_return_human[ ScheduleCount.Human.OTHER ], 0 )

        pass

    def test_func_condition_no_count_5(self):
        dict_morning_weather_condition_setting = { 
            int( ScheduleCount.Weather.RAIN ): 0.5,
            int( ScheduleCount.Weather.HEAVY_RAIN ): 1,
            int( ScheduleCount.Weather.TYPHOON ): 1,
            int( ScheduleCount.Weather.HOT ): 0.5,
            int( ScheduleCount.Weather.MUDDY ): 0,
            int( ScheduleCount.Weather.OTHER ): 0
        }
        dict_afternoon_weather_condition_setting = { 
            int( ScheduleCount.Weather.RAIN ): 0.5,
            int( ScheduleCount.Weather.HEAVY_RAIN ): 1,
            int( ScheduleCount.Weather.TYPHOON ): 0.5,
            int( ScheduleCount.Weather.HOT ): 1,
            int( ScheduleCount.Weather.MUDDY ): 1,
            int( ScheduleCount.Weather.OTHER ): 0
        }

        dict_morning_human_condition_setting = { 
            int( ScheduleCount.Human.POWER_OFF ): 1,
            int( ScheduleCount.Human.OTHER ): 0.5
        }

        dict_afternoon_human_condition_setting = { 
            int( ScheduleCount.Human.POWER_OFF ): 0.5,
            int( ScheduleCount.Human.OTHER ): 0.5
        }
        b_is_work_day = True
        n_suspend_work = 0
        n_morning_weather = int( ScheduleCount.Weather.OTHER ) # 0
        n_afternoon_weather = int( ScheduleCount.Weather.RAIN ) # 0.5
        n_morning_human = int( ScheduleCount.Human.POWER_OFF ) # 1
        n_afternoon_human = int( ScheduleCount.Human.OTHER ) # 0.5

        dict_return_suspend_work = {}
        dict_return_weather = {}
        dict_return_human = {}

        ScheduleCount.func_condition_no_count( b_is_work_day, 
                                               dict_morning_weather_condition_setting, dict_afternoon_weather_condition_setting,
                                               dict_morning_human_condition_setting, dict_afternoon_human_condition_setting,
                                               n_suspend_work,
                                               n_morning_weather, n_afternoon_weather, 
                                               n_morning_human, n_afternoon_human,
                                               dict_return_suspend_work, dict_return_weather, dict_return_human )
        
        self.assertEqual( dict_return_suspend_work[ ScheduleCount.SyspendWork.SUSPEND_WORK ], 0 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.RAIN ], 0.5 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.HEAVY_RAIN ], 0 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.TYPHOON ], 0 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.HOT ], 0 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.MUDDY ], 0 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.OTHER ], 0 )
        self.assertEqual( dict_return_human[ ScheduleCount.Human.POWER_OFF ], 0.5 )
        self.assertEqual( dict_return_human[ ScheduleCount.Human.OTHER ], 0 )

        pass

    def test_func_condition_no_count_6(self):
        dict_morning_weather_condition_setting = { 
            int( ScheduleCount.Weather.RAIN ): 0.5,
            int( ScheduleCount.Weather.HEAVY_RAIN ): 1,
            int( ScheduleCount.Weather.TYPHOON ): 1,
            int( ScheduleCount.Weather.HOT ): 0.5,
            int( ScheduleCount.Weather.MUDDY ): 0,
            int( ScheduleCount.Weather.OTHER ): 0
        }
        dict_afternoon_weather_condition_setting = { 
            int( ScheduleCount.Weather.RAIN ): 0.5,
            int( ScheduleCount.Weather.HEAVY_RAIN ): 1,
            int( ScheduleCount.Weather.TYPHOON ): 0.5,
            int( ScheduleCount.Weather.HOT ): 1,
            int( ScheduleCount.Weather.MUDDY ): 1,
            int( ScheduleCount.Weather.OTHER ): 0
        }

        dict_morning_human_condition_setting = { 
            int( ScheduleCount.Human.POWER_OFF ): 1,
            int( ScheduleCount.Human.OTHER ): 0.5
        }

        dict_afternoon_human_condition_setting = { 
            int( ScheduleCount.Human.POWER_OFF ): 0.5,
            int( ScheduleCount.Human.OTHER ): 1
        }
        b_is_work_day = True
        n_suspend_work = 0
        n_morning_weather = int( ScheduleCount.Weather.OTHER ) # 0
        n_afternoon_weather = int( ScheduleCount.Weather.RAIN ) # 0.5
        n_morning_human = int( ScheduleCount.Human.POWER_OFF ) # 0.5
        n_afternoon_human = int( ScheduleCount.Human.OTHER ) # 1

        dict_return_suspend_work = {}
        dict_return_weather = {}
        dict_return_human = {}

        ScheduleCount.func_condition_no_count( b_is_work_day, 
                                               dict_morning_weather_condition_setting, dict_afternoon_weather_condition_setting,
                                               dict_morning_human_condition_setting, dict_afternoon_human_condition_setting,
                                               n_suspend_work,
                                               n_morning_weather, n_afternoon_weather, 
                                               n_morning_human, n_afternoon_human,
                                               dict_return_suspend_work, dict_return_weather, dict_return_human )
        
        self.assertEqual( dict_return_suspend_work[ ScheduleCount.SyspendWork.SUSPEND_WORK ], 0 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.RAIN ], 0.5 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.HEAVY_RAIN ], 0 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.TYPHOON ], 0 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.HOT ], 0 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.MUDDY ], 0 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.OTHER ], 0 )
        self.assertEqual( dict_return_human[ ScheduleCount.Human.POWER_OFF ], 0.5 )
        self.assertEqual( dict_return_human[ ScheduleCount.Human.OTHER ], 0 )

        pass

    def test_func_condition_no_count_7(self):
        dict_morning_weather_condition_setting = { 
            int( ScheduleCount.Weather.RAIN ): 0.5,
            int( ScheduleCount.Weather.HEAVY_RAIN ): 1,
            int( ScheduleCount.Weather.TYPHOON ): 1,
            int( ScheduleCount.Weather.HOT ): 0.5,
            int( ScheduleCount.Weather.MUDDY ): 0,
            int( ScheduleCount.Weather.OTHER ): 0
        }
        dict_afternoon_weather_condition_setting = { 
            int( ScheduleCount.Weather.RAIN ): 0.5,
            int( ScheduleCount.Weather.HEAVY_RAIN ): 1,
            int( ScheduleCount.Weather.TYPHOON ): 0.5,
            int( ScheduleCount.Weather.HOT ): 1,
            int( ScheduleCount.Weather.MUDDY ): 1,
            int( ScheduleCount.Weather.OTHER ): 0
        }

        dict_morning_human_condition_setting = { 
            int( ScheduleCount.Human.POWER_OFF ): 1,
            int( ScheduleCount.Human.OTHER ): 0.5
        }

        dict_afternoon_human_condition_setting = { 
            int( ScheduleCount.Human.POWER_OFF ): 0.5,
            int( ScheduleCount.Human.OTHER ): 1
        }
        b_is_work_day = True
        n_suspend_work = 0
        n_morning_weather = int( ScheduleCount.Weather.OTHER ) # 0
        n_afternoon_weather = int( ScheduleCount.Weather.RAIN ) # 0.5
        n_morning_human = int( ScheduleCount.Human.POWER_OFF ) # 1
        n_afternoon_human = int( ScheduleCount.Human.OTHER ) # 1

        dict_return_suspend_work = {}
        dict_return_weather = {}
        dict_return_human = {}

        ScheduleCount.func_condition_no_count( b_is_work_day, 
                                               dict_morning_weather_condition_setting, dict_afternoon_weather_condition_setting,
                                               dict_morning_human_condition_setting, dict_afternoon_human_condition_setting,
                                               n_suspend_work,
                                               n_morning_weather, n_afternoon_weather, 
                                               n_morning_human, n_afternoon_human,
                                               dict_return_suspend_work, dict_return_weather, dict_return_human )
        
        self.assertEqual( dict_return_suspend_work[ ScheduleCount.SyspendWork.SUSPEND_WORK ], 0 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.RAIN ], 0.5 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.HEAVY_RAIN ], 0 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.TYPHOON ], 0 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.HOT ], 0 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.MUDDY ], 0 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.OTHER ], 0 )
        self.assertEqual( dict_return_human[ ScheduleCount.Human.POWER_OFF ], 0.5 )
        self.assertEqual( dict_return_human[ ScheduleCount.Human.OTHER ], 0 )

        pass

    def test_func_condition_no_count_8(self):
        dict_morning_weather_condition_setting = { 
            int( ScheduleCount.Weather.RAIN ): 0.5,
            int( ScheduleCount.Weather.HEAVY_RAIN ): 1,
            int( ScheduleCount.Weather.TYPHOON ): 1,
            int( ScheduleCount.Weather.HOT ): 0.5,
            int( ScheduleCount.Weather.MUDDY ): 0,
            int( ScheduleCount.Weather.OTHER ): 0
        }
        dict_afternoon_weather_condition_setting = { 
            int( ScheduleCount.Weather.RAIN ): 0.5,
            int( ScheduleCount.Weather.HEAVY_RAIN ): 1,
            int( ScheduleCount.Weather.TYPHOON ): 0.5,
            int( ScheduleCount.Weather.HOT ): 1,
            int( ScheduleCount.Weather.MUDDY ): 1,
            int( ScheduleCount.Weather.OTHER ): 0
        }

        dict_morning_human_condition_setting = { 
            int( ScheduleCount.Human.POWER_OFF ): 1,
            int( ScheduleCount.Human.OTHER ): 0.5
        }

        dict_afternoon_human_condition_setting = { 
            int( ScheduleCount.Human.POWER_OFF ): 0.5,
            int( ScheduleCount.Human.OTHER ): 1
        }
        b_is_work_day = True
        n_suspend_work = 0
        n_morning_weather = int( ScheduleCount.Weather.OTHER ) # 0
        n_afternoon_weather = int( ScheduleCount.Weather.OTHER ) # 0
        n_morning_human = int( ScheduleCount.Human.POWER_OFF ) # 1
        n_afternoon_human = int( ScheduleCount.Human.OTHER ) # 1

        dict_return_suspend_work = {}
        dict_return_weather = {}
        dict_return_human = {}

        ScheduleCount.func_condition_no_count( b_is_work_day, 
                                               dict_morning_weather_condition_setting, dict_afternoon_weather_condition_setting,
                                               dict_morning_human_condition_setting, dict_afternoon_human_condition_setting,
                                               n_suspend_work,
                                               n_morning_weather, n_afternoon_weather, 
                                               n_morning_human, n_afternoon_human,
                                               dict_return_suspend_work, dict_return_weather, dict_return_human )
        
        self.assertEqual( dict_return_suspend_work[ ScheduleCount.SyspendWork.SUSPEND_WORK ], 0 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.RAIN ], 0 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.HEAVY_RAIN ], 0 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.TYPHOON ], 0 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.HOT ], 0 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.MUDDY ], 0 )
        self.assertEqual( dict_return_weather[ ScheduleCount.Weather.OTHER ], 0 )
        self.assertEqual( dict_return_human[ ScheduleCount.Human.POWER_OFF ], 1 )
        self.assertEqual( dict_return_human[ ScheduleCount.Human.OTHER ], 0 )

        pass
if __name__ == '__main__':
    unittest.main()