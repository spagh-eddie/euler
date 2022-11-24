def find(n):
    #Find the largest palindrome from the product of two n-digit numbers
    def ispalindrome(i):
        i = str(i)
        if len(i) < 2:
            return True
        first, last = i[0], i[-1]
        if first == last:
            return ispalindrome(i[1:-1])
        return False
    i, j, lst = 1, 1, []
    while i < 10**n:
        while j < 10**n:
            lst.append(i*j)
            j += 1
        i, j = i + 1, 1
    return max([x for x in lst if ispalindrome(x)])
