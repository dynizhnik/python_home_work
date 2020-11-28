class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def eat(self, food):
        print(self.name, "eating food =", food)
        self.weight += food

    def show(self):
        print('Dog', self.name, self.age, self.weight)