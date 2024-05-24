from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.prompt import Confirm, IntPrompt
from rich.columns import Columns

console = Console()

commands = {1: 'Добавить товар',
            2: 'Что в корзине',
            3: 'Очистить корзину',
            4: 'Создать чек',
            5: 'Завершить работу'}



def start_menu():
    menu_table = Table(title="Касса.ру", title_justify="left")
    menu_table.add_column("Выбери одну из операций!", justify="left")
    for key, value in commands.items():
        menu_table.add_row(f"{key}. {value}")
    console.print(menu_table)


shop_cart = {}
def add_to_cart():
    supply = input('Что покупаем ')
    price = int(input('Сколько стоит '))
    if supply not in shop_cart:
        shop_cart.setdefault(supply, price)
        panel_1 = Panel(f'{supply}', title='Ваши товары')
        panel_2 = Panel(f'{price}', title='Цена')
        columns = Columns([panel_1, panel_2])
        console.print('Вы это сделали', columns)
    else:
        print('Остановитесь! Не будьте обжорой, этот товар уже в корзине')

def cart_details():
    if not shop_cart:
        console.print('Корзина пуста')
    else:
        cart_table = Table(title="Твои продукты", show_header=True)
        cart_table.add_column("Твои продукты")
        cart_table.add_column("Цена продуктов", justify="right")
        for item, price in shop_cart.items():
            cart_table.add_row(item, f"${price}")
        console.print(cart_table)
def clear_cart():
    shop_cart.clear()
    console.print('Корзина очищена')
def create_bill():
    if not shop_cart:
        console.print('Корзина пуста. Нет товаров для создания чека.', style="yellow")
    else:
        total = sum(shop_cart.values())
        receipt_text = (
            f"Большое спасибо за покупку!\n"
            f"Будем ждать вас еще!\n\n"
            f"-----------------------------\n"
            f"Кол-во товаров: {len(shop_cart)}\n"
            f"Общая стоимость: ${total}\n"
            f"Покупатель: Maxim Kutepov\n"
            f"Адрес магазина: Moscow"
        )
        receipt_panel = Panel(receipt_text, title="Чек", title_align="center")
        console.print(receipt_panel)
def end_session():
    pass


while True:
    start_menu()
    user_input = int(input('1-5 '))
    if user_input == 1:
        add_to_cart()
    elif user_input == 2:
        cart_details()
    elif user_input == 3:
        clear_cart()
    elif user_input == 4:
        create_bill()
    elif user_input == 5:
        if Confirm.ask("Вы действительно хотите выйти?"):
            console.print('Работа завершена. До свидания!')
            break
    else:
        console.print('Неверная команда, попробуйте снова.')

