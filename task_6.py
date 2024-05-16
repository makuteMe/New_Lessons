autos = ["BMW", "MB", "LADA", "KIA", "HONDA", 'HAVAL']

def count_autos():
    count_me = 0
    global autos
    for count in autos:
        print('Я езжу на автомабиле марки:', count)
        count_me += 10
        print(count_me)



count_autos()