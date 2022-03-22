from termcolor import colored
name=input("Enter your name:")
print("*****Choose color output*****")
print("You can choose Red,Green,Blue,Yellow")
choose=input("Choose color:")
if choose=="Red":
    print(colored(name,"red"))
elif choose=="Green":
    print(colored(name,"green"))
elif choose=="Blue":
    print(colored(name,"blue"))
elif choose=="Yellow":
    print(colored(name,"yellow"))
else:
    print("Plz only choose the four colours above<'_'>")