counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
print(len(counties_dict), " ", counties_dict)
print(counties_dict.items())
print(counties_dict.keys())
print(counties_dict.values())
print(counties_dict.get("Denver"))
print(counties_dict["Arapahoe"])

# New List
voting_data=[]
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
voting_data.insert(2, {"county":"El Paso", "registered_voters": 461149})
voting_data.remove({"county":"Arapahoe", "registered_voters": 422829})
voting_data.remove({"county":"Denver", "registered_voters": 463353})
voting_data.insert(2, {"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
print(len(voting_data), voting_data)

# #Including Inputs
# # How many votes did you get?
# my_votes = int(input("How many votes did you get in the election? "))
# #  Total votes in the election
# total_votes = int(input("What is the total votes in the election? "))
# # Calculate the percentage of votes you received.
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.")

#If Statements
counties = ["Arapahoe","Denver","Jefferson", "anothercounty"]
if counties[1] == 'Denver':
    print(counties[1])

if counties[3] != "Jefferson":
   print(counties[2])
else:
    print("not there")

#in and not in
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")


if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

#while 
x = 7
while x > 0:
    print("hello world")
    x = x - 1

#for
for county in counties:
    print(county)

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

#range
for num in range(5):
    print(num)

for i in range(len(counties)):
    print(counties[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)

for county in counties_dict:
    print(counties_dict[county])

for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict.get(county))

for key, value in counties_dict.items():
    print(key, value)

for key, value in counties_dict.items():
    print(key, "county has", value, "registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for i in range(len(voting_data)):
    print (voting_data[i])

#Get only values (county, voters)
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)


for county_dict in voting_data:
     print(county_dict['registered_voters'])


for county_dict in voting_data:
     print(county_dict['county'])


#f strings
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)
