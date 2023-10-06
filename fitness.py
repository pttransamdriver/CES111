"""
File: fitness.py
Author: Tim Illguth
Professor: Christian Eisinger

"""

import datetime

# Define the functions that we'll need to use for the conversions:
def lbs_to_kg(weight_pounds):
    return weight_pounds * 0.45359237

def in_to_cm(height_inches):
    return height_inches * 2.54


# Now let's define the calculations that we'll need to use for BMI and BMR:
def calculate_bmi(weight_kg, height_cm):
    # BMI formula: bmi = 10,000 * weight (kg) / (height (cm))^2
    return 10000 * weight_kg / (height_cm ** 2)


def calculate_bmr(weight_kg, height_cm, age, if_male):
    if if_male:
        # BMR formula for men
        return 88.362 + 13.397 * weight_kg + 4.799 * height_cm - 5.677 * age
    else:
        # BMR formula for women
        return 447.593 + 9.247 * weight_kg + 3.098 * height_cm - 4.330 * age

# Now that we have all the conversions and calculations figured out we can call them whenever we want
# Let's call them now in our "main()" function: 

def main():
    # Get user input
    gender_of_usr = input("Enter your gender (male/female): ").lower()
    birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
    weight_pounds = float(input("Enter your weight (in pounds): "))
    height_inches = float(input("Enter your height (in inches): "))

    # Calculate age
    birthdate = datetime.datetime.strptime(birthdate_str, '%Y-%m-%d').date()
    today = datetime.date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

    # Convert weight from pounds to kilograms
    weight_kg = lbs_to_kg(weight_pounds)

    # Convert height from inches to centimeters
    height_cm = in_to_cm(height_inches)

    # Calculate BMI
    bmi = calculate_bmi(weight_kg, height_cm)

    # Calculate BMR based on user gender
    man = gender_of_usr == 'male'
    bmr = calculate_bmr(weight_kg, height_cm, age, man)

    # Print the results
    print(f"Age:, {age}")
    print(f"Weight:, {weight_kg:.2f}kg")
    print(f"Height:, {height_cm:.2f}cm")
    print(f"BMI:, {bmi:.2f}")
    print(f"BMR:, {bmr:.2f}")
    print("BMI over 25 is bad :o")

# Call the main function
main()

