counter = 1
while True:
    print(f"Calculation number {counter}")
    try:
        a=float(input("Write first number: "))
    except:
        print("Wrong Value!")
        continue
    try:
        b=float(input("Write second number: "))
    except:
        print("Wrong Value!")
        continue
    print("Select the operation you want to perform: \n + for Addition \n - for Subtraction\n * for Multiplication\n"
    "/ for Division \n // for Floor Division \n % for Modulus \n ** for Power \n All for all calculations ")
    x = input("Type here: ")
    if x == "/" or x == "//" or x== "%":
        if b == 0:
            print("Denominator cannot be zero!!")
            continue

    
    operations ={
    "+": a+b,
    "-": a-b,
    "*": a*b,
    "/": a/b,
    "//": a//b,
    "%": a%b,
    "**": a**b
    }

    if x != "All" and x.lower() != "all" and x.upper() != "ALL":
        result = operations[x]
        print(f"{a} {x} {b} = {result}")  
    else:
        result = operations["+"]
        print(f"{a} + {b} = {result}")
        result = operations["-"]
        print(f"{a} - {b} = {result}")
        result = operations["*"]
        print(f"{a} * {b} = {result}")
        result = operations["/"]
        print(f"{a} / {b} = {result}")
        result = operations["//"]
        print(f"{a} // {b} = {result}")
        result = operations["**"]
        print(f"{a} ** {b} = {result}")
        result = operations["%"]
        print(f"{a} % {b} = {result}")
    
    counter += 1
    y= input('Type "Q or q" if you want to end here or just press enter to continue: ')

    if y == "Q" or y == "q":
        break