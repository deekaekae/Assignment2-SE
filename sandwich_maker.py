
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        for ingredient, required_resources in ingredients.items():
            available_resources = self.machine_resources[ingredient]
            if available_resources < required_resources:
                print(f"Sorry, there is not enough {ingredient}.")
                return False
        print("Sandwhich can be made")
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        for ingredient, amount in order_ingredients.items():
            if self.machine_resources[ingredient] < amount:
                self.machine_resources[ingredient] -= amount
        print(f"{sandwich_size} sandwiches is ready. Bon appetit!")
