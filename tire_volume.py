"""
CSE 111
Author: Tim Illguth
Instructor: Christian Eisingers
Filename: tire_volume.py
"""

import math
import datetime

# Printing the introduction and instructions
print("********************************************************************************")
print("Hello auto enthusiest")
print("********************************************************************************")
print("This program helps you calculate the air volume in your tires")
print("Your car tires will have numbers that look like this: 'P235/30ZR18' ")
print("********************************************************************************")
print("************************** Guide and Example ***********************************")
print("********************************************************************************")
print("The first number in this case is: 235 which is the width of the tire in mm.")
print("The 'P' means passanger vehicle. You might also see LT for Light Truck")
print("The next number is 30 in this case meaning the cross section width, meaning the distance from your")
print("rim to the road. The Z in this case is the speed rating. Only specified on faster car tires")
print("The R18 just means outside diameter of the Rim or wheel. In this case 18 inch wheel ")

# Defining the human inputs
wheel_diamet = float(input("Please type the diamter of your wheels(rims) in inches (18 in the example): "))
aspect_width = float(input("Please input the cross section width (The 30 from the example): "))
width_tire   = float(input("Now the tire diameter (235 from the example): "))

numerator_out = math.pi * (width_tire**2) * aspect_width
numerator_in  = (width_tire * aspect_width) + (2540 * wheel_diamet)
tire_volume   = (numerator_out * numerator_in)/10000000000

# Getting the current date
current_date = datetime.datetime.now().strftime("%Y-%m-%d")  # Format the date as YYYY-MM-DD

# Opening the volumes.txt file for appending
with open("volumes.txt", "a") as file:
    # File function to append the required values to the file
    file.write(f"{current_date}, {width_tire}, {aspect_width}, {wheel_diamet}, {tire_volume:.2f}\n")

print(f"Your tires have {tire_volume:.2f} liters of air in them")