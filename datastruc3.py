sam=[11,45,8,23,14,12,78,45,89]
length=len(sam)
chunk=len(sam)//3
start=0
end=chunk
for i in range(3):
    ind=slice(start,end)
    chunkli=sam[ind]
    print("chunk",i,chunkli)
    print("after reversing",chunkli[::-1])
    start=end
    end+=chunk