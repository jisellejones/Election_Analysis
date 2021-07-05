counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])
if counties[2] != "Jefferson":
    print(counties[2])
if "ElPaso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")
if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties")
else:
    print("Arapahoe and El Paso are not in the list of counties.")
for county in counties:
    print(county)
numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)
for nums in range(5):
    print(nums)
for i in range(len(counties)):
    print(counties[i])
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict.keys():
    print(county)
for voters in counties_dict.values():
    print(voters)
for county1 in counties_dict:
    print(counties_dict[county1])
for county2 in counties_dict:
    print(county2)
for county3 in counties_dict:
    print(counties_dict.get(county3))
#get both key and value from each county - first variable assigned to keys, 2nd variable assigned to values
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
for county_dict1 in voting_data:
        print(county_dict1.values())
for county_dict2 in voting_data:
    print(county_dict['registered_voters'])