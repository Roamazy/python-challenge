import os
import csv

candidate_list = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
vote_counts = {candidate: 0 for candidate in candidate_list}

election_data = os.path.join("Pypoll/Resources/election_data.csv")

with open(election_data, "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    for row in csv_reader:
        candidate=row[2]
        if candidate in candidate_list:
            vote_counts[candidate] += 1 

Total_votes = sum(vote_counts.values())

winner = max(vote_counts, key=vote_counts.get)


#print in terminal -- probably unecessary, but I like it for the sake of the project
print(f"Election Results")
print("----------------------")
print(f"Total Votes: {Total_votes}")
print("----------------------")

for candidate in vote_counts:
    percentage = (vote_counts[candidate] / Total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({vote_counts[candidate]})")

print("----------------------")
print(f"Winner: {winner}")
print("----------------------")
    

#output, write to Analysis folder
output_path = os.path.join("Pypoll/Analysis/poll_analysis.csv")

with open(output_path, "w") as csvfile:
    csv_writer = csv.writer(csvfile)
    
    csv_writer.writerow([f"Election Results"])
    csv_writer.writerow([f"----------------------"])
    csv_writer.writerow([f"Total votes: {Total_votes}"])
    csv_writer.writerow([f"----------------------"])

    for candidate in vote_counts:
        percentage = (vote_counts[candidate] / Total_votes) * 100
        csv_writer.writerow([f"{candidate}: {percentage:.3f}% ({vote_counts[candidate]})"])

    csv_writer.writerow([f"----------------------"])
    csv_writer.writerow([f"Winner: {winner}"])
    csv_writer.writerow([f"----------------------"])

print()
print("--> Results recorded in Pypoll/Analysis/poll_analysis.csv <--")
print()
#I just thought this little bit would be neat :)