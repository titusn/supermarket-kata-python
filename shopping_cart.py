class ShoppingCart:
    def __init__(self):
        self.count = 0

    def item_count(self):
        return self.count

    def add(self, item):
        self.count = 1

    def remove(self, param):
        if self.count == 0:
            raise UnderflowError
        self.count = 0


class UnderflowError(RuntimeError):
    pass
