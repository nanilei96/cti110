# Nicollette Washington
# 09/25/2024
# P1HW2
# Creating a travel budget calculator


print("This program calculates and displays travel expenses")



budget = int(input("Enter Budget: "))


destination = input("Enter your travel destination: ")


gas = int(input("How much do you think you will spend on gas? "))


hotel = int(input("Approximately, how much will you need for accomodation/hotel? "))


food = int(input("Last, how much do you need for food? "))


# Calculate total expenses
total = gas + hotel + food


# Calculate remaining budget
remaining_budget = budget - total



# Display results


print("-----------Travel Expenses---------")
print("Destination: " + destination)
print(f"Budget: {budget}")


print(f"Gas: {gas}")
print(f"Accomodation: {hotel}")
print(f"Food: {food}")


print(f"\nRemaining Balance: {remaining_budget}")
