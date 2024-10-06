#Nicollette Washington
#10/4/2024
#P2LAB2
#Writing code that uses dictonary to store user input and output.



my_dict = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}
print ("Keys:", list(my_dict.keys()))
# Get input for car model
car = input("Enter a vehicle to see it's mpg: ")
 
# See if car is is in dictionary
if car in my_dict:
    mpg = my_dict[car]
    print(f"The {car} gets {mpg} mpg.")

    #ask how many miles are to be driven
    miles = float(input(f"How many miles will you drive the {car}? "))

    # Calculate how many gallons are needed
    gallons_needed = miles / mpg

    # Show results
    print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {car} {miles:.1f} miles.")
