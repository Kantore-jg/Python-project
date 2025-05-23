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
profit=0
ressources={
    "water":300,
    "milk":200,
    "coffee":100,}
def is_ressources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>ressources[item]:
            print(f"sorry ther is not enough {item}")
            return False
        return True
def is_transaction_successful(money_received,drink_cost):
    if money_received>=drink_cost:
        change=round(money_received-drink_cost,2)
        print(f"here is ${change} in change.")
        global profit
        profit+=drink_cost
        return True
    else:
        print(f"sorry ther is not enough money, Money refunded.")
        return False


def process_coins():
    print("insert coins")
    total= int(input ("how many  quarters?: "))*0.25
    total+= int(input("how many  dimes?: "))*0.1
    total+= int(input("how many  nickles?: "))*0.05
    total+= int(input("how many  pennies?: "))*0.01
    return total
def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        ressources[item]-+order_ingredients[item]
    print(f"here is your {drink_name}🍨 enjoy")


is_on=True

while is_on:
    choice = input("🙌What would you like?(espresso/latte/cappuccino): 😎").lower()
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f'water: {ressources['water']}ml')
        print(f'milk: {ressources['milk']}ml')
        print(f'coffee: {ressources['coffee']}g')
        print(f'money: ${profit}')
    else:
        drink=MENU[choice]
        if is_ressources_sufficient(drink['ingredients']):
            payment=process_coins()
            if is_transaction_successful(payment,drink['cost']):
                make_coffee(choice,drink['ingredients'])


