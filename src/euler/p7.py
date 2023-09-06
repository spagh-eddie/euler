"""Euler project problem 7"""


def find(n):
    # Finds the nth prime number
    def isdivisible(n, lst):
        return any(map(lambda x: n % x == 0, lst))

    lst, count, i = [2], 1, 2
    while count < n:
        if not isdivisible(i, lst):
            lst.append(i)
            count += 1
        i += 1
    return i - 1


def main() -> None:
    print(find(10001))


if __name__ == "__main__":
    main()
