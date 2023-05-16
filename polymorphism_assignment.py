

# parent class
class Vehicle:
    brand = " "
    model = " "

    #methods
    def move(self):
        print("Go!")


# child class 
class Car(Vehicle):
    axles = 2
    doors = 4

    #method
    def move(self):
        print("Vrroom!")


# another child class 
class Boat(Vehicle):
    equipment = 'Motor'
    fuel = True

    #method
    def move(self):
        print("Whoosh!")
