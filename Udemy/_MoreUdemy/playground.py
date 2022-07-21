import operator

def single_letter_cost(word, letter):
    word_list = [char for char in word.lower()]
    return word_list.cost(letter)

# print(single_letter_cost("Hello World", "h"))


colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

def list_manipulation(list, command, location, value):
    if command == "remove" and location == "end":
        return list.pop()
    elif command == "remove" and location == "beginning":
        return list.pop(0) 
    elif command == "add" and location == "end":
        list.insert(0, value)
    elif command == "add" and location == "beginning":
        list.append(value)
    return list

# print(list_manipulation(colors, "add", "beginning", "razzberry"))
# print(list_manipulation(colors, "add", "end", "cream"))
# print(list_manipulation(colors, "remove", "beginning", "blue"))
# print(list_manipulation(colors, "remove", "end", "green"))

def is_palindrome(string):
    stripped = string.replace(" ", "")
    return stripped == stripped[::-1]

# print(is_palindrome("race car"))


def calculate(**kwargs):
    
    operation_dict = {
        "add": kwargs["first"] + kwargs["second"],
        "subtract": kwargs["first"] - kwargs["second"],
        "multiply": kwargs["first"] * kwargs["second"],
        "divide": kwargs["first"] / kwargs["second"]
    }
    
    if kwargs["second"] == 0:
       return "Error. Cannot divide by zero."
       
    is_float = kwargs["make_float"]
        
    if not is_float:
        return "{} {}".format(kwargs.get("message", "The result is"), int(operation_dict[kwargs["operation"]]))
    else:
        return "{} {}".format(kwargs.get("message", "The result is"), operation_dict[kwargs["operation"]])


# print(calculate(make_float=False, operation='add', message='You just added', first=2, second=4))
# print(calculate(make_float=True, operation='divide', first=3.5, second=5))

dict1 = {
    "name1": "Dave",
    "name2": "Joe",
    "name3": "Zach",
    "name4": "Avery"
}

def sort_by_value(_, action = "ascending"):
    if action == "descending":
        return dict(sorted(_.items(), key = operator.itemgetter(1), reverse=True))
    else:
        return dict(sorted(_.items(), key = operator.itemgetter(1)))

# print(sort_by_value(dict1))
# print(sort_by_value(dict1, "descending"))

def is_all_strings(lis):
    return all(type(i) == str for i in lis)

# print(is_all_strings(colors))

num_list_1 = [1, 2, 3, 4, 5, 6]
num_tuple = (4, 3, 55, 22, 64, 1)

def extremes(i):
    return (min(i), max(i))

# print(extremes(num_tuple))


# interwoven strings. if strings aren't the same length weird things happen
def interleave(str1, str2): 
    return "".join(["".join(i) for i in tuple(zip(str1, str2))])

print(interleave("htee", "ihr!"))

names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]

def extract_full_name(lis):
    # return list(map(lambda names: names.get("first") + " " + names.get("last"), lis))
    return [dictionary.get("first") + " " + dictionary.get("last") for dictionary in lis]

print(extract_full_name(names))

