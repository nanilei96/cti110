# Nicollette Washington
# 09/25/2024
# P1HW2
# Creating a travel budget calculator
"""

Pseudocode:
1.Print descrition
2.Input budget
3.Input travel destination
4.Input gas cost
5.Input hotel cost
6.Input food cost
7.Calculate remaining balance
8.Print travel espenses:
    - location
    - budget
    - gas cost
    - hotel cost
    - food cost
    - remaining balance
 """   



print("This program calculates and displays travel expenses")
print()



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
print()
print(f"Gas: {gas}")
print(f"Accomodation: {hotel}")
print(f"Food: {food}")
print()
print(f"\nRemaining Balance: {remaining_budget}")
