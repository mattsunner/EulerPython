"""
Problem Seven

Calculate the 1,000th Prime number

"""

class PrimeCalc:
    def __init__(self, nth_prime):
        self.nth_prime = nth_prime

    
    def calculate(self):
        lower = 1
        range_val = self.nth_prime
        primes = []
       
        for num in range(lower, range_val + 1):
           if num > 1:
               for i in range(2, num):
                    if (num % i) == 0:
                        break
                    else:
                        print(num)

        
test_val = 1000

calc = PrimeCalc(test_val)

print(calc.calculate())


"""
Answer: 
"""
