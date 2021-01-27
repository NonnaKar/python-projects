class Dog:
    # Class attribute
    species = "Canis familiaris"

    # Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Methods .__init__() and .__str__() are called DUNDER METHODS
    # Instance method
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} barks: {sound}"

class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)
    
class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

miles = JackRussellTerrier("Miles", 4)
balto = GoldenRetriever("Balto", 7)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)

# miles = Dog("Miles", 4, "Jack Russell Terrier")
# buddy = Dog("Buddy", 9, "Dachshund")
# jack = Dog("Jack", 3, "Bulldog")
# jim = Dog("Jim", 5, "Bulldog")

print(balto.speak())
print(balto.speak("Grrr"))
print(jim.speak("Woof"))

# print(type(jack))
# print(isinstance(jack, Dachshund))
# print(isinstance(jack, Bulldog))