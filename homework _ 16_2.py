from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.columns import Columns
from rich.align import Align

console = Console()


class Home:
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        panel_content = Align.center(str(floors))
        panel = Panel(panel_content, title='Кол-во этажей', width=10)
        console.print(panel)


new = Home()
new.setNewNumberOfFloors(10)
new.setNewNumberOfFloors(20)
