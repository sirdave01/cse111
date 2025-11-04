# A manufacturing company needs a program that will help its employees pack manufactured items 
# into boxes for shipping. Write a Python program named boxes.py that asks the user for two integers:
#
# the number of manufactured items
# the number of items that the user will pack per box
# Your program must compute and print the number of boxes necessary to hold the items. 
# This must be a whole number. Note that the last box may be packed with fewer items than the other boxes.

# This is mathematical program, and we'll import the Math module

import math

# Get the inputs from the user for the manufactured items and items packed per box and store as an int

manItems = int(input("Please, enter the number of manufactured items: "))

itemBox = int(input("Please, enter the number of item per box: "))

# compute the solution by dividing the manufactured items by the number of items 
# packed per box to get how many boxes needed with math.ceil()method

numBox = math.ceil(manItems / itemBox)

# print the total number of boxes needed

print("___________***__________")

# print empty space

print()

print(f"for {manItems} items, packing {itemBox} per box, you'll need {numBox} boxes.")