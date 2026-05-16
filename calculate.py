a=int(input("Write first number: "))
b=int(input("Write second number: "))
(print("Select the operation you want to perform: \n + for Addition \n - for Subtraction\n * for Multiplication\n / for Division"))
x = input("Type here: ")

if x=="+":
    print("Addition:  ", a+b)
elif x=="-":
    print("Subtraction:  ", a-b)
elif x=="*":
    print("Multiplication:  ", a*b)
elif x=="/":
    print("Division:  ", a/b)
else:
    print("Wrong Input!")