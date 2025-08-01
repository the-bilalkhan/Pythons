#Just For Fun On Every Random Generation One Random Generation Is of Your Choice ==> {Bilal}
import random

members = ["Bilal", "Hammad", "Shuja", "Murad", "Amish"]

l1 = random.choice(members)
l2 = random.choice(members)
l3 = random.choice(members)

if l1 == l2 == l3:
  if l1=="Bilal" and l2=="Bilal" and l3=="Bilal":
          print("Three Same Results")
          print(f"Final: {l1} {l2} {l3}")
elif l1 == l2 or l2 == l3 or l3 == l1:
    print("Two Same Results")
    # print(f"{l1} {l2} {l3}")
    if l1 == "Bilal" and  l2 == "Bilal" and l3 == "Bilal":
     print("Bilal are Both In l1, l2 and l3.")
     # print(f"{l1} {l2} {l3}")
    else:
        if l1 == "Bilal" and l2 == "Bilal" and not l3 == "Bilal":
         print("Bilal in l1 and l2.")
         print(f"Final: {l1} {l2} {l3}")
        elif not l1 == "Bilal" and l2 == "Bilal" and l3 == "Bilal":
         # print("Bilal in l2 and l3.")
         print(f"{l1} {l2} {l3}")
        elif l1 == "Bilal" and not l2 == "Bilal" and l3 == "Bilal":
           # print("Bilal in l1 and l3.")
           print(f"{l1} {l2} {l3}")
        elif not l1 == "Bilal" and not l2 == "Bilal" and not l3 == "Bilal":
           # print("Bilal are Not In Both l1, l2 and l3.")
           l3 = "Bilal"
           print(f"Final: {l1} {l2} {l3}")
        else:
             # print("Bilal or in l1, or in l2,and or in l3")
             print(f"{l1} {l2} {l3}")
else:
 if not l1 == "Bilal" and not l2 == "Bilal" and not l3 == "Bilal":
             l1 = "Bilal"

 print(f"Final:- {l1} {l2} {l3}")