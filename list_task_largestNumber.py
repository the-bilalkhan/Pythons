#program to find the largest number?

number = [10, 34, 65, 109, 4500, 10000, 23000, 23, 65, 765, 76532, 87, 9]

max = number[0]
for num in number:
    if num > max:
        max = num
print(max)