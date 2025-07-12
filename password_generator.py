# arr = [1, 2, 3, 4]
# prefit_sum = 0

# for i in range(len(arr)):
#     arr[i] += prefit_sum
#     prefit_sum = arr[i]

# print(arr)

import random
import string

def password_generator(
    length=12,
    uppercase=True,
    lowercase=True,
    digits=True,
    special_chars=True,
) -> str | None:
    characters = ""

    if uppercase:
        characters += string.ascii_uppercase

    if lowercase:
        characters += string.ascii_lowercase

    if digits:
        characters += string.digits

    if special_chars:
        characters += string.punctuation

    if not characters:
        print("Error: At least one character type must be selected")
        return None

    password = "".join(
        random.choice(characters) for _ in range(length)
    )  # list comprehension

    return password


print("Welcome to the Password Generator")
print("You can customize your password by selecting the character types to include")

pass_length = int(input("Enter the length of the password: "))

include_uppercase = input("Include uppercase letters (y/n): ").lower() in ("y", "yes")
include_lowercase = input("Include lowercase letters (y/n): ").lower() in ("y", "yes")
include_digits = input("Include digits letters (y/n): ").lower() in ("y", "yes")
include_special_chars = input("Include special characters letters (y/n): ").lower() in (
    "y",
    "yes",
)

password_generator = password_generator(
    length=pass_length,
    uppercase=include_uppercase,
    lowercase=include_lowercase,
    digits=include_digits,
    special_chars=include_special_chars,
)

if password_generator:
    print("Generated Password: ", password_generator)
else:
    print("No password generated. Try again")



