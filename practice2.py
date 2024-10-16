previousnum=0
print("printing current and previous number sum in a range(10")
for num in range(10):
    sum=num+previousnum
    print("current number",num,"previous number",previousnum,"sum:",sum)
    previousnum=num
