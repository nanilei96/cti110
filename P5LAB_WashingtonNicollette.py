import random

def disperse_change(change_amount):
    # Convert amount to cents
    # Notice how everything in the function is indented!
    cents = round(change_amount * 100)
    
    # Start counters
    dollars = cents // 100
    cents = cents % 100
    
    # Get quarters
    quarters = cents // 25
    cents = cents % 25
    
    # Get dimes
    dimes = cents // 10
    cents = cents % 10
    
    # Get nickels and pennies
    nickels = cents // 5
    pennies = cents % 5
    
    # Print the results
    if dollars > 0:
        if dollars == 1:
            print("1 Dollar")
        else:
            print(f"{dollars} Dollars")
            
    if quarters > 0:
        if quarters == 1:
            print("1 Quarter")
        else:
            print(f"{quarters} Quarters")
            
    if dimes > 0:
        if dimes == 1:
            print("1 Dime")
        else:
            print(f"{dimes} Dimes")
            
    if nickels > 0:
        if nickels == 1:
            print("1 Nickel")
        else:
            print(f"{nickels} Nickels")
            
    if pennies > 0:
        if pennies == 1:
            print("1 Penny")
        else:
            print(f"{pennies} Pennies")


def main():
    # Generate random purchase
    purchase_amount = round(random.uniform(0.01, 100.00), 2)
    print(f"Purchase amount: ${purchase_amount:.2f}")
    
    while True:
        try:
            payment = float(input("How much cash will you put in self-checkout?: $"))
            if payment >= purchase_amount:
                break
            else:
                print("Payment must be greater than or equal to purchase amount.")
        except ValueError:
            print("Please enter a valid number.")
# Calculate change
    change = payment - purchase_amount
    print(f"\nChange due: ${change:.2f}")
    disperse_change(change)

if __name__ == "__main__":
    main()


