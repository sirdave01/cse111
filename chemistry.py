
# Author = Osigwe Uchechukwu David Caleb

# Date: 30th November, 2025

# Purpose:
# You are an intern working for a government research facility. The chemistry lab has requested 
# a program that will calculate the molar mass and the number of moles for a given quantity of a chemical compound. 
# You have been assigned to create this program.

# Enhancement: 
#   - Rounds output to 4 decimal places for clean, readable results
#   - Handles known elements only (uses try/except with helpful error message)
#   - Displays a breakdown of each element's contribution (super useful for chemists!)


# i will import parse_formula from formula from the formula.py to design and run the program

from formula import parse_formula

def make_periodic_table():
    """Return a dictionary of the periodic table: symbol → [name, atomic_mass]"""
    return {
        "Ac": ["Actinium", 227], 
        "Ag": ["Silver", 107.8682], 
        "Al": ["Aluminum", 26.9815386],
        "Ar": ["Argon", 39.948], 
        "As": ["Arsenic", 74.9216], 
        "At": ["Astatine", 210],
        "Au": ["Gold", 196.966569], 
        "B": ["Boron", 10.811], 
        "Ba": ["Barium", 137.327],
        "Be": ["Beryllium", 9.012182], 
        "Bi": ["Bismuth", 208.9804], 
        "Br": ["Bromine", 79.904],
        "C": ["Carbon", 12.0107], 
        "Ca": ["Calcium", 40.078], 
        "Cd": ["Cadmium", 112.411],
        "Ce": ["Cerium", 140.116], 
        "Cl": ["Chlorine", 35.453], 
        "Co": ["Cobalt", 58.933195],
        "Cr": ["Chromium", 51.9961], 
        "Cs": ["Cesium", 132.9054519], 
        "Cu": ["Copper", 63.546],
        "Dy": ["Dysprosium", 162.5], 
        "Er": ["Erbium", 167.259], 
        "Eu": ["Europium", 151.964],
        "F": ["Fluorine", 18.9984032], 
        "Fe": ["Iron", 55.845], 
        "Fr": ["Francium", 223],
        "Ga": ["Gallium", 69.723], 
        "Gd": ["Gadolinium", 157.25], 
        "Ge": ["Germanium", 72.64],
        "H": ["Hydrogen", 1.00794], 
        "He": ["Helium", 4.002602], 
        "Hf": ["Hafnium", 178.49],
        "Hg": ["Mercury", 200.59], 
        "Ho": ["Holmium", 164.93032], 
        "I": ["Iodine", 126.90447],
        "In": ["Indium", 114.818], 
        "Ir": ["Iridium", 192.217], 
        "K": ["Potassium", 39.0983],
        "Kr": ["Krypton", 83.798], 
        "La": ["Lanthanum", 138.90547], 
        "Li": ["Lithium", 6.941],
        "Lu": ["Lutetium", 174.9668], 
        "Mg": ["Magnesium", 24.305], 
        "Mn": ["Manganese", 54.938045],
        "Mo": ["Molybdenum", 95.96], 
        "N": ["Nitrogen", 14.0067], 
        "Na": ["Sodium", 22.98976928],
        "Nb": ["Niobium", 92.90638], 
        "Nd": ["Neodymium", 144.242], 
        "Ne": ["Neon", 20.1797],
        "Ni": ["Nickel", 58.6934], 
        "Np": ["Neptunium", 237], 
        "O": ["Oxygen", 15.9994],
        "Os": ["Osmium", 190.23], 
        "P": ["Phosphorus", 30.973762], 
        "Pa": ["Protactinium", 231.03588],
        "Pb": ["Lead", 207.2], 
        "Pd": ["Palladium", 106.42], 
        "Pm": ["Promethium", 145],
        "Po": ["Polonium", 209], 
        "Pr": ["Praseodymium", 140.90765], 
        "Pt": ["Platinum", 195.084],
        "Pu": ["Plutonium", 244], 
        "Ra": ["Radium", 226], 
        "Rb": ["Rubidium", 85.4678],
        "Re": ["Rhenium", 186.207], 
        "Rh": ["Rhodium", 102.9055], 
        "Rn": ["Radon", 222],
        "Ru": ["Ruthenium", 101.07], 
        "S": ["Sulfur", 32.065], 
        "Sb": ["Antimony", 121.76],
        "Sc": ["Scandium", 44.955912], 
        "Se": ["Selenium", 78.96], 
        "Si": ["Silicon", 28.0855],
        "Sm": ["Samarium", 150.36], 
        "Sn": ["Tin", 118.71], 
        "Sr": ["Strontium", 87.62],
        "Ta": ["Tantalum", 180.94788], 
        "Tb": ["Terbium", 158.92535], 
        "Tc": ["Technetium", 98],
        "Te": ["Tellurium", 127.6], 
        "Th": ["Thorium", 232.03806], 
        "Ti": ["Titanium", 47.867],
        "Tl": ["Thallium", 204.3833], 
        "Tm": ["Thulium", 168.93421], 
        "U": ["Uranium", 238.02891],
        "V": ["Vanadium", 50.9415], 
        "W": ["Tungsten", 183.84], 
        "Xe": ["Xenon", 131.293],
        "Y": ["Yttrium", 88.90585], 
        "Yb": ["Ytterbium", 173.054], 
        "Zn": ["Zinc", 65.38],
        "Zr": ["Zirconium", 91.224]
    }

def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total molar mass from a symbol_quantity_list."""
    total_mass = 0.0
    SYMBOL_INDEX = 0
    QUANTITY_INDEX = 1

    print("\nBreakdown of molar mass calculation:")
    print("-" * 50)

    # loop through to get symbols and quantities from the molar moss

    for symbol, quantity in symbol_quantity_list:
        if symbol not in periodic_table_dict:
            raise KeyError(f"Unknown element: {symbol}")
        
        atomic_mass = periodic_table_dict[symbol][1]
        contribution = atomic_mass * quantity
        total_mass += contribution
        element_name = periodic_table_dict[symbol][0]
        print(f"{quantity:2} {symbol} ({element_name}): {quantity} × {atomic_mass:.6f} = {contribution:.6f}")

    print("-" * 50)
    return total_mass

def main():
    print("Chemical Molar Mass and Moles Calculator")
    print("========================================\n")

    # 1. Ask for chemical formula
    formula = input("Enter the chemical formula (e.g., H2O, C6H12O6): ").strip()
    if not formula:
        print("No formula entered. Goodbye!")
        return

    # 2. Ask for sample mass in grams
    while True:
        try:
            sample_mass = float(input("Enter the sample mass in grams: "))
            if sample_mass <= 0:
                print("Please enter a positive number.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    try:
        # 3. Get periodic table
        periodic_table = make_periodic_table()

        # 4. Parse the formula into symbol-quantity list
        symbol_quantity_list = parse_formula(formula, periodic_table)

        # 5. Compute molar mass
        molar_mass = compute_molar_mass(symbol_quantity_list, periodic_table)

        # 6. Display molar mass
        print(f"\nMolar mass: {molar_mass:.4f} grams/mole")

        # 7. Calculate number of moles
        moles = sample_mass / molar_mass

        # 8. Display number of moles
        print(f"Number of moles: {moles:.4f}")

    except KeyError as e:
        print(f"\nError: {e}")
        print("Please check your chemical formula for unknown or mistyped elements.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")


# Run the program
if __name__ == "__main__":
    main()
