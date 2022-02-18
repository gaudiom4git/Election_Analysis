#The data we need to retrieve.
# 1. The total number of votes to case
# 2.  A complete list of candidates who received votes
# 3.  The percentage of votes each candidate won
# 4.  The total number of votes each candidate won
# 5.  The winner of the election based on popular vote
# Assign a variable for the file to load and the path.
import csv
import os
#file_to_load = 'Resources/election_results.csv'
#election_data = open(file_to_load, 'r')
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")
#Initialize Total Votes
total_votes = 0
#Initialize List of Candidates
candidate_options = []
#Create empty dictionary of candidates and number of votes
candidate_votes = {}
# Open the election results and read the file.  No need
with open(file_to_load,'r') as election_data:
    csvreader = csv.reader(election_data, delimiter=",")
     # Loop through election data
    headers = next(csvreader)
    for row in csvreader:
        # To do: perform analysis.
        # increment vote total
        total_votes += 1
        # get candidate name
        candidate_name = row[2]
        # check if candidate already in list of candidate_options
        if candidate_name not in candidate_options:
            # Add candidate name to list of candidates
            candidate_options.append(candidate_name)
            # Add candidate to candidate votes dictionary 
            candidate_votes[candidate_name] = 0
        # Accumulate candidate's votes
        candidate_votes[candidate_name] += 1
    print(total_votes)
    print(candidate_votes)    
    # Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
    print(f"{candidate_name}: received {vote_percentage:.2f}% of the vote.")
    # Determine winning vote count and candidate
    # 1. Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # 2. If true then set winning_count = votes and winning_percent =
        # vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # 3. Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name
print(f"{winning_candidate} is the winner with {winning_count} with {winning_percentage} of votes.")
# Close the file.
#election_data.close()   

#outfile = open(file_to_save, 'w')
#outfile.write("Hello World")

#Close the output file
#outfile.close()
