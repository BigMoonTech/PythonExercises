
print("hey, how's it going")

action = True

while action:
    speech = input().lower()
    if speech == "":
        print("......")
    elif speech == "stop" or speech == "quit" or speech == "stop copying me":
        print("UGH, fine...")
        action = False
    else:
        print(speech.upper())