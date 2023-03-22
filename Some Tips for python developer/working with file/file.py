import openpyxl

file = openpyxl.load_workbook("FINAL450.xlsx")
sheet = file.active
print(sheet)
for row in sheet.iter_rows(values_only=True):
    print(row)
