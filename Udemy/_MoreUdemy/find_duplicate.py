# Write a function called find_the_duplicate() which accepts an array of numbers containing a single duplicate.
# The function returns the number which is a duplicate or None if there are no duplicates.


def find_the_duplicate(int_list):
    for i in int_list:
        if int_list.count(i) > 1:
            return i
    return None


print(find_the_duplicate([1, 2, 3, 3]))
