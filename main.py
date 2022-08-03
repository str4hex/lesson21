from abc import ABC, abstractmethod


class Storage(ABC):
    items = {}
    capacity = 0

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


class Store(Storage):
    capacity = 100
    items = []

    def add(self, title, count):
        if title in self.items:
            self.items[title] += count
        else:
            self.items[title] = count
        self.capacity -= count


    def remove(self, title, quantity):
        pass

    @property
    def get_free_space(self):
        return self.capacity

    @property
    def get_items(self):
        item = "\n".join([f"{item.product} - {item.amount}" for item in self.items])
        return item

    @property
    def get_unique_items_count(self):
        return set(self.items)


class Shop(Store):
    def __init__(self):
        super().__init__()
        self._capacity = 20


class Request:
    def __init__(self, fromm, to, amount, product):
        self.fromm = fromm
        self.to = to
        self.amount = amount
        self.product = product


def main():
    while True:
        user_input = input(
            "Введите текст в формате:<действие> <количество> <наименование товара> из <место откуда> в <место куда>,\n"
            "Например Доставить 3 печенье из склад в магазин\n").split(" ")
        print("\n")

        if user_input == "stop":
            break

        if len(user_input) != 7:
            print('Введен не верный запрос')

        store = Store()
        store.items = store_items

        if user_input[4].lower() == 'склад':
            pass

        if user_input[2] in store.items:
            print('Нужное количество есть на складе')
            print("\n")








# Доставить 3 печеньки из склад в магазин


if __name__ == "__main__":
    store = Store()
    # shop = Shop()

    store_items = {
        'печенье': 10,
        "чай": 20,
        "лимонад": 7,
    }
    main()
