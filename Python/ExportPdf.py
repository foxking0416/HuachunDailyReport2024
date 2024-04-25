import json
import os
from datetime import datetime
import ScheduleCount
import openpyxl
from openpyxl.drawing.image import Image
from openpyxl.utils import get_column_letter
from openpyxl.styles import Alignment
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

from openpyxl import Workbook
from openpyxl.drawing.spreadsheet_drawing import AbsoluteAnchor
from openpyxl.drawing.xdr import XDRPoint2D, XDRPositiveSize2D
from openpyxl.utils.units import pixels_to_EMU, cm_to_EMU
from openpyxl.drawing.spreadsheet_drawing import OneCellAnchor, AnchorMarker

import unittest


def ReadCellDimension( worksheet ):
    column_widthA = worksheet.column_dimensions["A"].width
    column_widthB = worksheet.column_dimensions["B"].width
    row_height1 = worksheet.row_dimensions[1].height
    row_height2 = worksheet.row_dimensions[2].height
    print(column_widthA)
    print(column_widthB)
    print(row_height1)
    print(row_height2)


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

    coloffset = cellw(0.5)
    rowoffset = cellh(0.5)

    h, w = img_template.height, img_template.width
    p2e = pixels_to_EMU
    size = XDRPositiveSize2D(p2e(w), p2e(h))

    # Open the Excel file
    workbook = openpyxl.load_workbook(input_excel)
    # Select the active worksheet
    worksheet = workbook.active


    with open(json_file_path,'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        date_obj = datetime.strptime(item["date"], "%Y-%m-%d")
        year = date_obj.year
        cell_num = get_cell_num(item["date"])
        column = cell_num['ColumnNum']-1
        row = cell_num['RowNum']-1
        img = None
        if year == 2023:
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
    date_obj = datetime.strptime(date, "%Y-%m-%d")
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
    date_obj = datetime.strptime(date, "%Y-%m-%d")
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

# input_excel = 'C:\\_Everything\\HuachunDailyReport2024\\Python\\DailyReportTemplate.xlsx'
# image_path_sun_all = 'C:\\_Everything\\HuachunDailyReport2024\\Python\\Sun_All.png'
# output_excel = 'C:\\_Everything\\HuachunDailyReport2024\\Python\\DailyReportFinal.xlsx'
# insert_image_into_excel(input_excel, output_excel, image_path_sun_all)

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