ints = [1, 4, 2, 5, 3]


def two_oldest(li):
    sort_list = sorted(li)
    return [sort_list[-2], sort_list[-1]]


print(two_oldest(ints))
