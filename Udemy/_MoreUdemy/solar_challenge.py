import math


# original solution
def solution(area):
    area_in_squares = []
    if area < 1 or area > 1000000:
        raise ValueError("Out of bounds.")
    while(area >= 1):
        area_sqrt = math.sqrt(area)
        if not area_sqrt.is_integer():
            area_sqrt = int(area_sqrt)
            item = area_sqrt**2
            area_in_squares.append(item)
            area -= item
        elif area == 1:
            area_in_squares.append(1)
            break
        else:
            area_in_squares.append(area)
            break
    return area_in_squares


# refactored solution using a lambda for practice
def solution_(area):
    area_in_squares = []
    sqrt = lambda x: math.sqrt(x)
    area_sqrt = sqrt(area)
    if area < 1 or area > 1000000:
        raise ValueError("Out of bounds.")
    while not area_sqrt.is_integer():
        item = int(area_sqrt)**2
        area_in_squares.append(item)
        area -= item
        area_sqrt = sqrt(area)
    if area_sqrt.is_integer():
        area_in_squares.append(area)
    return area_in_squares


print(solution_(241))


# Shorter solution I found online (refactored). It's bookmarked in Safari: solving google foobar challenges
def answer(area):
    if(area > 1000000 or area < 1):
        raise ValueError('Area is outside of bounds')
    area_in_squares = []
    while(area != 0):
        res = int(math.sqrt(area))
        area_in_squares.append(res*res)
        area -= res*res
    return area_in_squares


# print(answer(12))
