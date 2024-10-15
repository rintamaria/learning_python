class Dog:
    species="canis familiaris"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def description(self):
          return f"{self.name} is {self.age} years old"
#The f in return f"{self.name} is {self.age} years old" refers to an f-string, which is a convenient way to format strings in Python. The f stands for formatted.
a=Dog("rinta",22)
print(a.name)
print(a.description())