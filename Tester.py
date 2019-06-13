"""
Author: Tracy Pham
PID: A13917165

This file contains a method to test the methods in the Dessert.py file.
"""
import pytest

def test_points():
    """
    Description: A unit test to test the function called points() in the Dessert.py file.
    """
    
    # Invalid dessert name input
    result = points(["carrot cake"])    
    assert result == [0, 0, 0, 0, 0]
    
    # If the input includes correct inputs
    result = points(["fruit tart", "cookies", "chocolate cake", "strawberry shortcake", "panna cotta"])
    assert result == [1, 1, 1, 1, 1]
    
    # If the input is not a list
    result = points(2)    
    assert result == [0, 0, 0, 0, 0]
    
    # If the input is not a list of strings
    result = points([1, 2, 3, 4, 5])    
    assert result == [0, 0, 0, 0, 0]
    