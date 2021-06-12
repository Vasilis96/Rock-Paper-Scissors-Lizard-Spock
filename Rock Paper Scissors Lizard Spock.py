import random

Total_Pick = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

Random_Pick = random.choice(Total_Pick)

loop = True

print("Hello! My name is Sheldon Cooper and this is the classic game 'Rock Paper Scissors Lizard Spock'. The rules are quite simple. \n"
    "Scissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons Spock, Spock smashes scissors, scissors decapitates lizard, \n"
    "lizard eats paper, paper disproves Spock, Spock vaporizes rock, and as it always has, rock crushes scissors. \n"
    "Pick one of the following options and let's see who'll win! \n")



while loop:                             ###<---Infinite loop that allows game to be played again
    User_Input = input("[1] : Rock \n"
        "[2] : Paper \n"
        "[3] : Scissors \n"
        "[4] : Lizard \n"
        "[5] : Spock \n"
        "[6] : Exit \n")

    while User_Input != '1' and User_Input != '2' and User_Input != '3' and User_Input != '4' and User_Input != '5' and User_Input != '6':
        User_Input = input("You have to choose one of the following options: \n"
        "[1] : Rock \n"
        "[2] : Paper \n"
        "[3] : Scissors \n"
        "[4] : Lizard \n"
        "[5] : Spock \n"
        "[6] : Exit \n")

    if  Random_Pick is 'Rock':
        if User_Input is '1':
            print("Oh look at that! I chose", Random_Pick, "too!")
        elif User_Input is '2':
            print("Paper covers", Random_Pick, "and I chose", Random_Pick, ". So I guess you win!")
        elif User_Input is '3':
            print("I chose", Random_Pick, ". And as it always has, rock crushes scissors.")
        elif User_Input is '4':
            print("I chose", Random_Pick, "." ,Random_Pick, "crushes lizard.")
        elif User_Input is '5':
            print("I chose", Random_Pick, ". Spock vaporizes Rock.")
        elif User_Input is '6':
            exit()
        else:
            pass

    elif Random_Pick is 'Paper':
        if User_Input is '1':
            print("Paper covers", Random_Pick, "and I chose", Random_Pick, ". So I guess I win!")
        elif User_Input is '2':
            print("Oh look at that! I chose", Random_Pick, "too!")
        elif User_Input is '3':
            print("I chose", Random_Pick, ". Scissors cuts", Random_Pick, "so congratulations.")
        elif User_Input is '4':
            print("Damn! Lizard eats", Random_Pick, "and I chose", Random_Pick,", I lose.")
        elif User_Input is '5':
            print("I chose", Random_Pick, ".", Random_Pick, "disproves Spock!")
        elif User_Input is '6':
            exit()
        else:
            pass

    elif Random_Pick is 'Scissors':
        if User_Input is '1':
            print("I chose", Random_Pick, ". And as it always has, rock crushes scissors.")
        elif User_Input is '2':
            print("I chose", Random_Pick, ".", Random_Pick, "cuts paper, so I win.")
        elif User_Input is '3':
            print("Oh look at that! I chose", Random_Pick, "too!")
        elif User_Input is '4':
            print("I chose", Random_Pick, "and", Random_Pick, "decapitates Lizard. HA HA!")
        elif User_Input is '5':
            print("I chose", Random_Pick, ". Spock smashes", Random_Pick, "so you win.")
        elif User_Input is '6':
            exit()
        else:
            pass

    elif Random_Pick is 'Lizard':
        if User_Input is '1':
            print("I chose", Random_Pick, ". And Rock crushes", Random_Pick, ", so congratulations!")
        elif User_Input is '2':
            print("I chose", Random_Pick, ".", Random_Pick, "eats paper, so I win.")
        elif User_Input is '3':
            print("I chose", Random_Pick, "and  Scissors decapitates, ", Random_Pick, ". You win.")
        elif User_Input is '4':
            print("Oh look at that! I chose", Random_Pick, "too!")
        elif User_Input is '5':
            print("I chose", Random_Pick, ".", Random_Pick, "poisons Spock, so I win.")
        elif User_Input is '6':
            exit()
        else:
            pass

    elif Random_Pick is 'Spock':
        if User_Input is '1':
            print("I chose", Random_Pick, ".", Random_Pick, "vaporizes Rock, so you lose.")
        elif User_Input is '2':
            print("I chose", Random_Pick, ". Paper disproves", Random_Pick, ", so congratulations!")
        elif User_Input is '3':
            print("I chose", Random_Pick, ". Spock smashes", Random_Pick, "so ha ha!.")
        elif User_Input is '4':
            print("I chose", Random_Pick, ". Lizard poisons", Random_Pick, ", so you win.")
        elif User_Input is '5':
            print("Oh look at that! I chose", Random_Pick, "too!")
        elif User_Input is '6':
            exit()
        else:
            pass

    else:
        pass

    Repeat = input("Would you like to play again, or exit? \n"
            "[1] : Play again \n"
            "[2] : Exit \n")

    while Repeat != '1' and Repeat != '2':
        Repeat = input("You have to choose one of the following options: \n"
        "[1] : Play again \n"
        "[2] : Exit \n")
    
    if Repeat == '1':
        Random_Pick = random.choice(Total_Pick)
        continue
    elif Repeat == '2':
        exit()
    else:
        pass

