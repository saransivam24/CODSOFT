import random
import string

characters = string.ascii_uppercase + string.ascii_lowercase + string.punctuation + string.digits

length = int(input("Enter password length: "))

password = ""
for i in range(length):
    password = password + random.choice(characters)

print("Generated Password:", password)
