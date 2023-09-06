"""Euler project problem 3

One can reduce the problem of finding the primes of
a quotient and the primes of the divisor::

    primes(100) = [2] + primes(50)
                = [2, 2] + primes(25)
                = [2, 2, 5] + primes(5)
                = [2, 2, 5, 5]
"""


def find(n):
    tester = 2
    while tester * tester <= n:
        if n % tester == 0:
            n //= tester
            continue
        tester += 1
    return n


def main() -> None:
    print(find(600851475143))


def test_small():
    assert find(1) == 1
    assert find(10) == 5
    assert find(17) == 17
    assert find(25) == 5
    assert find(100) == 5
    assert find(600851475143) == 6857


if __name__ == "__main__":
    main()
