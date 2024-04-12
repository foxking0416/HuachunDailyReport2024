from openpyxl import Workbook

# 創建一個工作簿
wb = Workbook()
ws = wb.active

# 數據
data = [
    ["Name", "Age"],
    ["Alice", 30],
    ["Bob", 25],
    ["Charlie", 35]
]

# 將數據寫入工作表
for row in data:
    ws.append(row)

# 保存工作簿到文件
wb.save("C:\_Everything\HuachunDailyReport2024\Python\sample.xlsx")