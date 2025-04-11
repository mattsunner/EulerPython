"""
prob9.py 

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1,000.
Find the product abc.

"""

if __name__ == '__main__':
    for a in range(1, 998):
        for b in range(a+1, 999):
            for c in range(b + 1, 1000):
                if a+b+c==1000 and a < b < c and a**2 + b**2 == c**2:
                    print(a*b*c)
    
"""
Answer: 31,875,000
"""