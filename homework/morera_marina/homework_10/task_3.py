def decor(func):
    def wrapper(*args):
        first = args[0]
        second = args[1]
        if first == second:
            return func(first, second, '+')
        if first > second:
            return func(second, first, '-')
        if first < second:
            return func(first, second, '/')
        if first < 0 or second < 0:
            return func(first, second, '*')

    return wrapper


@decor
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == "-":
        return first - second
    elif operation == '/':
        return first / second
    elif operation == "*":
        return first * second


first_numb = int(input("Введите первое число "))
second_numb = int(input("Введите второе число "))
operation_any = 'any'

result = calc(first_numb, second_numb, operation_any)
print(result)
