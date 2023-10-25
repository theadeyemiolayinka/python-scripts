import json
import csv

with open('data.json') as json_file:
    data = json.load(json_file)

employee_data = data['emp_details']

data_file = open('data_file.csv', 'w')

csv_writer = csv.writer(data_file)

count = 0

for emp in employee_data:
    if count == 0:

        header = emp.keys()
        csv_writer.writerow(header)
        count += 1

    csv_writer.writerow(emp.values())

data_file.close()
