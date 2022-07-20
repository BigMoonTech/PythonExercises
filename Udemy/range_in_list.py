
li = [1, 2, 3, 4, 1]


def range_in_list(lis, start=0, end=None):
    list_len = len(lis)
    if end is None:
        total = sum([i for i in lis[start:]])
    elif end > list_len:
        total = sum([i for i in lis[start:list_len+1]])
    else:
        total = sum([i for i in lis[start:end+1]])
    return total


print(range_in_list(li, 1, 10))
