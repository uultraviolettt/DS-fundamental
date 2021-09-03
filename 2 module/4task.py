#Implement function max_sum_index(tuples), which returnes index
# of tuple in the list with maximum sum of elements


def max_sum_index(tuples):
    '''
    :param tuples: list[tuple]
    :return: int
    '''
    # YOUR CODE HERE
    index = tuples.index(max(tuples, key=sum))
    return index

print('Index: ', max_sum_index([(10, 20, 1, 2), (51, 32), (30, 25, 5)]))
print('Index: ', max_sum_index([(47, 22, 11), (23, 17)]))