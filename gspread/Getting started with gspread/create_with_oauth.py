import gspread

gc = gspread.oauth()

sh = gc.create("My new spreadsheet")

print(sh.sheet1.get("A1"))
