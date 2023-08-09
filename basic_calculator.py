choice=int(input('''Choose what you want to do:
                 1.Addition
                 2.Subtraction
                 3.Multiplication
                 4.Division'''))
    if choice==1:
        num1=int(input("Enter first number:"))
        num2=int(input("Enter second number:"))
        print(num1+num2)
    if choice==2:
        num1=int(input("Enter first number:"))
        num2=int(input("Enter second number:"))
        print(num1-num2)
    if choice==3:
        num1=int(input("Enter first number:"))
        num2=int(input("Enter second number:"))
        print(num1*num2)
    if choice==4:
        num1=int(input("Enter first number:"))
        num2=int(input("Enter second number:"))
        print(num1/num2)
