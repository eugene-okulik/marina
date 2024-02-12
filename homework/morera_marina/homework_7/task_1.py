number = 8

guest = int(input("Угадай цифру которую я загадал: "))
while number != guest:
    guest = int(input("Попробуйте снова: "))
print("Поздравляю! Вы угадали!")
