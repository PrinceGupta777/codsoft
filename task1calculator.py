x= float(input("Enter the value of x:"))
y= float(input("Enter the value of y:"))
opr = input(" Choose The operation you want to perform : '+','-','*','/' ")
match opr:
    case '+':
        print(x+y)
    case '-':
        print(x-y)
    case '*':
        print(x*y)
    case '/':
        if y !="0":
            print(x/y)
        else: 
            print("Error!,Division by zero.")    
    case _:
        print("Error!,Invalid value")