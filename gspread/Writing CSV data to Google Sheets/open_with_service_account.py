import gspread
import csv
import string

gc = gspread.service_account()
sh = gc.open("CSV dat to Google Spreadsheet")
worksheet = sh.get_worksheet(0)

with open("fake_users.csv", "r", encoding="UTF-8") as csv_file:
    csv_reader = csv.reader(csv_file)
    data = list(csv_reader)

# sh.update('A1:B2', [[1, 2], [3, 4]])

max_row_nr = len(data)
max_col_nr = max((len(l) for l in data))
max_col_letter = string.ascii_uppercase[max_col_nr - 1]

print(f"max_row={max_row_nr} max_col_nr={max_col_nr} max_col_letter={max_col_letter}")

worksheet.update(
    value=data,
    range_name=f"A1:{max_col_letter}{max_row_nr}",
)
