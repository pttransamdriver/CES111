"""
File: fuel_usage.py
Author: Tim Illguth
Professor: Christian Eisinger

"""


'''
This isn't too bad, to start we take the user inputs of:
1) Milage start aka "start_miles"
2) Milage end aka the variabe "end_miles"
3) Fuel used aka the variable "amount_gallons"

So the method here is to define the functions "def" that we'll need to call when we want them
We could do this without functions and just using variables to accompish the task of this assignment 
but that woun't help us get used to using functions

So let's start with the calculations functions first then use those for the main function "main()"
'''

# Defines a function called "miles_per_gallon" that takes the three parameters  
#  1) start_miles
#  2) end_miles 
#  3) amount_gallons 
# Remmeber that each of these functions only runs if they are called:
# To call this function use the name "miles_per_gallon" this is done later inside the "main()" function
def miles_per_gallon(start_miles, end_miles, amount_gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.

    Parameters
        start_miles: An odometer value in miles.
        end_miles: Another odometer value in miles.
        amount_gallons: A fuel amount in U.S. gallons.
    Return: Fuel efficiency in miles per gallon.
    """
    # This defines the variables that are called when the function is called. 
    miles_traveled = end_miles - start_miles
    mpg = miles_traveled / amount_gallons
    return mpg

# To call this function, use the term "lp100k_from_mpg()" which is done later inside the "main()" function
def lp100k_from_mpg(mpg):
    """Converts miles per gallon to liters per 100
    kilometers and return the converted value.

    Parameter mpg: A value in miles per gallon
    Return: The converted value in liters per 100km.
    """
    lp100k = 235.215 / mpg  # Conversion formula to take mpg and get liters per 100kl
    return lp100k

# This is the main fuction that gets called 
def main():
    # Get the start odometer miles from the user.
    start_miles = float(input("Enter the starting odometer value (miles): "))

    # Get the end odometer miles from the user.
    end_miles = float(input("Enter the ending odometer value (miles): "))

    # Get a fuel amount in gallons used from the user.
    amount_gallons = float(input("Enter the amount of fuel (gallons): "))

    # Call the miles_per_gallon function from above and store the result in a variable "mpg".
    mpg = miles_per_gallon(start_miles, end_miles, amount_gallons)

    # Call the lp100k_from_mpg function to convert mpg to lp100km and make the variable lp100k.
    lp100k = lp100k_from_mpg(mpg)

    # Display the results.
    print(f"Fuel efficiency: {mpg:.2f} miles per gallon")
    print(f"Fuel efficiency: {lp100k:.2f} liters per 100 kilometers")


# Call the main function from above
main()
