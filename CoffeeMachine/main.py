MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins = {
    "quarters": 1,
    "dimes": 1,
    "nickles": 1,
    "pennies": 1
}


def get_money():
    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01
    money = 0.0

    num_quarters = int(input("How many quarters ? "))
    num_dimes = int(input("how many dimes ?"))
    num_nickles = int(input("how many nickles ?"))
    num_pennies = int(input("how many pennies ?"))

    money = num_quarters * quarters + num_dimes * dimes + num_nickles * nickles + num_pennies * pennies

    return money


def turnoff():
    print("Turn off")


def check_resource(name, amount):
    available_resource = resources[name]
    if available_resource >= amount:
        resources[name] -= amount
        return True
    else:
        print("Not enough " + name + " available to make coffee \n")


def make_coffee(coffee_type):
    ingredients = MENU[coffee_type]['ingredients']

    if 'milk' in ingredients:
        check_resource('milk', ingredients['milk'])

    check_resource('coffee', ingredients['coffee'])
    check_resource('water', ingredients['water'])


def order_coffee(coffee):
    money = get_money()
    cost = MENU[coffee]['cost']

    if money < cost:
        print("Not enough money for coffee")
    else:
        change = money - cost
        print("Change = " + str(change) + "\n")
        make_coffee(coffee)


def report():
    print("do report \n")


userInput = ""
makingCoffee = True

while makingCoffee is True:
    request = input("What would you like ? (espresso, latte, cappuccino ) ")

    if request == "off":
        makingCoffee = False
        print("Turning off coffee machine")
    elif request == "espresso":
        order_coffee('espresso')
    elif request == "latte":
        order_coffee('latte')
    elif request == "cappuccino":
        order_coffee('cappuccino')
    elif request == "report":
        report()
    else:
        print("Option not recognised")
