
# list of dictionaries
dict_list = [{'First Name': 'John', 'Last Name': 'Jacobs'},
         {'First Name': 'Daryl', 'Last Name': 'Farmers'},
         {'First Name': 'Josh', 'Last Name': 'Aguilar'}]

# enumerate adds a counter to an iterable
# enumerate is an iterator so we can't access the values by index
# so instead, we use python's argument unpacking feature ie. index, elem
for index, elem in enumerate(dict_list):
    print(index, elem)