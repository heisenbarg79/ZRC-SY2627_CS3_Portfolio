
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return self.name + " eats food."

    def make_sound(self):
        return self.name + " makes a sound."


# Child class: Lion
class Lion(Animal):
    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        return self.name + " eats fresh meat."

    def make_sound(self):
        return self.name + " roars loudly."


# Child class: Elephant
class Elephant(Animal):
    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        return self.name + " eats grass and fruits."

    def make_sound(self):
        return self.name + " trumpets!"


# Child class: Monkey
class Monkey(Animal):
    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        return self.name + " eats bananas."

    def make_sound(self):
        return self.name + " chatters!"


# Create objects
lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")

# Store animals in a list
animals = [lion, elephant, monkey]

# Call the overridden methods using a for loop
for animal in animals:
    print(animal.make_sound())
    print(animal.eat())
    print("-----")
