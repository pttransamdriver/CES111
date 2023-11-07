"""
CSE 111 
Author: Tim Illguth
Instructor: 
File Team_05.py
"""

#Okay this line was super cool. This tab completed the functions from the names file. Geeked out a little about that :)
from names import make_full_name, extract_family_name, extract_given_name
import pytest


def test_make_full_name():
    assert make_full_name("Marie", "Toussaint") == "Toussaint; Marie"
    assert make_full_name("George", "Washington") == "Washington; George"

def test_extract_family_name():
    assert extract_family_name("Toussaint; Marie")   == "Toussaint"
    assert extract_family_name("Washington; George") == "Washington"

def test_extract_given_name():
    assert extract_given_name("Toussaint; Marie")   == "Marie"
    assert extract_given_name("Washington; George") == "George"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
 
    

