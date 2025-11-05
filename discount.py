# You work for a retail store that wants to increase sales on Tuesday and Wednesday, 
# which are the store’s slowest sales days. On Tuesday and Wednesday, 
# if a customer’s subtotal is $50 or greater, 
# the store will discount the customer’s subtotal by 10%.

# For this activity, I will import date time module 
# (Date time module will help to get the days of the week without asking for the cuastomer's input')

import datetime

# define calc_final_price function with 2 parameters

def calc_final_price(subtotal, subtotal_day):
    """
    Calculate the final price after applying discount if applicable.
    
    Args:
    subtotal (float): The customer's subtotal before discount.
    subtotal_day (str): The day of the week (e.g., 'Tuesday', 'Wednesday').
    
    Returns:
    float: The final price.
    """
    discount = 0.0

    if subtotal_day.lower() in ["tuesday", "wednesday"] and subtotal >= 50:
        discount = 0.10

        # calculate the discounted subtotal

        discounted_subtotal = subtotal * (1 - discount)

        print(f"discount applied:  10% off on {subtotal_day}. Subtotal: ${subtotal:.2f} -> Final: ${discounted_subtotal:.2f}")
        return discounted_subtotal
    else:
        print(f"No discount applied. Subtotal: {subtotal:.2f} -> Final: ${subtotal:.2f}")
        return subtotal
    
    # write the main program that gets the day of the wek, ask customer's subtotal and calculates the subtotal if any

# Main Program

if  __name__ == "__main__":

    # use datetime module to get current day

    today = datetime.datetime.now().strftime("%A")
    print(f"Today's date is {datetime.datetime.now().strftime('%B %d, %Y')}, which is a {today}")

    # calculate for subtotal if any with try keyword

    try:
        subtotal = float(input("Enter the customer's subtotal $: "))
        if subtotal < 0:
            raise ValueError ("Subtotal Cannot be Negative!")
    except ValueError as e:
        print(f"invalid input {e}.")
        subtotal = 0.0
    
    # calculate the final price

    final_price = calc_final_price(subtotal, today)

    # print the final price to be paid by the customer

    print("_________________***___________________")

    print()

    print(f"Transaction complete. Final amount due: ${final_price:.2f}. Thanks for your patronage!")

    print()

    print("_________________***___________________")