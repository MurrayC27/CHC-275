Check = False
import random
file = open("number.txt","r")
wheel = file.readlines()
print (wheel)
file.close()
while Check == False:
    
    print("red")
    print("black")
    print("even")
    print("odd")
    print("combined")
    print("input number")
    print("high/low")
    x = input("how would you like to bet? ").strip().lower()
    randomnumber = random.sample(wheel,1)[0].split(":")
    randomnumber[1] = randomnumber[1].replace("/n","").strip()
    if x == "even":
        if int(randomnumber[0]) %2 == 0:
            print("you win")
        else:
            print("you lose :( ")
    elif x == "odd":
        if int(randomnumber[0]) %2 == 0:
            print("you lose")
        else:
            print("you win!! ")
    elif x == "high/low":
        x = input("would you like to bet higher or lower? ")
        y = input("what is your number? ")
        y = int(y)
        if x == "higher":
            if int(randomnumber[0]) > y:
                print(f"the number was {randomnumber[0]}")
                print("you win!!!")
            else:
                print(f"the number was {randomnumber[0]}")
                print("you lose :( ")
        elif x == "lower":
            if y > int(randomnumber[0]):
                print(f"the number was {randomnumber[0]}")
                print("you win!!!")
            else:
                print(f"the number was {randomnumber[0]}")
                print("you lose :( ")
        else:
            print("that is not a function of high/low")
    elif x == randomnumber[1]:
        print(f"the color was {randomnumber[1]}")
        print("you win!!!")
    elif x == randomnumber[0]:
        print(f"the number was {randomnumber[0]}")
        print("you win!!!")
    else:
        print(f"the pick was {randomnumber}")
        print("you lose :( ")
