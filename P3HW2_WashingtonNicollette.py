#Nicollette Washington
#10/25/2024
#P3HW2
#Create a program to gather employee information to calculate payroll

# Get employee information
name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: $"))             

# Calculate pay
regular_hours = min(40, hours)
overtime_hours = max(0, hours - 40)
    
regular_pay = regular_hours * pay_rate
overtime_pay = overtime_hours * (pay_rate * 1.5) # Overtime is 1.5 times regular pay
gross_pay = regular_pay + overtime_pay

# Calculate overtime
if hours > 40:
    overtime_hours = hours - 40
    regular_hours = 40
else:
    overtime_hours = 0
    regular_hours = hours

print("-------------------------------")
    
# Print employee name
print(f"Employee name: {name}")
print()
    
# Print header 
print(f"{'Hours Worked':<15}{'Pay Rate':<15}{'OverTime':<15}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<15}")
print("-------------------------------------------------------------------------------------------------")
    
# Print calculations 
print(f"{hours:<15.1f}{pay_rate:<15.1f}{overtime_hours:<15.1f}${overtime_pay:<14.2f}${regular_pay:<14.2f}${gross_pay:<14.2f}")


