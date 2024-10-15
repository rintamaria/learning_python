#single inheritance , a child class inherits from a parent class
class Vechicle:
    def vechinfo(self):
        print("in vechicle class")
class Car(Vechicle):
    def carinfo(self):
        print("in car class")
car=Car()
car.vechinfo()
car.carinfo()