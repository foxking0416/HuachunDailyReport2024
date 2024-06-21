#打包指令
#pyinstaller --hidden-import "babel.numbers" PythonUI.py
import ScheduleCount
import ExportExpectFinishForm
import ExportDailyReportForm
from tkinter import *
from tkcalendar import Calendar

globalStartDate = None
globalCurrentDate = None

window = Tk()
window.title("工期計算測試程式")
window.minsize(width=500, height=500)
window.resizable(width=True, height=True)



def func_select_start_date(event):
    global globalStartDate
    globalStartDate = calendar_select_start_date.get_date()
    label_start_date_value.config(text= globalStartDate)


def func_select_current_date(event):
    global globalCurrentDate
    globalCurrentDate = calendar_select_current_date.get_date()
    label_current_date_value.config(text= globalCurrentDate)

def func_update_radio_button_selection():
    selected_option = radio_var.get()
    # selection_label.config(text="Selected option: " + selected_option)

def func_update_value():
    selected_value = spinbox_var.get()
    # value_label.config(text="Selected value: " + selected_value)


def func_calculate_schedule():
    arrConstHoliday = []
    arrConstWorkday = []
    dictWeatherRelatedHoliday = {}
    dictExtendData = {}
    ScheduleCount.load_json_holiday_data(arrConstHoliday,arrConstWorkday)
    ScheduleCount.load_json_daily_report_data(dictWeatherRelatedHoliday)
    ScheduleCount.load_json_extend_data(dictExtendData)
    returnValue = None
    if radio_var.get() == 'OneDayOff':
        returnValue = ScheduleCount.count_real_finish_date(ScheduleCount.WorkDay.ONE_DAY_OFF, int(spinbox_var.get()), globalStartDate, globalCurrentDate, arrConstHoliday, arrConstWorkday, dictWeatherRelatedHoliday, dictExtendData)
    elif radio_var.get() == 'TwoDayOff':
        returnValue = ScheduleCount.count_real_finish_date(ScheduleCount.WorkDay.TWO_DAY_OFF, int(spinbox_var.get()), globalStartDate, globalCurrentDate, arrConstHoliday, arrConstWorkday, dictWeatherRelatedHoliday, dictExtendData)
    elif radio_var.get() == 'NoDayOff':
        returnValue = ScheduleCount.count_real_finish_date(ScheduleCount.WorkDay.NO_DAY_OFF, int(spinbox_var.get()), globalStartDate, globalCurrentDate, arrConstHoliday, arrConstWorkday, dictWeatherRelatedHoliday, dictExtendData)
    label_expect_finish_date_value.config(text= returnValue['ExpectFinishDate'])
    label_expect_total_calendar_days_value.config(text= returnValue['ExpectTotalCalendarDays'])
    label_real_finish_date_value.config(text= returnValue['RealFinishDate'])
    label_real_total_calendar_days_value.config(text= returnValue['RealTotalCalendarDays'])
    label_from_start_work_days_value.config(text= returnValue['FromStartWorkDays'])
    label_from_start_calendar_days_value.config(text= returnValue['FromStartCalendarDays'])
    label_expect_rest_work_days_value.config(text= returnValue['ExpectRestWorkDays'])
    label_expect_rest_calendar_days_value.config(text= returnValue['ExpectRestCalendarkDays'])
    label_real_rest_work_days_value.config(text= returnValue['RealRestWorkDays'])
    label_real_rest_calendar_days_value.config(text= returnValue['RealRestCalendarkDays'])

def func_export_daily_eport():
    if globalStartDate and globalCurrentDate:

        if radio_var.get() == 'OneDayOff':
            ExportDailyReportForm.create_weather_report_form(ScheduleCount.WorkDay.ONE_DAY_OFF, globalStartDate, globalCurrentDate)
        elif radio_var.get() == 'TwoDayOff':
            ExportDailyReportForm.create_weather_report_form(ScheduleCount.WorkDay.TWO_DAY_OFF, globalStartDate, globalCurrentDate)
        elif radio_var.get() == 'NoDayOff':
            ExportDailyReportForm.create_weather_report_form(ScheduleCount.WorkDay.NO_DAY_OFF, globalStartDate, globalCurrentDate)

def func_export_expect_finish_form():
    if globalStartDate and globalCurrentDate:
        if radio_var.get() == 'OneDayOff':
            ExportExpectFinishForm.create_expect_finish_form(ScheduleCount.WorkDay.ONE_DAY_OFF, int(spinbox_var.get()), globalStartDate)
        elif radio_var.get() == 'TwoDayOff':
            ExportExpectFinishForm.create_expect_finish_form(ScheduleCount.WorkDay.TWO_DAY_OFF, int(spinbox_var.get()), globalStartDate)
        elif radio_var.get() == 'NoDayOff':
            ExportExpectFinishForm.create_expect_finish_form(ScheduleCount.WorkDay.NO_DAY_OFF, int(spinbox_var.get()), globalStartDate)
    pass

group_frame_select_date = Frame(window)
group_frame_select_date.pack(padx=10, pady=10)

calendar_select_start_date = Calendar(group_frame_select_date, selectmode='day', date_pattern='yyyy-mm-dd',year=2023,month=1,day=1)
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
radio_button_no_day_off = Radiobutton(window, text="無周休", variable=radio_var, value="NoDayOff", command=func_update_radio_button_selection)
radio_button_no_day_off.pack(padx=10, anchor="w")

radio_button_one_day_off = Radiobutton(window, text="周休一日", variable=radio_var, value="OneDayOff", command=func_update_radio_button_selection)
radio_button_one_day_off.pack(padx=10, anchor="w")

radio_button_two_day_off = Radiobutton(window, text="周休二日", variable=radio_var, value="TwoDayOff", command=func_update_radio_button_selection)
radio_button_two_day_off.pack(padx=10, anchor="w")

radio_var.set("OneDayOff")

group_frame_total_work_days = Frame(window)
group_frame_total_work_days.pack(anchor="w")

label_total_work_days = Label(group_frame_total_work_days, text="契約工期")
label_total_work_days.pack(side="left", padx=10, anchor="w")

spinbox_var = StringVar()
spinbox_total_work_days = Spinbox(group_frame_total_work_days, from_=1, to=1000, textvariable=spinbox_var, command=func_update_value)
spinbox_total_work_days.pack(side="left")


group_frame_expect_finish_date = Frame(window)
group_frame_expect_finish_date.pack(anchor="w")

label_expect_finish_date = Label(group_frame_expect_finish_date, text="預計完工日")
label_expect_finish_date.pack(side="left", padx=10)
label_expect_finish_date_value = Label(group_frame_expect_finish_date, text="?")
label_expect_finish_date_value.pack(side="left", padx=10)


group_frame_expect_total_calendar_days = Frame(window)
group_frame_expect_total_calendar_days.pack(anchor="w")

label_expect_total_calendar_days = Label(group_frame_expect_total_calendar_days, text="預計完工天數")
label_expect_total_calendar_days.pack(side="left", padx=10)
label_expect_total_calendar_days_value = Label(group_frame_expect_total_calendar_days, text="?")
label_expect_total_calendar_days_value.pack(side="left", padx=10)


group_frame_from_start_work_days = Frame(window)
group_frame_from_start_work_days.pack(anchor="w")

label_from_start_work_days = Label(group_frame_from_start_work_days, text="開工迄今工作天數")
label_from_start_work_days.pack(side="left", padx=10)
label_from_start_work_days_value = Label(group_frame_from_start_work_days, text="?")
label_from_start_work_days_value.pack(side="left", padx=10)


group_frame_from_start_calendar_days = Frame(window)
group_frame_from_start_calendar_days.pack(anchor="w")

label_from_start_calendar_days = Label(group_frame_from_start_calendar_days, text="開工迄今日曆天數")
label_from_start_calendar_days.pack(side="left", padx=10)
label_from_start_calendar_days_value = Label(group_frame_from_start_calendar_days, text="?")
label_from_start_calendar_days_value.pack(side="left", padx=10)


group_frame_real_finish_date = Frame(window)
group_frame_real_finish_date.pack(anchor="w")

label_real_finish_date = Label(group_frame_real_finish_date, text="變動完工日")
label_real_finish_date.pack(side="left",padx=10)
label_real_finish_date_value = Label(group_frame_real_finish_date, text="?")
label_real_finish_date_value.pack(side="left", padx=10)


group_frame_real_total_calendar_days = Frame(window)
group_frame_real_total_calendar_days.pack(anchor="w")

label_real_total_calendar_days = Label(group_frame_real_total_calendar_days, text="變動完工天數")
label_real_total_calendar_days.pack(side="left",padx=10)
label_real_total_calendar_days_value = Label(group_frame_real_total_calendar_days, text="?")
label_real_total_calendar_days_value.pack(side="left", padx=10)


group_frame_expect_rest_work_days = Frame(window)
group_frame_expect_rest_work_days.pack(anchor="w")

label_expect_rest_work_days = Label(group_frame_expect_rest_work_days, text="預計剩餘工期")
label_expect_rest_work_days.pack(side="left",padx=10)
label_expect_rest_work_days_value = Label(group_frame_expect_rest_work_days, text="?")
label_expect_rest_work_days_value.pack(side="left", padx=10)


group_frame_expect_rest_calendar_days = Frame(window)
group_frame_expect_rest_calendar_days.pack(anchor="w")

label_expect_rest_calendar_days = Label(group_frame_expect_rest_calendar_days, text="預計剩餘天數")
label_expect_rest_calendar_days.pack(side="left",padx=10)
label_expect_rest_calendar_days_value = Label(group_frame_expect_rest_calendar_days, text="?")
label_expect_rest_calendar_days_value.pack(side="left", padx=10)


group_frame_real_rest_work_days = Frame(window)
group_frame_real_rest_work_days.pack(anchor="w")

label_real_rest_work_days = Label(group_frame_real_rest_work_days, text="實際剩餘工期")
label_real_rest_work_days.pack(side="left",padx=10)
label_real_rest_work_days_value = Label(group_frame_real_rest_work_days, text="?")
label_real_rest_work_days_value.pack(side="left", padx=10)


group_frame_real_rest_calendar_days = Frame(window)
group_frame_real_rest_calendar_days.pack(anchor="w")

label_real_rest_calendar_days = Label(group_frame_real_rest_calendar_days, text="實際剩餘天數")
label_real_rest_calendar_days.pack(side="left",padx=10)
label_real_rest_calendar_days_value = Label(group_frame_real_rest_calendar_days, text="?")
label_real_rest_calendar_days_value.pack(side="left", padx=10)

group_frame_calculate_export = Frame(window)
group_frame_calculate_export.pack(anchor="w")

button_calculate = Button(group_frame_calculate_export, text="計算", command=func_calculate_schedule)
button_calculate.pack(side="left",padx=5)

button_export_dailyreport = Button(group_frame_calculate_export, text="輸出晴雨日報表", command=func_export_daily_eport)
button_export_dailyreport.pack(side="left",padx=5)

button_export_expect_finish = Button(group_frame_calculate_export, text="輸出預計完工表", command=func_export_expect_finish_form)
button_export_expect_finish.pack(side="left",padx=5)

window.mainloop()



