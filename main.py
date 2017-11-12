from random import randint
import argparse

composite = 'composite'
inconclusive = 'inconclusive'

parser = argparse.ArgumentParser(description="Miller Rabin Algorithm")
parser.add_argument('-n', help='Number to be checked if it is prime')  # number
parser.add_argument('-t', help='Number of trials')
args = parser.parse_args()


def divide_by(dividend, divisor):
    """
    find k and q values,
    where k is number of 'divisor' in dividend
    and q which hasn't consisted divisor in it
    :param dividend:
    :param divisor:
    :return: k and q
    """
    k = 0
    while dividend % divisor == 0:
        k += 1
        dividend /= divisor
    return k, dividend


def miller_rabin_algorithm(n):
    """
    miller rabin algorithm which decides given integer is prime or not.
    :param n: given integer
    :return: return 'composite' or 'inconclusive'
    """
    k, q = divide_by(n - 1, 2)
    a = randint(2, n - 2)
    temp = pow(a, q, n)
    if temp == n - 1 or temp == 1:
        return inconclusive
    for j in xrange(1, k):
        power = pow(2, j) * q
        temp = pow(a, power, n)
        if temp == 1:
            return composite
        if temp == n - 1:
            return inconclusive
    return composite


if __name__ == '__main__':
    n = int(args.n) if args.n is not None else None
    t = int(args.t) if args.t is not None else 1

    result = 'composite'
    found = False
    if n is None:
        while not found:
            n = randint(5, pow(2, 1024))
            temp_result = miller_rabin_algorithm(n)
            if temp_result == inconclusive:
                found = True
                break

    while t > 0:
        temp_result = miller_rabin_algorithm(n)
        if temp_result == composite:
            result = temp_result
            break
        else:
            result = inconclusive
        t -= 1

    print result, n
