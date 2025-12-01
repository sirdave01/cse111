# Background
# You are a junior software developer working for a cellular phone service 
# provider. Your company employs hundreds of workers 
# ranging from customer support to cell tower engineers. 
# The security team has recently discovered a breach of security 
# that they attribute to users using easy to guess passwords. 
# To help train users to create better passwords, 
# management has asked your team to create a password strength checker. 
# This tool will allow employees to get feedback on the strength of their passwords.

# to create the program for this project, I will first list the S.I for the complexity of passwords as lists in a global variable
# and follow it up by creating word_in_file function that takes 3 parameters, word_has_character that takes 2 parameters, 
# word_complexity that takes one parameter, password_strength that takes 3 parameters and main program

# Character lists for complexity calculation
LOWER = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
SPECIAL = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "\"", "\"", ",", ".", "<", ">", "?", "/", "`", "~"]

def word_in_file(word, filename, case_sensitive=False):
    """Checks if the given word exists in the specified file (returns bool, not list)."""
    # Open the file in read mode with UTF-8 encoding to handle international characters properly.
    with open(filename, 'r', encoding="utf-8") as file:
        # Iterate through each line in the file.
        for line in file:
            # Remove trailing newline or whitespace from the line using strip().
            file_word = line.strip()
            # Check for match: case-sensitive if True, otherwise case-insensitive.
            if case_sensitive:
                if word == file_word:
                    return True # Word found, return True.
            else:
                if word.lower() == file_word.lower():
                    return True # Word found (ignoring case), return True.
                
    # If no match found after checking all lines, return False.
    return False

def word_has_character(word, character_list):
    """returns True if any character from character_list is in password."""
    # Loop through each character in the input word.
    for char in word:
        # If the current character is in the character_list, return True immediately.
        if char in character_list:
            return True
    # If no characters match, return False.
    return False

def word_complexity(word):
    """returns the complexity score of the password based on character types."""
    # Initialize score to 0.
    score = 0
    # Check for lowercase letters and increment score if present.
    if word_has_character(word, LOWER):
        score += 1
    # Check for uppercase letters and increment score if present.
    if word_has_character(word, UPPER):
        score += 1
    # Check for digits and increment score if present.
    if word_has_character(word, DIGITS):
        score += 1
    # Check for special characters and increment score if present.
    if word_has_character(word, SPECIAL):
        score += 1
    # Return the final complexity score.
    return score

def password_strength(password, min_length=10, strong_length=16):
    """returns the strength of the password as an int (0-5); prints required messages."""
    # Check if password is a dictionary word (case-insensitive).
    if word_in_file(password, 'wordlist.txt', case_sensitive=False):
        print("'Password is a dictionary word and is not secure.")
        return 0  # Strength 0 for dictionary word.
    
    # Check if password is a known common password (case-sensitive).
    if word_in_file(password, 'toppasswords.txt', case_sensitive=True):
        print("Password is a commonly used password and is not secure.")
        return 0  # Strength 0 for common password.
    
    # Check if password is too short.
    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1  # Strength 1 for short password.
    
    # Check if password is long enough to be considered strong regardless of complexity.
    if len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5  # Strength 5 for long password.
    
    # For medium-length passwords, calculate based on complexity (no message).
    complexity = word_complexity(password)
    strength = 1 + complexity  # 1-5
    return strength

# Main Program
def main():
    """Main function that runs the interactive loop for testing passwords.
    Prompts user for input until 'q' or 'Q' is entered to quit.
    Calls password_strength and reports the result."""

    # Infinite loop to keep prompting for passwords.
    while True:
        # get the user input and strip whitespace
        user_input = input("Enter a password to check its strength (or 'q' to quit): ").strip()
        # check if user wants to quit (case-insensitive)
        if user_input.lower() == 'q':
            print("Exiting the password strength checker. Goodbye!")
            break
        # evaluate the password strength
        strength = password_strength(user_input)
        # display the strength result
        print(f"Password Strength: {strength}\n")

# Start the program by calling the main function
if __name__ == "__main__":
    main()