class Flower:

    def __init__(self, kind, color, height, price, lifetime_days):
        self.kind = kind
        self.color = color
        self.height = height
        self.price = price
        self.lifetime_days = lifetime_days


class Rose(Flower):
    def __init__(self, color, height, price, lifetime_days):
        super().__init__("Роза", color, height, price, lifetime_days)


class Romashka(Flower):
    def __init__(self, color, height, price, lifetime_days):
        super().__init__("Ромашка", color, height, price, lifetime_days)


class Lily(Flower):
    def __init__(self, color, height, price, lifetime_days):
        super().__init__("Лилия", color, height, price, lifetime_days)


rose = Rose("красный", 14, 23, 4)
romashka = Romashka("белый", 17, 25, 2)
lily = Lily("желтый", 10, 17, 3)


class Bouquet():
    def __init__(self, flowers_list, bouquet_name):
        self.flowers_list = flowers_list
        self.name = bouquet_name

    def total_price(self):
        total = 0
        for i in self.flowers_list:
            total += i.price
        return total

    def life(self):
        aver = 0
        for i in self.flowers_list:
            aver += i.lifetime_days
        return aver / len(self.flowers_list)

    def sort_by_freshness(self):
        return sorted(self.flowers_list, key=lambda x: x.lifetime_days)

    def sort_by_color(self):
        return sorted(self.flowers_list, key=lambda x: x.color)

    def sort_by_height(self):
        return sorted(self.flowers_list, key=lambda x: x.height)

    def sort_by_price(self):
        return sorted(self.flowers_list, key=lambda x: x.price)

    def search_by_name(self, name):
        return list(filter(lambda x: x.kind == name, self.flowers_list))


bouquet = Bouquet([rose, romashka, lily], "Полянка")
sorted_flowers = bouquet.sort_by_freshness()
sorted_color = bouquet.sort_by_color()
sorted_height = bouquet.sort_by_height()
sorted_price = bouquet.sort_by_price()
search_by_name = bouquet.search_by_name('Роза')

print(bouquet.total_price())
print(bouquet.life())
for flower in sorted_flowers:
    print(f'У цветка {flower.kind} время жизни: {flower.lifetime_days} дней')
for flower in sorted_color:
    print(f'У букета {bouquet.name} цветок {flower.kind} цвета {flower.color}')
for flower in sorted_height:
    print(f'Длина цветка {flower.kind}: {flower.height}')
for flower in sorted_price:
    print(f'Цена одного цветка {flower.kind}: {flower.price}')
for flower in search_by_name:
    print(f'В букете есть {flower.kind}: {flower.price}')
