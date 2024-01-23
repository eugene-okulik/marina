a = "результат операции: 42"
b = "результат операции: 514"
c = "результат работы программы: 9"

result_a = a.index('42')
result_b = b.index('514')
result_c = c.index('9')
new_a = int((a[result_a:]))
new_b = int((b[result_b:]))
new_c = int((c[result_c:]))
print(new_a + 10, new_b + 10, new_c + 10)
