import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)
cursor = db.cursor()
# Вставляем данные в таблицу students
cursor.execute("INSERT INTO students (name, second_name) VALUES ('Marina', 'Pitonova')")
student_id = cursor.lastrowid
# Выбираем данные из таблицы students
cursor.execute(f'SELECT * from students where id = {student_id}')
print(cursor.fetchone())
# сохраняем изменения
db.commit()
# Вставляем данные в таблицу books
query = 'INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)'
values = [('Biology', student_id),
          ('Python', student_id)]
cursor.executemany(query, values)
# сохраняем изменения
db.commit()
# Выводим данные из таблицы books
cursor.execute(f'SELECT * from books where taken_by_student_id = {student_id}')
print(cursor.fetchall())
# Вставляем данные в таблицу groups
cursor.execute("INSERT INTO `groups` (groups.title) VALUES ('Питон для продвинутых')")
group_id = cursor.lastrowid
# сохраняем изменения
db.commit()
# Выводим данные из таблицы groups
cursor.execute(f'SELECT * from `groups` where id = {group_id}')
print(cursor.fetchall())
# Обновляем данные в таблице students
cursor.execute(f"UPDATE students SET group_id = {group_id} where id = {student_id}")
# сохраняем изменения
db.commit()
# Выводим обновленные данные из таблицы students
cursor.execute(f'SELECT * from students where id = {student_id}')
print(cursor.fetchall())
# Вставляем данные в таблицу subjects
query = 'INSERT INTO subjets (title) VALUES (%s)'
values = [('Мастер-класс Питон',),
          ('Питон новый',)]
# Получаем ID только что вставленных записей
subject_ids = []
for value in values:
    cursor.execute(query, value)
    db.commit()
    subject_ids.append(cursor.lastrowid)
# Проверяем, что IDs корректно подставлены
for subject_id in subject_ids:
    cursor.execute(f'SELECT * FROM subjets WHERE id = {subject_id}')
    print(cursor.fetchall())
# Вставляем данные в таблицу lessons
query = 'INSERT INTO lessons (title, subject_id) VALUES (%s, %s)'
values = [('Вводное занятие', subject_ids[0]),
          ('Контрольная', subject_ids[1])
          ]
# Получаем ID только что вставленных записей
lesson_ids = []
for value in values:
    cursor.execute(query, value)
    db.commit()
    lesson_ids.append(cursor.lastrowid)
# Получаем ID только что вставленных записей
for lesson_id in lesson_ids:
    cursor.execute(f'SELECT * FROM lessons WHERE id = {lesson_id}')
    print(cursor.fetchall())
# Вставляем данные в таблицу marks
query = 'INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)'
values = [(5, lesson_ids[0], student_id),
          (4, lesson_ids[1], student_id)]
cursor.executemany(query, values)
# сохраняем изменения
db.commit()
cursor.execute(f'select * FROM marks where student_id = {student_id}')
print(cursor.fetchall())
cursor.execute(f'select * FROM books where taken_by_student_id = {student_id}')
print(cursor.fetchall())
cursor = db.cursor(dictionary=True)
query = f'''SELECT DISTINCT s.name, s.second_name, g.title, b.title, s2.title, l.title, m.value
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
on l.subject_id = s2.id
where s.id= %s'''
cursor.execute(query, (student_id,))
print(cursor.fetchall())
db.close()
