from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Lion(Animal):
    def make_sound(self):
        return "Roar"

lion = Lion()
print("-----Accessing the details of Lion class using abstraction of Animal class -----")
print(lion.make_sound())        