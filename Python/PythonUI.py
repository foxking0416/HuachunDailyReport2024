from tkinter import *
# import tkinter as tk
# from tkinter import ttk
from tkcalendar import Calendar

window = Tk()
window.title("工期計算測試程式")
window.minsize(width=500, height=500)
window.resizable(width=True, height=True)

def select_start_date():
    selected_date = calendar_select_start_date.get_date()
    label_start_date_value.config(text= selected_date)

def select_current_date():
    selected_date = calendar_select_current_date.get_date()
    label_current_date_value.config(text= selected_date)

group_frame_select_date = Frame(window)
group_frame_select_date.pack(padx=10, pady=10)

group_frame_select_start_date = Frame(group_frame_select_date)
group_frame_select_start_date.pack(side="left", padx=10)
calendar_select_start_date = Calendar(group_frame_select_start_date, selectmode='day', date_pattern='yyyy-mm-dd')
calendar_select_start_date.pack()
button_select_start_date = Button(group_frame_select_start_date, text="Select Start Date", command=select_start_date)
button_select_start_date.pack(padx=5)

group_frame_select_current_date = Frame(group_frame_select_date)
group_frame_select_current_date.pack(side="left", padx=10)
calendar_select_current_date = Calendar(group_frame_select_current_date, selectmode='day', date_pattern='yyyy-mm-dd')
calendar_select_current_date.pack()
button_select_current_date = Button(group_frame_select_current_date, text="Select Current Date", command=select_current_date)
button_select_current_date.pack(padx=5)

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

def update_radio_button_selection():
    selected_option = radio_var.get()
    # selection_label.config(text="Selected option: " + selected_option)

radio_var = StringVar()
radio_button_one_day_off = Radiobutton(window, text="周休一日", variable=radio_var, value="Option 1", command=update_radio_button_selection)
radio_button_one_day_off.pack()

radio_button_two_day_off = Radiobutton(window, text="周休二日", variable=radio_var, value="Option 2", command=update_radio_button_selection)
radio_button_two_day_off.pack()

def update_value():
    selected_value = spinbox_var.get()
    # value_label.config(text="Selected value: " + selected_value)

group_frame_total_work_days = Frame(window)
group_frame_total_work_days.pack(anchor="w")

label_total_workdays = Label(group_frame_total_work_days, text="契約工期")
label_total_workdays.pack(side="left", padx=10, anchor="w")

spinbox_var = StringVar()
spinbox = Spinbox(group_frame_total_work_days, from_=1, to=1000, textvariable=spinbox_var, command=update_value)
spinbox.pack(side="left")


group_frame_expect_total_calendar_days = Frame(window)
group_frame_expect_total_calendar_days.pack(anchor="w")

label_expect_total_calendar_days = Label(group_frame_expect_total_calendar_days, text="契約天數")
label_expect_total_calendar_days.pack(side="left", padx=10)
label_expect_total_calendar_days_value = Label(group_frame_expect_total_calendar_days, text="?")
label_expect_total_calendar_days_value.pack(side="left", padx=10)


group_frame_expect_finish_date = Frame(window)
group_frame_expect_finish_date.pack(anchor="w")

label_expect_finish_date = Label(group_frame_expect_finish_date, text="預計完工日")
label_expect_finish_date.pack(side="left", padx=10)
label_expect_finish_date_value = Label(group_frame_expect_finish_date, text="?")
label_expect_finish_date_value.pack(side="left", padx=10)


group_frame_real_finish_date = Frame(window)
group_frame_real_finish_date.pack(anchor="w")

label_real_finish_date = Label(group_frame_real_finish_date, text="變動完工日")
label_real_finish_date.pack(side="left",padx=10)
label_real_finish_date_value = Label(group_frame_real_finish_date, text="?")
label_real_finish_date_value.pack(side="left", padx=10)

button_calculate = Button(window, text="計算", command=select_start_date)
button_calculate.pack(padx=5)

window.mainloop()



