'''
* This program takes as input a csv file where each dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. 
* It analyzes the votes and calculates each of the following:
* 1. The total number of votes cast
* 2. A complete list of candidates who received votes
* 3. The percentage of votes each candidate won
* 4. The total number of votes each candidate won
* 5. The winner of the election based on popular vote.
*
* The input csv file will reside in the same folder as this program.
* The output csv file will be named electionresults.txt and will reside in the same folder as this program. The first time this program runs, 
* a blank version of it will need to be created.
*
* Assumptions - 1. The csv file has no duplicates on Voter ID
*               2. The csv file will be sorted on the candidate column
'''
import os
import csv

totalVotes = 0

resource_path = os.getcwd()

#Iterate through the files in the current dir and fetch path for files of type .csv
filepaths = []
for file in os.listdir(resource_path):
	if file.endswith(".csv"):
		filepaths.append(os.path.join(resource_path, file))   

#Read each .csv file and process per instructions in the assignment for PyPoll
csvList = []
for file in filepaths:	

	output = []
	j = 0
	candidateVotes = 0
	maxCandidateVotes = 0
	maxCandidateName = ''

	with open(file) as csvfile:
		csvRead = csv.reader(csvfile, delimiter = ',')
		for row in csvRead:
			#Build a list with the rows from the csv file
			csvList.append(row)

	#Total number of votes cast (based on the assumption that the file only contains unique voterids)
	totalVotes = len(csvList) - 1	

	#file.close()

	for i in csvList:
		
		#Skip the header row
		if j == 0:
			j = j+1
			continue
		#If this is the first row, set the candidate name to be that in the first row
		elif j == 1:	
			candidateName = i[2]
			j = 2

		#Compute the cumulative sum while it is still the same candidate; 
		# assumption is the csv file is sorted based on the candidate name
		if i[2] == candidateName:
				candidateVotes += 1
		else:
			percentVotesWon = (candidateVotes/totalVotes)*100
			if candidateVotes > maxCandidateVotes:
				maxCandidateVotes = candidateVotes
				maxCandidateName = candidateName

			output.append([candidateName, str(candidateVotes), str(percentVotesWon)])		
			candidateName = i[2]
			#Start vote counter for new candidate at 1
			candidateVotes = 1


	#Output the results into the electionresults.txt file in the same folder as where this program resides
	file = open("electionresults.txt","w") 
	file.write("Election Results\n")
	file.write("----------------------------------\n")
	file.write("Total Votes: " + str(totalVotes) + "\n")
	file.write("----------------------------------\n")
	for candidate in output:
		file.write(candidate[0] + ": " + str(candidate[2]) + "% (" + str(candidate[1]) + ")" + "\n")
	file.write("----------------------------------\n")
	file.write("Winner: " + maxCandidateName + "\n")
	file.close() 

	#Output the contents of the results file to the console
	with open("electionresults.txt","r") as f:
		print(f.read(), end = "")

	file.close()	