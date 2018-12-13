# * In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)

# * You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

import os
import csv

# Path to collect data from the Resources folder
pypollCSV = os.path.join('..', '..', 'pypoll', 'resources', 'election_data.csv')

pollTxt = open("pypoll.txt","w+")



#   * The total number of votes cast
voteTotal = 0


#   * A complete list of candidates who received votes
candidate = []
candidateCount = 0

#   * The percentage of votes each candidate won


#   * The total number of votes each candidate won
votesForCandidate = []


#   * The winner of the election based on popular vote.

# * As an example, your analysis should look similar to the one below:

#   ```text
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
#   ```

# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.

with open(pypollCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    candidateCount = 0

    for row in csvreader:
        # newCandidate is a flag to tell the loop the candidate is new
        newCandidate = True
        # since the data is not sorted by candidate we want to cycle through our candidate list to see if we already have already started 
        # accumulating a vote count for the candidate
        for candidateCount in range((len(candidate))):
            # if the canidate name is known add one to the vote count and voteTotal, set the newCandidate flag = False then break out of the loop
            if candidate[candidateCount] == row[2]:
                votesForCandidate[candidateCount] = votesForCandidate[candidateCount] + 1
                voteTotal = voteTotal + 1
                newCandidate = False
                break
            # otherwise we increment the candidate counter and search for a new
            else:
                candidateCount = candidateCount + 1
        # if the candidateCount is greater than the range and this is not a new candidate then candidateCount needs to be reset to 0 for the next row
        # allowing it to restart the candidate search in the next iteration of the row loop
        if newCandidate == False:
            candidateCount = 0
        # if the candidateCount is greater than the range and this is a new candidate then the new candidate needs to 
        # be added to candidate[] and the vote count needs to be initialized to 1, voteTotal is incremented by 1
        else:
            candidate.append(row[2])
            votesForCandidate.append(1)
            voteTotal = voteTotal + 1
        # reset the nextRow to False to allow proper processing on the next iteration

    electionResults = zip(candidate, votesForCandidate)

    # since I wanted to only run one for loop to output the candidate results I decided to put the screenoutput and update the text file together
    # instead of running a loop for each output type

    print("Election Results")
    pollTxt.write("Election Results\n")
    print("----------------------------")
    pollTxt.write("----------------------------\n")
    print(f"Total Votes: {voteTotal}")
    pollTxt.write("Total Votes: %d\n" % (voteTotal))
    print("----------------------------")
    pollTxt.write("----------------------------\n")
    for row in electionResults:
        votePercent = (row[1] / voteTotal) * 100
        print(f"{row[0]}: %.3f%% ({row[1]})" % (votePercent))
        pollTxt.write("%s: %.3f%% (%d)\n" % (row[0], votePercent, row[1]))
    print("----------------------------")
    pollTxt.write("----------------------------\n")
    findWinner = 0
    for row in votesForCandidate:
        if ((findWinner == 0) or (votesForCandidate[findWinner] > topVote)):
            topVote = votesForCandidate[findWinner]
            topVoteCandidate = findWinner
        findWinner = findWinner + 1
            
    print(f"Winner: {candidate[topVoteCandidate]}")
    pollTxt.write("Winner: %s\n" % (candidate[topVoteCandidate]))
    print("----------------------------")
    pollTxt.write("----------------------------\n")
    
    pollTxt.close()