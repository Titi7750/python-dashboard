import csv
import openpyxl

def csv_to_xlsx(csv_file, xlsx_file):
    workbook = openpyxl.Workbook()
    work_sheet = workbook.active

    with open(csv_file, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter='|')
        for row in reader:
            work_sheet.append(row)
    workbook.save(xlsx_file)

csv_to_xlsx('ventes_smartphones.csv', 'ventes_smartphones.xlsx')
