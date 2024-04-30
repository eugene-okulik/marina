import os

# file_path = 'C:/Users/9mari/projects/marina/homework/eugene_okulik/data/logs'
file_path = input('Введите полный путь к папке, в которой лежат файлы с логами')
dir_list = os.listdir(file_path)
print(dir_list)
text_file = input('Введите текст который нужно найти в файлах')
# text_file = 'hikari.pool.HikariProxyPreparedStatement.executeQuery(HikariProxyPreparedStatement.java)'

for file_name in dir_list:
    file_text = os.path.join(file_path, file_name)
    with open(file_text, 'r') as file:
        lines = file.readlines()
        line_number = 0
        for line in lines:
            line_number += 1
            if text_file in line:
                print(f'Найдено в файле: {file_name}. Порядковый номер строки файла {line_number}')
                index = line.find(text_file)
                start = max(0, index - 5)
                end = min(len(line), index + len(text_file) + 5)
                print(line[start:end])
