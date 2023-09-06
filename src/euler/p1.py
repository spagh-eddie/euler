"""Euler project problem 1

Find the sum of all the multiples of 3 or 5 below 1000.

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get
3, 5, 6, and 9. The sum of these multiples is 23.

The naive solution would be to do::

    total = 0
    for k in range(10):
        if k % 3 == 0 or k % 5 == 0:
            total += k

However, this takes ``O(n)`` time.

It can instead be done by recognizing a pattern in counting pips::

             .
            ..
           ...
          ....
         .....
        ......
       .......
      ........
     .........
    0--3-56--9

There will be ``n//3`` multiples of 3 and ``n//5`` multiples of 5.
This double-counts the multiples of 15, of which there are ``n//15``

The total number of pips in these sequences can be calculated as a triangular number
https://en.wikipedia.org/wiki/Triangular_number.
"""


def triangle(n):
    """Triangular number of n"""
    return (n * n + n) // 2


def find(n) -> int:
    n -= 1
    return 3 * triangle(n // 3) + 5 * triangle(n // 5) - 15 * triangle(n // 15)


def main() -> None:
    print(find(1000))


def test_10():
    assert find(10) == 23


def test_100():
    assert find(100) == 2318


if __name__ == "__main__":
    main()
