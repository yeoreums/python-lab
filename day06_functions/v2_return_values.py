import random

# one function that builds the character pool
def letter_generator():
    letters = list("abcdefghijklmnopqrstuvwxyzQWERTYUIOPLKJHGFDSAZXCVBNM")

    return letters


def number_generator():
    numbers = list("1234567890")
    
    return numbers


def symbol_generator():
    symbols = list("!@#$%^&*?")
    
    return symbols


# one function that generates the password
def password_generator(num1, num2, num3):
    password = []
    for i in range(num1):
        password.append(random.choice(letter_generator()))
    for i in range(num2):
        password.append(random.choice(number_generator()))
    for i in range(num3):
        password.append(random.choice(symbol_generator()))
    
    return password


# one function that returns the final string
def final_password(password):
    random.shuffle(password)    
    print("".join(password))


u_lettters = int(input("number of letters?\n"))
u_numbers = int(input("number of numbers?\n"))
u_symbols = int(input("number of symbols?\n"))

password = password_generator(u_lettters, u_numbers, u_symbols)
final_password(password)