myStr="hey"
rev=""
for i in range(len(myStr)-1,-1,-1):
    print(myStr[i])
    rev+=myStr[i]
print(rev)