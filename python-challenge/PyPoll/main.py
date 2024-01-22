import os
import csv

total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

csvpath = os.path.join('PyPoll', 'Resources', 'election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    print(f'Header: {csv_header}')

    for row in csvreader:
        candidate = row[2]
        total_votes += 1
        candidates[candidate]= candidates.get(candidate, 0) + 1

        if candidate not in candidates:
            candidates[candidate] = 0
            candidates[candidate] += 1


    results = []
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        results.append((candidate, percentage, votes))

for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

result_summary = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n")

for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    result_summary += f"{candidate}: {percentage:.3f}% ({votes})\n"

result_summary += (
    "-------------------------\n"
    f"Winner: {winner}\n"
    "-------------------------\n")

print(result_summary)

output_file = "election_results.txt"
with open(output_file, 'w') as f:
    f.write(result_summary)

print(result_summary)