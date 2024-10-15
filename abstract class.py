#abstract class can be considered as blueprint for other classes
# a class which contain one or more anstract method
# abstract method has declaration but not  have a implementation
from abc import ABC,abstractmethod
class Polygon(ABC):
    def noofsides(self):
        pass
class Triangle(Polygon):
    def noofsides(self):
        print("3 sides")
t=Triangle()
t.noofsides()