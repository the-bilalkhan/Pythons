
coordinates = (1, 2, 3, 4, 5)

#If We Want To Do:

# coordinates[0] * coordinates[1] * coordinates[2] * coordinates[3] * coordinates[4] ==> This Is Too Long
#For Shorter we can assigned lists values to variables

# v = coordinates[0]
# w = coordinates[1]
# x = coordinates[2]
# y = coordinates[3]
# z = coordinates[4]

# print(y)

#But By Using Unpacking feature of python we can do it very easily

v, w, x, y, z = coordinates  #unpacking features automaticly assigned values to variables on their index

print(w)
print(z)
print(y)
print(x)