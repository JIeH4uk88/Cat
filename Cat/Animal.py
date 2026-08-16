
class Animal:
    def __init__(self, name, species):
        self.name = name
        self._species = species
        self.__age = 0
    def get_age(self):
        return self.__age
    def set_age(self, age):
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным!")
        self.__age = age
        def voice(self):
            print("Звук")
class Cat(Animal):
    def __init__(self, name, color, species):
        super().__init__(name, species="Кошка")
    def voice(self):
        print("Мяу!")
    def purr(self):
        print("Мур-мур...")
class Dog(Animal):
    def __init__(self, name, breed, species):
        super().__init__(name, species="Собака")
    def voice(self):
        print("Гав!")
my_cat = Cat("Barsic", "Red", "Кошка")
my_dog = Dog("Чарли","Овчарка","Собака")

my_cat.voice()
my_cat.purr()

my_cat.set_age(10)
print(my_cat.get_age())

my_dog.set_age(-5)
print(my_dog.get_age())

