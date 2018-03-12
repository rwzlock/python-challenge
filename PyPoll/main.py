#Dependencies
import os
import csv

#Path of the 2 csv inputs
csvpath1 = os.path.join('Resources', 'election_data_1.csv')
csvpath2 = os.path.join('Resources', 'election_data_2.csv')
#Path of the 2 csv outputs
outputpath1 = os.path.join('output', 'results1.csv')
outputpath2 = os.path.join('output', 'results2.csv')
#election_data_1.csv has its results stored in results1.csv
#election_data_2.csv has its results stored in results2.csv

#The path has to be specified when the person running the program decides which file they want to run the data on. I could have repeated this for both files in the
#same program, but did not see a reason to double the length of the code when the person running it could just change the path to specify the file they want to use to 
#read or write.

#Variable for total number of votes
total_votes_cast = 0
#Lists for the names of the Candidates and the Corresponding votes for each of them
candidates = []
votes_count = []
#These lists are designed so that candidates[0] is the name of the candidate, and votes[0] is the count of their votes
#candidates[1] is the second candidate and votes[1] is the count of their votes. This continues for all candidates

#Read using CSV module
with open(csvpath1, 'r', newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #Skips the header line
    next(csvreader)
    
    for row in csvreader:
        #Add 1 to the total votes
        total_votes_cast=total_votes_cast+1
        if row[2] in candidates:
            #If the candidate name is in the list, add a vote to the corresponding position in the votes list
            vote = candidates.index(row[2])
            votes_count[vote]+=1
        else:
            #If the candidate name is not in the list, add them to the list and add them to the votes list with a starting votes value of 1
            candidates.append(str(row[2]))
            votes_count.append(1)
    
    #Series of print statements to print the results to the table for any number of candidates
    print("Election Results")
    print("-"*20)
    print("Total Votes: "+str(total_votes_cast))
    print("-"*20)
    for x in range(0, len(candidates)):
        print(candidates[x]+": "+str(round((100*votes_count[x]/total_votes_cast),2))+"% "+str(votes_count[x]))
    print("-"*20)
    winner = votes_count.index(max(votes_count))
    print("The winner is: "+candidates[winner])
    print("-"*20)
    
    #Use csvwriter to write the results into a csvfile
with open(outputpath1, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')
    
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['Total Votes:', str(total_votes_cast)])
    csvwriter.writerow(['Candidate', 'Percent of Votes', 'Votes Received'])
    for x in range(0, len(candidates)):
        csvwriter.writerow([candidates[x], str(round((100*votes_count[x]/total_votes_cast),2)), str(votes_count[x])])
    csvwriter.writerow(['The winner is: ', str(candidates[winner])])