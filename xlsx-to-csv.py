import openpyxl
import csv

# Открываем файл Excel
wb = openpyxl.load_workbook("e:\Projects\Current\test\excel.xlsx")

#"e:\Projects\Current\test\xlsx-to-csv.py"
# Получаем активный лист
sheet = wb.active

# Создаем новый файл CSV
with open("file.csv", "w", newline="") as f:

  # Создаем объект CSV Writer
  writer = csv.writer(f)

  # Пишем заголовки колонок
  writer.writerow(sheet.columns)

  # Пишем данные из листа Excel в файл CSV
  for row in sheet.rows:
    writer.writerow([cell.value for cell in row])

# Закрываем файл Excel
wb.close()