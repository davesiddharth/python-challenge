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

    votes = []
    candidates_list = []
    candidate_names = []
    candidate0_vote = []
    candidate1_vote = []
    candidate2_vote = []
    candidate3_vote = []
    
    for row in csvreader:
        #to calculate total number of votes casted
        voterID = row[0]
        votes.append(voterID)
        candidate = row[2]
        candidates_list.append(candidate)
        
        for x in candidates_list: 
        # check if exists in unique_list or not 
            if x not in candidate_names: 
                candidate_names.append(x) 
            
    #print(candidate_names)
    total_votes = len(votes)

    for candidate in candidates_list:
        #to count candidates individual votes
        if candidate == candidate_names[0]:
            candidate0_vote.append(candidate)
        elif candidate == candidate_names[1]:
            candidate1_vote.append(candidate)
        elif candidate == candidate_names[2]:
            candidate2_vote.append(candidate)
        elif candidate == candidate_names[3]:
            candidate3_vote.append(candidate)
        

    candidate_vote0_percentage = (len(candidate0_vote)/total_votes)*100
    candidate_vote1_percentage = (len(candidate1_vote)/total_votes)*100
    candidate_vote2_percentage = (len(candidate2_vote)/total_votes)*100
    candidate_vote3_percentage = (len(candidate3_vote)/total_votes)*100

    vote_count = [len(candidate0_vote),len(candidate1_vote),len(candidate2_vote),len(candidate3_vote)]

    win_ind = vote_count.index(max(vote_count))
    #print(win_ind)
    winner = candidate_names[win_ind]

print("Election Results")
print("-------------------------------------")
print(f"Total Votes: {total_votes}")
print(candidate_names)
print(f"{candidate_names[0]}: {round(candidate_vote0_percentage,3)}% ({len(candidate0_vote)})")
print(f"{candidate_names[1]}: {round(candidate_vote1_percentage,3)}% ({len(candidate1_vote)})")
print(f"{candidate_names[2]}: {round(candidate_vote2_percentage,3)}% ({len(candidate2_vote)})")
print(f"{candidate_names[3]}: {round(candidate_vote3_percentage,3)}% ({len(candidate3_vote)})")
print("-------------------------------------")
print(f"Winner: {winner}")
print("-------------------------------------")

sys.stdout = open("C:/Users/siddh/Desktop/Data Analytics Bootcamp/03 PYTHON/Homework/python-challenge/PyPoll/results_main.txt", "w")
print("Election Results")
print("-------------------------------------")
print(f"Total Votes: {total_votes}")
print(candidate_names)
print(f"{candidate_names[0]}: {round(candidate_vote0_percentage,3)}% ({len(candidate0_vote)})")
print(f"{candidate_names[1]}: {round(candidate_vote1_percentage,3)}% ({len(candidate1_vote)})")
print(f"{candidate_names[2]}: {round(candidate_vote2_percentage,3)}% ({len(candidate2_vote)})")
print(f"{candidate_names[3]}: {round(candidate_vote3_percentage,3)}% ({len(candidate3_vote)})")
print("-------------------------------------")
print(f"Winner: {winner}")
print("-------------------------------------")
