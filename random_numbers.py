"""
File: random_numbers.py
Author: Commander Data
Professor: Christian Eisinger

"""

# As the only andriod of my kind I am studying anchent ways in which humans interacted with their computers. 
# I've decided to take an assignment I found from an anchient higher learning class assignment from an
# anchient school called "B" "Y" "U" Idaho. This was from before the states borders where expanded :) 

import random

def main():
    # Initializing the lists of numbers with Stardate readings.
    stardate_readings = [43125.8, 45156.7, 46424.4]
    print("Initial Stardate Readings:", stardate_readings)

    # Adding a new Stardate reading to the list.
    append_random_numbers(stardate_readings)
    print("Stardate Readings after adding one entry:", stardate_readings)

    # Adding multiple new Stardate readings to the list.
    append_random_numbers(stardate_readings, 3)
    print("Stardate Readings after adding three entries:", stardate_readings)

    # Initializing a list of crew member names.
    crew_names = ['Picard', 'Riker', 'Geordi']
    print("Initial Crew Names:", crew_names)

    # Adding random names of crew members to the list.
    append_random_words(crew_names, 2)
    print("Crew Names after adding two members:", crew_names)

def append_random_numbers(stardates_list, quantity=1):
    # Generating and appending new Stardate readings.
    for _ in range(quantity):
        new_stardate = round(random.uniform(40000, 50000), 1)
        stardates_list.append(new_stardate)

def append_random_words(names_list, quantity=1):
    # List of available crew member names from the Starship Enterprise.
    available_crew = ['Data', 'Worf', 'Troi', 'Crusher', 'Wesley', 'Guinan']
    for _ in range(quantity):
        random_crew_member = random.choice(available_crew)
        names_list.append(random_crew_member)

main()
