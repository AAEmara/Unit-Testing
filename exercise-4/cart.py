class Cart():
    def __init__(self):
        self.items = []
        self.items_count = 0


    def add_item(self, item):
        if type(item) == str:
            self.items.append(item)
            self.items_count += 1


    def remove_item(self, item):
        if type(item) == str and item in self.items:
            self.items.remove(item)
            self.items_count -= 1


    def calculating_totals(self):
        if self.items_count < 0:
            self.items_count = 0
        return self.items_count



