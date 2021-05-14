
def pos_sign():
    for a in range(5):
        if a == 2:
            print("+ + + + +")
        else:
            print("    +")


def neg_sign():
    for a in range(3):
        print("- - - - -")


word = "key"
guess = ""
count = 0
wrong_guess = False
limit = 5

while guess != word and not wrong_guess:
    if count < limit:
        guess = input("Give a try: ")
        count += 1
    else:
        wrong_guess = True

if wrong_guess:
    print("ahh, you lost the game!")
    print(neg_sign())
else:
    print("Congrats")
    print(pos_sign())


