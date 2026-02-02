import random

letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
symbols = list("?!@#$%^&*()")

u_letters = int(input("number of letters?\n"))
u_numbers = int(input("number of numbers?\n"))
u_symbols = int(input("number of symbols?\n"))

password_temp = []

for _ in range(u_letters):
    password_temp.append(random.choice(letters))

for _ in range(u_numbers):
    password_temp.append(random.choice(numbers))

for _ in range(u_symbols):
    password_temp.append(random.choice(symbols))


print(password_temp)    # To check if shuffle works
random.shuffle(password_temp)

password = "".join(password_temp)
print(password)