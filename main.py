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
    items = {}

    def add(self, title, count):
        if title in self.items:
            self.items[title] += count
        else:
            self.items.update({title: count})
        self.capacity -= count

    def remove(self, title, count):
        global qnt
        if title in self.items:
            qnt = self.items[title] - count
        if qnt <= 0:
            for key, value in list(self.items.items()):
                if key == title:
                    del store_items[key]
        else:
            self.items[title] = qnt
        self.capacity -= count

    @property
    def get_free_space(self):
        return self.capacity

    @property
    def get_items(self):
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
    global fromm
    global to
    global amount
    global product

    while True:
        print("\n")
        user_input = input(
            "Введите текст в формате:<действие> <количество> <наименование товара> из <место откуда> в <место куда>,\n"
            "Например: Доставить 10 Зефир из склад в магазин\n").split(" ")
        print("\n")
        try:
            fromm = user_input[4]
            to = user_input[6]
            amount = int(user_input[1])
            product = user_input[2]
        except Exception as e:
            print(e)
            print("Ошибка ввода текста, попробуйте пожалуйста снова,"
                  "Например: Доставить 10 Зефир из склад в магазин")

        if user_input == "stop":
            break

        if len(user_input) != 7:
            print('Введен не верный запрос')
        else:
            if fromm.lower() == 'склад':
                if amount > shop.capacity:
                    print('Нет свободного места на кладе')
                else:
                    if product in store.items:
                        for keys, values in list(store.items.items()):
                            if keys == product:
                                if amount <= int(values):
                                    print('Нужное количество есть на складе')
                                    print(f'Курьер везет {amount} {product} со {fromm} в {to}')
                                    shop.add(product, amount)
                                    print(store.items)
                                    store.remove(product, amount)
                                    print(store.items)
                                    print(f'Курьер доставил {amount} {product} в {to}')
                                    print('В склад хранится:')
                                    print(store.get_items)
                                    print(f'Свободное место на складе {store.capacity} из 100')
                                    print('В магазин хранится:')
                                    print(shop.get_items)
                                    print(f'Свободное место в магазине {shop.capacity} из 20')
                                    print(store.get_unique_items_count)
                                    print(shop.get_unique_items_count)
                                else:
                                    print('Не хватает на складе, попробуйте заказать меньше')
                                    print("\n")
                    else:
                        print("Данного товара нет на складе")

            elif to.lower() == 'магазин':
                print("перевозка из магазина на склад в разработке")

            else:
                print("Такой перевозки у нас нет")


if __name__ == "__main__":
    store = Store()
    shop = Shop()

    store_items = {
        'Зефир': 10,
        "Кокос": 20,
        "Иван-чай": 7,
        "Репа": 80,
        "Картошка": 190,
        "Икра-Заморская": 1
    }
    store.items = store_items
    main()


# Доставить 9 Зефир из склад в магазин
# Доставить 3 Кокос из склад в магазин
# Доставить 3 Иван-чай из склад в магазин
# Доставить 3 Репа из склад в магазин
# Доставить 3 Картошка из склад в магазин
# Доставить 3 Икра-Заморская из склад в магазин
