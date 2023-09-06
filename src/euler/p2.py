"""Euler project problem 2"""


def memoize(f):
    cache = {}

    def decorated_function(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]

    return decorated_function


@memoize
def fib(n):
    return n if n < 2 else fib(n - 2) + fib(n - 1)


def find(n):  # Find the sum of the even Fibonacci numbers less than n
    lst, x = [], 1
    while fib(x) < n:
        lst.append(fib(x))
        x = x + 1
    return sum([x for x in lst if x % 2 == 0])


def main() -> None:
    print(find(4000000))


if __name__ == "__main__":
    main()
