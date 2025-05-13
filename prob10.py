"""
prob10.py 

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import math

def num_is_prime(num: int):
    res = []
    for i in range(2, num):  
        is_prime = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            res.append(i)
    return sum(res)


if __name__ == '__main__':
    print(num_is_prime(2_000_000))


"""
Answer: 142,913,828,922
"""
