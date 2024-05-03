grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = list(students)
students_list.sort()
print(students_list)
avg_grades = []
for ocenki in grades:
    avg_grades.append(sum(ocenki) / len(ocenki))
print(avg_grades)
personal_avg_grade = dict(zip(students_list, avg_grades))
print(personal_avg_grade)
print('----------------пример автоматизации расчета среднего бала-------------')
list_2 = []
list_3 = []
list_ = tuple(input('Введите оценки студента, без пробелов подряд '))
for i in list_:
    list_2.append(int(i))
name = input('Введите имя студента ')
list_3.append(sum(list_2) / len(list_2))
print('Средний бал ', list_3)
print('Студент ', name)