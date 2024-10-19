str1=input("enter a string")
print("original string",str1)
lower=[]
upper=[]
for i in str1:
    if i.islower():
        lower.append(i)
    else:
        upper.append(i)
sorted=''.join(lower+upper)
print(sorted)
