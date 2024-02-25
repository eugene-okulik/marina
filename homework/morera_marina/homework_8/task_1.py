from random import random, choice

salary = int(input("Введите свою заработную плату: "))
bonus = choice([True, False])

if bonus:
    print(f"{salary}, {bonus} - '${salary + (int(random() * 100))}'")
else:
    print(f"{salary}, {bonus} - '${salary}'")
