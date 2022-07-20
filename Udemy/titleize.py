
def titleize(sentence):
    """
    Capitalize the first letter of a string of words
    :param sentence: a sentence
    :return: new string
    """
    li = sentence.split()
    li2 = []
    s = " "
    for item in li:
        i = item[0].upper() + item[1:]
        li2.append(i)
    return s.join(li2)


print(titleize("the good the bad and the ugly"))  # --> The Good The Bad And The Ugly
