# Implement function prime_nums(n) that returns list of numbers which are simple and < n

def prime_nums(n):
    a = range(2, n + 1)
    b, c = [], a
    while c[0] * c[0] < n:
        firstElement = c[0]
        b += [firstElement]
        c = [x for x in c if x % firstElement != 0]
        res = b + c
    return res


print('Prime numbers: ', prime_nums(30))


#Prime numbers:	[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
