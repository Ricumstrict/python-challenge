import os
import csv
total_months = 0
net = 0
profits = 0
changes = []
months = []

csvpath = os.path.join('PyBank', 'Resources', 'budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    print(f'Header: {csv_header}')
    for row in csvreader:   
         date = row[0]
         profit = int(row[1])
        
       
         total_months += 1
         net += profit
        
       
         if total_months > 1:
            change = profit - profits
            changes.append(change)
            months.append(date)
        
         profits = profit

average_change = round(sum(changes) / len(changes), 2)
greatest_increase = max(changes)
greatest_increase_date = months[changes.index(greatest_increase)]
greatest_decrease = min(changes)
greatest_decrease_date = months[changes.index(greatest_decrease)]

print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

output_file = "financial_analysis.txt"
with open(output_file, 'w') as output:
    output.write("Financial Analysis\n")
    output.write("--------------------------\n")
    output.write(f"Total Months: {total_months}\n")
    output.write(f"Total: ${net}\n")
    output.write(f"Average Change: ${average_change}\n")
    output.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    output.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")