import os
import csv
csvpath = os.path.join('PyPoll', 'Resources', 'election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    print(f'Header: {csv_header}')
    for row in csvreader:
        print(row)
    total_votes = 0
    candidates = {}

    for row in csvreader:
        candidate = row[2]
        total_votes += 1
        candidates[candidate]= candidates.get(candidate, 0) + 1


    results = []
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        results.append((candidate, percentage, votes))
