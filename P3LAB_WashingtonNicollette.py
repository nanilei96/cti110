#Nicollette Washington
#10/17/2024
#P3LAB
#creating a program that converts money into dollars and cent.

def calculate_coins(amount):
    # Convert amount to cents
    cents = round(amount * 100)

    if cents == 0:
        return ["No change"]
    
    # Start counters
    dollars = cents // 100
    cents %= 100
    quarters = cents // 25
    cents %= 25
    dimes = cents // 10
    cents %= 10
    nickels = cents // 5
    pennies = cents % 5
    
    # Prepare output
    output = []
    if dollars > 0:
        output.append(f"{dollars} Dollar{'s' if dollars > 1 else ''}")
    if quarters > 0:
        output.append(f"{quarters} Quarter{'s' if quarters > 1 else ''}")
    if dimes > 0:
        output.append(f"{dimes} Dime{'s' if dimes > 1 else ''}")
    if nickels > 0:
        output.append(f"{nickels} Nickel{'s' if nickels > 1 else ''}")
    if pennies > 0:
        output.append(f"{pennies} Penn{'ies' if pennies > 1 else 'y'}")
    
    return output


amount = float(input("Enter the amount of money as a float: $ "))
result = calculate_coins(amount)

if result == ["No change"]:
    print("No change")

else:
    for item in result:
        print(item)
