temparture = 30

if temparture > 30:
     print("It's Hot Day.")
else:
     print("It's Cold Day.")

print("-------------------------------Exerecise Task----------------------------------------------")

name = input("Enter Your Name? ")

if len(name) < 3:
    print("Name Must Be At Least Three Charactres.")
elif len(name) > 50:
    print("Name Can Be Maximum of 50 Characters. ")
else:
    print("Name Looks GOOD!")
