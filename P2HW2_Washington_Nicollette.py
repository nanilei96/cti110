#Nicollette Washington
#10/10/2024
#P2HW2
#Design a program that asks user for grades for various modules.
"""
Pseudocode:
1. Create an empty list to keep grades
2. Get user to enter grades for module 1-6
3. Convert input to float
4. Add all grades to list
5. Calculate lowest grade
6. Calculate highest grade
7. Calculate the sum of the grades
8. Calculate the average of grades
9. Show results
10.Show average grade with two decimal places.


"""
# List to store the grades
all_grades = []

# Ask for grades for each module
Module1 = float(input("Enter grade for Module 1: "))
all_grades.append(Module1)

Module2 = float(input("Enter grade for Module 2: "))
all_grades.append(Module2)

Module3 = float(input("Enter grade for Module 3: "))
all_grades.append(Module3)

Module4 = float(input("Enter grade for Module 4: "))
all_grades.append(Module4)

Module5 = float(input("Enter grade for Module 5: "))
all_grades.append(Module5)

Module6 = float(input("Enter grade for Module 6: "))
all_grades.append(Module6)

# Calculate and show the required information
lowest_grade = min(all_grades)
highest_grade = max(all_grades)
sum_of_grades = sum(all_grades)
average_grade = sum_of_grades / len(all_grades)

# Show the results
print("------------Results----------------")

print(f"Lowest grade: {lowest_grade}")
print(f"Highest grade: {highest_grade}")
print(f"Sum of grades: {sum_of_grades}")
print(f"Average grade: {average_grade:.2f}")
print("--------------------------------------")
