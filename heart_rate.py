# When you physically exercise to strengthen your heart, 
# you should maintain your heart rate within a range for at least 20 minutes. 
# To find that range, subtract your age from 220. 
# This difference is your maximum heart rate per minute. 
# Your heart simply will not beat faster than this maximum (220 − age). 
# When exercising to strengthen your heart, 
# you should keep your heart rate between 65% and 85% of your heart’s maximum rate.

# FIRST ASSIGNMENT

# Write a Python program named heart_rate.py that asks for a person’s age and computes 
# and outputs the slowest and fastest rates necessary to strengthen his heart. 
# To start your program, copy and paste the following code into your program and use it as 
# an outline as you write code. Note that in a Python program, 
# a triple quoted string at the top of the file acts as a comment for the entire program.

"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""
print ("*** Welcome to Heart Rate program by Osigwe Uchechukwu Davidcaleb ***")

print("---------------------***--------------------------")

# first step, get the user's age as a string

response = input("Please, enter your age?: ")

# convert the response into an integer

age = int(response)

# calculate the heart rate by subtracting the person's age by 20 
# and multiplying by the rate of 65% - 85%

hRate = 220 - age

slowRate = hRate * 0.65

fastRate = hRate * 0.85

# using the f string to print the result on the terminal for the user to see

print ("When you exercise to strengthen your heart,")
print(f"you should keep your heart rate between {slowRate} and {fastRate} beats per minute.")