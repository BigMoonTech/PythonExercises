from passgen import passgen

# Write a password generator in Python. Be creative with how you generate passwords
# strong passwords have a mix of lowercase letters, uppercase letters, numbers,
# and symbols. The passwords should be random, generating a new password every
# time the user asks for a new password. Include your run-time code in a main method.
#
# Extra:
# Ask the user how strong they want their password to be. For weak passwords, pick
# a word or two from a list.


def main():

    while True:
        print("How strong do want your password to be?")
        strength = input("Input a number from 1 to 3: ")

        if strength == "1":
            pw = passgen(length=8, digits=False, case='lower')
        elif strength == "2":
            pw = passgen()
        else:
            pw = passgen(length=16, punctuation=True)
        print(f"Generated Password: {pw}")

        prompt = input("Again? ('q' to quit): ")

        if prompt == "q":
            exit()


if __name__ == "__main__":
    main()
