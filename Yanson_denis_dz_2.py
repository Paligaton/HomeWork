from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, v):
        self.v = v
    @property
    @abstractmethod
    def count(self):
        pass
    def __add__(self, other):
        return self.count() + other.count()
class Coat(Clothes):
    def count(self):
        return self.v/6.5+0.5
class Suit(Clothes):
    def count(self):
        return self.v*2+0.3

suit=Suit(5)
coat=Coat(5)
print(coat.count())
print(suit.count())
print(coat+suit)