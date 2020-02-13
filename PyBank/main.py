#Importing the module to create file path across operating system
import os

#import module to read csv files
import csv

csvpath = os.path.join("C:/Users/siddh/Desktop/Data Analytics Bootcamp/03 PYTHON/Homework/python-challenge/Resources/PyBank_budget_data.csv")

#reading csv file
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    #read the header row and print it
    csv_header = next(csvreader)
    #print(f"{csv_header}")

    #total_months = len(list(csvreader))
    #print(total_months)
    
    total_amount = 0 
    for row in csvreader:
        total_amount += int(row[1])
    print(total_amount)
