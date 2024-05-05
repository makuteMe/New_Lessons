print('--------------------task_1----------------------------')
n = int(input('Введите число '))
triangle = []
for i in range(n, 0, -1):
    star = '*'
    triangle.append(star)
    print(*triangle)

print('--------------------task_2----------------------------')

a, b, c, d = int(input('1')), int(input('2')), int(input('3')), int(input('4'))
if a <= b or a < 10 or c <= d or c < 10:
    list_ = [[a, b], [c, d]]
    list_2 = []
    for i in range(a, b + 1):
        for k in range(c, d + 1):
            list_2.append(i * k)
            print(list_2)
else:
    print('no')

print('--------------------task_3----------------------------')

n =int(input('enter the number '))
current_number = 1

for row in range(1, n + 1):
    for count in range(row):
        print(current_number, end=' ')
        current_number += 1
    print()

print('--------------------task_4----------------------------')

a, b, c = int(input('введите длину стороны 1 ')), int(input('введите длину стороны 2 ')), int(input('введите длину стороны 3 '))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Равносторонний")
    elif a == b or b == c or a == c:
        print("Равнобедренный")
    else:
        print("Разносторонний")
else:
    print("Такой треугольник не существует")


print('--------------------task_5----------------------------')

color_red = 'red'
color_blue = 'blue'
color_yellow = 'yellow'

a, b = str(input('choose color 1: red or yellow or blue ')), str(input('choose color 2: red or yellow or blue '))
if a != color_red or a != color_yellow or a != color_blue or b != color_red or b != color_yellow or b != color_blue:
    if a == color_red and b == color_blue or a == color_blue and b == color_red:
        print('violet')
    if a == color_red and b == color_yellow or b == color_red and a == color_yellow:
        print('orange')
    if a == color_blue and b == color_yellow or b == color_blue and a == color_yellow:
        print('green')
    if a == b:
        print('nice joke')
else:
    print('Ooops, wrong input')