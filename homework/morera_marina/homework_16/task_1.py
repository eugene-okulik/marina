import csv
import mysql.connector as mysql
import creds
import os
import dotenv

dotenv.load_dotenv()
db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=creds.host,
    port=creds.port,
    database=creds.database
)

with open('../../eugene_okulik/Lesson_16/hw_data/data.csv', newline='') as csv_file:
    file_data = csv.reader(csv_file)
    data_csv = []
    for csv_row in file_data:
        data_csv.append(csv_row)

cursor = db.cursor()
cursor.execute('''SELECT DISTINCT s.name, s.second_name, g.title as group_title, b.title as book_title, 
s2.title as subject_title, l.title as lesson_title, m.value as mark_value 
FROM students s
JOIN books b
on s.id = b.taken_by_student_id
JOIN `groups` g
on s.group_id=g.id
JOIN marks m
on s.id = m.student_id
JOIN lessons l
on l.id=m.lesson_id
JOIN subjets s2
on l.subject_id = s2.id''')

data_db = cursor.fetchall()
data_as_list = [list(row) for row in data_db]
matched_data = []

for csv_row in data_csv[1:]:
    is_match = False
    for db_row in data_as_list:
        if csv_row == db_row:
            is_match = True
            break
    if not is_match:
        matched_data.append(csv_row)

print(f'Следующих данных нет в бд: {matched_data}')
