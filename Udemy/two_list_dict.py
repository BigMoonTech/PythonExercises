
li1 = ["one", "two", "three", "four"]
li2 = [1, 2]


def two_list_dictionary(keys, values):
    if len(keys) <= len(values):
        dict_from_li = dict(zip(keys, values))
    else:
        for i in range(len(keys) - len(values)):
            values.append(None)
        dict_from_li = dict(zip(keys, values))
    return dict_from_li


print(two_list_dictionary(li1, li2))
