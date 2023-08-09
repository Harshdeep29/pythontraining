from random import *
movies=["titanic","jurrasic","sholay"]
name=list(movies[randint(0,len(movies)-1)])
print(name)
temp=[]
for i in range(len(name)):
    temp.append("_")
print(temp)
chance=0
while(temp!=name):
    guess=input("Guess the name: ")
    for i in range(len(name)):
        if guess==name[i]:
            temp[i]=guess
        if guess!=name[i]:
            print("ERROR")
            break
    print(temp)
if (temp==name):
    print("Congratulations You guessed it correct!!")