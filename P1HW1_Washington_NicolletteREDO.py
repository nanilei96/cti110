#Nicollette Washington
#9/25/2024
#P1HW1
#Creating a code that does math for you.




print("-----Calculating Exponents----")



base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))



#calculate result
result = base**exponent



#print result
print(f"{base} raised to the power of {exponent} is {result} !!")



print("\n-----Addition and Subtraction-----")



#get three integers from user
start = int(input("Enter a starting integer: "))
add = int(input("Enter an integer to add: "))
subtract = int(input("Enter an integer to subtract: "))



#perform calculation
final_result = start + add - subtract



#print result
print(f"\n{start} + {add} - {subtract} is equal to {final_result}")
