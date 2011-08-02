from abc import ABC, abstractmethod


class Storage(ABC):

    def __init__(self, items, capacity):
        self.items = items
        self.capacity = capacity

    @abstractmethod
    def add(self, items, capacity):
        pass

    @abstractmethod
    def remove(self, items, capacity):
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

    def __init__(self, items, capacity):
        super().__init__(items, capacity)
        self._items = {}
        self._capacity = 100

    def add(self, items, capacity):
        pass

    def remove(self, items, capacity):
        pass

    def get_free_space(self):
        pass

    def get_items(self):
        pass

    def get_unique_items_count(self):
        pass


class Shop(Storage):

    def __init__(self, items, capacity):
        super().__init__(items, capacity)
        self._items = {}
        self._capacity = 20

    def add(self, items, capacity):
        pass

    def remove(self, items, capacity):
        pass

    def get_free_space(self):
        pass

    def get_items(self):
        pass

    def get_unique_items_count(self):
        pass
