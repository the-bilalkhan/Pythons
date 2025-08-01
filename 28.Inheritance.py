
class Mammal:  #Parent Class
      def walk(self):
          print(f"Hey,Walk")


class Dog(Mammal):        #Child Class
         def bark(self):
             print("Bark On Him")


class Cat(Mammal):   #Child Class
        def KillingRat(self):
            print("Kill The Rat")



dog1 = Dog()
dog1.walk()   #Parent Habbit
dog1.bark()    #Own Habbit

cat1 = Cat()
cat1.walk()  #Parent Habbit
cat1.KillingRat() #Own Habbit