#!/usr/bin/python3
""
A function that returns a list of lists of integers
""
def pascal_triangle(n):
    if n <= 0:
        return []

    # Initialize the Pascal's Triangle with the first row.
    triangle = [[1]]

    # Generate the remaining rows.
    for i in range(1, n):
        row = [1]  # Each row starts with 1.
        prev_row = triangle[i - 1]

        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])  # Calculate the next value.

        row.append(1)  # Each row ends with 1.
        triangle.append(row)

    return triangle

# Test the function with n = 5 (you can replace this with any desired value).
n = 5
result = pascal_triangle(n)
for row in result:
    print(row)
