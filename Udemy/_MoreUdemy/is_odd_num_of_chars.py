
string_1 = "amazing"


# def is_odd_string(string):
#     for i, v in enumerate(string):
#         total = i
#     if total % 2 == 0:
#         return False
#     return True


def is_odd_string(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    li = [alphabet.index(char) + 1 for char in string]
    return bool(sum(li) % 2)


print(is_odd_string(string_1))
