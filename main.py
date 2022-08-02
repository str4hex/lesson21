from abc import ABC, abstractmethod

class Storage:

    def __init__(self,items, capacity ):
        self.items = []
        self.capacity = capacity

    def add(self):
        pass

    def remove(self):
        pass

    def get_free_space(self):
        pass

    def get_items(self):
        pass

    def get_unique_items_count(self):
        pass

