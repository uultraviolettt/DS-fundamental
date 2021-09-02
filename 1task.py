# Implement function str_to_dict(some_str) which returnes dictionary,
# where keys are string characters, and values are their quantity in the string
def str_to_dict(some_str):
    result = list(some_str)
    dict_res = dict((x, result.count(x)) for x in set(result) if result.count(x) >= 1)

    return dict_res


print('Str to dict:', str_to_dict('dataroot_university'))
