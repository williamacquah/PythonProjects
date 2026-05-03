from coffee_data import *
def check_choice(choice, money):
    """Handles user input."""
    if choice == "off":
        return False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: ${money}")
        return None
    else:
        return True

def check_resources(choice):
    """Checks if there are enough ingredients to make coffee"""
    drink_ingredients = MENU[choice]["ingredients"]
    for item, amount in drink_ingredients.items():
        if resources[item] < amount:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    quarters = float(input("How many quarters?:"))
    dimes = float(input("How many dimes?:"))
    nickels = float(input("How many nickles?:"))
    pennies = float(input("How many pennies?:"))
    return quarters*0.25+dimes*0.1+nickels*0.05+pennies*0.01

def enough_money(money_received, drink_cost):
    if money_received < drink_cost:
        print("Sorry, not enough money. Money refunded.")
        return False
    elif money_received > drink_cost:
        print(f"Here is your change: {money_received-drink_cost}")
        return True
    else:
        return True

def make_coffee(choice):
    drink_ingredients = MENU[choice]["ingredients"]
    for item, amount in drink_ingredients.items():
        resources[item] -= amount
    print(f"Here is your {choice}, enjoy☕.")

def main():
    money = 0
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        action = check_choice(choice, money)
        if action == False:
            break
        elif action:
            if check_resources(choice):
                money_received = process_coins()
            if enough_money(money_received, MENU[choice]["cost"]):
                money += MENU[choice]["cost"]
                make_coffee(choice)

main()