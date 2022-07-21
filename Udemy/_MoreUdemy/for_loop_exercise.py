
# times = int(input("How many times do I have to tell you? "))

# for i in range(times):
#     print("Clean your room!")

for x in range(1,21):
    if x == 4 or x== 13:
        state = "unlucky!"
    elif x % 2 == 0:
        state = "even."
    else:
        state = "odd."
    print(f"{x} is {state}")