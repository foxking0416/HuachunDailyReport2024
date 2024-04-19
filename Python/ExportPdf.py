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


def InsertImageIntoExcel(excel_file, image_path, output_excel):
    # Open the Excel file
    workbook = openpyxl.load_workbook(excel_file)
    


    # Select the active worksheet
    worksheet = workbook.active
    ReadCellDimension(worksheet)



    # Load the image
    img = Image(image_path)
    
    # Calculate dimensions and resize if needed
    img.width, img.height = img.width * 0.2, img.height * 0.2
    
    c2e = cm_to_EMU
    # Calculated number of cells width or height from cm into EMUs
    cellh = lambda x: c2e((x * 49.77)/99)
    cellw = lambda x: c2e((x * (18.65-1.71))/10)


    h, w = img.height, img.width
    p2e = pixels_to_EMU
    size = XDRPositiveSize2D(p2e(w), p2e(h))

    column = 0
    coloffset = cellw(0.5)
    row = 0
    rowoffset = cellh(0.5)
    marker = AnchorMarker(col=column, colOff=coloffset, row=row, rowOff=rowoffset)
    img.anchor = OneCellAnchor(_from=marker, ext=size)

    worksheet.add_image(img)

    # Save the modified Excel file
    workbook.save(output_excel)


    pass

def read_data_and_export_file():
    arrGlobalConstHoliday = []
    arrGlobalConstWorkday = []
    dictGlobalWeatherRelatedHoliday = {}
    dictGlobalExtendData = {}
    ScheduleCount.LoadJsonHolidayData(arrGlobalConstHoliday,arrGlobalConstWorkday)

    current_dir = os.path.dirname(__file__)
    json_file_path = os.path.join(current_dir, 'DailyReport.json')

    with open(json_file_path,'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        date_obj = datetime.strptime(item["date"], "%Y-%m-%d")
        year = date_obj.year
        month = date_obj.month
        day = date_obj.day

        weekday = date_obj.weekday()

        first_day_per_month = datetime(year, month, day)


        # nWeekday = kExpectEndDate.weekday()

        if item["morning_weather"] == 0:
            if item["afternoon_weather"] == 0:
                pass
            else:
                pass
            pass
        else:
            if item["afternoon_weather"] == 0:
                pass
            else:
                pass
    pass

def test_week_num( date ):
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

# Example usage
# excel_file = 'C:\\_Everything\\HuachunDailyReport2024\\Python\\test.xlsx'
# image_path_sun_all = 'C:\\_Everything\\HuachunDailyReport2024\\Python\\Sun_All.png'
# image_path_rain_all = 'C:\\_Everything\\HuachunDailyReport2024\\Python\\Rain_All.png'



# output_excel = 'C:\\_Everything\\HuachunDailyReport2024\\Python\\testOutput.xlsx'
# pdf_file = 'C:\\_Everything\\HuachunDailyReport2024\\Python\\output.pdf'
# InsertImageIntoExcel(excel_file, image_path_sun_all, output_excel)

# read_data_and_export_file()

# test_week_num('2024-03-10')

class TestFunction(unittest.TestCase):
    def test_week_number_1(self):
        returnValue = test_week_num('2024-02-14')
        self.assertEqual(returnValue, 3)
        returnValue = test_week_num('2024-03-09')
        self.assertEqual(returnValue, 2)
        returnValue = test_week_num('2024-03-10')
        self.assertEqual(returnValue, 3)
        returnValue = test_week_num('2024-03-31')
        self.assertEqual(returnValue, 6)
        returnValue = test_week_num('2024-04-06')
        self.assertEqual(returnValue, 1)
        returnValue = test_week_num('2024-04-07')
        self.assertEqual(returnValue, 2)
        returnValue = test_week_num('2024-06-30')
        self.assertEqual(returnValue, 6)
        returnValue = test_week_num('2024-09-07')
        self.assertEqual(returnValue, 1)
        returnValue = test_week_num('2024-09-14')
        self.assertEqual(returnValue, 2)





if __name__ == '__main__':
    unittest.main()