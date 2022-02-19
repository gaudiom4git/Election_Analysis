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
	County| Total Votes Cast |  Pct of Total Votes Cast
	Jefferson| 38,855  |  10.5%	
	Denver| 306,055 | 82.8%
	Arapahoe| 24,801 | 6.7%
* Denver had the largest number of votes
* Vote Summary by Candidate
* Diana DeGette was the winner with Vote Count=272,292  Percentage of Votes: 73.8%


## Election-Audit Summary

