a = "результат операции: 42"
b = "результат операции: 514"
c = "результат работы программы: 9"

result_a = a.index(':')
result_b = b.index(':')
result_c = c.index(':')
new_a = int(a[result_a+1:])
new_b = int(b[result_b+1:])
new_c = int(c[result_c+1:])
print(new_a + 10, new_b + 10, new_c + 10)
