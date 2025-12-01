# 1. Read the contents of the file into a list where each line of text in the file is stored in a separate element in the list.
# 2. Print the entire list.
# 3. Remove the first element from the list.
# 4. Remove the last element from the list.
# 5. Replace all occurrences of "AB" in the list with "Alberta".
# 6. Count the number of elements that are "Alberta" and print that number.

def main():

    # 1. Read the contents of a text file named plants.txt into a list.
    my_list = read_list("provinces.txt")

    # 2. print the entire list
    print(my_list)

    print("********************************************************")

    # 3. remove the first element from the list
    my_list.pop(0)

    # print the updated list
    print(my_list)

    print("********************************************************")

    # 4. remove the last element from the list
    my_list = my_list[:-1]

    # print the updated list
    print(my_list)

    print("********************************************************")

    # 5. Replace all occurrences of "AB" in the list with "Alberta".
    # by knowing the index of AB in the list
    my_list = ["Alberta" if x == "AB" else x for x in my_list]

    # print the updated list
    print(my_list)

    print("********************************************************")

    # 6. Count the number of elements that are "Alberta" and print that number
    al = my_list.count("Alberta")

    # print the number of times Alberta appeared in the list
    print(f"Alberta appeared {al} times in the list")

# function to read the list

def read_list(filename):
    """Read the contents of a text file into a list, remove the first element from the list
    remove the last element from the list, replace all occurencies of "AB" in the list with "Alberta"
    count the number of elements that are "Alberta" and print the number
    and return the list. Each element in the list will contain
    one line of text from the text file.
    Parameter filename: the name of the text file to read
    Return: a list of strings
    """

    # Create an empty list that will store
    # the lines of text from the text file.

    my_list = []

    # Open the text file for reading and store a reference
    # to the opened file in a variable named text_file.

    with open(filename, "rt") as text_file:
        # Read the contents of the text
        # file one line at a time.

        for line in text_file:
            # Remove white space, if there is any,
            # from the beginning and end of the line.

            clean_line = line.strip()

            # Append the clean line of text
            # onto the end of the list.
            my_list.append(clean_line)

    # Return the list that contains the lines of text.
    return my_list

# Call main to start this program.
if __name__ == "__main__":
    main()