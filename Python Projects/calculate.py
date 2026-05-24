while True:
    try:
        a=int(input("Write first number: "))
    except:
        print("Wrong Value!")
        continue
    try:
        b=int(input("Write second number: "))
    except:
        print("Wrong Value!")
        continue
    print("Select the operation you want to perform: \n + for Addition \n - for Subtraction\n * for Multiplication\n"
    "/ for Division \n // for Floor Division \n % for Modulus \n ** for Power \n All for all calculations ")
    x = input("Type here: ")

    if x=="+":
        print("Addition:  ", a+b)
    elif x=="-":
        print("Subtraction:  ", a-b)
    elif x=="*":
        print("Multiplication:  ", a*b)
    elif x=="/":
        if b == 0:
            print("Denominator cannot be zero!!")
        else:
            print("Division:  ", a/b)
    elif x=="//":
        if b == 0:
            print("Denominator cannot be zero!!")
        else:
            print("Floor Division:  ", a//b)
    elif x=="**":
        print(f"{a} power of {b}:  ", a**b)
    elif x=="%":
        print("Modulus:  ", a%b)
    elif x=="All" or x == "ALL" or x == "all":
        print("Addition:  ", a+b)
        print("Subtraction:  ", a-b)
        print("Multiplication:  ", a*b)
        print("Modulus:  ", a%b)
        print(f"{b} power of {a}:  ", a**b)
        if b == 0:
            print("Denominator cannot be zero!!")
        else:
            print("Division:  ", a/b)
        if b == 0:
            print("Denominator cannot be zero!!")
        else:
            print("Floor Division:  ", a//b)
        
    else:
        print("Wrong Input!")

    y= input('Type "Q or q" if you want to end here or just press enter to continue: ')

    if y == "Q" or y == "q":
        break