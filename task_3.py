immutable_var = ('string', 1, [2, 4, 'hello'])
# immutable_var[0] = 3 # пытаюсь изменить элемент кортежа (tuple), что невозможно, так как кортежи в Python неизменяемы
print(immutable_var)

mutable_list = list(immutable_var)
mutable_list[0] = 67
print(mutable_list)