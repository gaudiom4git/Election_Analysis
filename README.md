# Election_Analysis
Python Module 3 repository

## Overview of Project
The objective of this project was to analyze election votes and determine election results by candidate and county.  Election votes were 
provided in a comma delimited text file with three columns, Ballot ID, County and Candidates.   There were 3 counties where votes were 
recorded.  Voters had 3 candidates to choose from.  The winning would be the person who received the most amount of votes across all 3
counties.  The project also wanted analysis on voter turnout across all 3 counties, which one had the highest voter turnout and breakdown
of the percentage of total turnout by county.

### Purpose

The project challenge was looking for election results to be presented on the terminal as well as in a text file.  The program was
written in Python using 2 dependencies (os and csv) that allowed the program to open / read / write to text files.  We used lists to 
record counties and candidates and dictionaries to hold the number of votes by county and candidates.

F strings were used to format results both on the terminal and in the output file.

## Results
* Total Votes cast = 369,711
* Vote Summary By County
	* Jefferson 38,855 votes	10.5%	
	* Denver  	306,055 votes	82.8%
	* Arapahoe  24,801 voter	6.7%
* Denver had the largest number of votes
* Vote Summary by Candidate
	* Charles Casper Stockham	85,213		23.0%	
	* Diana DeGette				272,892		3.8%
	* Raymon Anthony Doane		11,606		3.1%
* Diana DeGette was the winner with Vote Count=272,292  Percentage of Votes: 73.8%

This output can be found here: [election_analysis.txt](https://github.com/gaudiom4git/Election_Analysis/tree/main/analysis/election_analysis.txt).


## Election-Audit Summary
This script provides summaries at the county level.  It can be modified to provide summaries at state and national levels as well.
Similarly, you can have more than one position in an election, say a County Secretary and a County Sheriff.   

You assume that the state and position would be added as columns to the data file (election_results.csv).  
The script has to be modified so that it brings in the headers (added columns) and using DictReader.   You can reference the "keys"
in the csvreader object so that you can reference them in your loop.   This method is useful when you don't know how many columns are
in your file.

