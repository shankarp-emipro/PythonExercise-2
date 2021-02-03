import csv
from openpyxl import Workbook

wb = Workbook()
ws = wb.active      # getting the active worksheet

with open("data2.csv", 'r') as file:
    # loading csv file
    csv_file = csv.reader(file, delimiter=',')
    for row in csv_file:
        # appending each row of csv file into the .xls file
        ws.append(row)
    file.close()
# save file - if file does not exist then new file will be created
wb.save('data3.xls')
print('Data is stored in data3.xls file.')
