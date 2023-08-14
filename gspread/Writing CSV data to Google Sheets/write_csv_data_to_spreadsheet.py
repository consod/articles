import csv
import gspread

gc = gspread.service_account()
sh = gc.open("CSV data to Google Spreadsheet")
worksheet = sh.get_worksheet(0)

with open("fake_users.csv", "r", encoding="UTF-8") as csv_file:
    csv_reader = csv.reader(csv_file)
    data = list(csv_reader)  # list of lists

# gspread = 5.10.0
worksheet.update(
    "A3",
    data,
)

# gspread >= 6.0.0
# worksheet.update(data, "A3")
