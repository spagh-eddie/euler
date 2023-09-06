"""Euler project problem 9"""


def find(n):
    """Finds Pythagorean triplets whose sum is n"""
    ispyth = lambda a: a[0] ** 2 + a[1] ** 2 == a[2] ** 2
    a, b, lst = 1, 1, []
    while a < n:
        while b < n:
            c = n - a - b
            lst.append([a, b, c])
            b += 1
        a, b = a + 1, a + 1
    return [x for x in lst if ispyth(x)]


def main() -> None:
    print(find(1000))


if __name__ == "__main__":
    main()
