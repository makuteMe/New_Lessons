grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(list(students))
avg_grade = []

for element in grades:
    for sub_element in element:
        sub_element = sum(element) / len(element)
    avg_grade.append(sub_element)
#print(avg_grade)

dict_new = dict(zip(students, avg_grade))
print(dict_new)