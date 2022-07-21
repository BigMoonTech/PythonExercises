#custom for loop

def my_for(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            i = next(iterator)
        except StopIteration:
            break
        else:
            func(i)


def square(num):
    print(num * num)

my_for("hello there!", print)
my_for([1,2,3,4,5], square)