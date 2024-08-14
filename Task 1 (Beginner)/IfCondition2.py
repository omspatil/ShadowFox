# Define the list of cities per country
countries = {
    "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth"],
    "UAE": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"],
    "India": ["Mumbai", "Bangalore", "Chennai", "Delhi"]
}

# Ask the user to enter a city name
city = input("Enter a city name: ")

# Determine the country for the given city
country_found = None
for country, cities in countries.items():
    if city in cities:
        country_found = country
        break

# Output the result
if country_found:
    print(f"{city} is in {country_found}")
else:
    print(f"{city} is not in the list")
