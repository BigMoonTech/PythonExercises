
def truncate(string, num):
    if num >= 3:
        st = ""
        if len(string) >= num:
            for i in range(num-3):
                st += string[i]
            st += "..."
        else:
            return string
        return st
    else:
        return "Truncation must be at least 3 characters."


print(truncate("Another test", 12))
