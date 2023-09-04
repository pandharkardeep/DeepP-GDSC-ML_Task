import random
import string

def generate_password(length, use_uppercase, use_digits, use_special_chars):
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase if use_uppercase else ''
    digit_chars = string.digits if use_digits else ''
    special_chars = '!@#$%^&*()_+[]{}|;:,.<>?/' if use_special_chars else ''

    all_chars = lowercase_chars + uppercase_chars + digit_chars + special_chars

    
    if length < 4 :
        raise ValueError("Password should be atleast of 4 chars length")

    password = ''
    for _ in range(length):
        password += random.choice(all_chars)

    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

length = int(input('Enter length of your password: '))
use_uppercase = bool(int(input('Enter 1 if you want to use uppercase else 0: ')))
print(use_uppercase)
use_digits = bool(int(input('Enter 1 if you want to use digits else 0: ')))
use_special_chars = bool(int(input('Enter 1 if you want to use special characters else 0: ')))
password = generate_password(length, use_uppercase, use_digits, use_special_chars)
print("Generated Password:", password)
