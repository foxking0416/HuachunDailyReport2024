# import pandas as pd
# import matplotlib.pyplot as plt

# # 創建一個示例數據
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David'],
#     'Age': [25, 30, 35, 40],
#     'Salary': [50000, 60000, 70000, 80000]
# }

# # 將數據轉換為 DataFrame
# df = pd.DataFrame(data)

# # 繪製表格
# plt.figure(figsize=(8, 4))
# plt.axis('off')  # 不顯示軸
# table = plt.table(cellText=df.values, colLabels=df.columns, loc='center')

# # 調整表格的格式
# table.auto_set_font_size(False)
# table.set_fontsize(12)
# table.scale(1.2, 1.2)

# # 將圖表保存為 PDF 檔案
# plt.savefig('E:\dev\_Python\HuachunDailyReport2024\Python\\table.pdf', bbox_inches='tight')
# plt.close()

# from reportlab.lib.pagesizes import letter
# from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image
# from reportlab.lib import colors

# def create_pdf_with_table_and_image(pdf_file, table_data, image_file):
#     doc = SimpleDocTemplate(pdf_file, pagesize=letter)
    
#     # 定義表格數據
#     img = Image('C:\\Users\\WeichienTu\\Desktop\\ScreenShot\\New_ZoomOut.png', width=50, height=50)
#     table_data_with_image = [['', '', img],
#                              ['Value 1', 'Value 2', '']]
#     data = table_data_with_image
    
#     # 定義表格樣式
#     style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
#                         ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
#                         ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
#                         ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
#                         ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
#                         ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
#                         ('GRID', (0, 0), (-1, -1), 1, colors.black)])
    
#     # 創建表格對象
#     table = Table(data)
    
#     # 設置表格樣式
#     table.setStyle(style)
    
#     # 將圖片添加到表格中

    
#     # 將表格數據添加到文檔中
#     doc.build([table])

# # 指定 PDF 文件的路径
# pdf_file = "E:\\dev\\_Python\\HuachunDailyReport2024\\Python\\table.pdf"

# # 指定表格数据
# table_data = [
#     ['Column 1', 'Column 2', 'Column 3'],
#     ['Value 1', 'Value 2', 'Value 3'],
#     ['Value 4', 'Value 5', 'Value 6']
# ]

# # 指定图像文件的路径
# image_file = "example.png"

# # 创建包含表格和图像的 PDF
# create_pdf_with_table_and_image(pdf_file, table_data, image_file)

import openpyxl
from openpyxl.drawing.image import Image
from openpyxl.utils import get_column_letter
from openpyxl.styles import Alignment
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

def InsertImageIntoExcel(excel_file, image_path, output_excel):
    # Open the Excel file
    wb = openpyxl.load_workbook(excel_file)
    
    # Select the active worksheet
    ws = wb.active
    
    # Load the image
    img = Image(image_path)
    
    # Calculate dimensions and resize if needed
    img.width, img.height = img.width * 0.2, img.height * 0.2
    
    cell = ws['C8']
    # Add image to the worksheet
    # img.offset = (20,20)
    ws.add_image(img, 'C8')
    # ws.add_image(img, anchor=f"{get_column_letter(cell.column)}{cell.row}", x=20, y=20)
    
    # Set alignment for the cell containing the image
    # cell.alignment = Alignment(horizontal='center', vertical='center')
    
    # Save the modified Excel file
    wb.save(output_excel)


    pass


# Example usage
excel_file = 'C:\\_Everything\\HuachunDailyReport2024\\Python\\DailyReportTemplate.xlsx'
image_path_sun_all = 'C:\\_Everything\\HuachunDailyReport2024\\Python\\Sun_All.png'
output_excel = 'C:\\_Everything\\HuachunDailyReport2024\\Python\\testOutput.xlsx'
pdf_file = 'C:\\_Everything\\HuachunDailyReport2024\\Python\\output.pdf'

InsertImageIntoExcel(excel_file, image_path_sun_all, output_excel)