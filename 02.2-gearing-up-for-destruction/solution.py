import numpy as np
from fractions import Fraction

def all_gears_sizes_at_least_one(pegs, r):
    for i in range(0, len(pegs) -1):
        if r < 0 or pegs[i+1] - pegs[i] - r < 1:
            return False
        r = pegs[i+1] - pegs[i] - r
    return True

def solution(pegs):
    impossible = [-1, -1]
    num_pegs = len(pegs)
    # peg-coefficients for calculation of r0
    coef = np.ones(num_pegs)
    coef[1:-1] += 1
    coef[::2] *= -1
    coef *= pegs
    coef = np.array([Fraction(coef[i]) for i in range(num_pegs)])

    r0 = np.sum(coef)
    if num_pegs % 2 == 0:
        even = True
        multiplier = Fraction(2, 3)
    else:
        even = False
        multiplier = Fraction(2)
    r0 *= multiplier

    if r0 < 1:
        return impossible
    elif all_gears_sizes_at_least_one(pegs, r0):
        return [r0.numerator, r0.denominator]
    return impossible



if __name__ == "__main__":
    solution([4, 30, 50]) #12,1

    solution([4, 17, 50]) #-1,-1
