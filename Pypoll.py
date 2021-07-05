# import csv and os
import csv
import os

#Assign a variable to load a file rather than file_to_load = "resources/election_results.csv"
file_to_load = os.path.join("resources", "election_results.csv")
# Assign a variable to save a file
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open the election results and read the file.
with open(file_to_load, "r") as election_data:
    #read the file with reader function
    file_reader = csv.reader(election_data)
    #Print the header row
    headers = next(file_reader)
    print(headers)
    # Print each row in the CSV file.
    #for row in file_reader:
        #print(row[0])

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    txt_file.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")



#1. Total number of votes cast
#2. A complete list of candidates who received votes
#3. Total number of votes each candidate received
#4. Percentage of votes each candidate won
#5. The winner of the election based on popular vote