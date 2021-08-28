import random
comp= random.randint(1,30)
i=9
j=0
for i in range (9,0,-1):
    a= int(input("guess the number= "))
    if a>comp:
        print("you went high,Go low")
        print("you have",i-1 ,"guesses left")
    elif a<comp:
        print("went low this time.fly high again")
        print("you have", i-1,"guesses left")
    elif j==9:
        print("You have exhausted all your guess limits.GAME OVER")
    elif a==comp:
        print("congrats ! You guessed it in ",j+1,"attempts.")
        break
    j+=1