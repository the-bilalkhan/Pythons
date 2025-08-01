
class Person:

    def __init__(self, Name, Age): #Constructer
           self.Name = Name
           self.Age = Age

    def persn_info(self):
           print(f"Name:{self.Name} Age:{self.Age}")





new = Person("jawad Shuja",25)
new.persn_info()