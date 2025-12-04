class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

    def bark(self):
        print(f"{self.name} says Woof!")

# Creating objects (instances) of the Dog class
my_dog = Dog("Buddy", 3)
your_dog = Dog("Lucy", 5)

# Accessing attributes and calling methods
print(my_dog.name)
print(your_dog.age)
print(my_dog.species)
print(your_dog.species)
my_dog.bark()
your_dog.bark()