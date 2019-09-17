import os
import csv

PyPoll_csv = os.path.join('..', 'Resources', 'election_data.csv')

with open(PyPoll_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)

    voter_count = 0
    voter_names = []
    Khan_count = []
    Correy_count = []
    Li_count = []
    Tooley_count = []
    for row in csvreader:
        voter_count = voter_count + 1

        if row[2] == "Khan":
            Khan_count.append(csvreader)
        elif row[2] == "Correy":
            Correy_count.append(csvreader)
        elif row[2] == "Li":
            Li_count.append(csvreader)
        else:
            Tooley_count.append(csvreader)
    
    Khan_votes = round((len(Khan_count) / voter_count) * 100)
    Correy_votes = round((len(Correy_count) / voter_count) * 100)
    Li_votes = round((len(Li_count) / voter_count) * 100)
    Tooley_votes = round((len(Tooley_count)/ voter_count) * 100)

print("Election Results")
print("-------------------------")
print(f"Total Votes: {voter_count}")
print("--------------------------")
print(f"Khan: {Khan_votes}% ({len(Khan_count)})")
print(f"Correy: {Correy_votes}% ({len(Correy_count)})")
print(f"Li: {Li_votes}% ({len(Li_count)})")
print(f"O'Tolley: {Tooley_votes}% ({len(Tooley_count)})")
print("---------------------------")

Khan = len(Khan_count) 
Correy = len(Correy_count) 
Li = len(Li_count)
Tooley = len(Tooley_count)
    
if Khan > Correy and Li and Tooley:
        print("Winner: Khan")
elif Correy > Khan and Li and Tooley:
        print("Winner: Correy")
elif Li > Khan and Correy and Tooley:
        print("Winner: Li")
elif Tooley > Khan and Correy and Tooley:
        print("Winner: O'Tooley")
else:
        print("No Winner")

print("----------------------------")

