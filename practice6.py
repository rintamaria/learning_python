listt=input("enter values for a list seperated by space")
clist=listt.split()
clist=[int(i) for i in clist]  # the values in the list are string
                                 #so converting to integer values'
print("the given list is",clist)
print("divisible by 5")
for i in clist:
    if i%5==0:
        print(i)
    else:
        continue



