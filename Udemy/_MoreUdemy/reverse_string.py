
def reverse_string(string):
    reversed_str = ""
    for ltr in string[::-1]:
        reversed_str += ltr
    return reversed_str

print(reverse_string("race car"))