def find(n):
    """Finds the sum of all primes below n"""
    assert n >= 2
    def isprime(n):
        if n < 2:
            return False
        from math import sqrt
        i = 2
        while i <= sqrt(n):
            if n%i==0:
                return False
            i += 1
        return True
    lst = list(range(n))
    lst.pop()
    return sum([x + 1 for x in lst if isprime(x + 1)])
