
def repeat(string, num):
    st = ''
    if num == 0:
        return st
    for i in range(num):
        st += string
    return st


print(repeat("abc", 5))
