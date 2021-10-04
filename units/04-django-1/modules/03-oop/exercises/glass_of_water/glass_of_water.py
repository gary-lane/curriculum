class Glass:
    def __init__(self, capacity):
        self.capacity = capacity
        self.amount = 0

    def pour_in(self, amount):
        if self.capacity <= (self.amount + amount):
            self.amount = self.capacity
        else:
            self.amount += amount

    def pour_out(self, amount):
        if 0 >= (self.amount - amount):
            self.amount = 0
        else:
            self.amount -= amount
