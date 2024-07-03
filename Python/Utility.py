import os
import win32com.client
import openpyxl
from openpyxl.drawing.image import Image
from openpyxl.drawing.xdr import XDRPoint2D, XDRPositiveSize2D
from openpyxl.utils.units import pixels_to_EMU, cm_to_EMU
from openpyxl.drawing.spreadsheet_drawing import OneCellAnchor, AnchorMarker


current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
json_file_path = os.path.join(current_dir, 'ExternalData\\DailyReport.json')
input_excel =  os.path.join(current_dir, 'ExternalData\\DailyReportTemplate.xlsx')
output_excel = os.path.join(parent_dir, 'DailyReportFinal.xlsx') 
image_path_holiday = os.path.join(current_dir, 'ExternalData\\Image\\Holiday.png') 
image_path_workday = os.path.join(current_dir, 'ExternalData\\Image\\Workday.png') 
image_path_start_day = os.path.join(current_dir, 'ExternalData\\Image\\StartDay.png') 
image_path_expect_finish_day = os.path.join(current_dir, 'ExternalData\\Image\\ExpectFinishDay.png') 
image_path_sun_up = os.path.join(current_dir, 'ExternalData\\Image\\Sun_Up.png')
image_path_sun_down = os.path.join(current_dir, 'ExternalData\\Image\\Sun_Down.png')
image_path_rain_up = os.path.join(current_dir, 'ExternalData\\Image\\Rain_Up.png')
image_path_rain_down = os.path.join(current_dir, 'ExternalData\\Image\\Rain_Down.png') 
image_path_heavyrain_up = os.path.join(current_dir, 'ExternalData\\Image\\HeavyRain_Up.png')
image_path_heavyrain_down = os.path.join(current_dir, 'ExternalData\\Image\\HeavyRain_Down.png') 
image_path_typhoon_up = os.path.join(current_dir, 'ExternalData\\Image\\Typhoon_Up.png')
image_path_typhoon_down = os.path.join(current_dir, 'ExternalData\\Image\\Typhoon_Down.png')
image_path_hot_up = os.path.join(current_dir, 'ExternalData\\Image\\Hot_Up.png')
image_path_hot_down = os.path.join(current_dir, 'ExternalData\\Image\\Hot_Down.png')

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

