from math import sqrt

x = int(input("Введите первый катет: "))
y = int(input("Введите второй катет: "))
hypotenyza = sqrt((x**2)+(y**2))
S = (x*hypotenyza)/2 #Либо можно было по формуле 0.5 * x * y
print("Гипотенуза:",hypotenyza, "\nПлощадь:",S)

