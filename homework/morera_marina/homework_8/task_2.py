def fib(n):
    a, b = 0, 1
    for __ in range(n):
        yield a
        a, b = b, a + b


count = 1
indexes = [5, 200, 1000, 100000]
for i in fib(100000):
    if count in indexes:
        print(i)
    count += 1
