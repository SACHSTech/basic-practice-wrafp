"""
-------------------------------------------------------------------------------------------
Name: oz_to_ml.py 
Purpose: A website only lists recipes with ingredients for 4 servings. This program helps to convert ounces to milliliters and compute the amount of mililiters needed to create number of servings.

Author: Huang.K 

Created:    date in 3/12/2020
-------------------------------------------------------------------------------------------
"""

print("-----[Ounces and Millimeter Converter]-----")

# Input # of ounces and servings needed to compute
ounces = float(input("Enter the amount of fluid in ounces: "))
servings = int(input("Enter the amount of servings needed: "))

# Compute milliliters
ml = (ounces * 29.5735) * servings/4

import time
time.sleep(3)

# Output milliliters
print("\n\n\nYou need", ml, "ml.")

