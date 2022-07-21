
def sum_pairs(arry, num):
    ary = []
    for i in arry:
        for x in arry[:i:]:
            if i + x == num:
                ary.append(i)
                ary.append(x)
                break
        if len(ary) == 2:
            break
    arry = ary
    return arry


print(sum_pairs([4,2,10,5,1], 6))