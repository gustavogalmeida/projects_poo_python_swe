from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Example usage
dog = Dog()
print("The dog says:", dog.make_sound())

cat = Cat()
print("The cat says:", cat.make_sound())