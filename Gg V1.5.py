def GusG():
    print("hello to my new game ! ")
    
    print("it now time for you to Choose the level that you want !")

    box = input("level 1, level 2, level  3, just put 1 or 2 or 3 ! ")
    if box == "1":
        level1()
    elif box == "2":
        level2()
    elif box == "3":
        level3()

def level1():
    box = input("what is the colour of the sky [blue,green,red]: ")
    int = Score = 0
    if box == "blue":
        print("you are right it is blue !")
        Score += 1 
        '''print(Score)'''
    else:
        print("you are wrong")
        Score -= 1
    box == ""
    box = input("what is the colour of the sun [yellow,green,red]: ")
    if box == "yellow":
        print("you are right it is " + box + "! ")
        Score += 1
        '''print(Score)'''
    else:
        print("you are wrong")
        Score -= 1
    box == ""
    box = input("what is the colour of the youtube logo [blue,green,red]: ")
    if box == "red":
        print("you are right it is " + box + "! ")
        Score += 1
        '''print(Score)'''
    else:
        print("you are wrong")
        Score -= 1
    print("your score is ")
    print(Score)
    


def level2():
    print("i did code levl 2 yet so sorry but level 1 is working tho xd")
    GusG()
def level3():
    print("i did code levl 3 yet so sorry but level 1 is working tho xd")
    GusG()



GusG()