"""
File: fuel_usage.py
Author: Tim Illguth
Professor: Christian Eisinger

"""


'''
This isn't too bad, to start we take the user inputs of:
1) Milage start
2) Milage end
3) Fuel used
Let's call the user inputs as the assignment asks:
1) start_miles
2) end_miles
3) amount_gallons
We'll do this with the "start_miles = float(input("Enter the starting odomete miles : "))
but we'll put that into the function definition "def" instead of out by itself like we did last semester
'''

# Defines a function called "miles_per_gallon" that takes the three variables 
#  "start_miles, end_miles, amount_gallons" 
# Remmeber that each of these functions only runs if they are called:
# To call this function use the name "miles_per_gallon"
def miles_per_gallon(start_miles, end_miles, amount_gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.

    Parameters
        start_miles: An odometer value in miles.
        end_miles: Another odometer value in miles.
        amount_gallons: A fuel amount in U.S. gallons.
    Return: Fuel efficiency in miles per gallon.
    """
    # This defines the veriables that are called when the function is called. 
    miles_traveled = end_miles - start_miles
    mpg = miles_traveled / amount_gallons
    return mpg

#To call this function, use the term "lp100k_from_mpg()"
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
    # Get an odometer value in miles from the user.
    start_miles = float(input("Enter the starting odometer value (miles): "))

    # Get another odometer value in miles from the user.
    end_miles = float(input("Enter the ending odometer value (miles): "))

    # Get a fuel amount in gallons from the user.
    amount_gallons = float(input("Enter the amount of fuel (gallons): "))

    # Call the miles_per_gallon function and store the result in a variable "mpg".
    mpg = miles_per_gallon(start_miles, end_miles, amount_gallons)

    # Call the lp100k_from_mpg function to convert the miles per gallon to liters per 100 kilometers
    # and store the result in a variable named lp100k.
    lp100k = lp100k_from_mpg(mpg)

    # Display the results for the user to see.
    print(f"Fuel efficiency: {mpg:.2f} miles per gallon")
    print(f"Fuel efficiency: {lp100k:.2f} liters per 100 kilometers")


# Call the main function so that this program will start executing.
main()
