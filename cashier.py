class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input(how many quarters?: )"""
        dollar = int(input("How many dollar coins?: "))
        quarters = int(input("How many quarters?: ")) *.25
        dimes = int(input("How many dimes?: ")) *.10
        nickles = int(input("How many nickles?: ")) *.05
        balance = dollar + quarters + dimes + nickles
        print(f"Your balance is ${balance}.")
        return balance

    def transaction_result(self, coins, cost):
        if coins >= cost:
            change = coins - cost
            print(f"Here is ${change} in change.")
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False
