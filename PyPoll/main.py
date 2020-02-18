#Importing the module to create file path across operating system
import os

#import module to read csv files
import csv

csvpath = os.path.join("C:/Users/siddh/Desktop/Data Analytics Bootcamp/03 PYTHON/Homework/python-challenge/Resources/PyPoll_election_data.csv")

#reading csv file
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    #print(f"{csv_header}")

    votes = []

    for row in csvreader:
        #to calculate total number of votes casted
        voterID = row[0]
        votes.append(voterID)
        

    total_votes = len(votes)

    print("Election Results")
    print("-------------------------------------")
    print(f"Election Results: {total_votes}")

