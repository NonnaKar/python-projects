
# * Creational patterns
# * Singleton example

class Borg:
    # * Borg class making class attributes global
    _shared_state = {}  # Attribut dictionary

    def __init__(self):
        self.__dict__ = self._shared_state  # Make it an attribute dictionary


class Singleton(Borg):  # Inherits from the Borg class
    # * This class now shares all its attributes among its various instances
    # * This essensially makes the singleton objects an object-oriented global variable

    def __init__(self, **kwargs):
        Borg.__init__(self)
        # Update the attribute dictionary by inserting a new key-value pair
        self._shared_state.update(kwargs)

    def __str__(self):
        # Returns the attribute dictionary for printing
        return str(self._shared_state)


# todo: Let's create a singleton oject and add our first acronym
x = Singleton(HTTP="Hyper Text Transfer Protocol")
print(x)

# todo: Let's create another singleton object and if it refers to the same attribute dictionary by adding another acronym
y = Singleton(SNMP="Simple Network Management Protocol")
print(y)
