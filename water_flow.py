"""
File: water_flow.py
Author: Tim Illguth
Professor: Christian Eisinger

"""

# Calculate the height of our water column.
def water_column_height(tower_height, tank_height):
    h = tower_height + (3 * tank_height) / 4
    return h

# Calulate the pressure gain resulting from the height of our water column.
def pressure_gain_from_water_height(height):
    density_water = 998.2
    gravity = 9.80665
    pressure = (density_water * gravity * height) / 1000
    return pressure

# Calculate the pressure loss along the pipeline.
def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    density_water = 998.2
    pressure_loss = -(friction_factor * pipe_length * density_water * fluid_velocity**2) / (2000 * pipe_diameter)
    return pressure_loss
