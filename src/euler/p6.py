"""Euler project problem 6"""


def find(n):
    # Find the difference between the sum of squares and square of sums of 1...n
    lst = list(range(n))
    for i in range(n):
        lst[i] += 1
    return sum(lst) ** 2 - sum(map(lambda x: x**2, lst))


def main() -> None:
    print(find(100))


if __name__ == "__main__":
    main()
