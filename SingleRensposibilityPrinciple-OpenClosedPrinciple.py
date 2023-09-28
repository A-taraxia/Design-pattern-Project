class Dish:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price


class Order:
    def __init__(self):
        self.dishes = []

    def add_dish(self, dish):
        self.dishes.append(dish)

    def remove_dish(self, dish):
        self.dishes.remove(dish)

    def calculate_total_price(self):
        total_price = 0
        for dish in self.dishes:
            total_price += dish.get_price()
        return total_price


class Restaurant:
    def __init__(self):
        self.orders = []

    def take_order(self, order):
        self.orders.append(order)

    def process_orders(self):
        for order in self.orders:
            total_price = order.calculate_total_price()
            # Εδώ μπορούμε να προσθέσουμε λογική για την εκτύπωση, αποθήκευση, κλπ.
            print(f"Total price: {total_price}")


# Παράδειγμα χρήσης
dish1 = Dish("Pasta", 10)
dish2 = Dish("Salad", 5)

order = Order()
order.add_dish(dish1)
order.add_dish(dish2)

restaurant = Restaurant()
restaurant.take_order(order)
restaurant.process_orders()
