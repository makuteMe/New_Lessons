def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params(b = 25)
print_params(c = [1,2,3])
print_params()

values_list = [1, 'string', 10]
values_dict = {'a': 'string', 'b': 33, 'c': 10}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [[1, 2, 3], 3 ]
print(*values_list_2, 42)
