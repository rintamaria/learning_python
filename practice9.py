num=input("enter a number")
print("original number",num)
if num==num[::-1]:
    print("yes the given number is a palindrome number")
else:
    print("no. the given number is not a palindrome number")