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
            self.items.append(f'{title}:{count}')
        self.capacity -= count

    def remove(self, title, quantity):
        pass

    @property
    def get_free_space(self):
        return self.capacity

    @property
    def get_items(self):
        item = "\n".join([f"{keys} - {values}" for keys, values in self.items.items()])
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
        print("\n")
        user_input = input(
            "Введите текст в формате:<действие> <количество> <наименование товара> из <место откуда> в <место куда>,\n"
            "Например Доставить 3 печенье из склад в магазин\n").split(" ")
        print("\n")

        if user_input == "stop":
            break

        if len(user_input) != 7:
            print('Введен не верный запрос')



        if user_input[4].lower() == 'склад':
            pass

        if user_input[2] in store.items:
            for keys, values in store.items.items():
                if keys == user_input[2]:
                    if int(user_input[1]) < int(values):
                        print('Нужное количество есть на складе')
                        print("\n")
                    else:
                        print('Не хватает на складе, попробуйте заказать меньше')
                        print("\n")

        print(f'Курьер везет {user_input[1]} {user_input[2]} со {user_input[4]} в {user_input[6]}')
        print("\n")
        shop.add(user_input[2], int(user_input[1]))
        print(f'Курьер доставил {user_input[1]} {user_input[2]} в {user_input[6]}')
        print('В склад хранится:')
        print(store.get_items)
        print('В магазин хранится:')
        print(shop.get_items)


# Доставить 3 печеньки из склад в магазин


if __name__ == "__main__":
    store = Store()
    shop = Shop()

    store_items = {
        'печенье': 10,
        "чай": 20,
        "лимонад": 7,
    }

    store.items = store_items



    main()
