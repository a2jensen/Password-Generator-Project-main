import random

print("Your password: ")

# This variable storess all possible values that can be put in our password
chars = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"

# Make our password variable
password = ''

# Since this password will be 16 characters long, range is set to 16
# A random value will be added to password from the chars variable
for x in range(16):
    password += random.choice(chars)

# Prints out password that was randomly created
print(password)