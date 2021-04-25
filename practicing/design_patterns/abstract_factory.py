
# * Creational patterns
# * Abstract factory example

class Dog:
    # One of the objects to be returned
    def speak(self):
        return "Woof!"

    def __str__(self):
        return "Dog"


class DogFactory:
    # Concrete factory
    def get_pet(self):
        return Dog()

    def get_food(self):
        return "Dog Food!"


class PetStore:
    # PetStore houses our abstarct factory
    def __init__(self, pet_factory=None):
        # pet_factory is our abstract factory
        self._pet_factory = pet_factory

    def show_pet(self):
        # utility method to display the details of the objects returned by the DogFactory
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print(f"Our pet is {pet}")
        print(f"Our pet says hello by {pet.speak()}")
        print(f"Its food is {pet_food}")


# todo: Create a concrete factory
factory = DogFactory()

# todo: Create a pet store housing our abstract factory
shop = PetStore(factory)

# todo: Involve the utility method to show the details of our pet
shop.show_pet()
