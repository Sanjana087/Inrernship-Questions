import random
import string
def password_generator(length):
    character = string.ascii_letters + string.digits
    password = "".join(random.choice(character)for i in range (length))
    return password
length = int(input("Enter the length of the password:"))
password = password_generator(length)
print(password)