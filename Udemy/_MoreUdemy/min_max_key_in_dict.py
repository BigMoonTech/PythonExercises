
d = {2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'}


def min_max_key_in_dictionary(dictionary):
    min_key = min(dictionary.keys())
    max_key = max(dictionary.keys())
    return [min_key, max_key]


print(min_max_key_in_dictionary(d))
