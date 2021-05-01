from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

makingCoffee = True

coffeeMaker = CoffeeMaker ()
menu = Menu()

while makingCoffee is True:
    request = input("What would you like ? " + menu.get_items() + "\n")

    if request == "off":
        makingCoffee = False
        print("Turning off coffee machine")
    elif request == "report":
        coffeeMaker.report()
    else:
        print("Do something!")
