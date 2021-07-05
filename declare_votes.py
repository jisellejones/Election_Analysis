# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))
message_to_candidate = (
    f"You received {my_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {my_votes / total_votes * 100: .2f}% of the total vote."
)
print(message_to_candidate)
# Calculate the percentage of votes you received - older code
#percentage_votes = (my_votes / total_votes) * 100
#print("I received " + str(percentage_votes)+"% of the total votes.")