import os
import csv
count = 0
total = 0


csvpath = os.path.join('PyBank', 'Resources', 'budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    print(f'Header: {csv_header}')
    for row in csvreader:   
        print(row)
        total = 0
        counts = 0

    for row in csvreader:
        count = count + 1
        
        