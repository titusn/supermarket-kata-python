class ShoppingCart:
    def __init__(self):
        self._items = []

    def item_count(self):
        return len(self._items)

    def add(self, item):
        self._items.append(item)

    def remove(self, item):
        if self.item_count() == 0:
            raise UnderflowError
        self._items.remove(item)

    def items(self):
        return self._items


class UnderflowError(RuntimeError):
    pass
