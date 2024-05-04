def print_params(name):
    print("Hello ", name * 2, sep='\n')
name = 'Max'
print_params(name)

def print_params_2():
    print(sep='\n')
    print('Hello' * 2)

print_params_2()