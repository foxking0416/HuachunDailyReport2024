import unittest
import ScheduleCount
import ExportExpectFinishForm
import ExportDailyReportForm
import datetime

arr_global_const_holiday = []
arr_global_const_workday = []
dict_global_weather_related_holiday = {}
dict_global_extend_data = {}

class TestFunction(unittest.TestCase):
    def test_week_number_1(self):
        returnValue = ExportDailyReportForm.func_get_cell_num( datetime.datetime.strptime( '2024-02-14', "%Y-%m-%d" ) )
        self.assertEqual(returnValue['WeekNum'], 3)
        self.assertEqual(returnValue['RowNum'], 10)
        self.assertEqual(returnValue['ColumnNum'], 19)
        self.assertEqual(returnValue['ColumnString'], 'S')

        returnValue = ExportDailyReportForm.func_get_cell_num( datetime.datetime.strptime( '2024-03-09', "%Y-%m-%d" ) )
        self.assertEqual(returnValue['WeekNum'], 2)
        self.assertEqual(returnValue['RowNum'], 12)
        self.assertEqual(returnValue['ColumnNum'], 15)
        self.assertEqual(returnValue['ColumnString'], 'O')

        returnValue = ExportDailyReportForm.func_get_cell_num( datetime.datetime.strptime( '2024-03-10', "%Y-%m-%d" ) )
        self.assertEqual(returnValue['WeekNum'], 3)
        self.assertEqual(returnValue['RowNum'], 12)
        self.assertEqual(returnValue['ColumnNum'], 16)
        self.assertEqual(returnValue['ColumnString'], 'P')

        returnValue = ExportDailyReportForm.func_get_cell_num( datetime.datetime.strptime( '2024-03-31', "%Y-%m-%d" ) )
        self.assertEqual(returnValue['WeekNum'], 6)
        self.assertEqual(returnValue['RowNum'], 12)
        self.assertEqual(returnValue['ColumnNum'], 37)
        self.assertEqual(returnValue['ColumnString'], 'AK')

        returnValue = ExportDailyReportForm.func_get_cell_num( datetime.datetime.strptime( '2024-04-06', "%Y-%m-%d" ) )
        self.assertEqual(returnValue['WeekNum'], 1)
        self.assertEqual(returnValue['RowNum'], 14)
        self.assertEqual(returnValue['ColumnNum'], 8)
        self.assertEqual(returnValue['ColumnString'], 'H')

        returnValue = ExportDailyReportForm.func_get_cell_num( datetime.datetime.strptime( '2024-04-07', "%Y-%m-%d" ) )
        self.assertEqual(returnValue['WeekNum'], 2)
        self.assertEqual(returnValue['RowNum'], 14)
        self.assertEqual(returnValue['ColumnNum'], 9)
        self.assertEqual(returnValue['ColumnString'], 'I')

        returnValue = ExportDailyReportForm.func_get_cell_num( datetime.datetime.strptime( '2024-06-30', "%Y-%m-%d" ) )
        self.assertEqual(returnValue['WeekNum'], 6)
        self.assertEqual(returnValue['RowNum'], 18)
        self.assertEqual(returnValue['ColumnNum'], 37)
        self.assertEqual(returnValue['ColumnString'], 'AK')

        returnValue = ExportDailyReportForm.func_get_cell_num( datetime.datetime.strptime( '2024-09-07', "%Y-%m-%d" ) )
        self.assertEqual(returnValue['WeekNum'], 1)
        self.assertEqual(returnValue['RowNum'], 24)
        self.assertEqual(returnValue['ColumnNum'], 8)
        self.assertEqual(returnValue['ColumnString'], 'H')
        
        returnValue = ExportDailyReportForm.func_get_cell_num( datetime.datetime.strptime( '2024-09-14', "%Y-%m-%d" ) )
        self.assertEqual(returnValue['WeekNum'], 2)
        self.assertEqual(returnValue['RowNum'], 24)
        self.assertEqual(returnValue['ColumnNum'], 15)
        self.assertEqual(returnValue['ColumnString'], 'O')

    def test_OneDayOffExpectFinishDate1( self ):
        ScheduleCount.func_load_json_holiday_data( arr_global_const_holiday, arr_global_const_workday )
        returnValue = ScheduleCount.func_count_expect_finish_date( ScheduleCount.WorkDay.ONE_DAY_OFF, 1, datetime.datetime.strptime('2023-01-01', "%Y-%m-%d"), arr_global_const_holiday, arr_global_const_workday )
        self.assertEqual(returnValue['ExpectFinishDate'], datetime.datetime.strptime('2023-01-03', "%Y-%m-%d") )
        self.assertEqual(returnValue['ExpectTotalCalendarDays'], 3)

    def test_OneDayOffExpectFinishDate2( self ):
        ScheduleCount.func_load_json_holiday_data( arr_global_const_holiday,arr_global_const_workday )
        returnValue = ScheduleCount.func_count_expect_finish_date( ScheduleCount.WorkDay.ONE_DAY_OFF, 60, datetime.datetime.strptime('2023-01-01', "%Y-%m-%d"), arr_global_const_holiday, arr_global_const_workday )
        self.assertEqual(returnValue['ExpectFinishDate'], datetime.datetime.strptime('2023-03-25', "%Y-%m-%d") )
        self.assertEqual(returnValue['ExpectTotalCalendarDays'], 84)
        
    def test_TwoDayOffExpectFinishDate( self ):
        ScheduleCount.func_load_json_holiday_data( arr_global_const_holiday,arr_global_const_workday )
        returnValue = ScheduleCount.func_count_expect_finish_date( ScheduleCount.WorkDay.TWO_DAY_OFF, 60, datetime.datetime.strptime('2023-01-01', "%Y-%m-%d"), arr_global_const_holiday, arr_global_const_workday )
        self.assertEqual(returnValue['ExpectFinishDate'], datetime.datetime.strptime('2023-03-31', "%Y-%m-%d") )
        self.assertEqual(returnValue['ExpectTotalCalendarDays'], 90)

    def test_OneDayOffRealFinishDate( self ):
        ScheduleCount.func_load_json_holiday_data( arr_global_const_holiday,arr_global_const_workday )
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
        ScheduleCount.func_load_json_holiday_data( arr_global_const_holiday,arr_global_const_workday )
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
        ScheduleCount.func_load_json_holiday_data( arr_global_const_holiday,arr_global_const_workday )
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
        ScheduleCount.func_load_json_holiday_data( arr_global_const_holiday,arr_global_const_workday )
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
        self.assertEqual(returnValue['RealFinishDate'], datetime.datetime.strptime('2023-04-17', "%Y-%m-%d") )
        self.assertEqual(returnValue['RealTotalCalendarDays'], 107)#31+28+31+17
        self.assertEqual(returnValue['FromStartCalendarDays'], 72)#31+28+13
        self.assertEqual(returnValue['FromStartWorkDays'], 37)
        self.assertEqual(returnValue['ExpectRestWorkDays'], 23)#60-37
        self.assertEqual(returnValue['ExpectRestCalendarkDays'], 18)# 0313~0331 
        self.assertEqual(returnValue['RealRestWorkDays'], 23)#60-37
        self.assertEqual(returnValue['RealRestCalendarkDays'], 35)#18+17

    def test_TwoDayOffRealFinishDate4(self):
        ScheduleCount.func_load_json_holiday_data(arr_global_const_holiday,arr_global_const_workday)
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
        self.assertEqual(returnValue['RealFinishDate'], datetime.datetime.strptime('2023-05-08', "%Y-%m-%d") )
        self.assertEqual(returnValue['RealTotalCalendarDays'], 128)#31+28+31+30+8
        self.assertEqual(returnValue['FromStartCalendarDays'], 73)#31+28+14
        self.assertEqual(returnValue['FromStartWorkDays'], 38)
        self.assertEqual(returnValue['ExpectRestWorkDays'], 22)#60-38
        self.assertEqual(returnValue['ExpectRestCalendarkDays'], 17)#0314~0331
        self.assertEqual(returnValue['RealRestWorkDays'], 37)#60+15-38
        self.assertEqual(returnValue['RealRestCalendarkDays'], 55)#0314~0508=17+30+8


if __name__ == '__main__':
    unittest.main()