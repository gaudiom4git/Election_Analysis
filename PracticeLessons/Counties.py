counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict.keys():
    print(county)
for votes in counties_dict.values():
    print(votes)
# This for loop will provide the values in a dict
print("Loop 3")
for county in counties_dict:
    print(counties_dict[county])
# This for loop will provide both keys and values in a dict
for county, voters in counties_dict.items():
    print(county, voters)
# Displaying a list of dictionaries.
# county is a key AND registered_voters is a key
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
# Looping through a list of voting data list of dictionaries                
for county_dict in voting_data:
    print(county_dict)
# Looping through a list   and provide list index and key from dictionary to bring back value.
for i in range(len(voting_data)):
    print(voting_data[i]['county'])
    #print(voting_data[i]['registered_voters'])
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
for county_dict in voting_data:
    for county in county_dict:
       print(county_dict[county])