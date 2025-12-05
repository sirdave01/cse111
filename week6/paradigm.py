# Example 1 - procedural programming
# A Python procedural program for computing the average is shown in example 1

def main():
    numbers = [87, 95, 72, 92, 95, 88, 84]
    total = 0
    for x in numbers:
        total += x
    average = total / len(numbers)
    print(f"average: {average:.2f}")
# Call main to start this program.
if __name__ == "__main__":
    main()


# -- Example 2
# Example 2 contains SQL code that causes the computer to compute the average of a column of numbers

# SELECT AVG(numbers) FROM table;


# Example 3 - functional programming

from functools import reduce
def main():
    numbers = [87, 95, 72, 92, 95, 88, 84]
    func_add = lambda a, b: a + b
    total = reduce(func_add, numbers)
    average =  total / len(numbers)
    print(f"average: {average:.2f}")
# Call main to start this program.
if __name__ == "__main__":
    main()




# Example 4
# The code in example 4 uses the dot operator (.) to call the append method
def main():
    numbers = [87, 95, 72, 92, 95, 88, 84]
    numbers.append(78)
    numbers.append(72)
    print(numbers)
# Call main to start this program.
if __name__ == "__main__":
    main()


# Creating objects, for example:

# obj = datetime.now()


# Accessing the attributes of an object using the dot operator (.), for example:

# year = obj.year


# Calling the methods of an object using the dot operator (.), for example:

# new_obj = obj.replace(year=2035)
# day_of_week = obj.weekday()