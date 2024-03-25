class Book:
    material = 'бумага'
    text = 'yes'
    flag = True

    def __init__(self, name_book, author, number_page, isbn, flag):
        self.name_book = name_book
        self.author = author
        self.number_page = number_page
        self.isbn = isbn
        self.flag = flag


books = [Book('Идиот', 'Достоевкий', '500', '-', False),
         Book('Сияние', 'Кинг', '642', '-', True),
         Book('Мастер и Маргарита', 'Булгаков', '153', '-', False),
         Book('Мертвые души', 'Гоголь', '541', '-', False),
         Book('Палата', 'Чехов', '324', '-', False)]

for i in books:
    if i.flag:
        print(
            f'Название: {i.name_book}, Автор: {i.author}, страниц: {i.number_page}, '
            f'материал: {i.material}, зарезервирована')
    else:
        print(f'Название: {i.name_book}, Автор: {i.author}, страниц: {i.number_page}, '
              f'материал: {i.material}')


class SchoolBook(Book):
    def __init__(self, name_book, author, number_page, isbn, subject, scholl_class, any_task, flag):
        super().__init__(name_book, author, number_page, isbn, flag)
        self.subject = subject
        self.school_class = scholl_class
        self.any_task = any_task


scholl_books = [SchoolBook('Алгебра', 'Иванов', '200', '-', 'Математика', '9',
                           True, False),
                SchoolBook('Геометрия', 'Иванов', '312', '-', 'Математика', '9',
                           True, True),
                SchoolBook('География 5 ', 'Александров', '142', '-', 'География', '9',
                           True, False),
                SchoolBook('Русский язык', 'Михайлов', '412', '-', 'Русский', '9',
                           True, False),
                SchoolBook('Физра', 'Петров', '324', '-', 'Физкультура', '9',
                           True, True)]
for i in scholl_books:
    if i.flag:
        print(
            f'Название: {i.name_book}, Автор: {i.author}, страниц: {i.number_page}, '
            f'предмет: {i.subject}, класс: {i.school_class}, зарезервирована')
    else:
        print(f'Название: {i.name_book}, Автор: {i.author}, страниц: {i.number_page}, '
              f'предмет: {i.subject}, класс: {i.school_class}')
