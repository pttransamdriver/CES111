"""
CSE 111
Author: Tim Illguth
Instructor: Christian Eisingers
Filename: Prep_05.py
"""


# Start by importing the pytest library
import pytest

# Our mission is to write a function that converts Fahrenheit to Celsius, and we need to test it like pros.

# Let's write the main function first:
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Now, let's write the test function "test_fahrenheigt_to_celssius" using assert statements and pytest's 'approx' function thingy.
def test_fahrenheit_to_celsius():
    # Negative temperatures are very common in Alaska :)
    assert fahrenheit_to_celsius(-25) == pytest.approx(-31.66667)
    assert fahrenheit_to_celsius(0)   == pytest.approx(-17.77778)
    assert fahrenheit_to_celsius(32)  == pytest.approx(0)
    assert fahrenheit_to_celsius(70)  == pytest.approx(21.1111)

# This is where the action begins. We call our test function.
pytest.main(["-v", "--tb=line", "-rN", __file__])
