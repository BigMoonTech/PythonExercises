
def list_check(array):
    for i in array:
        if type(i) != list:
            return False
    return True


ary = [[2], 3, 5, [4]]
ary2 = [[2], [3], [5], [4]]
print(list_check(ary))
