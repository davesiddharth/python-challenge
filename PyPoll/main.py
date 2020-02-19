#Importing the module to create file path across operating system
import os

#import module to read csv files
import csv

csvpath = os.path.join("C:/Users/siddh/Desktop/Data Analytics Bootcamp/03 PYTHON/Homework/python-challenge/Resources/PyPoll_election_data_subset.csv")

#reading csv file
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    #print(f"{csv_header}")

    votes = []
    candidate_names = []
    candidate0_vote = []
    candidate1_vote = []
    candidate2_vote = []
    candidate3_vote = []

    for row in csvreader:
        #to calculate total number of votes casted
        voterID = row[0]
        votes.append(voterID)

        #to find each candidate from the dataset and their total vote
        names = row[2]
        candidate_names.append(names)
        candidate_names = list(set(candidate_names))
        
        if row[2] == "Khan": #candidate_names[0]:
            candidate0_vote.append(row[2])
        elif row[2] == "Correy": #candidate_names[1]:
            candidate1_vote.append(row[2])
        elif row[2] == "Li": #candidate_names[2]:
            candidate2_vote.append(row[2])
        elif row[2] == "O'Tooley": #candidate_names[3]:
            candidate3_vote.append(row[2])
        
    total_votes = len(votes)

    candidate_vote0_percentage = (len(candidate0_vote)/total_votes)*100
    candidate_vote1_percentage = (len(candidate1_vote)/total_votes)*100
    candidate_vote2_percentage = (len(candidate2_vote)/total_votes)*100
    candidate_vote3_percentage = (len(candidate3_vote)/total_votes)*100

    print("Election Results")
    print("-------------------------------------")
    print(f"Total Votes: {total_votes}")
    print(candidate_names)
    print(f"Khan: {candidate_vote0_percentage}% ({len(candidate0_vote)})")
    print(f"Correy: {candidate_vote1_percentage}% ({len(candidate1_vote)})")
    print(f"Li: {candidate_vote2_percentage}% ({len(candidate2_vote)})")
    print(f"O'Tooley: {candidate_vote3_percentage}% ({len(candidate3_vote)})")
    print("-------------------------------------")
    print(f"Winner: ")
    print("-------------------------------------")
