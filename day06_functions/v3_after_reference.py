import random

def build_pools():
    letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers = list("0123456789")
    symbols = list("!@#$%^&*?")
    return letters, numbers, symbols

def password_generator(n_letters, n_numbers, n_symbols):
    letters, numbers, symbols = build_pools()
    password = []

    for _ in range(n_letters):
        password.append(random.choice(letters))
    for _ in range(n_numbers):
        password.append(random.choice(numbers))
    for _ in range(n_symbols):
        password.append(random.choice(symbols))

    random.shuffle(password)
    return "".join(password)


u_letters = int(input("number of letters?\n"))
u_numbers = int(input("number of numbers?\n"))
u_symbols = int(input("number of symbols?\n"))

password = password_generator(u_letters, u_numbers, u_symbols)
print(password)