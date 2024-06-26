#!/usr/bin/python3
''' A module that returns a list of lists of
   integers representing the Pascal’s triangle of n
'''


def pascal_triangle(n):
    '''Creates a list of lists of integers representing
    the Pascal's triangle of given integer.
    '''
    triangle = []
    if type(n) is not int or n <= 0:
        return triangle
    for i in range(n):
        line = []
        for k in range(i + 1):
            if k == 0 or k == i:
                line.append(1)
            elif i > 0 and k > 0:
                line.append(triangle[i - 1][k - 1] + triangle[i - 1][k])
        triangle.append(line)
    return triangle
