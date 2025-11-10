# Background
# In many countries, food is stored in steel cans (also known as tin cans) that are shaped like cylinders. 
# There are many different sizes of steel cans. 
# The storage efficiency of a can tells us 
# how much a can stores versus how much steel is required to make the can. 
# Some sizes of cans require a lot of steel to store a small amount of food. 
# Other sizes of cans require less steel and store more food. 
# A can size with a large storage efficiency is considered 
# more friendly to the environment than a can size with a small storage efficiency.

# Real World Solution

import math

# writing and declaring functions to compute volume name compute_volume
def compute_volume(radius, height):
    """Compute and return the volume of a cylinder given its radius and height."""
    volume = math.pi * radius**2 * height
    return volume

# function to compute the surface named compute_surface_area
def compute_surface_area(radius, height):
    """Compute and return the surface area of a cylinder given its radius and height."""
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

# function to compute storage efficiency named compute_storage_efficiency
def compute_storage_efficiency(radius, height):
    """Compute and return the storage efficiency of a cylinder given its radius and height."""
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = volume / surface_area
    return storage_efficiency

# writing the can sizes as a list of tuples named can_sizes
# Note: Table values are diameters in cm, so true_radius = diameter / 2
can_sizes = [
    ("#1 Picnic", 6.83 / 2, 10.16),
    ("#1 Tall", 7.78 / 2, 11.91),
    ("#2", 8.73 / 2, 11.59),
    ("#2.5", 10.32 / 2, 11.91),
    ("#3 Cylinder", 10.79 / 2, 17.78),
    ("#5", 13.02 / 2, 14.29),
    ("#6Z", 5.40 / 2, 8.89),
    ("#8Z short", 6.83 / 2, 7.62),
    ("#10", 15.72 / 2, 17.78),
    ("#211", 6.83 / 2, 12.38),  # Diameter 6.83 cm, height 12.38 cm
    ("#300", 7.62 / 2, 11.27),
    ("#303", 8.10 / 2, 11.11)
]

# main program to iterate through the can sizes and compute storage efficiency
print("Storage efficiency for each Can Size (cubic cm per square cm):\n")

efficiencies = []

for name, r, h in can_sizes:
    eff = compute_storage_efficiency(r, h)
    efficiencies.append((name, eff))
    print(f"Can Size: {name}, Storage Efficiency: {eff:.2f}")

# find the can size with the highest storage efficiency
best_can = max(efficiencies, key=lambda x: x[1])
print(f"\nCan size with the highest storage efficiency: {best_can[0]} with efficiency {best_can[1]:.2f}")