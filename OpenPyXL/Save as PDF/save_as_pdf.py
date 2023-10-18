from pathlib import Path
from openpyxl import Workbook
from win32com import client
from pywintypes import com_error

# Remember to install pillow, pip install pillow

wb = Workbook()
ws = wb.active
ws["A1"] = "Hello!"

# Fit sheet to one page
ws.sheet_properties.pageSetUpPr.fitToPage = True
ws.page_setup.fitToHeight = True
ws.page_setup.fitToWidth = True

wb.save("Hello!.xlsx")

folder_path = Path(__file__).resolve(strict=True).parent
excel_path = folder_path / "Hello!.xlsx"
pdf_path = folder_path / "Hello!.pdf"

# Open Microsoft Excel
excel = client.Dispatch("Excel.Application")

try:
    workbook = excel.Workbooks.Open(excel_path)
    work_sheet = workbook.Worksheets[0]
    # Convert into PDF File
    work_sheet.ExportAsFixedFormat(0, str(pdf_path))

except com_error as e:
    print(f"Failed to export to PDF: {e}")
else:
    print("Export to PDF succeeded")

finally:
    work_sheet = None
    workbook = None
    excel.Quit()
    excel = None
