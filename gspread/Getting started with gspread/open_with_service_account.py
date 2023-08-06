import gspread

gc = gspread.service_account()

sh = gc.open("Gspread Service Account test")

print(sh.sheet1.get("A1"))
