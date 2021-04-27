import os
import time
answer = "0"
while True:
    print("???: Welcome to the zone between the world and the realm. \n How can I help you?")
    print("L: Load","N: New Game", "Q: Quit", sep="\n")
    answer = input(">>> ")
    if answer == ("l"):
        print("???: Ok, let's go into the forgotten realm, exactly the place where we were.")
        time.sleep(5)
        import prpg
    elif answer == ("n"):
        print("???: Are you really sure?")
        answer = input("[yes or no?] ")
        if answer == ("yes"):
            print("???: Ok, then let us go into the forgotten realm.")
            time.sleep(5)
            import newGame
    elif answer == ("q"):
        print("Well then...")
        print("Farewell, and let us see each other's voice again....")
        break
    else:
        print("???: Please type again.")
