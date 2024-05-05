import ScheduleCount
import json
import os
import datetime
import unittest
import openpyxl
import win32com.client
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

def insert_image(worksheet, image_path, marker, size):
    img = Image(image_path)
    img.anchor = OneCellAnchor(_from=marker, ext=size)
    worksheet.add_image(img)

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

def excel_to_pdf(excel_file, pdf_file):
    # 创建Excel应用程序对象
    excel = win32com.client.Dispatch("Excel.Application")
    # 打开Excel文件
    wb = excel.Workbooks.Open(excel_file)

    sheet_index = 0
    for sheet in wb.Sheets:

        serial_number = 1
        filename, extension = os.path.splitext(pdf_file)
        filename = filename + '_' + sheet.Name
        output_pdf = filename + '.pdf'
        while os.path.exists(output_pdf):
            # 如果文件已经存在，则添加流水号并重新检查
            output_pdf = f"{filename}_{serial_number}{extension}"
            serial_number += 1

        # 选择要保存为PDF的工作表
        ws = wb.Worksheets[sheet_index]

        # 将Excel文件保存为PDF
        ws.ExportAsFixedFormat(0, output_pdf)
        sheet_index += 1

    # 关闭Excel文件和应用程序
    wb.Close(False)
    excel.Quit()

def read_data_and_export_file(eCountType, start_day, end_day):
    arrGlobalConstHoliday = []
    arrGlobalConstWorkday = []
    dictGlobalWeatherRelatedHoliday = {}
    dictGlobalExtendData = {}
    ScheduleCount.LoadJsonHolidayData(arrGlobalConstHoliday,arrGlobalConstWorkday)

    current_dir = os.path.dirname(__file__)
    json_file_path = os.path.join(current_dir, 'DailyReport.json')
    input_excel =  os.path.join(current_dir, 'DailyReportTemplate.xlsx')
    output_excel = os.path.join(current_dir, 'DailyReportFinal.xlsx') 
    image_path_holiday = os.path.join(current_dir, 'Image\\Holiday.png') 
    image_path_workday = os.path.join(current_dir, 'Image\\Workday.png') 
    image_path_sun_all = os.path.join(current_dir, 'Image\\Sun_All.png') 
    image_path_rain_all = os.path.join(current_dir, 'Image\\Rain_All.png') 
    image_path_sun_up_rain_down = os.path.join(current_dir, 'Image\\Sun_Up_Rain_Down.png') 
    image_path_rain_up_sun_down = os.path.join(current_dir, 'Image\\Rain_Up_Sun_Down.png') 
    image_path_sun_up = os.path.join(current_dir, 'Image\\Sun_Up.png')
    image_path_sun_down = os.path.join(current_dir, 'Image\\Sun_Down.png')
    image_path_rain_up = os.path.join(current_dir, 'Image\\Rain_Up.png')
    image_path_rain_down = os.path.join(current_dir, 'Image\\Rain_Down.png') 

    img_template = Image(image_path_sun_all)



    c2e = cm_to_EMU
    # Calculated number of cells width or height from cm into EMUs
    cellh = lambda x: c2e((x * 49.77)/99)
    cellw = lambda x: c2e((x * (18.65-1.71))/10)

    col_offset = cellw(0.1) #60984
    row_up_offset = cellh(0.25) #45245
    row_down_offset = cellh(1) #180981

    p2e = pixels_to_EMU

    whole_size = XDRPositiveSize2D(p2e(30), p2e(30))
    half_size = XDRPositiveSize2D(p2e(30), p2e(15))

    workbook = openpyxl.load_workbook(input_excel)
    worksheet = workbook.active


    with open(json_file_path,'r', encoding='utf-8') as f:
        data = json.load(f)

    #先看有多少年的資料，建立所需worksheet
    lastyear = 0
    for item in data:
        date_obj = datetime.datetime.strptime(item["date"], "%Y-%m-%d")

        start_date_obj = datetime.datetime.strptime(start_day, "%Y-%m-%d")
        end_date_obj = datetime.datetime.strptime(end_day, "%Y-%m-%d")

        if date_obj < start_date_obj:
            continue

        if date_obj > end_date_obj:
            break

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
        start_date_obj = datetime.datetime.strptime(start_day, "%Y-%m-%d")
        end_date_obj = datetime.datetime.strptime(end_day, "%Y-%m-%d")
        if date_obj < start_date_obj:
            continue

        if date_obj > end_date_obj:
            break

        nWeekday = date_obj.weekday()
        year = date_obj.year
        cell_num = get_cell_num(item["date"])
        column = cell_num['ColumnNum']-1
        row = cell_num['RowNum']-1
        up_marker = AnchorMarker(col=column, colOff=col_offset, row=row, rowOff=row_up_offset)
        down_marker = AnchorMarker(col=column, colOff=col_offset, row=row, rowOff=row_down_offset)

        if year != lastyear:
            worksheet = workbook.worksheets[worksheet_index]
            fill_in_day_each_month(worksheet, year)
            lastyear = year
            worksheet_index += 1
    
        print( item["date"])
        if item["morning_weather"] == 0:
            insert_image( worksheet, image_path_sun_up, up_marker, half_size)
        else:
            insert_image( worksheet, image_path_rain_up, up_marker, half_size)
        if item["afternoon_weather"] == 0:
            insert_image( worksheet, image_path_sun_down, down_marker, half_size)
        else:
            insert_image( worksheet, image_path_rain_down, down_marker, half_size)



        if eCountType == ScheduleCount.WorkDay.ONE_DAY_OFF:
            if nWeekday == 6:#Sunday
                if item["date"] in arrGlobalConstWorkday:
                    insert_image( worksheet, image_path_workday, up_marker, whole_size)
                else:
                    insert_image( worksheet, image_path_holiday, up_marker, whole_size)
            else:
                if item["date"] in arrGlobalConstHoliday:
                    insert_image( worksheet, image_path_holiday, up_marker, whole_size)
        elif eCountType == ScheduleCount.WorkDay.TWO_DAY_OFF:
            if nWeekday == 6 or nWeekday == 5:#Sunday Saturday
                if item["date"] in arrGlobalConstWorkday:
                    insert_image( worksheet, image_path_workday, up_marker, whole_size)
                else:
                    insert_image( worksheet, image_path_holiday, up_marker, whole_size)
            else:
                if item["date"] in arrGlobalConstHoliday:
                    insert_image( worksheet, image_path_holiday, up_marker, whole_size)
        elif eCountType == ScheduleCount.WorkDay.NO_DAY_OFF:
            if item["date"] in arrGlobalConstHoliday:
                    insert_image( worksheet, image_path_holiday, up_marker, whole_size)

    any_serial_num = False
    serial_number = 1
    filename, extension = os.path.splitext(output_excel)
    while os.path.exists(output_excel):
        # 如果文件已经存在，则添加流水号并重新检查
        output_excel = f"{filename}_{serial_number}{extension}"
        serial_number += 1
        any_serial_num = True

    # serial_number = 1
    # filename, extension = os.path.splitext(output_pdf)
    # while os.path.exists(output_pdf):
    #     # 如果文件已经存在，则添加流水号并重新检查
    #     output_pdf = f"{filename}_{serial_number}{extension}"
    #     serial_number += 1
    if any_serial_num:
        serial_number -= 1
        output_pdf = f"{filename}_{serial_number}{'.pdf'}"
    else:
        output_pdf = f"{filename}{'.pdf'}"
    workbook.save( output_excel )
    excel_to_pdf( output_excel, output_pdf )
    print('finish')
    pass


# read_data_and_export_file(ScheduleCount.WorkDay.TWO_DAY_OFF, '2023-02-10', '2023-04-16' )




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