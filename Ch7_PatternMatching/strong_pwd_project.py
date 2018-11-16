import re

counter = 0

print('Please put a strong password\n')

while counter < 1:
    password = input(">")
    if len(password) < 8:
        print("Invalid. Your pw must have at least 8 characters ")
    elif not re.search(r'[a-z]', password):
        print("Invalid. Your pw must have lowercase characters")
    elif not re.search(r'[A-Z]', password):
        print("Invalid. Your pw must have capital characters")
    elif not re.search(r'[0-9]', password):
        print("Invalid. Make sure your password includes at least one digit")
    else:
        print("This is a valid password")
        counter += 1
