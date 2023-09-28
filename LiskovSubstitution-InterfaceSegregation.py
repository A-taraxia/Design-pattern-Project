from abc import ABC, abstractmethod


class StoreInterface(ABC):
    @abstractmethod
    def buy_product(self, product):
        pass

    @abstractmethod
    def sell_product(self, product):
        pass


class Store(StoreInterface):
    def __init__(self):
        self.products = []

    def buy_product(self, product):
        self.products.append(product)
        print(f"Bought {product}")

    def sell_product(self, product):
        if product in self.products:
            self.products.remove(product)
            print(f"Sold {product}")
        else:
            print(f"{product} not available")


class OnlineStore(Store):
    def __init__(self):
        super().__init__()

    def buy_product(self, product):
        print("Online store does not support buying products directly.")
        print("Please place an order instead.")


class PhysicalStore(Store):
    def __init__(self):
        super().__init__()


# Παράδειγμα χρήσης
store = PhysicalStore()
store.buy_product("Shirt")
store.sell_product("Shirt")

online_store = OnlineStore()
online_store.buy_product("Shirt")
online_store.sell_product("Shirt")
