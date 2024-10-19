firstset={23,42,65,57,78,83,29}
secondset={57,83,29,67,73,43,48}
intersec=firstset.intersection(secondset)
print("intersection:",intersec)
for i in intersec:
    firstset.remove(i)
print("after removing",firstset)