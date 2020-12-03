"""
-------------------------------------------------------------------------------------------
Name: cake_joy.py 
Purpose: A program that computes the amount of jogging needed to burn the calories of the cake slices the user has eaten.

Author: Huang.K 

Created:    date in 3/12/2020
-------------------------------------------------------------------------------------------
"""

print("-----[Cake & Jog Program]-----")

# Input amount of cake slices eaten
cake_slices = int(input("\nEnter amount of cake slices you've eaten: "))

# Compute the amount of jogging needed to burn the calories made when eaten the cake slices
jogging_needed = (cake_slices * 225) /100

# Output the calculation
print("\n\nTo burn", cake_slices * 225, "calories,\nYou need to jog", jogging_needed, "km.")