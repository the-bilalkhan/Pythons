
def wellcome_massege(first_name, last_name):        #Function Definition
    print(f"Hello {first_name} {last_name}")
    print("Wellcome To The School")


print("Start Function Here")

print("-------------------------Using Positional Arguments-------------------------------")
wellcome_massege("Khan", "Bilal")  #In this case arguments are not passes to correct parameters

#So For avoid that error we use KeyWords Arguments
print("-------------------------Using KeyWord Arguments-------------------------------")
wellcome_massege(last_name = "Khan", first_name = "Bilal")

print("-------------------------Using Both Positional&KeyWord Arguments-------------------------------")
wellcome_massege("Bilal", last_name="Khan")