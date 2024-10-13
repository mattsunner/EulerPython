"""
Euler Project - Problem 6

The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is, (1+2+3+...+10)^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


class SquareDiff:
    def __init__(self, max_val: int):
        self.max_val = max_val


    def sum_natural_squares(self):
        max_val = self.max_val + 1
        res_list = []

        for i in range(max_val):
            res_list.append(i**2)
        
        result = sum(res_list)

        return result


    def square_natural_list(self):
        max_val = self.max_val + 1
        res_list = []

        for i in range(max_val):
            res_list.append(i)

        sum_list = sum(res_list)

        result = sum_list ** 2

        return result

    
    def final_answer(self):
        return self.square_natural_list() - self.sum_natural_squares()


# Calcualte the Answer
max_val = 100

answer = SquareDiff(max_val)
print(answer.final_answer())


"""
Answer: 25,164,150 
"""

