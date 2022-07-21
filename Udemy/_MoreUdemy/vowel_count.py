
def vowel_count(string):
    a = string.lower().count("a")
    e = string.lower().count("e")
    i = string.lower().count("i")
    o = string.lower().count("o")
    u = string.lower().count("u")
    vowels = {
        "a": a,
        "e": e,
        "i": i,
        "o": o,
        "u": u
    }
    return {k:v for k,v in vowels.items() if v > 0}

print(vowel_count("aaaajjjjff"))