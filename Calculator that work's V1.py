def plusorNeg():
    Ibox = input("put + or - or * or  / ")
    if Ibox == "+":
        cal()
    elif Ibox == "-":
        calN()
    elif Ibox == "*":
        calT()
    elif Ibox == "/":
        calD()

def cal():
    box = input("input here ")
    box2 = input("input here the number you want to + ")
    box3 = 0
    box3 += int (box) + int (box2)
    print(box3)

def calN():
    box = input("input here  ")
    box2 = input("input here the number you want to - ")
    box3 = 0
    box3 += int (box) - int (box2)
    print(box3)

def calT():
    box = input("input here  ")
    box2 = input("input here the number you want to * ")
    box3 = 0
    box3 += int (box) * int (box2)
    print(box3)

def calD():
    box = input("input here  ")
    box2 = input("input here the number you want to / ")
    box3 = 0
    box3 += int (box) / int (box2)
    print(box3)

plusorNeg()




