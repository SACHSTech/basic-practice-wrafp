"""
///////////////////////////////////////////////////////////////////////////////////////////
Name: avg_marks.py
Purpose: Compute the averages of 4 marks and output it to the user

Author: Huang.K 
Created:     date in 3/12/2020
///////////////////////////////////////////////////////////////////////////////////////////
"""

# Get 4 marks from the user
mark1 = float(input("Enter Student 1's Mark: "))
mark2 = float(input("Enter Student 2's Mark: "))
mark3 = float(input("Enter Student 3's Mark: "))
mark4 = float(input("Enter Student 4's Mark: "))

# Compute the averages of the 4 marks
avg_mark = (mark1 + mark2 + mark3 + mark4)/4

# Output the averages to the user
print("The average of the marks is " + str(avg_mark))
