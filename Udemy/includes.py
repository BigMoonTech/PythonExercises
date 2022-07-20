
li = [1, 2, 3, 4]
di = {"key01": "bug", "key02": "love", "key03": "smells good"}
st = "Josh"


def includes(collection, val, start=None):
    """
    iterate through a collection and see if a specified value is within the collection
    :param collection: list, dict, or str
    :param val: value to search for
    :param start: (optional) starting value; ignored for dicts
    :return: boolean representing value in collection or not in collection
    """
    if type(collection) == dict:
        return val in collection.values()
    if start is None:
        return val in collection
    return val in collection[start:]


print(includes(li, 4, 2))
