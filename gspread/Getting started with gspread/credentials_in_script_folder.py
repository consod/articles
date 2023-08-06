import gspread

gc = gspread.oauth(
    credentials_filename="credentials.json",
    authorized_user_filename="authorized_user.json",
)

sh = gc.create("Spreadsheet")

print(sh.sheet1.get("A1"))
