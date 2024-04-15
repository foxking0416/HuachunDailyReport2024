from tkinter import *
# import tkinter as tk
# from tkinter import ttk
from tkcalendar import Calendar

window = Tk()
window.title("日報表測試程式")
window.minsize(width=500, height=500)
window.resizable(width=True, height=True)

def select_start_date():
    selected_date = calendar_select_start_date.get_date()
    label_selected_start_date.config(text= selected_date)

def select_current_date():
    selected_date = calendar_select_current_date.get_date()
    label_selected_current_date.config(text= selected_date)

group_frame_select_date = Frame(window)
group_frame_select_date.pack(padx=10, pady=10)

group_frame_select_start_date = Frame(group_frame_select_date)
group_frame_select_start_date.pack(side="left", padx=10)
calendar_select_start_date = Calendar(group_frame_select_start_date, selectmode='day', date_pattern='yyyy-mm-dd')
calendar_select_start_date.pack(pady=20)
button_select_start_date = Button(group_frame_select_start_date, text="Select Start Date", command=select_start_date)
button_select_start_date.pack(pady=10, padx=5)


group_frame_select_current_date = Frame(group_frame_select_date)
group_frame_select_current_date.pack(side="left", padx=10)
calendar_select_current_date = Calendar(group_frame_select_current_date, selectmode='day', date_pattern='yyyy-mm-dd')
calendar_select_current_date.pack(pady=20)
button_select_current_date = Button(group_frame_select_current_date, text="Select Current Date", command=select_current_date)
button_select_current_date.pack(pady=10, padx=5)

group_frame_start_date_label = Frame(window)
group_frame_start_date_label.pack(anchor="w")

label_start_date = Label(group_frame_start_date_label, text="開工日期")
label_start_date.pack(side="left",padx=10)

# 顯示選擇的日期
label_selected_start_date = Label(group_frame_start_date_label, text="")
label_selected_start_date.pack(side="left")


group_frame_current_date_label = Frame(window)
group_frame_current_date_label.pack(anchor="w")

label_current_date = Label(group_frame_current_date_label, text="今日日期")
label_current_date.pack(side="left",padx=10 )

# 顯示選擇的日期
label_selected_current_date = Label(group_frame_current_date_label, text="")
label_selected_current_date.pack(side="left")





label_total_workDays = Label(window, text="契約工期")
label_total_workDays.pack(padx=10, anchor="w")

label_expect_total_calendar_days = Label(window, text="契約天數")
label_expect_total_calendar_days.pack(padx=10, anchor="w")



window.mainloop()



