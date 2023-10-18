from openpyxl import Workbook

# Create a workbook and sheets
wb = Workbook()
ws = wb.active

# Freeze the top row
# Do not freeze A1 as you
# need to freeze the row above
# the reference
ws.freeze_panes = "A2"

wb.save("Freeze_header_row.xlsx")
