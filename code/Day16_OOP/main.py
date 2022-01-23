from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
on = True

while on:
    option = input(f"What would you like? ({menu.get_items()}): ")
    if option == "report":
        coffee_maker.report()
        money_machine.report()
    elif option == "off":
        on = False
    else:
        order = menu.find_drink(option)
        if order is None:
            print("That option is not available.")
        if coffee_maker.is_resource_sufficient(order) and money_machine.make_payment(order.cost):
                coffee_maker.make_coffee(order)
