import random
print("Welcome, this project will roll a die for you")
Die = random.randint(1,6)
if Die == 1:
    print("_________")
    print("|       |")
    print("|   .   |")
    print("|       |")
    print("_________")
    print("You got a one!")
elif Die == 2:
    print("_________")
    print("|  .    |")
    print("|       |")
    print("|     . |")
    print("_________")
    print("You got a two!")
elif Die == 3:
    print("_________")
    print("| .     |")
    print("|   .   |")
    print("|      .|")
    print("_________")
    print("You got a three!")
elif Die == 4:
    print("_________")
    print("|  .  . |")
    print("|       |")
    print("|  .  . |")
    print("_________")
    print("You got a four!")
elif Die == 5:
    print("_________")
    print("|  .  . |")
    print("|    .  |")
    print("|  .  . |")
    print("_________")
    print("You got a five!")
elif Die == 6:
    print("_________")
    print("|  .  . |")
    print("|  .  . |")
    print("|  .  . |")
    print("_________")
    print("You got a six!")
print("Thanks for rollin' :)")
