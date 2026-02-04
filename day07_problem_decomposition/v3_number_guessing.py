import random

set_number = random.randint(1, 100)

user_life = 5


while user_life != 0:
    user_input = int(input("guess the number from 1 to 100\n"))
    if user_input < set_number:
        print("Higher!")
        user_life -= 1
    elif user_input > set_number:
        print("Lower!")
        user_life -= 1
    else:
        print("You win!")
        break

if user_life == 0:
    print("You lose!")

