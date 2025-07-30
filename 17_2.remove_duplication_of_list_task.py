print("----------------------------For Numbers-----------------------------------------")
numbers = [12, 22, 34, 34, 34, 45, 54, 45, 56, 54, 46, 78, 87, 78, 123, 321, 123]
uniques = []

for unique_numbers in numbers:
      if unique_numbers not in uniques:
          uniques.append(unique_numbers)
print(uniques)

print("------------------------For Alphabets---------------------------------------------")
alphabets = ["a", "b", "c", "c", "d", "e", "d", "e", "z", "z", "y"]
uniques = []

for unique_alphabets in alphabets:
    if unique_alphabets not in uniques:
        uniques.append(unique_alphabets)
print(uniques)