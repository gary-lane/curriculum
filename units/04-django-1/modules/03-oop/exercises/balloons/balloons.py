class BalloonTooFull(Exception):
    pass


class Balloon:
    def pump(self):
        self.amount += 3
        if self.amount > self.capacity:
            raise BalloonTooFull("Pop!")

    def release(self):
        self.amount -= 2
        self.amount = max(0, self.amount)

class SwordBalloon(Balloon):
    capacity = 5
    amount = 0

class DogBalloon(Balloon):
    capacity = 7
    amount = 0

class TriforceBalloon(Balloon):
    capacity = 11
    amount = 0