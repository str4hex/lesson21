from abc import ABC, abstractmethod


class Storage(ABC):
    items = {}
    capacity = 0

    def add(self, items):
        pass

    def remove(self, items, capacity):
        pass

    def get_free_space(self):
        pass

    def get_items(self):
        pass

    def get_unique_items_count(self):
        pass


class Store(Storage):
    capacity = 100
    items = []

    @classmethod
    @abstractmethod
    def add(cls, items):
        cls.items.append(items)

    @abstractmethod
    def remove(self, items, quantity):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @property
    @abstractmethod
    def get_items(self):
        item = "\n".join([f"{item.product} - {item.amount}" for item in self.items])
        print(item)
        return item

    @abstractmethod
    def get_unique_items_count(self):
        pass


class Shop(Storage):
    capacity = 20
    items = []

    @abstractmethod
    def add(self, items, quantity):
        pass

    @abstractmethod
    def remove(self, items, quantity):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass


class Request:
    def __init__(self, fromm, to, amount, product):
        self.fromm = fromm
        self.to = to
        self.amount = amount
        self.product = product


def main():
    # deliviry = input("").split(" ")
    deliviry = 'Доставить 3 печеньки из склад в магазин'.split(" ")
    request = Request(fromm=deliviry[4], to=deliviry[6], amount=deliviry[1], product=deliviry[2])
    store = Store
    store.add(request)
    print(store.get_items)


# Доставить 3 печеньки **из** склад в магазин


main()
