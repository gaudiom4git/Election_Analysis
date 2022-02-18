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
# Open the election results and read the file.  No need
with open(file_to_load,'r') as election_data:
    csvreader = csv.reader(election_data, delimiter=",")
     # Loop through election data
    headers = next(csvreader)
    print(headers)
#    for row in csvreader:
        # To do: perform analysis.
        #print(election_data.readline())
        #print(row)
# Close the file.
#election_data.close()   
#file_to_write = os.path.join("analysis", "election_analysis.txt")
#outfile = open(file_to_write, 'w')
#outfile.write("Hello World")

#Close the output file
#outfile.close()
