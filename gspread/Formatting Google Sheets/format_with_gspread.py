import gspread
from gspread_formatting.models import CellFormat, Color, TextFormat, NumberFormat
from gspread_formatting.functions import format_cell_ranges, set_frozen

gc = gspread.oauth()

# sh = gc.create("Formatting with gspread")
sh = gc.open("Formatting with gspread")
worksheet = sh.get_worksheet(0)

worksheet.update("A1", "Hellooo!")
worksheet.update("B1", 0.55)
worksheet.update("C1", 98.69)

fmt = CellFormat(
    backgroundColor=Color(red=0.2, green=0.0, blue=0.7, alpha=1),
    textFormat=TextFormat(
        foregroundColor=Color(1, 1, 1),
        fontFamily="Merriweather",
        fontSize=16,
        bold=True,
        italic=True,
        strikethrough=True,
        underline=True,
    ),
    horizontalAlignment="LEFT",
)

fmt2 = CellFormat(
    numberFormat=NumberFormat(type="PERCENT", pattern="0.00%"),
    horizontalAlignment="CENTER",
)

fmt3 = CellFormat(numberFormat=NumberFormat(type="CURRENCY", pattern="0.00€"))

# Format one range
format_cell_ranges(worksheet, [("A1", fmt)])

# Format multiple ranges
format_cell_ranges(worksheet, [("B1:B2", fmt2), ("C1:C2", fmt3)])

# Freeze row 1
set_frozen(worksheet, rows=1)

# Unfreeze row 1
set_frozen(worksheet, rows=0)

# Freeze column 1
set_frozen(worksheet, cols=1)

# Unfreeze column 1
set_frozen(worksheet, cols=0)

# Freeze row 1 and column 1
set_frozen(worksheet, rows=1, cols=1)

# Unfreeze row 1 and column 1
set_frozen(worksheet, rows=0, cols=0)
