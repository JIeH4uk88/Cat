class Cat:
    special = "кот"
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.hunger = 50
    def meow(self):
        print("Мяу")
    def feed(self,amount):
        self.hunger -= amount < 0
        if self.hunger < 0:
            self.hunger = 0
    def is_hungry(self):
        return self.hunger > 20

    @classmethod
    def get_species(self, cls):
        return cls.species
my_cat = Cat("Barsic","red")
print(my_cat.meow())
print(my_cat.feed(10))
print(my_cat.is_hungry())

