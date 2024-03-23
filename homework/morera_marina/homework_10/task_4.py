PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''


def price_list(p_list):
    list_new = p_list.split('\n')
    for item in list_new:
        name, price_str = item.split()
        price = int(price_str[:-1])
        yield name, price


print(dict(list(price_list(PRICE_LIST))))
