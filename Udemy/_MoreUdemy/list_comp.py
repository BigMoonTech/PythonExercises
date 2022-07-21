#List Comprehension vs. looping: 
# Problem solved - Count all the letters in a list of words then return a new array of those numbers
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
char_count_colors = []


#for-loop version
for i in range(len(colors)):
    word_length = len(colors[i])
    char_count_colors.append(word_length)

print(char_count_colors) #[3, 6, 6, 5, 4, 6, 6]






shapes = ["square", "circle", "triangle", "geometric"]

#List comprehension version
char_count_shapes = [len(shape[:]) for shape in shapes]

print(char_count_shapes) #[6, 6, 8, 9]





#Nested list comprehension

numbers = [["X" if num == 1 else "O" for num in range(3)] for val in range(3)]

print(numbers)
print(numbers[0][0])

