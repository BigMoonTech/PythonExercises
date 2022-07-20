# Write a program (function!) that takes a list and returns a new list
# that contains all the elements of the first list minus all the duplicates.
#
# Extras:
# Write two different functions to do this - one using a loop and constructing
# a list, and another using sets.Go back and do Exercise 5 using sets, and
# write the solution for that in a different function.

li = ["Anna", "Bill", "Seyma", "Julee", "George", "Julee"]


def remove_duplicate_loop(collection):
    r_list = []
    for i in collection:
        if i not in r_list:
            r_list.append(i)
    return r_list


def remove_duplicate(collection):
    set_list = set(collection)
    return list(set_list)


new_list = remove_duplicate(li)
print()
