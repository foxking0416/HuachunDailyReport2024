import ScheduleCount
import json
import os
import datetime
import unittest
import openpyxl
from openpyxl.drawing.image import Image
from openpyxl.drawing.xdr import XDRPoint2D, XDRPositiveSize2D
from openpyxl.utils.units import pixels_to_EMU, cm_to_EMU
from openpyxl.drawing.spreadsheet_drawing import OneCellAnchor, AnchorMarker

def insert_image_into_excel(input_excel, output_excel, image_path):
    # Open the Excel file
    workbook = openpyxl.load_workbook(input_excel)

    # Select the active worksheet
    worksheet = workbook.active
    # ReadCellDimension(worksheet)

    # Load the image
    img = Image(image_path)
    
    # Calculate dimensions and resize if needed
    c2e = cm_to_EMU
    # Calculated number of cells width or height from cm into EMUs
    cellh = lambda x: c2e((x * 49.77)/99)
    cellw = lambda x: c2e((x * (18.65-1.71))/10)


    h, w = img.height, img.width
    p2e = pixels_to_EMU
    size = XDRPositiveSize2D(p2e(w), p2e(h))

    column = 1
    coloffset = cellw(0.5)
    row = 1
    rowoffset = cellh(0.5)
    marker = AnchorMarker(col=column, colOff=coloffset, row=row, rowOff=rowoffset)
    img.anchor = OneCellAnchor(_from=marker, ext=size)

    worksheet.add_image(img)


    img2 = Image(image_path)
    img2.width, img2.height = img2.width * 0.2, img2.height * 0.2
    column = 2
    row = 2
    marker = AnchorMarker(col=column, colOff=coloffset, row=row, rowOff=rowoffset)
    img2.anchor = OneCellAnchor(_from=marker, ext=size)

    worksheet.add_image(img2)

    # Save the modified Excel file
    workbook.save(output_excel)

def fill_in_day_each_month(worksheet, input_year):
    first_day = str(input_year) + '-01-01'
    date_obj = datetime.datetime.strptime(first_day, "%Y-%m-%d")  
    is_leap_year = ( input_year % 4 == 0 )

    if is_leap_year:
        days_a_year = 366
    else:
        days_a_year = 365

    for i in range(days_a_year):
        day = date_obj.day
        str_date = date_obj.strftime("%Y-%m-%d")

        cell_num = get_cell_num(str_date)
        column = cell_num['ColumnNum']
        row = cell_num['RowNum']+1
        cell = number_to_string(column)+str(row)
        worksheet[cell] = day
        date_obj += datetime.timedelta(days=1)

def read_data_and_export_file():
    arrGlobalConstHoliday = []
    arrGlobalConstWorkday = []
    dictGlobalWeatherRelatedHoliday = {}
    dictGlobalExtendData = {}
    ScheduleCount.LoadJsonHolidayData(arrGlobalConstHoliday,arrGlobalConstWorkday)

    current_dir = os.path.dirname(__file__)
    json_file_path = os.path.join(current_dir, 'DailyReport.json')
    input_excel =  os.path.join(current_dir, 'DailyReportTemplate.xlsx')
    output_excel = os.path.join(current_dir, 'DailyReportFinal.xlsx') 
    image_path_sun_all = os.path.join(current_dir, 'Image\\Sun_All.png') 
    image_path_rain_all = os.path.join(current_dir, 'Image\\Rain_All.png') 
    image_path_sun_up_rain_down = os.path.join(current_dir, 'Image\\Sun_Up_Rain_Down.png') 
    image_path_rain_up_sun_down = os.path.join(current_dir, 'Image\\Rain_Up_Sun_Down.png') 

    img_template = Image(image_path_sun_all)


    c2e = cm_to_EMU
    # Calculated number of cells width or height from cm into EMUs
    cellh = lambda x: c2e((x * 49.77)/99)
    cellw = lambda x: c2e((x * (18.65-1.71))/10)

    coloffset = cellw(0.1) #304919
    rowoffset = cellh(0.25) #90490

    h, w = img_template.height, img_template.width #pixel
    p2e = pixels_to_EMU
    p2ew = p2e(w) #30 pixel = 285750 EMU ==> 1 pixel = 9525
    p2eh = p2e(h) #29 pixel = 276225 EMU ==> 1 pixel = 9525

    size = XDRPositiveSize2D(p2e(w), p2e(h))

    workbook = openpyxl.load_workbook(input_excel)
    worksheet = workbook.active


    with open(json_file_path,'r', encoding='utf-8') as f:
        data = json.load(f)

    #先看有多少年的資料，建立所需worksheet
    lastyear = 0
    for item in data:
        date_obj = datetime.datetime.strptime(item["date"], "%Y-%m-%d")
        year = date_obj.year

        if year != lastyear:
            if lastyear != 0:
                worksheet = workbook.copy_worksheet(worksheet)
            worksheet.title = str(year) + '年'
            worksheet['B4'] = str(year) + '年(' + str(year-1911) + '年)' 

            lastyear = year

    worksheet_index = 0
    lastyear = 0
    for item in data:
        date_obj = datetime.datetime.strptime(item["date"], "%Y-%m-%d")
        year = date_obj.year
        cell_num = get_cell_num(item["date"])
        column = cell_num['ColumnNum']-1
        row = cell_num['RowNum']-1
        img = None

        if year != lastyear:
            worksheet = workbook.worksheets[worksheet_index]
            fill_in_day_each_month(worksheet, year)
            lastyear = year
            worksheet_index += 1
    
        print( item["date"])
        if item["morning_weather"] == 0:
            if item["afternoon_weather"] == 0:
                img = Image(image_path_sun_all)
            else:
                img = Image(image_path_sun_up_rain_down)
            pass
        else:
            if item["afternoon_weather"] == 0:
                img = Image(image_path_rain_up_sun_down)
            else:
                img = Image(image_path_rain_all)
        marker = AnchorMarker(col=column, colOff=coloffset, row=row, rowOff=rowoffset)
        img.anchor = OneCellAnchor(_from=marker, ext=size)
        worksheet.add_image(img)

    serial_number = 1
    filename, extension = os.path.splitext(output_excel)
    while os.path.exists(output_excel):
        # 如果文件已经存在，则添加流水号并重新检查
        output_excel = f"{filename}_{serial_number}{extension}"
        serial_number += 1


    workbook.save(output_excel)

    print('finish')
    pass

def number_to_string(n):
    result = ''
    while n > 0:
        n -= 1
        result = chr(ord('A') + n % 26) + result
        n //= 26
    return result

def get_cell_num( date ):
    date_obj = datetime.datetime.strptime(date, "%Y-%m-%d")
    month = date_obj.month
    day = date_obj.day
    weekday = ( date_obj.weekday() + 2 ) % 7 
    if weekday == 0:
        weekday += 7
    row_num = 6 + month * 2
    week_num = get_week_num( date )
    column_num = 1 + ( week_num - 1 ) * 7 + weekday


    returnValue = {}
    returnValue['WeekNum'] = week_num
    returnValue['RowNum'] = row_num
    returnValue['ColumnNum'] = column_num
    returnValue['ColumnString'] = number_to_string( column_num )
    return returnValue

def get_week_num( date ):
    date_obj = datetime.datetime.strptime(date, "%Y-%m-%d")
    day = date_obj.day

    weekday = ( date_obj.weekday() + 2 ) % 7 
    if weekday == 0:
        weekday += 7
    week_num = (day - 1) // 7 + 1
    rest = day % 7
    if rest == 0:
        rest += 7
    if weekday - rest < 0:
        week_num += 1
    
    return week_num


read_data_and_export_file()

class TestFunction(unittest.TestCase):
    def test_week_number_1(self):
        returnValue = get_cell_num('2024-02-14')
        self.assertEqual(returnValue['WeekNum'], 3)
        self.assertEqual(returnValue['RowNum'], 10)
        self.assertEqual(returnValue['ColumnNum'], 19)
        self.assertEqual(returnValue['ColumnString'], 'S')

        returnValue = get_cell_num('2024-03-09')
        self.assertEqual(returnValue['WeekNum'], 2)
        self.assertEqual(returnValue['RowNum'], 12)
        self.assertEqual(returnValue['ColumnNum'], 15)
        self.assertEqual(returnValue['ColumnString'], 'O')

        returnValue = get_cell_num('2024-03-10')
        self.assertEqual(returnValue['WeekNum'], 3)
        self.assertEqual(returnValue['RowNum'], 12)
        self.assertEqual(returnValue['ColumnNum'], 16)
        self.assertEqual(returnValue['ColumnString'], 'P')

        returnValue = get_cell_num('2024-03-31')
        self.assertEqual(returnValue['WeekNum'], 6)
        self.assertEqual(returnValue['RowNum'], 12)
        self.assertEqual(returnValue['ColumnNum'], 37)
        self.assertEqual(returnValue['ColumnString'], 'AK')

        returnValue = get_cell_num('2024-04-06')
        self.assertEqual(returnValue['WeekNum'], 1)
        self.assertEqual(returnValue['RowNum'], 14)
        self.assertEqual(returnValue['ColumnNum'], 8)
        self.assertEqual(returnValue['ColumnString'], 'H')

        returnValue = get_cell_num('2024-04-07')
        self.assertEqual(returnValue['WeekNum'], 2)
        self.assertEqual(returnValue['RowNum'], 14)
        self.assertEqual(returnValue['ColumnNum'], 9)
        self.assertEqual(returnValue['ColumnString'], 'I')

        returnValue = get_cell_num('2024-06-30')
        self.assertEqual(returnValue['WeekNum'], 6)
        self.assertEqual(returnValue['RowNum'], 18)
        self.assertEqual(returnValue['ColumnNum'], 37)
        self.assertEqual(returnValue['ColumnString'], 'AK')

        returnValue = get_cell_num('2024-09-07')
        self.assertEqual(returnValue['WeekNum'], 1)
        self.assertEqual(returnValue['RowNum'], 24)
        self.assertEqual(returnValue['ColumnNum'], 8)
        self.assertEqual(returnValue['ColumnString'], 'H')
        
        returnValue = get_cell_num('2024-09-14')
        self.assertEqual(returnValue['WeekNum'], 2)
        self.assertEqual(returnValue['RowNum'], 24)
        self.assertEqual(returnValue['ColumnNum'], 15)
        self.assertEqual(returnValue['ColumnString'], 'O')

# if __name__ == '__main__':
#     unittest.main()