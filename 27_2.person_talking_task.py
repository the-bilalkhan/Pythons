class Person:
    def __init__(self,Name):
        self.Name = Name

    def talk(self):
        print(f"Hello, I am {self.Name}")





bilal = Person("Bilal Khan")
bilal.talk()

jawad = Person("Jawad Shuja")
jawad.talk()

ghayor = Person("Ghayor")
ghayor.talk()