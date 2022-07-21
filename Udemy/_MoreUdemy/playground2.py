
# Write a Python program to count the values
# associated with a key in a dictionary

array = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Alex'}, {'id': 3, 'success': True, 'name': 'Alex'}]

def count_values(lis, key, search_term):
    res = [1 for item in lis if item.get(key) == search_term]
    return f"There are {len(res)} occurrences of '{search_term}' in the '{key}' category."

print(count_values(array, "name", "Alex"))