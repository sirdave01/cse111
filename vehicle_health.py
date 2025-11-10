# this code defines a function to calculate vehicle health based miles per gallon and provides a main program to interact with the user.

# this program will have 3 user defined functions: main, miles per gallon with 3 parameters and lp100k with one parameter

def main():
    """"
    this main function interacts with the user to get start and end odometer readings
    and the amount of fuel used, performs the calculations and prints the results.
    """

    print("Welcome to the Vehicle Health Calculator! Please provide the following information:")

    start = float(input("Enter the starting odometer reading (in miles): "))
    end = float(input("Enter the ending odometer reading (in miles): "))
    gallons = float(input("Enter the amount of fuel used (in gallons): "))

    # calculate_mpg(start, end, gallons)
    mpg = miles_per_gallon(start, end, gallons)
    lp100k = lp100k_from_mpg(mpg)

    print(f"\nYour vehicle's fuel efficiency is {mpg:.1f} miles per gallon (MPG).")
    print(f"This is equivalent to {lp100k:.2f} liters per 100 kilometers (L/100km).")

def miles_per_gallon(start, end, gallons):
    """"returns miles per gallon given start and end odometer readings divided gallons used."""
    return (end - start) / gallons

def lp100k_from_mpg(mpg):
    """returns liters per 100 kilometers given miles per gallon."""
    return 235.215 / mpg

# main program
if __name__ == "__main__":
    main()