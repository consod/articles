from openpyxl import load_workbook

# pip install openpyxl

wb = load_workbook("Fruits.xlsx")
ws = wb.active

# All worksheets are contained as a list of worksheet
# objects in the workbooks worksheet property
print(wb.worksheets)
print(type(wb.worksheets))
# --> [<Worksheet "Apples">, <Worksheet "Bananas">, <Worksheet "Pineapples">]
# --> <class 'list'>

# To get a worksheets name, access the worksheets title property
print(ws.title)
# --> Apples

# List all the worksheet names with a list comprehension
print([ws.title for ws in wb.worksheets])
# --> ['Apples', 'Bananas', 'Pineapples']

# You do not need the sheet name to access a sheet, you can access it by index
# Remember that we use zero indexes. The first worksheet is at index 0
ws_pineapples = wb.worksheets[2]
print(ws_pineapples.title)
# --> Pineapples
