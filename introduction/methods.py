class People:
    def __init__(self, name):
        self._name = name
    def __str__(self):
        return self._name

people_1 = People('Jhon')
print(people_1)

people_2 = People('Mike')
print(people_2)

class numbersList:
    def __init__(self, numbers):
        self.numbers = numbers
    def __str__(self):
        return ",".join([str(n) for n in self.numbers])
    def addition(self):
        return sum(self.numbers)
    def media(self):
        return self.addition()/len(self.numbers)

myList = numbersList([1,3,5,7,9])
print(f"The sum of {myList} is {myList.addition()}")
print(f"The media of {myList} is {myList.media()}")


