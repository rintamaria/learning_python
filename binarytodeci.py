binary=input("enter a binary number")
deci=0
expo=len(binary)-1
for i in binary:
    deci=deci+int(i)*2**expo
    expo-=1
print(deci)