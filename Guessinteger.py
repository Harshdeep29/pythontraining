from random import *
gen = randint(0,50)
for i in range(5):
    guess=int(input("Guess the number in range 0-50:"))
    if guess==gen:
        print("Hurray you guessed it right")
        break
    if guess<gen:
        print("Enter a bigger number")
    if guess>gen:
        print("Enter a smaller number")
    if i==4:
        print("You loose. The number is ",gen)

