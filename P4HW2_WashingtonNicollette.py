#Nicollette Washington
#11/7/2024
#P4HW2
#Create a program to gather multiple employees hours and pay to calculate payroll


def calculate_pay(hours, rate):
    # Calculate regular and overtime hours
    regular_hours = min(40, hours)
    overtime_hours = max(0, hours - 40)
    
    # Calculate pay
    regular_pay = regular_hours * rate
    overtime_pay = overtime_hours * (rate * 1.5)
    gross_pay = regular_pay + overtime_pay
    
    return overtime_hours, overtime_pay, regular_pay, gross_pay


total_employees = 0
total_overtime_pay = 0
total_regular_pay = 0
total_gross = 0

while True:
    # Get employee name
    name = input("Enter employee's name or \"Done\" to terminate: ")
    if name.lower() == "done":
        break
    
    # Get hours and pay rate
    hours = float(input(f"How many hours did {name} work? "))
    rate = float(input(f"What is {name}'s pay rate? "))
    
    # Calculate pay
    overtime_hours, overtime_pay, regular_pay, gross_pay = calculate_pay(hours, rate)
    
    # Print employee details
    print(f"\nEmployee name:    {name}\n")
    print("Hours Worked    Pay Rate    OverTime    OverTime Pay    RegHour Pay    Gross Pay")
    print("-" * 75)
    print(f"{hours:<15.1f}{rate:<12.2f}{overtime_hours:<12.1f}${overtime_pay:<14.2f}${regular_pay:<14.2f}${gross_pay:.2f}\n")
    
    # Update totals
    total_employees += 1
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross += gross_pay

# Print totals
print(f"Total number of employees entered: {total_employees}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross:.2f}")
