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
    x = input("how would you like to bet? ").strip().lower()
    randomnumber = random.sample(wheel,1)[0].split(":")
    print(randomnumber)
    randomnumber[1] = randomnumber[1].replace("/n","")
    if x == randomnumber[1]:
        print("you win!!!")
    elif x == randomnumber[0]:
        print("you win!!!")
    else:
        print("you lose :( ")
