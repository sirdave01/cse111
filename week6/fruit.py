
def main():
  # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
    print("*****************************")

    # 3.  Add code to reverse and print fruit_list
    print(f"Reversed: {fruit_list[::-1]}")
    print("............................")

    # 4. Add code to append "orange" to the end of fruit_list and print the list
    fruit_list.append("orange")
    print(f"New List: {fruit_list}")
    print("##############################")

    # 5. Add code to find where "apple" is located in fruit_list
    #  and insert "cherry" before "apple" in the list and print the list

    # to find apple's position
    apple_index = fruit_list.index("apple")

    # to insert cherry before apple
    fruit_list.insert(apple_index, "cherry")

    # print the list
    print(f"New list after the changes: {fruit_list}")
    print("*****************************")

    # 6. Add code to remove "banana" from fruit_list and print the list
    fruit_list.remove("banana")
    print(f"The new list after removing Banana: {fruit_list}")
    print()

    # 7. Add code to pop the last element from fruit_list and print the popped element and the list

    # to remove the last element
    popped_list = fruit_list.pop()

    # to print both the popped_list element and the entire list
    print(f"Popped list element: {popped_list} and the full list is: {fruit_list}\n")

    # 8. Add code to sort and print fruit_list
    fruit_list.sort()
    print(f"Sorted list: {fruit_list}")

    # 9. Add code to clear and print fruit_list
    fruit_list.clear()
    print(f"\nFull List after clearing: {fruit_list}\n")
  
main()