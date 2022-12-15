import random
import string

length = int(input("Enter The Length of Password: "))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

whole = lower + upper + num + symbols

temp = random.sample(whole, length)
password = "".join(temp)

print("your password is ", password)
