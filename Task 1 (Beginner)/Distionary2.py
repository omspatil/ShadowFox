# Your expenses
your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

# Your partner's expenses
partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

# Calculate total expenses for each of you
total_your_expenses = sum(your_expenses.values())
total_partner_expenses = sum(partner_expenses.values())

# Print the results
print(f"Your total expenses: {total_your_expenses}")
print(f"Your partner's total expenses: {total_partner_expenses}")

# Determine who spent more
if total_your_expenses > total_partner_expenses:
    print("You spent more money overall.")
elif total_partner_expenses > total_your_expenses:
    print("Your partner spent more money overall.")
else:
    print("You both spent the same amount of money.")

# Find the category with the significant difference in spending
significant_difference = 0
significant_category = None

for category in your_expenses:
    difference = abs(your_expenses[category] - partner_expenses[category])
    if difference > significant_difference:
        significant_difference = difference
        significant_category = category

# Print the category with the significant difference
print(f"The expense category with the significant difference is '{significant_category}' with a difference of {significant_difference}.")
