import time
import os

def enemy(boy, girl):
    print("'Your friends will believe in your potential, your enemies will make you live up to it.'\nHey {} and {}... Some relationships are like Tom and Jerry. They tease each other, knock down each other, irritate each other, but can't live without each other. Always, remember that a wise man gets more use from his enemies than a fool from his friends. Learn to forgive your enemies; nothing annoys them so much. Peace out !!!".format(boy, girl))

def friend(boy, girl):
    print("Hola {} and {}!!! Best Friends Forever!!! Since the day you guys met, you've always had a strong and wonderful connection. Sometimes, being with your best friend, is all the therapy you need. This is the motto of your life. In the cookie of life, pairs like yours are the chocolate chips. You guys adore the chaotic madness you share as well as the moments of silence you share together, where words donâ€™t need to be said, but you know that you are in it together.".format(boy, girl))

def love(boy, girl):
    print("Hey {} and {}, your love is an inspiration to all your near and dear ones. You do millions of little things that bring joy and happiness to your life and makes it wonderful! Your lives are like a romantic movie that is being played again and again. You smile, you love, you flirt and fight and you do it again and again. Yet, you love each other infinitely!".format(boy, girl))

def marriage(boy, girl):
    print("Congratulations {} and {} on a spectacular wedding and a lifetime of love and happiness ahead. Warmest wishes on your big day and as you start a new chapter of life and love together. May God grant you wisdom, blessings, and happiness. The two of you are a blessing not only to each other but to all those around you.".format(boy,girl))

d = {"E" : enemy, "F" : friend, "L" : love, "M" : marriage}

def relationChecking(boy, girl):
    status = checkRelation(boy, girl)
    status(boy.split()[0], girl.split()[0])


def checkRelation(boy, girl):
    l = ["E", "F", "L", "M"]
    # displayRelation = display(boy, girl)

    boy = list(map(str.upper, boy.replace(" ", "")))
    girl = list(map(str.upper, girl.replace(" ","")))
    charSetBoy = {}
    charSetGirl = {}
    for b in boy:
        if b not in charSetBoy.keys():
            charSetBoy[b] = 1
        else:
            charSetBoy[b] += 1
    for g in girl:
        if g not in charSetGirl.keys():
            charSetGirl[g] = 1
        else:
            charSetGirl[g] += 1
    for b in charSetBoy.keys():
        if b in charSetGirl.keys():
            sub = min(charSetBoy[b], charSetGirl[b])
            charSetBoy[b] -= sub
            charSetGirl[b] -= sub

    decideVar = 4

    predictLen = sum(charSetBoy.values()) + sum(charSetGirl.values())
    # print(predictLen)
    while len(l) > 1:
        removeChar = predictLen % decideVar
        # print(removeChar, predictLen, decideVar)
        l.remove(l[removeChar - 1])
        slice1 = l[removeChar - 1 : ]
        slice2 = l[: removeChar - 1]
        # print(slice1, slice2)
        l = slice1 + slice2
        # print(l)
        decideVar -= 1
        
    # print(d[l[0]])
    return d[l[0]]
if __name__ == "__main__":

    print("Loading........")
    time.sleep(3)
    print()
    os.system("clear")
    
    print("===================================================")
    print("Welcome to our Relationship Predictor v 1.0")
    print("===================================================")
    print()
    boy = input("Please enter the Boy's name => ")
    girl = input("Please enter the Girl's name => ")
    print()
    print("Calculating your relationship status.....")
    time.sleep(3)
    print()
    # relationChecking = display(boy, girl)
    relationChecking(boy, girl)