num=int(input("enter a number"))
print("checking whether the number is prime or not")
if num<=1:
    print("not prime")
for i in range(2,num):
        if num%i==0:
            print("not prime")
            break
else:
        print("prime number")