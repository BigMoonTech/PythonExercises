
def eat(food, is_healthy):
    if not is_healthy:
        return f"I'm eating {food}, because I don't care about my body right now"
    else:
        return f"I'm eating {food}, because it is healthy"


def nap(nap_len):
    if nap_len > 2:
        return "I napped for too long and now I feel more tired"
    elif 0 < nap_len <= 2:
        return "I love this length of nap"
    else:
        return "Can't have a negative/zero nap!"