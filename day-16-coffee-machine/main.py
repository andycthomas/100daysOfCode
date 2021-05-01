from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

makingCoffee = True

coffeeMaker = CoffeeMaker()
menu = Menu()
moneyMachine = MoneyMachine()

while makingCoffee is True:
    request = input("What would you like ? " + menu.get_items() + "\n")

    if request == "off":
        makingCoffee = False
        print("Turning off coffee machine")
    elif request == "report":
        coffeeMaker.report()
        moneyMachine.report()
    else:
        coffeeItem = menu.find_drink(request)
        if coffeeItem is not None:
            if coffeeMaker.is_resource_sufficient(coffeeItem) and moneyMachine.make_payment(coffeeItem.cost):
                coffeeMaker.make_coffee(coffeeItem)

