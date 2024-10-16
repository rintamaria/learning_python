def removechar(stri,n):
    return stri[n:]
stri=input("enter a string")
n=int(input("enter the number of characters to be removed from string"))
newstri=removechar(stri,n)
print(newstri)