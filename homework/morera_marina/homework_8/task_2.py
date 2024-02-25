def fib(n):
    a, b = 0, 1
    for __ in range(n):
        yield a
        a, b = b, a + b


fib_list = list(fib(100000))
indexes = [5, 200, 1000, 100000]
for i in indexes:
    print(fib_list[i - 1])
