from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.columns import Columns


console = Console()
class Home:
    def __init__(self):

        self.numberOfFloors = 0


    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        table = Table(title='Информация о доме')
        table.add_column('Кол-во этажей', justify='center')
        table.add_row(str(floors))
        console.print(table)

new = Home()
new.setNewNumberOfFloors(10)
new.setNewNumberOfFloors(20)