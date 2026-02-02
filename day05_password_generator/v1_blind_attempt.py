import random

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
            "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lower_letters = []
for i in letters:
    if i.isupper():
        lower_letters.append(i.lower())
# print(lower_letters)
symbols = ["!", "@", "#", "$", "%", "^", "&", "*"]
numbers = []
for i in range(1, 11):
    numbers.append(str(i))
# print(numbers)
# print(random.choice(letters))
password = []

user_letters = int(input("number of letters?"))
user_numbers = int(input("number of numbers?"))
user_symbols = int(input("number of symbols?"))

for j in range(user_letters):
    password.append(random.choice(letters))

for j in range(user_numbers):
    password.append(random.choice(numbers))

for j in range(user_symbols):
    password.append(random.choice(symbols))

password_secured = []
for i in password:
    password_secured.append(random.choice(password))
print("".join(password))
print("".join(password_secured))
