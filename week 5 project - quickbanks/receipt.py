# this project helps me build a grocery store receipt program for my uncle

# Enhancement: Prints a coupon for one randomly selected ordered item

# Author: Osigwe Uchechukwu DavidCaleb
# Project: Mini-Quickbank for Grocery Store program

import csv

from datetime import datetime, timedelta

import random

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound dictionary
    and return the dictionary.
    
    Parameters:
        filename: the name of the CSV file to read
        key_column_index: the index of the column containing the key
    Return: a compound dictionary with product data
    """

    dictionary = {}

    try:
        with open(filename, "rt") as csv_file:
            reader = csv.reader(csv_file)
            next(reader) #skips the header

            for row in reader:
                if len(row) > 0:
                    key = row[key_column_index]
                    dictionary[key] = row

    except FileNotFoundError as e:
        print(f"error: Missing File \n {e}")
    
    except PermissionError as e:
        print(f"error: Permission denied when reading file {filename} \n {e}")

    return dictionary

def main():
    try:
        # reading products.csv
        products_dict = read_dictionary("products.csv", 0)

        # store name
        store_name = "Samco Emporium"
        print("*******************************")
        print(store_name)

        # open and process customer's order
        total_items = 0
        subtotal = 0.0

        ordered_products = [] # to track items for the coupon later

        with open("request.csv", "rt") as request_file:
            reader = csv.reader(request_file)
            next(reader) # skips the header row

            for row in reader:
                if len(row) < 2:
                    continue
                product_id = row[0]
                quantity = int(row[1])

                # look up products in catalog
                product = products_dict[product_id]
                name = product[1]
                price = float(product[2])

                # track for summary
                total_items += quantity
                subtotal += price * quantity

                # store for coupon selection
                ordered_products.append((name, price))

                # print line item
                print(f"{name}: {quantity} @ {price}")

            #calculate tax and total
            tax_rate = 0.06
            sales_tax = subtotal * tax_rate
            total = subtotal + sales_tax

            # print summary
            print(f"\nnumber of items: {total_items}")
            print(f"\nSubtotal: {subtotal}")
            print(f"\n Sales tax: {sales_tax}")
            print(f" \nTotal: {total:.2f}")

            # Thank you message
            print(f"\n Thank you for shopping at {store_name}")
            print()

            #current date and time
            current_datetime = datetime.now()
            print(current_datetime.strftime("%a %b %d %H %M %S %Y"))

            # Exceeding Requirements

            # Print a coupon with percentage off and date of promo sales at the bottom of the receipt
            # for a random ordered product

            if ordered_products:
                coupon_item_name, coupon_price = random.choice(ordered_products)
                discount = coupon_price * 0.20 # 20% off

                # print the coupon
                print("\n **** COUPON ****")
                print(f" \nGet 20% off your next {coupon_item_name}!")
                print(f" \nSave {discount:.2f} on your next purchase!")
                print(" \nValid through December 31, 2025 \n")

    except FileNotFoundError as e:
        print("error: Missing file")
        print(e)

    except PermissionError as e:
        print("error: Permission denied")
        print(e)
    
    except KeyError as e:
        print("error: unknown product ID in the request.csv file")
        print(e)

    except ValueError as e:
        print("Error: invalid data in request.csv (quantity must be a number)")
        print(e)

    except Exception as e:
        print(f"Unexpected error: {e}")

# Protect the main function call
if __name__ == "__main__":
    main()
        



