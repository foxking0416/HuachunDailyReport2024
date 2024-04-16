#打包指令
#pyinstaller --hidden-import "babel.numbers" PythonUI.py
import ScheduleCount
from tkinter import *
from tkcalendar import Calendar

globalStartDate = None
globalCurrentDate = None

window = Tk()
window.title("工期計算測試程式")
window.minsize(width=500, height=500)
window.resizable(width=True, height=True)



def SelectStartDate(event):
    global globalStartDate
    globalStartDate = calendar_select_start_date.get_date()
    label_start_date_value.config(text= globalStartDate)


def SelectCurrentDate(event):
    global globalCurrentDate
    globalCurrentDate = calendar_select_current_date.get_date()
    label_current_date_value.config(text= globalCurrentDate)

def UpdateRadioButtonSelection():
    selected_option = radio_var.get()
    # selection_label.config(text="Selected option: " + selected_option)

def UpdateValue():
    selected_value = spinbox_var.get()
    # value_label.config(text="Selected value: " + selected_value)


def CalculateSchedule():
    arrConstHoliday = []
    arrConstWorkday = []
    dictWeatherRelatedHoliday = {}
    dictExtendData = {}
    ScheduleCount.LoadJsonHolidayData(arrConstHoliday,arrConstWorkday)
    ScheduleCount.LoadJsonDailyReportData(dictWeatherRelatedHoliday)
    ScheduleCount.LoadJsonExtendData(dictExtendData)
    if radio_var.get() == 'OneDayOff':
        returnValue = ScheduleCount.CountRealFinishDate(ScheduleCount.WorkDay.ONE_DAY_OFF, int(spinbox_var.get()), globalStartDate, globalCurrentDate, arrConstHoliday, arrConstWorkday, dictWeatherRelatedHoliday, dictExtendData)
        label_expect_finish_date_value.config(text= returnValue['ExpectFinishDate'])
        label_expect_total_calendar_days_value.config(text= returnValue['ExpectTotalCalendarDays'])
        label_real_finish_date_value.config(text= returnValue['RealFinishDate'])
        label_real_total_calendar_days_value.config(text= returnValue['RealTotalCalendarDays'])
        label_expect_rest_work_days_value.config(text= returnValue['ExpectRestWorkDays'])
        label_expect_rest_calendar_days_value.config(text= returnValue['ExpectRestCalendarkDays'])
        label_real_rest_work_days_value.config(text= returnValue['RealRestWorkDays'])
        label_real_rest_calendar_days_value.config(text= returnValue['RealRestCalendarkDays'])
    elif radio_var.get() == 'TwoDayOff':
        returnValue = ScheduleCount.CountRealFinishDate(ScheduleCount.WorkDay.TWO_DAY_OFF, int(spinbox_var.get()), globalStartDate, globalCurrentDate, arrConstHoliday, arrConstWorkday, dictWeatherRelatedHoliday, dictExtendData)
        label_expect_finish_date_value.config(text= returnValue['ExpectFinishDate'])
        label_expect_total_calendar_days_value.config(text= returnValue['ExpectTotalCalendarDays'])
        label_real_finish_date_value.config(text= returnValue['RealFinishDate'])
        label_real_total_calendar_days_value.config(text= returnValue['RealTotalCalendarDays'])
        label_expect_rest_work_days_value.config(text= returnValue['ExpectRestWorkDays'])
        label_expect_rest_calendar_days_value.config(text= returnValue['ExpectRestCalendarkDays'])
        label_real_rest_work_days_value.config(text= returnValue['RealRestWorkDays'])
        label_real_rest_calendar_days_value.config(text= returnValue['RealRestCalendarkDays'])

group_frame_select_date = Frame(window)
group_frame_select_date.pack(padx=10, pady=10)

calendar_select_start_date = Calendar(group_frame_select_date, selectmode='day', date_pattern='yyyy-mm-dd',year=2023,month=1,day=1)
calendar_select_start_date.pack(side="left", padx=10)
calendar_select_start_date.bind("<<CalendarSelected>>", SelectStartDate)

calendar_select_current_date = Calendar(group_frame_select_date, selectmode='day', date_pattern='yyyy-mm-dd',year=2023,month=1,day=1)
calendar_select_current_date.pack(side="left", padx=10)
calendar_select_current_date.bind("<<CalendarSelected>>", SelectCurrentDate)

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
radio_button_one_day_off = Radiobutton(window, text="周休一日", variable=radio_var, value="OneDayOff", command=UpdateRadioButtonSelection)
radio_button_one_day_off.pack(padx=10, anchor="w")

radio_button_two_day_off = Radiobutton(window, text="周休二日", variable=radio_var, value="TwoDayOff", command=UpdateRadioButtonSelection)
radio_button_two_day_off.pack(padx=10, anchor="w")

radio_var.set("OneDayOff")

group_frame_total_work_days = Frame(window)
group_frame_total_work_days.pack(anchor="w")

label_total_work_days = Label(group_frame_total_work_days, text="契約工期")
label_total_work_days.pack(side="left", padx=10, anchor="w")

spinbox_var = StringVar()
spinbox_total_work_days = Spinbox(group_frame_total_work_days, from_=1, to=1000, textvariable=spinbox_var, command=UpdateValue)
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


button_calculate = Button(window, text="計算", command=CalculateSchedule)
button_calculate.pack(padx=5)

window.mainloop()



