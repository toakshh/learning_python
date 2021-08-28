import random
def comp_input():
    list=["rock","paper","scissor"]
    return random.choice(list)

print("Welcome to a weird testing game of Rock,Paper and scissor.")
a=int(input("1.Play\n2.Exit\n"))
Your_score=0
Comp_score=0
if a==1:   
    i=1   
    while i<=10:
        match=comp_input()
        print("Round ---->",i)
        user=input("----------------------\nRock\nPaper\nScissor\n-------------------\n--->>>")
        user.lower
        if match== "rock" and user=="scissor":
            print(f"Computer choose= {match}")
            print("Comp win.You loose")
            Comp_score = Comp_score + 1
        elif match== "paper" and user== "rock":
            print(f"Computer choose= {match}")
            print("Comp win.You loose")
            
            Comp_score = Comp_score + 1     
        elif match=="scissor" and user== "paper":
            print(f"Computer choose= {match}")
            print("Comp win.You loose")
            
            Comp_score= Comp_score + 1         
        elif user== "rock" and match=="scissor":
            print(f"Computer choose= {match}")
            print("You won.Comp loose.")
            
            Your_score =Your_score+1    
        elif user== "paper" and match== "rock":
            print(f"Computer choose= {match}")
            print("You won.Comp loose.")
            
            Your_score =Your_score+1           
        elif user=="scissor" and match== "paper":
            print(f"Computer choose= {match}")
            print("You won.Comp loose.")
            
            Your_score =Your_score+1
        elif match == user:
            print(f"Computer choose= {match}")
            print("This round is draw.Moving to next one.")     
        else:
            print("You entered a wrong choice.Please check it again.")
        i+=1
    print((f"Final standings:\nYour_score---> {Your_score} <-------> {Comp_score} <---Comp_score"))      
    print("Thank You for playing this game.Hope you have enjoyed it.")
elif a==2:
    print("Come again and play.")
else:
    print("Wrong input.")