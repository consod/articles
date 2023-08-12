from win32com import client
import win32api
import pathlib
### pip install pypiwin32 if module not found

excel_file = "pdf_me.xlsx"
pdf_file = "pdf_me.pdf"
excel_path = str(pathlib.Path.cwd() / excel_file)
pdf_path = str(pathlib.Path.cwd() / pdf_file)

excel = client.DispatchEx("Excel.Application")
excel.Visible = 0

wb = excel.Workbooks.Open(excel_path)
ws = wb.Worksheets[1]

try:
    wb.SaveAs(pdf_path, FileFormat=57)
except Exception as e:
    print("Failed to convert")
    print(str(e))
finally:
    wb.Close()
    excel.Quit()
