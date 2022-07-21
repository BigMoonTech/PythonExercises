
# copy('story.txt', 'story_copy.txt') # None
# expect the contents of story.txt and story_copy.txt to be the same


def copy(original_file, copied_file):
    with open(original_file, "r") as file_01:
        text = file_01.readlines()
    with open(copied_file, "w") as copied:
        copied.writelines(text)


def copy_and_reverse(original_file, reversed_file):
    with open(original_file) as read_file:
        read = read_file.read()
    with open(reversed_file, "w") as write_file:
        write_file.write(read[::-1])


def statistics(file_name):
    with open(file_name) as in_file:
        read_lines = in_file.readlines()
        lines = len(read_lines)
        chars = sum(len(line) for line in read_lines)
        words = sum(len(line.split(" ")) for line in read_lines)
    return {"lines" : lines, "words" : words, "characters" : chars}


def find_and_replace(filename, search_term, replacement):
    with open(filename) as in_file:
        file_str = in_file.read()
    with open(filename, "w") as write_file:
        write_file.write(
            file_str.replace(search_term, replacement)
        )
