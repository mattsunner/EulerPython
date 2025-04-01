"""
Euler Project - Problem Three

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?

https://projecteuler.net/problem=3

"""
num = 20

def prime_factors(n):
    factor_list = []
    div = 2

    while n >1:
        while n % div == 0:
            factor_list.append(div)
            n //= div
        div += 1
    
    return factor_list


if __name__ == '__main__':
    num = 600851475143
    
    prime_list = prime_factors(num)

    print(max(prime_list))

"""
The Result is: 6857
"""
