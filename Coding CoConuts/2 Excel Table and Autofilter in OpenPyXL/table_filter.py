from random import randint
from openpyxl import Workbook
from openpyxl.worksheet.table import Table, TableStyleInfo

wb = Workbook()
ws = wb.active

headers = ["ID", "Value"]
ws.append(headers)

data = [(randint(1, 100), randint(555, 1000)) for x in range(5)]

for row in data:
    ws.append(row)

table1 = Table(displayName="Table1", ref="A1:B6")
table_style = TableStyleInfo(name="TableStyleLight1", showRowStripes=True)
table1.tableStyleInfo = table_style
ws.add_table(table1)

wb.save("table_wb.xlsx")
table1.autoFilter = None
wb.save("table_wb.xlsx")
