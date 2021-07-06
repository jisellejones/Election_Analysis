# Add dependencies
import csv
import os

#Assign a variable to load a file rather than file_to_load = "resources/election_results.csv"
file_to_load = os.path.join("resources", "election_results.csv")
# Assign a variable to save a file
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Adds total vote counter
total_votes = 0

#Declare a new list to hold candidates
candidate_options = []

#Declare an empty dictionary to hold votes for candidates.
candidate_votes ={}

#Open the election results and read the file.
with open(file_to_load, "r") as election_data:
    file_reader = csv.reader(election_data)

    #Read the header row
    headers = next(file_reader)
    
    # Print each row in the CSV file and add total vote count
    for row in file_reader:
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # Check to see if candidate name is in the lis.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        #Begin counting votes
        candidate_votes[candidate_name] += 1

# Iterate through the candidate list.
for candidate_name in candidate_votes:

    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]

    #Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    #Print the candidate name and percentage of votes.
    print(f"{candidate_name}: recieved {vote_percentage:.1f}% of votes.")
    

#1. Total number of votes cast
#2. A complete list of candidates who received votes
#3. Total number of votes each candidate received
#4. Percentage of votes each candidate won
#5. The winner of the election based on popular vote