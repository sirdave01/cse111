# Modifications made to the original file:
# - Added constants for EARTH_ACCELERATION_OF_GRAVITY, WATER_DENSITY, and WATER_DYNAMIC_VISCOSITY at the top for better readability and to avoid hardcoding values inside functions.
# - In pressure_gain_from_water_height: Implemented the missing function using the formula P = (ρ * g * h) / 1000, replacing the TODO and return 0.
# - In pressure_loss_from_pipe: Corrected the denominator from 200 to 2000 to match the formula P = -f L ρ v² / (2000 d).
# - In pressure_loss_from_fittings: Fixed the formula by changing fluid_velocity * 2 to fluid_velocity ** 2 (squared) to match P = -0.04 ρ v² n / 2000.
# - In reynolds_number: Implemented the missing function using R = (ρ * d * v) / μ, replacing the TODO and return 0.
# - In pressure_loss_from_pipe_reduction: Corrected the k formula from ((D/d)^4 + 1) to ((D/d)^4 - 1) to match the specified formula.
# - Added a new function kpa_to_psi to convert kPa to psi as an exceeding requirement.
# - In main: Added calculation and print for pressure in psi to display both units.

EARTH_ACCELERATION_OF_GRAVITY = 9.80665  # Added constant for gravity (meter / second²)
WATER_DENSITY = 998.2  # Moved and standardized density constant (kilogram / meter³)
WATER_DYNAMIC_VISCOSITY = 0.0010016  # Added constant for viscosity (Pascal seconds)
PVC_SCHED80_INNER_DIAMETER = 0.28687  # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)
HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)

def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))
    
    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)
    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss
    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss
    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss
    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss
    psi = kpa_to_psi(pressure)  # Added to calculate and print pressure in psi as exceeding requirement
    print(f"Pressure at house: {pressure:.1f} kilopascals")
    print(f"Pressure at house: {psi:.1f} pounds per square inch")  # Added print for psi

def water_column_height(tower_height, tank_height):
    return tower_height + 3 * tank_height / 4 

def pressure_gain_from_water_height(height):

    return (WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * height) / 1000

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):

    numerator = -friction_factor * pipe_length * WATER_DENSITY * fluid_velocity ** 2
    denominator = 2000 * pipe_diameter 
    return numerator / denominator

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):

    return -0.04 * WATER_DENSITY * fluid_velocity ** 2 * quantity_fittings / 2000

def reynolds_number(hydraulic_diameter, fluid_velocity):

    return (WATER_DENSITY * hydraulic_diameter * fluid_velocity) / WATER_DYNAMIC_VISCOSITY

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    
    k = (0.1 + 50 / reynolds_number) * ((larger_diameter / smaller_diameter) ** 4 - 1)
    return -k * WATER_DENSITY * fluid_velocity ** 2 / 2000

def kpa_to_psi(pressure_kpa):
    # Added: New function to convert kPa to psi (exceeding requirements); conversion factor is approximate
    return pressure_kpa / 6.89475729

if __name__ == "__main__":
    main()