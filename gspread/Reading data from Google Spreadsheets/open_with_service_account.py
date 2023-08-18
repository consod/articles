from pprint import pprint
import re
import gspread

gc = gspread.service_account()
sh = gc.open("Reading data from Google Spreadsheets")

# Selecting Worksheet by title
worksheet = sh.worksheet("Companies")

# Cell properties
# cell.value = the value of the cell
# cell.row = the cells row number
# cell.col = the cells column number
# cell.address = The A1 notation coordinates of the cell

# Get value of cell A1 with A1 notation
cell_a1_value = worksheet.acell("A1").value
print(cell_a1_value)

# Get formula of cell with A1 notation
cell_a1_formula = worksheet.acell("A1", value_render_option="FORMULA").value

# Get value of cell A1 with cell(row, column)
cell_value = worksheet.cell(1, 1).value
print(cell_value)
print()

# Get formula of cell with cell(row_column)
cell_formula = worksheet.cell(1, 1, value_render_option="FORMULA").value

# Get all values from worksheet as list of lists
list_of_lists = worksheet.get_all_values()
pprint(list_of_lists[0:3])
print()

# Get all values from worksheet as list dictionaries
list_of_dictionaries = worksheet.get_all_records()
pprint(list_of_dictionaries[0:3])

# Find all cells matching a text.
# Returns a list of cells or an empty list if nothing matches
cell_list = worksheet.findall("Armenia")
print(cell_list)
print()

# Find all cells matching a regular expression
companies_re = re.compile(r"Martinez|Martinique")
cell_list_re = worksheet.findall(companies_re)
pprint(cell_list_re)
pprint([cell.value for cell in cell_list_re])
