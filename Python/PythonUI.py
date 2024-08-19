# pip install pywin32
# pip install tkcalendar
# pip install openpyxl
# pip install Pillow
# pip install pyinstaller
# pip install lunarcalendar

#打包指令
# cd C:\_EveryThing\_code\HuachunDailyReport2024\Python     
# pyinstaller --hidden-import "babel.numbers" --add-data "ExternalData;./ExternalData" PythonUI.py
import ScheduleCount
import ExportExpectFinishForm
import ExportDailyReportForm
import datetime
from tkinter import *
from tkcalendar import Calendar

global_obj_start_date = None
global_obj_current_date = None

window = Tk()
window.title("工期計算測試程式")
window.minsize(width=500, height=500)
window.resizable(width=True, height=True)



def func_select_start_date(event):
    global global_obj_start_date
    str_start_date = calendar_select_start_date.get_date()
    global_obj_start_date = datetime.datetime.strptime( str_start_date, "%Y-%m-%d" )  
    label_start_date_value.config( text = str_start_date )


def func_select_current_date(event):
    global global_obj_current_date
    str_current_date = calendar_select_current_date.get_date()
    global_obj_current_date = datetime.datetime.strptime( str_current_date, "%Y-%m-%d" )  
    label_current_date_value.config( text = str_current_date )


def func_calculate_schedule():
    arr_const_holiday = []
    arr_const_workday = []
    dict_weather_related_holiday = {}
    dict_extend_data = {}
    dict_holiday_reason = {}
    ScheduleCount.func_load_json_holiday_data( arr_const_holiday,arr_const_workday, dict_holiday_reason )
    ScheduleCount.func_load_json_daily_report_data( dict_weather_related_holiday )
    ScheduleCount.func_load_json_extend_data( dict_extend_data )
    returnValue = None
    if radio_var.get() == 'OneDayOff':
        returnValue = ScheduleCount.func_count_real_finish_date( ScheduleCount.WorkDay.ONE_DAY_OFF, float( spinbox_var_total_work_days.get() ), global_obj_start_date, global_obj_current_date, arr_const_holiday, arr_const_workday, dict_weather_related_holiday, dict_extend_data)
    elif radio_var.get() == 'TwoDayOff':
        returnValue = ScheduleCount.func_count_real_finish_date( ScheduleCount.WorkDay.TWO_DAY_OFF, float( spinbox_var_total_work_days.get() ), global_obj_start_date, global_obj_current_date, arr_const_holiday, arr_const_workday, dict_weather_related_holiday, dict_extend_data)
    elif radio_var.get() == 'NoDayOff':
        returnValue = ScheduleCount.func_count_real_finish_date( ScheduleCount.WorkDay.NO_DAY_OFF, float( spinbox_var_total_work_days.get() ), global_obj_start_date, global_obj_current_date, arr_const_holiday, arr_const_workday, dict_weather_related_holiday, dict_extend_data)
    label_expect_finish_date_value.config( text = returnValue['ExpectFinishDate'].strftime("%Y-%m-%d") )
    label_expect_total_calendar_days_value.config( text = returnValue['ExpectTotalCalendarDays'] )
    label_real_finish_date_value.config( text = returnValue['RealFinishDate'].strftime("%Y-%m-%d") )
    label_real_total_calendar_days_value.config( text = returnValue['RealTotalCalendarDays'] )
    label_from_start_work_days_value.config( text = returnValue['FromStartWorkDays'] )
    label_from_start_calendar_days_value.config( text = returnValue['FromStartCalendarDays'] )
    label_expect_rest_work_days_value.config( text = returnValue['ExpectRestWorkDays'] )
    label_expect_rest_calendar_days_value.config( text = returnValue['ExpectRestCalendarkDays'] )
    label_real_rest_work_days_value.config( text = returnValue['RealRestWorkDays'] )
    label_real_rest_calendar_days_value.config( text = returnValue['RealRestCalendarkDays'] )

def func_export_daily_eport():
    if global_obj_start_date and global_obj_current_date:
        ExportDailyReportForm.func_set_info( entry_box_info_project_no.get(), entry_box_info_project_name.get(), 
                                             entry_box_info_project_owner.get(), entry_box_info_project_supervisor.get(),
                                             entry_box_info_project_designer.get(), entry_box_info_project_contractor.get() )
        if radio_var.get() == 'OneDayOff':
            ExportDailyReportForm.func_create_weather_report_form( ScheduleCount.WorkDay.ONE_DAY_OFF, float( spinbox_var_total_work_days.get() ), global_obj_start_date, global_obj_current_date )
        elif radio_var.get() == 'TwoDayOff':
            ExportDailyReportForm.func_create_weather_report_form( ScheduleCount.WorkDay.TWO_DAY_OFF, float( spinbox_var_total_work_days.get() ), global_obj_start_date, global_obj_current_date )
        elif radio_var.get() == 'NoDayOff':
            ExportDailyReportForm.func_create_weather_report_form( ScheduleCount.WorkDay.NO_DAY_OFF, float( spinbox_var_total_work_days.get() ), global_obj_start_date, global_obj_current_date )

def func_export_expect_finish_form():
    if global_obj_start_date and global_obj_current_date:
        ExportExpectFinishForm.func_set_info( entry_box_info_project_no.get(), entry_box_info_project_name.get(), 
                                              entry_box_info_project_owner.get(), entry_box_info_project_supervisor.get(),
                                              entry_box_info_project_designer.get(), entry_box_info_project_contractor.get() )
                
        if radio_var.get() == 'OneDayOff':
            ExportExpectFinishForm.func_create_expect_finish_form( ScheduleCount.WorkDay.ONE_DAY_OFF, float( spinbox_var_total_work_days.get() ), global_obj_start_date )
        elif radio_var.get() == 'TwoDayOff':
            ExportExpectFinishForm.func_create_expect_finish_form( ScheduleCount.WorkDay.TWO_DAY_OFF, float( spinbox_var_total_work_days.get() ), global_obj_start_date )
        elif radio_var.get() == 'NoDayOff':
            ExportExpectFinishForm.func_create_expect_finish_form( ScheduleCount.WorkDay.NO_DAY_OFF, float( spinbox_var_total_work_days.get() ), global_obj_start_date )
    pass

group_frame_select_date = Frame( window )
group_frame_select_date.pack(padx=10, pady=10)

calendar_select_start_date = Calendar( group_frame_select_date, selectmode='day', date_pattern='yyyy-mm-dd',year=2023,month=1,day=1 )
calendar_select_start_date.pack(side="left", padx=10)
calendar_select_start_date.bind("<<CalendarSelected>>", func_select_start_date)

calendar_select_current_date = Calendar(group_frame_select_date, selectmode='day', date_pattern='yyyy-mm-dd',year=2023,month=1,day=1)
calendar_select_current_date.pack(side="left", padx=10)
calendar_select_current_date.bind("<<CalendarSelected>>", func_select_current_date)

group_frame_start_date_label = Frame(window)
group_frame_start_date_label.pack(anchor="w")

label_start_date = Label(group_frame_start_date_label, text="開工日期")
label_start_date.pack(side="left",padx=10)
label_start_date_value = Label(group_frame_start_date_label, text="?")
label_start_date_value.pack(side="left")


group_frame_current_date_label = Frame(window)
group_frame_current_date_label.pack(anchor="w")

label_current_date = Label(group_frame_current_date_label, text="今日日期")
label_current_date.pack(side="left",padx=10 )
label_current_date_value = Label(group_frame_current_date_label, text="?")
label_current_date_value.pack(side="left")



radio_var = StringVar()
radio_button_no_day_off = Radiobutton(window, text="無周休", variable=radio_var, value="NoDayOff")
radio_button_no_day_off.pack(padx=10, anchor="w")

radio_button_one_day_off = Radiobutton(window, text="周休一日", variable=radio_var, value="OneDayOff")
radio_button_one_day_off.pack(padx=10, anchor="w")

radio_button_two_day_off = Radiobutton(window, text="周休二日", variable=radio_var, value="TwoDayOff")
radio_button_two_day_off.pack(padx=10, anchor="w")

radio_var.set("OneDayOff")

group_frame_total_work_days = Frame(window)
group_frame_total_work_days.pack(anchor="w")

label_total_work_days = Label(group_frame_total_work_days, text="契約工期")
label_total_work_days.pack(side="left", padx=10, anchor="w")

spinbox_var_total_work_days = StringVar()
spinbox_total_work_days = Spinbox(group_frame_total_work_days, from_=1, to=1000, increment=0.5, textvariable=spinbox_var_total_work_days)
spinbox_total_work_days.pack(side="left")


group_frame_expect_finish_date = Frame(window)
group_frame_expect_finish_date.pack(anchor="w")

label_expect_finish_date = Label(group_frame_expect_finish_date, text="預計完工日")
label_expect_finish_date.pack(side="left", padx=10)
label_expect_finish_date_value = Label(group_frame_expect_finish_date, text="?")
label_expect_finish_date_value.pack(side="left", padx=10)


label_expect_total_calendar_days = Label(group_frame_expect_finish_date, text="預計完工天數")
label_expect_total_calendar_days.pack(side="left", padx=10)
label_expect_total_calendar_days_value = Label(group_frame_expect_finish_date, text="?")
label_expect_total_calendar_days_value.pack(side="left", padx=10)


group_frame_from_start_work_days = Frame(window)
group_frame_from_start_work_days.pack(anchor="w")

label_from_start_work_days = Label(group_frame_from_start_work_days, text="開工迄今工作天數")
label_from_start_work_days.pack(side="left", padx=10)
label_from_start_work_days_value = Label(group_frame_from_start_work_days, text="?")
label_from_start_work_days_value.pack(side="left", padx=10)


label_from_start_calendar_days = Label(group_frame_from_start_work_days, text="開工迄今日曆天數")
label_from_start_calendar_days.pack(side="left", padx=10)
label_from_start_calendar_days_value = Label(group_frame_from_start_work_days, text="?")
label_from_start_calendar_days_value.pack(side="left", padx=10)


group_frame_real_finish_date = Frame(window)
group_frame_real_finish_date.pack(anchor="w")

label_real_finish_date = Label(group_frame_real_finish_date, text="變動完工日")
label_real_finish_date.pack(side="left",padx=10)
label_real_finish_date_value = Label(group_frame_real_finish_date, text="?")
label_real_finish_date_value.pack(side="left", padx=10)


label_real_total_calendar_days = Label(group_frame_real_finish_date, text="變動完工天數")
label_real_total_calendar_days.pack(side="left",padx=10)
label_real_total_calendar_days_value = Label(group_frame_real_finish_date, text="?")
label_real_total_calendar_days_value.pack(side="left", padx=10)


group_frame_expect_rest_work_days = Frame(window)
group_frame_expect_rest_work_days.pack(anchor="w")

label_expect_rest_work_days = Label(group_frame_expect_rest_work_days, text="預計剩餘工期")
label_expect_rest_work_days.pack(side="left",padx=10)
label_expect_rest_work_days_value = Label(group_frame_expect_rest_work_days, text="?")
label_expect_rest_work_days_value.pack(side="left", padx=10)


label_expect_rest_calendar_days = Label(group_frame_expect_rest_work_days, text="預計剩餘天數")
label_expect_rest_calendar_days.pack(side="left",padx=10)
label_expect_rest_calendar_days_value = Label(group_frame_expect_rest_work_days, text="?")
label_expect_rest_calendar_days_value.pack(side="left", padx=10)


group_frame_real_rest_work_days = Frame(window)
group_frame_real_rest_work_days.pack(anchor="w")

label_real_rest_work_days = Label(group_frame_real_rest_work_days, text="實際剩餘工期")
label_real_rest_work_days.pack(side="left",padx=10)
label_real_rest_work_days_value = Label(group_frame_real_rest_work_days, text="?")
label_real_rest_work_days_value.pack(side="left", padx=10)


label_real_rest_calendar_days = Label(group_frame_real_rest_work_days, text="實際剩餘天數")
label_real_rest_calendar_days.pack(side="left",padx=10)
label_real_rest_calendar_days_value = Label(group_frame_real_rest_work_days, text="?")
label_real_rest_calendar_days_value.pack(side="left", padx=10)


group_frame_info_project_no = Frame(window)
group_frame_info_project_no.pack(anchor="w")

label_info_project_no = Label(group_frame_info_project_no, text="案號      ")
label_info_project_no.pack(side="left",padx=10)

entry_box_info_project_no  = Entry(group_frame_info_project_no, width=20)
entry_box_info_project_no.pack(side="left",padx=10)
entry_box_info_project_no.insert(0, "Avenger001")

label_info_project_name = Label(group_frame_info_project_no, text="工程名稱")
label_info_project_name.pack(side="left",padx=10)

entry_box_info_project_name  = Entry(group_frame_info_project_no, width=20)
entry_box_info_project_name.pack(side="left",padx=10)
entry_box_info_project_name.insert(0, "復仇者聯盟總部興建工程")


group_frame_info_project_owner = Frame(window)
group_frame_info_project_owner.pack(anchor="w")

label_info_project_owner = Label(group_frame_info_project_owner, text="業主      ")
label_info_project_owner.pack(side="left",padx=10)


entry_box_info_project_owner  = Entry(group_frame_info_project_owner, width=20)
entry_box_info_project_owner.pack(side="left",padx=10)
entry_box_info_project_owner.insert(0, "神盾局")

label_info_project_supervisor = Label(group_frame_info_project_owner, text="監造單位")
label_info_project_supervisor.pack(side="left",padx=10)

entry_box_info_project_supervisor  = Entry(group_frame_info_project_owner, width=20)
entry_box_info_project_supervisor.pack(side="left",padx=10)
entry_box_info_project_supervisor.insert(0, "復仇者聯盟")


group_frame_info_project_designer = Frame(window)
group_frame_info_project_designer.pack(anchor="w")

label_info_project_designer = Label(group_frame_info_project_designer, text="設計單位      ")
label_info_project_designer.pack(side="left",padx=10)

entry_box_info_project_designer  = Entry(group_frame_info_project_designer, width=20)
entry_box_info_project_designer.pack(side="left",padx=10)
entry_box_info_project_designer.insert(0, "東尼史塔克")

label_info_project_supervisor = Label(group_frame_info_project_designer, text="承攬廠商")
label_info_project_supervisor.pack(side="left",padx=10)

entry_box_info_project_contractor  = Entry(group_frame_info_project_designer, width=20)
entry_box_info_project_contractor.pack(side="left",padx=10)
entry_box_info_project_contractor.insert(0, "賈維斯")



group_frame_calculate_export = Frame(window)
group_frame_calculate_export.pack(anchor="w")

button_calculate = Button(group_frame_calculate_export, text="計算", command=func_calculate_schedule)
button_calculate.pack(side="left",padx=5)

button_export_dailyreport = Button(group_frame_calculate_export, text="輸出晴雨日報表", command=func_export_daily_eport)
button_export_dailyreport.pack(side="left",padx=5)

button_export_expect_finish = Button(group_frame_calculate_export, text="輸出預計完工表", command=func_export_expect_finish_form)
button_export_expect_finish.pack(side="left",padx=5)

window.mainloop()



