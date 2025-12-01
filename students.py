# student Lookup with CSV and Dictionary

import csv

def read_dictionary(filename, key_column_index=0):
    """Read the contents of a CSV file into a compound dictionary
    where the first column is the key and the second column is the value.
    Parameters:
        filename: the name of the CSV file to read
        key_column_index: which column contains the key (usually 0)
    Return: a compound dictionary
    """
    dictionary = {}
    
    with open(filename, "r", encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip the header row
        
        for row in reader:
            if len(row) >= 2:  # Make sure row has enough columns
                key = row[key_column_index].strip()
                value = row[1].strip()  # Name is in column 1
                dictionary[key] = value
    
    return dictionary


def clean_id(user_input):
    """Remove dashes and validate the ID number format."""
    # Remove dashes
    cleaned = user_input.replace("-", "")
    
    # Check if it contains only digits
    if not cleaned.isdigit():
        print("Invalid ID Number")
        return None
    
    # Check length (BYU-I student IDs are 9 digits)
    if len(cleaned) < 9:
        print("Invalid ID Number: too few digits")
        return None
    elif len(cleaned) > 9:
        print("Invalid ID Number: too many digits")
        return None
    
    return cleaned


def main():
    # Read the CSV file into a dictionary: {id: name}
    students = read_dictionary("students.csv")
    
    print("Student Name Lookup System")
    print()
    
    while True:
        user_id = input("Please enter an ID Number (xxxxxxxxx or xxx-xxx-xxxx, or 'quit' to exit): ").strip()
        
        if user_id.lower() == "quit":
            print("Goodbye!")
            break
        
        # Clean and validate the ID
        clean_id_result = clean_id(user_id)
        
        if clean_id_result is None:
            print("Please try again.\n")
            continue
        
        # Look up the student
        name = students.get(clean_id_result)
        
        if name:
            print(name)
        else:
            print("No such student")
        
        print()  # Blank line for readability


# Call main to run the program
if __name__ == "__main__":
    main()