def outer(a,b):
    print(a)
    print(b)
    def add(a,b):
        sum=a+b
        return sum
    r=add(a,b)
    print(r)
    s=r+5
    print("outer function result",s)
a=int(input("enter the first number"))
b=int(input("enter the second number"))
outer(a,b)