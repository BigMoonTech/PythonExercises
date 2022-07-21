# function vs. generator function
# generator uses yield instead of return
# generator can yield multiple times


# This is a generator function, and is not in itself a generator
# but returns a generator object
def count_up_to(max):
    count = 1
    while count < max:
        # yield is what creates and returns the generator
        yield count
        count += 1

# counter is a generator
counter = count_up_to(10)
print(counter)




# beat maker generator

def current_beat():
    tempo = 1
    while True:
        yield tempo
        if tempo == 4: tempo = 0
        tempo += 1

beat = current_beat()

print(next(beat))
print(next(beat))
print(next(beat))
print(next(beat))
print(next(beat))




# 99 bottles song

def make_song(count=99, beverage="soda"):
    while count > -1:
        if count > 1:
            yield "{} bottles of {} on the wall.".format(count, beverage)
        elif count == 1:
            yield "Only 1 bottle of {} left!".format(beverage)
        else:
            yield "No more {}!".format(beverage)
        count -= 1

song = make_song(3)

print(next(song))
print(next(song))
print(next(song))
print(next(song))
print(next(song))
