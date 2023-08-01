#!/usr/bin/env python3

"""
Iterating over tables in an existing workbook
"""
from openpyxl import load_workbook

FILENAME = "Tables.xlsx"

wb = load_workbook(FILENAME)

ws = wb.active

for table in ws.tables.values():
    print(table.name, table.ref)
