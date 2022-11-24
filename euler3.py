def find(n): # Find the largest prime factor of n
    from math import sqrt
    def isprime(x):
        i = 2
        while i < int(sqrt(x)):
            if x%i==0:
                return False
            i += 1
        return True
    factors, i = [1], 2
    while i < int(sqrt(n)):
        if n%i==0 and isprime(i):
            factors.append(i)
        i += 1
    return max(factors)
