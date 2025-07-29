# xxxxx
# xx
# xxxxx
# xx
# xx

print("-----------------------Using Simple Method----------------------")
numbers = [5, 2, 5, 2, 2]
cha = "X"
result = ""
for final in numbers:
    result = cha * final
    print(f"{result}")

print("-----------------------Using Nested Loop----------------------")
numb = [5, 2, 5, 2, 2]
for output in numb:
    result = ""
    for final in range(output):
        result += "X"
    print(result)
