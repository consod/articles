import gspread

gc = gspread.service_account()

sh = gc.create("Example spreadsheet Service Account")

sh.share("your_account@gmail.com", perm_type="user", role="writer")

print(sh.sheet1.get("A1"))
