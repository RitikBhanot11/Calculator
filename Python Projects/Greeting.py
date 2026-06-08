import time

x = input("Tell me your name: ")

hour = time.localtime().tm_hour

if 5 <= hour <=12:
    print(f"Good Moring {x}!")
elif 12 < hour <=16:
    print(f"Good Afternoon {x}!")
elif 16 < hour <=20:
    print(f"Good Evening {x}!")
else:
    print(f"Good Night {x}!")