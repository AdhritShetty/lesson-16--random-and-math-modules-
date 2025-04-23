import random
playing=True
num=str(random.randint(10,20))

print("I will generate a random number from 10-20, and you have to guess the digit one guess at a time")
print("the game ends when you get no.1 hero!")
while playing:
    guess=input("give me your buest guess!\n")
    if num==guess:
        print("you win the game")
        print("the number was",num)
        break
    else:
        print("your guess isn't quite right.try again \n")
    

