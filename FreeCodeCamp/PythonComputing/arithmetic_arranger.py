
def main():
    print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], False))


def arithmetic_arranger(operations, display_result=False):

    if len(operations) > 5:
        return "Error: Too many problems."

    # list of tuples (split the list of operations at whitespace)
    op_list = []

    # list of first terms only
    first_operands = []

    # list of second terms
    sec_operands = []

    # list of operators
    operators = []

    # list each operation's result
    results = []

    # list of the max lengths in an individual operation, used for formatting later
    max_lens = []

    # iterate through problems - extract values, save as a tuple, append tuple to op_list
    for operation in operations:
        op_list.append(tuple(operation.split()))  # ex output: [('32', '+', '698'), (and so on..)]

    # s1 through s4 represents the 3 or 4 lines to print
    s1 = ''
    s2 = ''
    s3 = ''

    if display_result:
        s4 = ''
    else:
        s4 = None

    # iterate over each tuple in op_list to get longest operand, and the math operator
    for op in op_list:

        if op[1] not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        else:
            # operator
            operator = op[1]

        if op[0].isnumeric() and op[2].isnumeric():
            # first term as int
            operand1 = int(op[0])
            # second term as int
            operand2 = int(op[2])
        else:
            return 'Error: Numbers must only contain digits.'

        if len(str(operand1)) > 4 or len(str(operand2)) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        # both terms as a string in a tuple
        both_terms = (str(operand1), str(operand2))

        # longest term is needed to track required whitespace
        max_len = len(max(both_terms, key=len))

        # append all the bits and pieces to the lists
        first_operands.append(operand1)
        sec_operands.append(operand2)
        operators.append(operator)
        max_lens.append(max_len)

        # actual math results appended to results list
        if operator == '+':
            results.append(operand1 + operand2)
        elif operator == '-':
            results.append(operand1 - operand2)

    # line 1 as one string
    for i, val in enumerate(first_operands):
        # right justify 1st operand: width is the longest term + 2 (+2 for the operator and a space), and 4 spaces
        s1 += str(val).rjust(max_lens[i] + 2) + '    '

    # line 2 as one string
    for i, val in enumerate(sec_operands):
        # operator + a space + the 2nd operand (r-justified with a width = to longest term), and 4 spaces
        s2 += operators[i] + ' ' + str(val).rjust(max_lens[i]) + '    '

    # line 3 as one string (the dashes)
    for i in range(len(operations)):
        s3 += ''.rjust(max_lens[i] + 2, '-') + '    '

        # line 4 as one string if required
        if display_result:
            s4 += str(results[i]).rjust(max_lens[i] + 2) + '    '

    # clean up trailing whitespace
    s1 = s1.rstrip()
    s2 = s2.rstrip()
    s3 = s3.rstrip()

    # if s4 is not None, clean trailing whitespace, and return the 4 lines as one string
    if s4:
        s4 = s4.rstrip()
        return f"{s1}\n{s2}\n{s3}\n{s4}"

    # if not display_result, return the 3 lines as one string
    return f"{s1}\n{s2}\n{s3}"


if __name__ == '__main__':
    main()
