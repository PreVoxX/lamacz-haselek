import random
import string
def wygeneruj_hasło(min_lengh, numbers=True, special_characters=True): 

    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    character = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meets_criteria = False
    has_numbers = False
    has_special = False

    while not meets_criteria or len(pwd)


wygeneruj_hasło(10)