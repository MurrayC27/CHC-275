Check = False
import random
red = []
black = []
even = []
odd = []
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
    if x == randomnumber[1]:
        print("you win!!!")
    if x == randomnumber[0]:
        print("you win!!!")
