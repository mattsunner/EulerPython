""" 
Euler Project - Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

https://projecteuler.net/problem=5

"""

test_num = 1

while True:
    if test_num % 20 == 0:
        if test_num % 19 == 0:
            if test_num % 18 == 0:
                if test_num % 17 == 0:
                    if test_num % 16 == 0:
                        if test_num % 15 == 0:
                            if test_num % 14 == 0:
                                if test_num % 13 == 0:
                                    if test_num % 12 == 0:
                                        if test_num % 11 == 0:
                                            print(f'Result Found: {test_num}')
                                            break
    test_num += 1


""" 
Answer: 232,792,560 

Note: this is a TERRIBLE solution...
"""
