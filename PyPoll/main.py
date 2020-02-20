#Importing the module to create file path across operating system
import os

#import module to read csv files
import csv
import sys

csvpath = os.path.join("C:/Users/siddh/Desktop/Data Analytics Bootcamp/03 PYTHON/Homework/python-challenge/Resources/PyPoll_election_data.csv")

#reading csv file
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    #print(f"{csv_header}")

    total_votes = 0
    candidates_list = []
    candidate_names = []
    candidate_vote = []
    candidate_vote_percentage = []
    vote_percent = 0.000

    for row in csvreader:
        #count total number of votes casted
        total_votes +=1
    #print(total_votes)
        #read in the candidate list from row 3 of the csv file
        candidates_list = row[2]
        if candidates_list in candidate_names:
            candidate_index = candidate_names.index(candidates_list)
            candidate_vote[candidate_index] += 1
        else:
            candidate_names.append(candidates_list)
            candidate_vote.append(1)
    #print the candidate's list and their vote total individual votes
    #print(candidate_names)
    #print(candidate_vote)

    for percentage in range(len(candidate_names)):
        vote_percent = format((candidate_vote[percentage]/total_votes)*100,'.3f')
        candidate_vote_percentage.append(vote_percent)
    #print(candidate_vote_percentage)

    #find the winner from the candidate_names list
    winner_index = candidate_vote_percentage.index(max(candidate_vote_percentage))
    #print(winner_index)
    winner = candidate_names[winner_index]
    #print(winner)
#Final results printing:
print("Election Results")
print("-------------------------------------")
print(f"Total Votes: {total_votes}")

for x in range(len(candidate_names)):
    print(f"{candidate_names[x]}: {candidate_vote_percentage[x]}% ({candidate_vote[x]})")

print("-------------------------------------")
print(f"Winner: {winner}")
print("-------------------------------------")

#Printing results to the text file
sys.stdout = open("C:/Users/siddh/Desktop/Data Analytics Bootcamp/03 PYTHON/Homework/python-challenge/PyPoll/results_main.txt", "w")
print("Election Results")
print("-------------------------------------")
print(f"Total Votes: {total_votes}")

for x in range(len(candidate_names)):
    print(f"{candidate_names[x]}: {candidate_vote_percentage[x]}% ({candidate_vote[x]})")

print("-------------------------------------")
print(f"Winner: {winner}")
print("-------------------------------------")