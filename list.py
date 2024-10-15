print([1,24,56])
for i in [1,24,56]:
    print(i)
friends=['jin','suga','rm','jhope']
for i in friends:
    print("anneyong",i)
friends[2]='jk'
print(friends)
print(len(friends))
fri=['rm','jimin','v']
bts=friends+fri
print(bts)
print(bts[1:3])
stuff=list()
stuff.append('book')
stuff.append('bag')
stuff.extend(['ball','pen'])
print(stuff)
print(stuff.pop())
print(stuff.sort())
abc="heyhey rinta"
ab=abc.split()
print(ab)