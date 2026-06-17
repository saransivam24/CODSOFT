import random
option=["stone","paper","scissors"]
computer=random.choice(option)
user=input("Enter the stone/paper/scissors: ")
if user==computer:
    print("game draw")
elif user=="stone" and computer=="scissors":
    print("User win")
elif user=="paper" and computer=="stone":
    print("User win")
elif user=="scissors" and computer=="paper":  
    print("User win")
elif computer=="stone" and user=="scissors":
    print("computer win")
elif computer=="paper" and user=="stone":
    print("computer win")
elif computer=="scissors" and user=="paper":
    print("computer win")
else:
    print("Invalid input")
