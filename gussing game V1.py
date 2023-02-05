def gruss():
    box = input("i am big and gray and i have a long nose and i am a animal that live in africa what i am ? and if you dont kow just put idk ")
    win = False
    while win == False:
        if box == "Elephant":
            print("you are right it is " + box)
            win = True
        elif box == "elephant":
            print("you are right it is " + box)
            win = True
        elif box == "idk":
            print("the Answer is Elephant ")
            win = True
            calB()
        else:
            print("you are wrong lol ")
            win = True
            calB()

def calB():
    gruss()

gruss()





