list1=[10,20,25,30,35]
list2=[40,45,60,75,90]
newlist=list()
for num in list1:
    if num%2!=0:
        newlist.append(num)
for num in list2:
    if num%2==0:
        newlist.append(num)
print(newlist)