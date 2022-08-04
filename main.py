from abc import ABC, abstractmethod


# Создаём абтсрактный класс

class Storage(ABC):
    _items = {}
    _capacity = 0

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
    def get_items(self, items):
        pass

    @abstractmethod
    def items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass


# Создаем класс который наследует астрактный класс Storage
# Используется Полимарфизм классами Store и Shop

class Store(Storage):
    # Инкапсулируем переменные
    _capacity = 100
    _items = {}

    # Добавляем айтем в список на склад и отнимаем место у склада
    def add(self, title, count):
        if title in self._items:
            self._items[title] += count
        else:
            self._items.update({title: count})
        self._capacity -= count

    # Добавили на склад и если товара 0 то удаляем его из списка
    def remove(self, title, count):
        global qnt
        if title in self._items:
            qnt = self._items[title] - count
        if qnt <= 0:
            for key, value in list(self._items.items()):
                if key == title:
                    del store_items[key]
        else:
            self._items[title] = qnt
        self._capacity -= count

    # Возвращаем свободное кол-во на складе
    @property
    def get_free_space(self):
        return self._capacity

    # Возвращаем список что находится на складе
    @property
    def get_items(self):
        item = "\n".join([f"{key} - {values}" for key, values in self._items.items()])
        return item

    # передаем список айтемов и кол-ва в функции main()
    @get_items.setter
    def get_items(self, items):
        self._items = items

    # Возвращаем айтемы на складе для проверки
    @property
    def items(self):
        return self._items

    # Возвразаем уникальные товары на складе
    @property
    def get_unique_items_count(self):
        return set(self._items)


# Создаем класс с наследованием Stora -> Storage
class Shop(Store):
    def __init__(self):
        super().__init__()
        self._capacity = 20


# Так и не понял для чего, в домашке просто указали создать а где использовать?
class Request:
    def __init__(self, fromm, to, amount, product):
        self.fromm = fromm
        self.to = to
        self.amount = amount
        self.product = product


# Функция main()
def main():
    global fromm
    global to
    global amount
    global product

    # Бесконечный цикл, прервать цикл написать в диалоговое окно stop
    while True:
        print("\n")
        # Получаем команду от пользователя
        user_input = input(
            "Введите текст в формате:<действие> <количество> <наименование товара> из <место откуда> в <место куда>,\n"
            "Например: Доставить 10 Зефир из склад в магазин\n").split(" ")
        print("\n")
        # обрабатываем ошибки
        try:
            fromm = user_input[4]
            to = user_input[6]
            amount = int(user_input[1])
            product = user_input[2]
        # Выводим сообщение если ошибка
        except Exception as e:
            print(e)
            print("Ошибка ввода текста, попробуйте пожалуйста снова,"
                  "Например: Доставить 10 Зефир из склад в магазин")
        # Останавливаем цикл
        if user_input == "stop":
            break
        # Проверяем правльность кол-ва слов в команде
        if len(user_input) != 7:
            print('Введен не верный запрос')
        # Если ошибки нет то обрабатываем исключение
        else:
            # Проверяем от куда везем
            if fromm.lower() == 'склад':
                # Проверяем кол-во на складе
                if amount > shop.get_free_space:
                    print('Нет свободного места на кладе')
                # Если есть места обрабатываем
                else:
                    # Условие поиск товара введеного от пользователя в списке
                    if product in store.items:
                        # Цикл перебираем ключ и значение
                        for keys, values in list(store.items.items()):
                            # Условие если в списке совпал продукт с пользователем следуем далее
                            if keys == product:
                                # Проверяем кол-во свободного товара на складе
                                if amount <= int(values):
                                    print('Нужное количество есть на складе')
                                    print(f'Курьер везет {amount} {product} со {fromm} в {to}')
                                    # Добавляем товар в список на склад
                                    shop.add(product, amount)
                                    # удаляем товар с списке или меняем кол-во
                                    store.remove(product, amount)
                                    print(f'Курьер доставил {amount} {product} в {to}')
                                    print('В склад хранится:')
                                    # Выводим товар на скаде
                                    print(store.get_items)
                                    print(f'Свободное место на складе {store.get_free_space} из 100')
                                    print('В магазин хранится:')
                                    # Выводим товар в Магазине
                                    print(shop.get_items)
                                    print(f'Свободное место в магазине {shop.get_free_space} из 20')
                                # Выводим ошибку если не хватает места на складе
                                else:
                                    print('Не хватает на складе, попробуйте заказать меньше')
                                    print("\n")
                    # Выводим ошибку если заданого товара пользователем нет на складе
                    else:
                        print("Данного товара нет на складе")
            # Выводим сообщение что товар с магазина на склад ещё не возим
            elif to.lower() == 'магазин':
                print("перевозка из магазина на склад в разработке")
            # Выводим сообщеения о других родах перевозки
            else:
                print("Такой перевозки у нас нет")


# Так я не понял в итоге что значит __name__ == "__main__": как и у flaska
if __name__ == "__main__":
    # Инициализируем классы
    store = Store()
    shop = Shop()

    # Передаем список в сеттер
    store_items = {
        'Зефир': 10,
        "Кокос": 20,
        "Иван-чай": 7,
        "Репа": 80,
        "Картошка": 190,
        "Икра-Заморская": 1
    }
    store.get_items = store_items
    # Вызываем функцию main()
    main()

# Доставить 3 Зефир из склад в магазин
# Доставить 3 Кокос из склад в магазин
# Доставить 3 Иван-чай из склад в магазин
# Доставить 3 Репа из склад в магазин
# Доставить 5 Картошка из склад в магазин
# Доставить 3 Икра-Заморская из склад в магазин
