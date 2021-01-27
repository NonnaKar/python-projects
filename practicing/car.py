class Car:

    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"The {self.color} car has {self.mileage} miles."

car1 = Car(mileage=20_000, color="blue")
car2 = Car(mileage=30_000, color="red")

print(car1)
print(car2)
