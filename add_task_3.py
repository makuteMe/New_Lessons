data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

counter = 0

def process_element(element):
    global counter
    if isinstance(element, int):  # Если элемент - целое число
        counter += element
    elif isinstance(element, str):  # Если элемент - строка
        counter += len(element)
    elif isinstance(element, dict):  # Если элемент - словарь
        for key, value in element.items():
            process_element(key)
            process_element(value)
    elif isinstance(element, (list, tuple, set)):  # Если элемент - список, кортеж или множество
        for item in element:
            process_element(item)

for item in data_structure:
    process_element(item)

print(counter)  # Выводит общую сумму


process_element(data_structure)