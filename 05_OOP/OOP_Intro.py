class Dog: #No space and each word starts with a capital
    animal_kind = "Canine"

    def __init__(self, name, colour): # Double Underscore Initialise
        self.legs = 4
        animal_kind = "Canine"
        self.name = name
        self._colour = colour # the underscore makes this private so it is hidden

    def bark(self): #looks like a function but it is a METHOD, SELF REFERS TO CURRENT CLASS
        return f"Woof! i am a {self.animal_kind}"

    def get_colour(self):
        return self._colour

    def set_colour(self, new_colour):
        self._colour = new_colour


fido = Dog("Fido", "Black") #Instantiation, fido is an instance of class dog
print(fido.bark()) # how to call the method inside class Dog
print(fido.animal_kind)

print(fido.get_colour())
fido.set_colour("green")
print(fido.get_colour())
fido._colour = "purple"
print(fido.get_colour())
print(fido._colour)


Dog.animal_kind = "Canine"
print(fido.legs)
fido.legs = 8
print(fido.legs)
print(fido.animal_kind)