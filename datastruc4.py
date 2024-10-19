sample=[11,45,8,11,23,45,23,45,89]
freq=dict()
for i in sample:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)