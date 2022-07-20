# Use open to access a file. open() is called a FILE HANDLE.
# Its like the handle of a coffee mug, you need to grab the handle to get
# what's inside, ie. the coffee/file contents
# The file handle is treated like a sequence in python. You can iterate through.


# create a file with the numbers 0-9 on each line
with open('file_example.txt', 'w') as fhand:
    for num in range(10):
        fhand.write(str(num)+'\n')

with open('file_example.txt', 'r') as fhand:
    # read the first line, strip the newline char
    line = fhand.readline().rstrip()

    # loop through the remaining lines
    while line != '':
        print('The line contents are: ' + line)
        line = fhand.readline().rstrip()
