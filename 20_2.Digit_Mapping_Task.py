
number = input("Numbers:")

digts_maping = {
    "0" : "zero",
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
    "9" : "nine"
}

output = ""

for values in number:
    output += digts_maping.get(values, "!") + " "
print(output)