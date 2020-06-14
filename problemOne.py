"""
Euler Project - Problem One

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

https://projecteuler.net/problem=1

"""

def main():
    count = 0
    max = 1000
    solutionList = []
    while (count < max):
        if count % 3 == 0:
            solutionList.append(count)
        elif count % 5 == 0:
            solutionList.append(count)
        else:
            pass
        count = count + 1

    print(sum(solutionList))

if __name__ == '__main__':
    main()


"""
The Result is: 233,168
"""