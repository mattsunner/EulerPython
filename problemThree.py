"""
Euler Project - Problem Three

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

https://projecteuler.net/problem=3

"""

base = 600851475143
factors = []
primes = []


def factor_func():
    for i in range(base):
        r = base / (i+1)
        if r.is_integer():
            factors.append(r)
        i += 1 

def main():
    factor_func()
    for factor in factors:
        if (base % factor) == 0:
            print(factor)
     
        


if __name__ == '__main__':
    main()


"""
The Result is:
"""