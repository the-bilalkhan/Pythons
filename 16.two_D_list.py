# matrix = \
# [
#     [0, 1, 2],
#     [3, 4, 5],
#     [6, 7, 8]
# ]
#
# print("--------------------Access Lists With Specific element---------------------------")
#
# print('''
#      [0, 1, 2],
#      [3, 4, 5],
#      [6, 7, 8]
# ''')
#
# print(f"matrix[0][0]: {matrix[0][0]}")
# print(f"matrix[0][1]: {matrix[0][1]}")
# print(f"matrix[2][1]: {matrix[2][1]}")
# print(f"matrix[1][2]: {matrix[1][2]}")
#
# print("--------------------Access Lists With Modify---------------------------")
#
# matrix[2][1] = 70
# matrix[0][2] = 20
# matrix[1][1] = 40
#
# print('''
# matrix[2][1] = 70
# matrix[0][2] = 20
# matrix[1][1] = 40
# ''')
#
# print(f"matrix[2][1]: {matrix[2][1]}")
# print(f"matrix[0][2]: {matrix[0][2]}")
# print(f"matrix[1][1]: {matrix[1][1]}")

print("--------------------Access Lists Full Elements---------------------------")

matrix = \
[
   [1, 2, 3],
   [4, 5, 6],
   [7, 8, 9]
]

for row in matrix:
    for numbers in row:
         print(numbers)
