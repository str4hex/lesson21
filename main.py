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
            self.items.append({title: count})
        self.capacity -= count

    def remove(self, title, quantity):
        if title in self.items:
            qnt = self.items[title] - quantity
            if qnt < 0:
                self.items[title] = 0
            else:
                self.items[title] = qnt


    @property
    def get_free_space(self):
        return self.capacity

    @property
    def get_items(self):
        if len(self.items) == 1:
            item = "\n".join([f"{keys} - {values}" for item in self.items for keys, values in item.items()])
            return item
        else:
            item = "\n".join([f"{key} - {values}" for key, values in self.items.items()])
            return item

    @property
    def get_unique_items_count(self):
        return set(self.items)


class Shop(Store):
    def __init__(self):
        super().__init__()
        self.capacity = 20


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
        else:
            if user_input[4].lower() == 'склад':
                if user_input[2] in store.items:
                    for keys, values in store.items.items():
                        if keys == user_input[2]:
                            if int(user_input[1]) < int(values):
                                print('Нужное количество есть на складе')
                                print(
                                    f'Курьер везет {user_input[1]} {user_input[2]} со {user_input[4]} в {user_input[6]}')
                                shop.add(user_input[2], int(user_input[1]))
                                store.remove(user_input[2], int(user_input[1]))
                                print(f'Курьер доставил {user_input[1]} {user_input[2]} в {user_input[6]}')
                                print('В склад хранится:')
                                print(store.get_items)
                                print(f'Свободное место на складе {store.capacity} из 100')
                                print('В магазин хранится:')
                                print(shop.get_items)
                                print(f'Свободное место в магазине {shop.capacity} из 20')
                            else:
                                print('Не хватает на складе, попробуйте заказать меньше')
                                print("\n")
                else:
                    print("Данного товара нет на складе")

            elif user_input[4].lower() == 'магазин':
                print("перевозка из магазина на склад в разработке")

            else:
                print("Такой перевозки у нас нет")


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
