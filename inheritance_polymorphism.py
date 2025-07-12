class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def make_sound(self):
        print(f"{self.name} makes a sound")

    def walk(self):
        print(f"{self.name} is walking")

    def run(self):
        print(f"{self.name} is running")


class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} bark: Woof !")

    def run(self):
        print(f"{self.name} is running happlily")


class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} meows!")

    def walk(self):
        print(f"{self.name} is walking gracefully")

buddy = Dog("Buddy")

whiskers = Cat("Whiskers")


buddy.eat()
buddy.make_sound()
buddy.run()

# Cat
whiskers.eat()
whiskers.make_sound()
whiskers.walk()
whiskers.run()
