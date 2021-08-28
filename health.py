def gettime():
    import datetime
    return datetime.datetime.now()

def harry():
    a= int(input("what would you like to do?\n1.Log_in\n2.Retrieve\n--->>>"))
    if a==1:
        log()
    elif a==2:
        retrieve()
    else:
        invalid()

def rohan():
    a= int(input("what would you like to do?\n1.Log_in\n2.Retrieve\n--->>"))
    if a==1:
        log()
    elif a==2:
        retrieve()
    else:
        invalid()

def hammad():
    a= int(input("what would you like to do?\n1.Log_in\n2.Retrieve\n--->>"))
    if a==1:
        log()
    elif a==2:
        retrieve()
    else:
        invalid()

def log():
    intake= int(input("what do you want to log?\n1.Food\n2.Exercise\n--->>"))
    if intake==1:
        data= input("Enter the food you ate--->")
        food=open(f"{user}_food.txt","a")
        time=food.write(str(f"{gettime()}-----"))
        diet=food.write(f"{data}\n")
        food.close()
        print(time,diet)
    elif intake==2:
        data= input("Enter the exercise you did--->")
        exer=open(f"{user}_exercise.txt","a")
        time=exer.write(str(f"{gettime()}-----"))
        exercise=exer.write(f"{data}\n")
        exer.close()
        print(time,exercise)
    else:
        invalid()

def retrieve():
    intake=int(input("what would you like to see?\n1.Food\n2.Exercise\n"))
    if intake==1:
        food= open(f"{user}_food.txt","r")
        for i in food:
            print(i,end="")
        food.close()
    elif intake==2:
        exercise= open(f"{user}_exercise.txt","r")
        print(exercise.readlines())
        exercise.close()
    else :
        invalid()


def loop():
    inn=int(input("Would you like to add more?\n1.Yes\n2.No\n--->>"))
    while True:
        if inn==1 and users==1:
            harry()
        elif inn==1 and users==2:
            rohan()
        elif inn==1 and users==3:
            hammad()
        else:
            break

def invalid():
    try:
        print("\nInvalid Input.")
    except Exception as e:
        print(e)


print("Welcome to Health Management System.")
while True:
    con=1
    users= int(input("Whose data would you like to review or edit?:\n1.Harry\n2.Rohan\n3.Hammad\n--->>>"))
    
    if users==1:
        user="Harry"
    elif users==2:
        user= "Rohan"
    elif users==3:
        user= "Hammad"

    
    if users==1:
            harry()
            loop()
    elif users==2:
            rohan()
            loop()
    elif users ==3:
            hammad()
            loop()
    else:
        invalid()
    
    con= int(input("would you like to continue?\n1.Yes\n2.No\n"))
    if con==2:
        print("Thank You for using our Health Manangement System.")
        break