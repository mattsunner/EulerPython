"""
Problem Seven

Calculate the 1,000th Prime number

"""

import sys

class PrimeCalc:
    def __init__(self, nth_prime):
        self.nth_prime = nth_prime

    def calculate(self):
        primes = []
        num = 2
        while len(primes) < self.nth_prime:
            for prime in primes:
                if num % prime == 0:
                    break
            else:
                primes.append(num)
            num += 1
        return primes[-1]


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: Include a Number of Prime Desired")
        sys.exit(1)

test_val = int(sys.argv[1])

calc = PrimeCalc(test_val)
print(calc.calculate())

"""
Answer: 104,743
"""
