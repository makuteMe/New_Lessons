
class Building:
    def __init__(self, building_type, number_of_floors):
        self.building_type = str(building_type)
        self.number_of_floors = int(number_of_floors)
        self.display_data()

    def display_data(self):
        print(self.building_type, self.number_of_floors)

    def __eq__(self, other):
        return (self.building_type == other.building_type
                and self.number_of_floors == other.number_of_floors)


nomer_1 = Building('Частный дом', 2)
nomer_2 = Building('Многоэтажный дом', 15)

print(nomer_1 == nomer_2)