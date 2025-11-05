# Write a program that will accept user input that describes a tire 
# then calculate and display the tire's volume, 
# and if the user wants to make purchase, his/her phone number will be required and saved in the file.
# Record the tire information in a log file.

"""
I'll import math module for calculations and datetime 
from datetime for days of the week and time (if needed)
"""

import math

from datetime import datetime

# get user inputs

width = float(input("Enter the width of the tire in mm (ex 205):"))

aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60):"))

diameter = float(input("Enter the diameter of the wheel in inches (ex 15):"))

# calculate the volume of the tyre example:
"""
v = 
π w2 aw a + 2,540 d
10,000,000,000
v is the volume in liters,
π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
w is the width of the tire in millimeters,
a is the aspect ratio of the tire, and
d is the diameter of the wheel in inches.
"""

height = aspect_ratio / 100 * width # for the sidewall height in mm

rim = diameter * 25.4 # rim diameter in mm

volume = math.pi * width * (rim * height + height ** 2)

v = volume / 1_000_000 #convert to litres

# display the total litres

print("___________________***_____________________")

print()

print(f"The approximate volume is {v:.2f} liters")

print()

print("___________________***_____________________")

print()

# ask the user if they want to make purchase yet

buy = input("Would you like to buy tires with these dimensions? (yes/no): ").strip().lower()

phone = ""

# use the condition statement to see if the user wants to make purchase 
# and print both the phone into the file

if buy == "yes":
    phone = input("Please enter your phone number: ").strip()

# log/save the information into the volume.txt file

current = datetime.now()

today = f"{current:%Y-%m-%d}"

# open and save the information into the volume text file

with open("volumes.txt", "at") as file:
    print(f"{today}, {width}, {aspect_ratio}, {diameter}, {v:.2f}", file=file)

    # if the user bought, then the user's phone number will also be added in the text file
    if phone:
        print(f"phone: {phone}", file=file)