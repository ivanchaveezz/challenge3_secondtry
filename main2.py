# PYPOLL
import csv
import collections
import operator

with open("/Users/ivanchavez/Desktop/BOOTCAMP TEC DATA /CHALLENGES/Starter_Code-8/PyPoll/Resources/election_data.csv", mode = "r") as file:
    csvFile = csv.reader(file, delimiter=",")
    csvFile2 = list(csvFile)

header  = csvFile2.pop(0)
#print(csvFile2)

print("ELECTION RESULTS")
print("-----------------------------")
#TOTAL NUMBER OF VOTES CAST
tot_votes = len(csvFile2) - 1
print("Total Votes " , tot_votes)

# CANDIDATOS
candidatos = []
cand = [row[2] for row in csvFile2]
for i in cand:
    if i not in candidatos:
        candidatos.append(i)
#print(candidatos)

#PERCENTAGE OF VOTES PER CANDIDATE
cand2 = collections.Counter(cand)
vote_count = collections.OrderedDict(cand2)
for key,value in vote_count.items():
    print(key,round((value/tot_votes*100),3),"%", "(",value,")")

#WINNER ELECTION 
winner = max(vote_count.items(), key=operator.itemgetter(1))[0]
print("Winner:", winner)
