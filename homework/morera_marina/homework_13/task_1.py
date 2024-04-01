import os
import datetime

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
hw_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')


def read_file():
    with open(hw_file_path, 'r', encoding='utf-8') as data_file:
        for line in data_file.readlines():
            yield line


with open(hw_file_path, 'a', encoding='utf-8') as new_file:
    for i, data_line in enumerate(read_file()):
        new_data_string = data_line[3:29]
        new_data = datetime.datetime.strptime(new_data_string, '%Y-%m-%d %H:%M:%S.%f')
        if i == 0:
            week_later = new_data + datetime.timedelta(weeks=1)
            print(week_later)
        elif i == 1:
            print("День недели", new_data.weekday() + 1)
        elif i == 2:
            today_datetime = datetime.datetime.today()
            today_date = today_datetime.date()
            new_data_date = new_data.date()
            difference = today_date - new_data_date
            print(f'Дата {new_data.date()} была {difference.days} дней назад')
