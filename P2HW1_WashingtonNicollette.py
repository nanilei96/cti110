# Nicollette Washington
# 10/7/2024
# P2HW1
# Creating a travel budget calculator with a nicer format.
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
print()
destination = input("Enter your travel destination: ")
print()
gas = int(input("How much do you think you will spend on gas? "))
print()
hotel = int(input("Approximately, how much will you need for accomodation/hotel? "))
print()
food = int(input("Last, how much do you need for food? "))


# Calculate total expenses
total = gas + hotel + food


# Calculate remaining budget
remaining_budget = budget - total



# Display results


print("-----------Travel Expenses---------")
print(f"{'Destination:':<20} {destination}")
print(f"{'Budget:':<20} ${budget:.2f}")
print(f"{'Gas:':<20} ${gas:.2f}")
print(f"{'Accomodation:':<20} ${hotel:.2f}")
print(f"{'Food:':<20} ${food:.2f}")
print("-----------------------------------")
print()
print(f"{'Remaining Balance:':<20} ${remaining_budget:.2f}")
