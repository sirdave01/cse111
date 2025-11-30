# random_numbers.py
# A program that demonstrates default parameters and pass-by-reference
# by appending random numbers and random words to lists.

import random

# List of fun, bird-themed words for the enhancement
WORDS = [
    "parrot", "finch", "canary", "cockatoo", "budgie",
    "sparrow", "hawk", "eagle", "owl", "penguin",
    "flamingo", "hummingbird", "robin", "cardinal", "toucan"
]

def main():
    # --- Core Requirements ---
    numbers = []                     # Start with an empty list
    print("Original numbers list:", numbers)

    # First call: uses default quantity = 1
    append_random_numbers(numbers)
    print("After adding 1 random number:", numbers)

    # Second call: specify quantity = 5
    append_random_numbers(numbers, 5)
    print("After adding 5 more random numbers:", numbers)

    # --- Enhancement 1 & 2: Random Words ---
    print("\n--- Now with random words! ---")
    words = []
    print("Original words list:", words)

    # Add 3 random words
    append_random_words(words, 3)
    print("After adding 3 random words:", words)

    # Add 2 more (using default quantity = 1 twice would also work)
    append_random_words(words, 2)
    print("After adding 2 more random words:", words)

    # --- Creative Enhancement ---
    print("\n" + "="*50)
    print("BONUS: Let's make a fun mixed list!")
    mixed = []
    append_random_numbers(mixed, 3)
    append_random_words(mixed, 3)
    random.shuffle(mixed)  # Shuffle for extra fun!
    print("Your random mixed list:", mixed)
    print("="*50)


def append_random_numbers(numbers_list, quantity=1):
    """
    Appends 'quantity' random integers (1–100) to numbers_list.
    Demonstrates pass-by-reference: the original list is modified.
    """
    for _ in range(quantity):
        rand_num = random.randint(1, 100)
        numbers_list.append(rand_num)


def append_random_words(words_list, quantity=1):
    """
    Appends 'quantity' random words from the WORDS list to words_list.
    """
    for _ in range(quantity):
        word = random.choice(WORDS)
        words_list.append(word)


# Run the program
if __name__ == "__main__":
    # Optional: Seed for reproducible results during testing
    # random.seed(42)
    main()