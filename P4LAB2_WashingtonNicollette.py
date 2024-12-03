# Nicollette Washington
# 11/2/2024
# P4LAB2
# Create a program where whatever integer is entered a multiplication table is produced.

def print_multiplication_table(number):
    for i in range(1, 13):
        print(f"{number} * {i} = {number * i}")

def main():
    while True:
        try:
            number = int(input("Enter an integer: "))
            
            if number < 0:
                print("This program does not handle negative numbers")
            else:
                print_multiplication_table(number)
            
            choice = input("Would you like to run the program again? ").lower()
            if choice != 'yes':
                print("Exiting program...")
                break
                
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

main()
