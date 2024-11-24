# Nicollette Washington
# 11/22/2024
# P5HW
# Create a code that generates a math quiz.

import random

def math_quiz():
    # Show menu options
    print("Welcome to Math Quiz")
    print("")
    print("MAIN MENU")
    print("-" * 25)
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")
    print()  # Fixed empty print statement
    
    # Get menu choice
    choice = input("Please choose one of the menu options: ")
    
    if choice == "1":
        # Create addition problem
        num1 = random.randint(1, 300)
        num2 = random.randint(1, 300)
        print(f"{num1:>4}")
        print(f"+{num2:>3}")
        
        # Get user's answer 
        guess_count = 0
        correct_answer = num1 + num2
        while True:
            try:
                user_guess = int(input("Enter answer: "))
                guess_count += 1
                if user_guess == correct_answer:
                    print(f"Congratulations!!!! Your answer is correct.")
                    print(f"Number of guesses: {guess_count}")
                    break
                elif user_guess < correct_answer:
                    print("Sorry, guess is too low.")
                else:
                    print("Sorry, guess is too high.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    elif choice == "2":
        # Show subtraction problem
        num1 = random.randint(1, 500)
        num2 = random.randint(1, num1)
        print(f"{num1:>4}")
        print(f"-{num2:>3}")
        
        # Get user's answer 
        guess_count = 0
        correct_answer = num1 - num2
        while True:
            try:
                user_guess = int(input("Enter answer: "))
                guess_count += 1
                if user_guess == correct_answer:
                    print(f"Congratulations!!!! Your answer is correct.")
                    print(f"Number of guesses: {guess_count}")
                    break
                elif user_guess < correct_answer:
                    print("Sorry, guess is too low.")
                else:
                    print("Sorry, guess is too high.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    elif choice == "3":
        print("Thank you for playing...")
        print("Bye!!")
    else:
        print("Invalid choice. Please try again.")

def main():
    while True:
        math_quiz()
        
        play_again = input("Play again? (yes/no) ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":  # Fixed the name variable syntax
    main()
