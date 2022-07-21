# Create a lambda function that adds 15 to a given number 
# passed in as an argument. Also, create a lambda function 
# that multiplies argument x with argument y and print the result.


add_15 = lambda x: x + 15
multiply = lambda x,y: x * y


print(add_15(15))
print(multiply(10,10))




# Write a Python program to sort a list of tuples using Lambda


tuple_list = [(1,1), (2,2), (4,4), (3,3)]

tuple_list.sort(key = lambda x: x[1])


print(tuple_list)




# Write a Python program to sort a list of dictionaries using Lambda


dict_list = [{"name": "jenny", "age": 33}, {"name": "tom", "age": 11}, {"name": "jerry", "age": 3}]

dict_list.sort(key = lambda x: x["age"])


print(dict_list)




# Write a Python function to seperate evens & odds
# from a list of integers using Lambda. Return a tuple. 


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def seperate_even_vals(nums):
    evens = list(filter(lambda x: x % 2 == 0, nums))
    odds = list(filter(lambda x: x % 2 != 0, nums))
    return tuple([odds] + [evens])


print(seperate_even_vals(nums))




# Write a Python program that removes the positive numbers
# from a given list of numbers. Sum the negative numbers 
# and print the absolute value using lambda function. 
# Print the result.


negative_nums = [-1, -3, 3, 2, 1, 30, 0, 1]


def exercise_func(nums):
    negatives = list(filter(lambda x: x < 0, nums))
    total = sum(negatives)
    return abs(total)


print(remove_neg_sum_pos(negative_nums))
