import sys
import string


def character_sum(text):
    """
    Function cheacking in input None giving to user write own input
    if input non None it will count summery of upper, lower, punctuation,
    digit, and spaces
    """
    if text is None or len(text) == 0:
        text = input("What is the text to count?\n")

    upper_count = sum(1 for char in text if char.isupper())
    lower_count = sum(1 for char in text if char.islower())
    punctuation_count = sum(1 for char in text if char in string.punctuation)
    digit_count = sum(1 for char in text if char.isdigit())
    space_count = sum(1 for char in text if char.isspace())

    total_characters = len(text)

    print(f"The text contains {total_characters} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punctuation_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")


if __name__ == "__main__":
    assert len(sys.argv) > 2, "AssertionError: argument not provided"
    character_sum(sys.argv[1])
