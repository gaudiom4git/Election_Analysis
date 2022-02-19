#  F Strings
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")
print(f"I received {my_votes/total_votes * 100}% of the total votes.")
# Now try with dictionaries
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")
#Adding commas
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")