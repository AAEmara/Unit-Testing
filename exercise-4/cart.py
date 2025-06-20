class Cart():
    def __init__(self):
        self.items = []
        self.items_count = 0


    def add_item(self, item):
        self.items.append(item)
        self.items_count += 1


    def remove_item(self, item):
        self.items.remove(item)
        self.items_count -= 1


    def calculating_totals(self):
        return self.items_count
