"""Euler project problem 5"""


def find(n):
    # Finds the smallest positive number divisible by 1 through n
    def divisible(n, lst):
        return all(map(lambda x: n % x == 0, lst))

    test, under = n, list(range(n))
    for i in range(n):
        under[i] += 1
    while not divisible(test, under):
        test += 1
    return test


def main() -> None:
    print(find(20))


if __name__ == "__main__":
    main()
