#Importing the module to create file path across operating system
import os

#import module to read csv files
import csv

csvpath = os.path.join("C:/Users/siddh/Desktop/Data Analytics Bootcamp/03 PYTHON/Homework/python-challenge/Resources/PyPoll_election_data_subset.csv")

#def candidate(candidate_data):
    #name = candidate_name.append(row[2])

#reading csv file
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    #print(f"{csv_header}")

    votes = []
    candidate_names = []
    candidate_vote = []
    candidate_vote0 = []
    candidate_vote1 = []
    candidate_vote2 = []
    candidate_vote3 = []

    for row in csvreader:
        #to calculate total number of votes casted
        voterID = row[0]
        votes.append(voterID)

        #to find each candidate from the dataset
        #candidate(row)
        names = row[2]
        candidate_names.append(names)
        candidate_names = list(set(candidate_names))

        if candidate_names[0] == row[2]:
            candidate_vote0.append(row[0])
        elif candidate_names[1] == row[2]:
            candidate_vote1.append(row[0])
        elif candidate_names[2] == row[2]:
            candidate_vote2.append(row[0])
        else:
            candidate_vote3.append(row[0])
        
    
    total_votes = len(votes)
    candidate_vote0_total = len(candidate_vote0)
    candidate_vote1_total = len(candidate_vote1)
    candidate_vote2_total = len(candidate_vote2)
    candidate_vote3_total = len(candidate_vote3)

    print("Election Results")
    print("-------------------------------------")
    print(f"Election Results: {total_votes}")
    print(f"{candidate_names[0]}: ({candidate_vote0_total})")
    print(f"{candidate_names[1]}: ({candidate_vote1_total})")
    print(f"{candidate_names[2]}: ({candidate_vote2_total})")
    print(f"{candidate_names[3]}: ({candidate_vote3_total})")

