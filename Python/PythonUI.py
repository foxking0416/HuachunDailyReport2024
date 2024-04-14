from tkinter import *
# import tkinter as tk
# from tkinter import ttk
from tkcalendar import Calendar

window = Tk()
window.title("日報表測試程式")
window.minsize(width=500, height=500)
window.resizable(width=True, height=True)

label = Label(text="my label", font=("Arial", 14, "bold"), padx=5, pady=5, bg="red", fg="yellow")
label.pack()

def button_clicked():
    label.config(text="Hello World!")

button = Button(text="Click Me", font=("Arial", 14, "bold"), padx=5, pady=5, bg="blue", fg="light green", command=button_clicked)
button.pack()

cal = Calendar(window, selectmode='day', date_pattern='yyyy-mm-dd')
cal.pack(pady=20)

def select_date():
    selected_date = cal.get_date()
    selected_date_label.config(text="Selected date: " + selected_date)

labelStartDate = Label(window, text="開工日期")
labelStartDate.pack(padx=10, pady=10, anchor="w")

labelTotalWorkDays = Label(window, text="契約工期")
labelTotalWorkDays.pack(padx=10, anchor="w")

labelExpectTotalCalendarDays = Label(window, text="契約天數")
labelExpectTotalCalendarDays.pack(padx=10, anchor="w")

# 顯示選擇的日期
selected_date_label = Label(window, text="")
selected_date_label.pack(pady=10)

# 添加按鈕來獲取選擇的日期
select_button = Button(window, text="Select Date", command=select_date)
select_button.pack(pady=10, side="left", padx=5)

cancel_button = Button(window, text="Cancel")
cancel_button.pack(pady=10, side="left", padx=5)


window.mainloop()



