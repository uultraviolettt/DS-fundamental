# Implement recursive sum of the list


def recursive_list_sum(data_list):
    if not isinstance(data_list, list) : return data_list

    sum = 0

    for x in data_list:
        sum += recursive_list_sum(x)
    return sum


print('The sum of a list is ', recursive_list_sum([1, 2, [3, 4], [5, 6], [7, 8, 9, [10]]]))
