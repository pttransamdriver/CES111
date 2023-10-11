"""
File: fitness.py
Author: Tim Illguth
Professor: Christian Eisinger

"""

import math 

# List stating the can names, sizes and costs. This sets the list with a directory 
# structure to allow the program to sort them. 
can_sizes = [
    {"name": "#1 Picnic",  "radius": 6.83,  "height": 10.16, "cost": 0.28},
    {"name": "#1 Tall",    "radius": 7.78,  "height": 11.91, "cost": 0.43},
    {"name": "#2",         "radius": 8.73,  "height": 11.59, "cost": 0.45},
    {"name": "#2.5",       "radius": 10.32, "height": 11.91, "cost": 0.61},
    {"name": "#3 Cylinder","radius": 10.79, "height": 17.78, "cost": 0.86},
    {"name": "#5",         "radius": 13.02, "height": 14.29, "cost": 0.83},
    {"name": "#6Z",        "radius": 5.40,  "height": 8.89,  "cost": 0.22},
    {"name": "#8Z",        "radius": 6.83,  "height": 7.62,  "cost": 0.26},
    {"name": "#10",        "radius": 15.72, "height": 17.78, "cost": 1.53},
    {"name": "#211",       "radius": 6.83,  "height": 12.38, "cost": 0.34},
    {"name": "#300",       "radius": 7.62,  "height": 11.27, "cost": 0.38},
    {"name": "#303",       "radius": 8.10,  "height": 11.11, "cost": 0.42},]

# Function to compute the volume of the cans
def compute_volume(radius, height):
    volume_1 = math.pi * radius**2 * height
    return volume_1

# Function to compute the surface area of the cans
def compute_surface_area(radius, height):
    suface_area = 2 * math.pi * radius * (radius + height)
    return suface_area

# Function to computer the efficiancy of that volume to materail used 
def compute_storage_efficiency(volume, surface_area):
    vol_efficiency = volume / surface_area
    return vol_efficiency

# Function to calculate the material cost efficiancy to volume of contents
def compute_cost_efficiency(volume, cost):
    cost_efficiency = volume / cost
    return cost_efficiency

# Main function to call the other functions
def main():
    # Default variable declaration so the for loop can function properly
    highest_storage_efficiency = float(0)
    highest_storage_efficiency_can = "Variable Place Holder so the for loop will work"

    # Default variable declaration so the for loop can function properly
    highest_cost_efficiency = float(0)
    highest_cost_efficiency_can = "Variable Place Holder so the for loop will work"

    # For loop that declares variables from the calls it makes from the defined 
    # functions at the top of the code block
    for can in can_sizes:
        volume = compute_volume(can["radius"], can["height"])
        surface_area = compute_surface_area(can["radius"], can["height"])
        storage_efficiency = compute_storage_efficiency(volume, surface_area)
        cost_efficiency = compute_cost_efficiency(volume, can["cost"])

        print(f"Can Size: {can['name']}")
        print(f"Storage Efficiency: {storage_efficiency:.2f}")
        print(f"Cost Efficiency: {cost_efficiency:.2f}")
        print()

        # If statement that iterates inside the for loop to find the most storage efficiant can 
        # in the group and sets the 'highest_storage_efficiency' variable to that. Then sets the 
        # findes the corrisponding name of that can from the directory and sets that to be the 
        # 'highest_storage_efficiency_can' variable value
        if storage_efficiency > highest_storage_efficiency:
            highest_storage_efficiency = storage_efficiency
            highest_storage_efficiency_can = can['name']

        # If statement that iterates inside the for loop to find the most cost efficiant can 
        # in the group and sets the 'highest_cost_efficiency' variable to that. Then sets the 
        # findes the corrisponding name of that can from the directory and sets that to be the 
        # 'highest_cost_efficiency_can' variable value
        if cost_efficiency > highest_cost_efficiency:
            highest_cost_efficiency = cost_efficiency
            highest_cost_efficiency_can = can['name']

    print("Can size with highest storage efficiency:", highest_storage_efficiency_can)
    print("Can size with highest cost efficiency:", highest_cost_efficiency_can)


main()
