
# create a (F) that accepts a list and returns a new list
# with every second value removed


def remove_every_other(array):
    count = 0
    ary = []
    while count < len(array):
        ary.append(array[count])
        count += 2
    array = ary
    return array


ary = [1, 2, 3, 4, 5, 6]
ary2 = [5, 1, 2, 4, 1, 6, 7]
print(remove_every_other(ary2))