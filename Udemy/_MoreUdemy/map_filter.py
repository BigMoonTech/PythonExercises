
# return a list of strings uppercased using map() 

my_pets = ['alfred', 'tabitha', 'william', 'arla']

def make_upper(collection):
    return list(map(lambda name: name.upper(), collection))

print(make_upper(my_pets))

# Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda

ran_nums = [13, 15, 19, 22, 28, 234, 213, 343, 12, 26]

def divisible_19_13(collection):
    li = list(filter(lambda num: num % 13 == 0 or num % 19 == 0, collection))
    result = ""
    for i in li:
        result += ".." + str(i)
    return result

    # stringed_li = [str(i) for i in li]
    
    # for i in range(len(stringed_li)):
    #     result += "..." + stringed_li[i]
    # return "The nums divisble by 13 or 19 are:{}".format(result)

print(divisible_19_13(ran_nums))