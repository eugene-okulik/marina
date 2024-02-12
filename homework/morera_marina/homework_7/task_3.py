a = "результат операции: 42"
b = "результат операции: 514"
c = "результат работы программы: 9"


def calc(numbers):
    for i in numbers:
        new = i.split(':')
        value = int(new[1]) + 10
        print(value)


calc([a])
calc([b])
calc([c])
