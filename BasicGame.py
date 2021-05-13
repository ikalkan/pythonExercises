
print("Welcome to the game")
name = input("What is your name buddy? ")
age = int(input("How old are you child? "))

health = 10

if age >= 18:
    print("Cool! You are not a child. ")

    wannaPlay = input("Are you ready to play? (Yes or No) ").upper()

    if wannaPlay == "YES":
        print("OK let's go!")
        print("Remember: Your health = ", health)

        direction = input("Which direction do you wanna follow? (Right or Left) ").upper()
        if direction == "RIGHT":
            answer = input("Well, you reach a lake. Do you swim across or go around? (Across or Around) ").upper()

            if answer == "AROUND":
                print("Nice choice. You reached the other side")
            elif answer == "ACROSS":
                print("Well, you reached the other side but you lost 5 health")
                health -= 5

            answer = input("There is a house and a river. Select one: ( River or house)").upper()
            if answer == "HOUSE":
                print("You came the house and get attacked. You lose 5 health")
                health -= 5

                if health <= 0:
                    print("You have 0 health. You lost the game.")
                else:
                    print("Congrats! You win! ")
            else:
                print("Sorry, you fell in the river.")
        else:
            print("Sorry you lost!")

    else:
        print("Go away child!")
else:
    print("Go away child! I don't wanna see you around! ")
