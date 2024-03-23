PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

list_new = PRICE_LIST.split('\n')

prices_dict = {}
for item in list_new:
    name, price_str = item.split()
    price = int(price_str[:-1])
    prices_dict[name] = price

print(prices_dict)
