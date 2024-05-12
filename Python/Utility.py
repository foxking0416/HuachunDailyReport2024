import os
import win32com.client

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