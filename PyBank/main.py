#Importing the module to create file path across operating system
import os

#import module to read csv files
import csv
import sys

csvpath = os.path.join("C:/Users/siddh/Desktop/Data Analytics Bootcamp/03 PYTHON/Homework/python-challenge/Resources/PyBank_budget_data.csv")

# Define the the functions to calculate total months, total profit/loss, average change, greatest increase in profits and greatest decrease in profits
#def total_months():
    
#reading csv file
with open(csvpath, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    #read the header row and print it
    csv_header = next(csvreader)
    #print(f"{csv_header}")

    total_amount = 0
    profit_losses_list = []
    months = []

    for row in csvreader:
        #to find the total number of months in dataset
        date = row[0]
        months.append(date)

        #to find the total amount of the dataset
        total_amount += int(row[1])

        #to find the average change of the dataset
        profit_losses_list.append(row[1])
    
    total_months = len(months)
    #print(profit_losses_list)

    #to find the greatest profit and loss in the dataset
    pro_list = []
    for index in range(1, len(profit_losses_list)):
        pro = int(profit_losses_list[index]) - int(profit_losses_list[index-1])
        pro_list.append(pro)
    
    mean = round(sum(pro_list)/len(pro_list),2)
    max_profit = max(pro_list)
    max_loss = min(pro_list)

    max_profit_ind = pro_list.index(max_profit)+1
    max_loss_ind = pro_list.index(max_loss)+1

    print("Financial Analysis")
    print("--------------------------------------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_amount}")
    print(f"Average Change: ${mean}")
    print(f"Greatest Increase in Profits: {months[max_profit_ind]} (${max_profit})")
    print(f"Greatest Decrease in Profits: {months[max_loss_ind]} (${max_loss})")


sys.stdout = open("C:/Users/siddh/Desktop/Data Analytics Bootcamp/03 PYTHON/Homework/python-challenge/PyBank/results_main.txt", "w")
print("Financial Analysis")
print("--------------------------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_amount}")
print(f"Average Change: ${mean}")
print(f"Greatest Increase in Profits: {months[max_profit_ind]} (${max_profit})")
print(f"Greatest Decrease in Profits: {months[max_loss_ind]} (${max_loss})")
