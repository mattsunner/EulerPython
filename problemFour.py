"""
Euler Project - Problem Four

A palindromic number reads the same both ways. The largest palindrome made from the product of two -digit numbers is .

Find the largest palindrome made from the product of two -digit numbers.

https://projecteuler.net/problem=4

"""

def num_generator() -> list:
    products = []

    x = 100
    y = 100

    while x <= 999:
        while y <= 999:
            res = x * y
            products.append(res)
            y += 1
        x += 1
        y = 100

    return products

def palindrome_finder(nums: list) -> list:
    results = []

    for num in nums: 
        numstr = str(num)
        if numstr == numstr[::-1]:
            results.append(num)
    
    return results

if __name__ == '__main__':
    res = palindrome_finder(num_generator())
    print(max(res))

"""
Answer: 906609
"""
