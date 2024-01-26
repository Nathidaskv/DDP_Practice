# Code from Chat GPT

"""
Write a Python function named case_counter that counts the number of uppercase and lowercase letters in a given string.

The function should calculate and return two numbers: the count of uppercase letters and the count of lowercase letters in the string.
If there are no letters of a particular case (uppercase or lowercase) in the string, the function should return 0 for that case.
Non-alphabetic characters in the string should be ignored and not counted.
"""


def case_counter(text):
    # Initialize counts for uppercase and lowercase letters
    uppercase_count = 0
    lowercase_count = 0

    # Iterate through each character in the string
    for char in text:
        # Check if the character is an uppercase letter
        if char.isupper():
            uppercase_count += 1
        # Check if the character is a lowercase letter
        elif char.islower():
            lowercase_count += 1

    # Return the counts as a formatted string
    return f"Uppercase letters: {uppercase_count}, Lowercase letters: {lowercase_count}"


# Test cases
print(case_counter("Hello World!"))  # Expected: Uppercase letters: 2, Lowercase letters: 8
print(case_counter("PYTHON"))  # Expected: Uppercase letters: 6, Lowercase letters: 0
print(case_counter("python"))  # Expected: Uppercase letters: 0, Lowercase letters: 6
print(case_counter("1234!@#$"))  # Expected: Uppercase letters: 0, Lowercase letters: 0
