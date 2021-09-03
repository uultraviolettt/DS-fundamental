#Implement function gcd(x, y), which returns the greatest common divisor of n and m

def gcd(x, y):
    '''
    :params m,n: int
    :return: int
    '''
    # YOUR CODE HERE
    while y != 0:
        (x, y) = (y, x % y)
    return x

print('GCD: ', gcd(160, 180))