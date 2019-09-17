import os
import csv

PyBank_csv = os.path.join('..', 'Resources', 'budget_data.csv')


total_months = 0
net_amt = 0
monthly_changes = []
months = []
profit_loss = []

with open(PyBank_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader, None)

    first_row = next(csvreader)
    total_months = total_months + 1
    net_amt = net_amt + int(first_row[1])
    initial_amt = int(first_row[1])
    

    
    for row in csvreader:
        #Gather list of all the months
        months.append(row[0])
        total_months = total_months + 1
    
        
        #Calculate total profit/loss
        profit_loss.append(int(row[1]))
        net_amt = net_amt + int(row[1])

        #Gather list of average changes per month
        monthly_diff = int(row[1]) - initial_amt
        initial_amt = int(row[1])
        monthly_changes.append(monthly_diff)

        #Greatest increase in profits
        greatest_increase = max(monthly_changes)

        #Greatest decrease in profits
        greatest_decrease = min(monthly_changes)

total_month_avg = round(sum(monthly_changes) / total_months, 2)

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: {net_amt}")
print(f"Average Change: ${total_month_avg}")
print(f"Greatest Increase in Profits: $({greatest_increase})")
print(f"Greatest Decrease in Profits: $({greatest_decrease})")

