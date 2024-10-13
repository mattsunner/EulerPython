"""
Euler Project - Problem 6

The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is, (1+2+3+...+10)^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def sum_natural_squares(max_val):
    max_val += 1
    res_list = []

    for i in range(max_val):
        res_list.append(i**2)
    
    result = sum(res_list)

    return result


def square_natural_list(max_val):
    max_val += 1
    res_list = []

    for i in range(max_val):
        res_list.append(i)

    sum_list = sum(res_list)

    result = sum_list ** 2

    return result


# Calcualte the Answer
max_val = 100

answer = square_natural_list(max_val) - sum_natural_squares(max_val)
print(sum_natural_squares(max_val))
print(square_natural_list(max_val))
print(answer)


"""
Answer: 25,164,150 
"""

