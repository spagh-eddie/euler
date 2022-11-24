def find(n, number):
    """Find the n adjacent digits that create the greatest product in number"""
    import functools
    number = list(map(int, str(number)))
    partitions = [number[i:i+n] for i in range(len(number) - (n-1))]
    return max(partitions, key = lambda lst: functools.reduce(lambda x,y:x*y, lst))
