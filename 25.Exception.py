
try:
   age = int(input("Age:"))
   income = 20000
   risk = income / age
   print(age)
except ValueError:
    print("Invalid Value.Use Only Integers Values.")
except ZeroDivisionError:
    print("Age Cannot Be Zero.Reenter the value.")