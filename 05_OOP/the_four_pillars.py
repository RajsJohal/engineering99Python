#4 pillars of OOP LEARN AND DEMONSTRATE UNDERSTANDING OF THESE PILLARS

#Abstraction
#Making life easy for the user by providing obvious inputs/ outputs

#Encapsulation
#Private variables

#Inheritance
#Passing on attributes and methods to avoid repetition

#Polymorphism
#Changing some behaviors of a inherited class, overriding methods
#"Many Forms"

#Demonstration of inheritance
class Animal:
    def __init__(self, legs):
        self.alive = True
        self.legs = legs

    def breathe(self):
        print("Breathing in ... breathing out...")

    def eat(self):
        print("nom nom nom")

class Mammal(Animal):
    def __init__(self, legs):
        super().__init__(legs) # inherits the __init__ function in superclass
        self.warmblood = True #replaces the __init__ inside super class Animal

    def reproduce(self):
        print("Giving birth to live young")

class Cat(Mammal): # Animal -> Mammal -> Cat
    def __init__(self, breed):
        super().__init__(4)
        self.breed = breed

class Platypus(Mammal):
    def __init__(self):
        super().__init__(4)

    def reproduce(self):
        print("Laying Eggs")

    #Method overloading
    def reproduce(self, n):
        print(f"Laying {n} eggs")

blue = Platypus()
blue.reproduce(5)

