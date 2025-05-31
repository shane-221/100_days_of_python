from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu= Menu()
is_on = True



while is_on:
    options =  menu.get_items()
    choice =  input(f"What would you like to order? [{options}]")
    if choice =="off":
        is_on = False
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink= menu.find_drink(choice)
        
