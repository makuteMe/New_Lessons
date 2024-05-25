from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.columns import Columns

console = Console()

class House:
    def __init__(self, name, number_of_floors, initial_floor):
        self.name = name
        self.number_of_floors = number_of_floors
        self.current_floor = 0
        self.go_to(initial_floor)  # Вызов метода go_to при инициализации объекта

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            floors = list(range(1, new_floor + 1))
            self.current_floor = new_floor
            floor_panels = [Panel(str(floor), title="Этаж") for floor in floors]
            columns = Columns(floor_panels)
            console.print(columns)
        else:
            console.print(Panel("Такого этажа не существует", style="bold red"))

    def display_info(self):
        table = Table(title="Информация о доме")

        table.add_column("Атрибут", justify="right", style="cyan", no_wrap=True)
        table.add_column("Значение", style="magenta")

        table.add_row("Название", self.name)
        table.add_row("Количество этажей", str(self.number_of_floors))
        table.add_row("Текущий этаж", str(self.current_floor))

        console.print(table)


house = House('ЖК Эльбрус', 30, 5)  # Переход на этаж 5 при создании объекта


house.display_info()
house.go_to(10)  # Пример корректного перехода на этаж
house.go_to(31)  # Пример некорректного перехода на этаж
house.go_to(0)  # Пример некорректного перехода на этаж
house.display_info()
