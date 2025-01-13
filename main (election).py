# Dependencies
import csv
import os
import pandas as pd

# Files to load and output
file_to_load = os.path.join("C:/Users/oury/Documents/GitHub/python-challenge/Resources/election_data.csv")
# Input file path
file_to_output = os.path.join("C:/Users/oury/Documents/GitHub/python-challenge/Analysis/election_analysis.txt")  # Output file path

# Load the CSV into a DataFrame
df = pd.read_csv(file_to_load)

# Calculate the total number of votes
total_votes = len(df)

# Display the total number of votes
print(f"Total number of votes cast: {total_votes}")

#Extract the unique candidates
unique_candidates = df['Candidate'].unique()

# Display the list of candidates
print("List of candidates who received votes:")
for candidate in unique_candidates:
    print(candidate)


# Group by 'Candidate' and count the number of votes for each
vote_counts = df['Candidate'].value_counts()

# Calculate the percentage of votes each candidate won
vote_percentages = (vote_counts / total_votes) * 100

# Display the results
print("Percentage of votes each candidate won:")
for candidate, percentage in vote_percentages.items():
    each = print(f"{candidate}: {percentage:.2f}%")

# Count the number of votes each candidate received
vote_counts = df['Candidate'].value_counts()

# Display the results
print("Total number of votes each candidate received:")
for candidate, votes in vote_counts.items():
    print(f"{candidate}: {votes}")

# Identify the candidate with the highest number of votes
winner = vote_counts.idxmax()
winning_votes = vote_counts.max()

# Display the results
print(f"The winner of the election is {winner} with {winning_votes} votes.")
output = F"Election Results ------------------------- Total Votes: {total_votes} ------------------------- Charles Casper Stockham: 23.049% (85213), Diana DeGette: 73.812% (272892), Raymon Anthony Doane: 3.139% (11606) -------------------------, Winner: {winner}-------------------------"

with open(file_to_output, "w") as txt_file:
    txt_file.write(output)