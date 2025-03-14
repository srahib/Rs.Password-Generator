#password generated

import random
import string

def generated_password(length = 12):
    character = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(character) for _ in range (length))
    return password

length = int(input("Enter the length of your desired password:"))
password = generated_password(length)
print("your desired generated_password:", password)   