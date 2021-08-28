from colorama import Fore , Back
from colorama.ansi import Style
while True:
    print(Fore.GREEN+"Welcome! Do your lazy calculations here.\n")
    print(Fore.RED+" 1. Addition\n 2. Substraction\n 3. Multiplication\n 4. Division\n 5. Remainder\n 6. Exit\n ")
    data= int(input(Fore.GREEN+"select your option-"))
    if data==1:
        a=int(input(Fore.RED+"enter your first number-"))
        b=int(input(Fore.RED+"enter your second number-"))
        print(Fore.GREEN+Back.RED+ f"Your added result is {a+b}",Style.RESET_ALL)
    elif data==2:
        a=int(input(Fore.RED+"enter your first number-"))
        b=int(input(Fore.RED+"enter your second number-"))
        print(Fore.GREEN+Back.RED+ f"Your substracted result is {a-b}",Style.RESET_ALL)
    elif data==3:
        a=int(input(Fore.RED+"enter your first number-"))
        b=int(input(Fore.RED+"enter your second number-"))
        print(Fore.GREEN+Back.RED+ f"Your result is {a*b}",Style.RESET_ALL)
    elif data==4:
        a=int(input(Fore.RED+"enter your first number-"))
        b=int(input(Fore.RED+"enter your second number-"))
        print(Fore.GREEN+Back.RED+ f"Your result is {a/b}",Style.RESET_ALL)
    elif data==5:
        a=int(input(Fore.RED+"enter your first number-"))
        b=int(input(Fore.RED+"enter your second number-"))
        print(Fore.GREEN+Back.RED+ f"Your remainder is {a%b}",Style.RESET_ALL)
    elif data==6:
        print(Fore.RED+Back.GREEN+ "Thank you for using calculator.",Style.RESET_ALL)
        break
    else:
        print("------->",Fore.RED+"INVALID INPUT",Fore.GREEN,"<-------\n",Style.RESET_ALL+Fore.RED+"Please check options again.")