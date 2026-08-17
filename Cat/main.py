class Cat:
    special = "кот"
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.hunger = 50
    def meow(self):
        print("Мяу")
    def feed(self,amount):
        self.hunger -= amount
        if self.hunger < 0:
            self.hunger = 0
    def is_hungry(self):
        return self.hunger > 20
    @classmethod
    def get_species(cls):
        return cls.special
my_cat = Cat("Barsic","red")
print(my_cat.meow())
print(my_cat.hunger) # 50
print(my_cat.feed(10))
print(my_cat.hunger) # 40
print(my_cat.is_hungry())
print(my_cat.get_species())

