userinput=input("enter the values of list")
ulist=userinput.split()
print("the list is",ulist)
lastele=ulist[len(ulist)-1]
if ulist[0]==lastele :
    print("True")
else:
    print("False")