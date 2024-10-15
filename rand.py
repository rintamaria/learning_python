import random
small=int(input("enter a small numner"))
large=int(input("enter a larger number"))
mynum=random.randint(small,large)
count=0
while True:
    count+=1
    usernum=int(input("guess the number"))
    if usernum>mynum:
        print("too large")
    elif usernum<mynum:
        print("small")
    else:
        print("yay!!! u got it")
        break
    print(count)