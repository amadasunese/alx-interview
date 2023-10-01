#!/usr/bin/python3
"""
Function that returns Pascal’s triangle
"""
def pascal_triangle(n):
    """
    Pascal triangle
    """
    if n <= 0:
        return []
    
    # Pascal's Triangle first row.
    triangle = [[1]]
    
    # Remaining rows.
    for i in range(1, n):
        row = [1]
        prev_row = triangle[i - 1]
        
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        
        row.append(1)
        triangle.append(row)
    
    return triangle
