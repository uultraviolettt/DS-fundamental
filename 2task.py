# Implement function sec_smallest(numbers) which
# returns second smallest item in the list,
# without using the built-in sorting methods
# (your code mustn't contain such words as 'sort', 'sorted')

def sec_smallest(numbers):

    numbers = [x for x in numbers if x != min(numbers)]  # deletes the min element from the list
    result = (min(numbers))

    return result


print('Sec_smallest: ', sec_smallest([1, 2, -8, -8, -2, 0]))