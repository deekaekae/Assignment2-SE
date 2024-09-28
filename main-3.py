import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()

machine = sandwich_maker_instance
def main():
    choice = input("What would you like? (small/medium/large/off/report): ")
    if choice == "small":
        cashier_instance.transaction_result(cashier_instance.process_coins(), recipes["small"]["cost"])
        machine.make_sandwich("small", recipes["small"]["ingredients"])
    if choice == "medium":
        cashier_instance.transaction_result(cashier_instance.process_coins(), recipes["medium"]["cost"])
        machine.make_sandwich("medium", recipes["medium"]["ingredients"])
    if choice == "large":
        cashier_instance.transaction_result(cashier_instance.process_coins(), recipes["large"]["cost"])
        machine.make_sandwich("large", recipes["large"]["ingredients"])
    if choice == "off":
        exit()
    if choice == "report":
        print(machine.machine_resources)

if __name__=="__main__":
    main()



