def calc(func):
    def wrapper(first, second):
        operation = func(first, second)
        if operation == '+':
            return first + second
        elif operation == "-":
            return second - first
        elif operation == '/':
            return first / second
        elif operation == "*":
            return first * second

    return wrapper


@calc
def task(first, second):
    if first == second:
        return '+'
    elif first > second:
        return '-'
    elif first < second:
        return '/'
    elif first < 0 or second < 0:
        return '*'


first = int(input("Введите первое число"))
second = int(input("Введите второе число"))

result = task(first, second)
print(result)
