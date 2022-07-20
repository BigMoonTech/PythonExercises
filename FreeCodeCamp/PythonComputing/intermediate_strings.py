# Extract a single number from a string and convert to float

my_str = 'X-DSPAM-Confidence: 0.8475'


def extract_float(a_str):
    # Split the string into a list, default sep is a space
    li = a_str.split()

    for i in li:
        # try to convert the list item to a float
        try:
            num = float(i)
            return num
        except ValueError:
            pass
    # if no float in the string return none
    return None


print(extract_float(my_str))
