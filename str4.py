#count all letters,digits ans special symbols from a string
str1=input("enter a string with letters, digits and special symbols")
char_count=0
dig_count=0
sym_count=0
for i in str1:
    if i.isalpha():
        char_count+=1
    elif i.isdigit():
        dig_count+=1
    else:
        sym_count+=1
print("charcount",char_count)
print("digitcount",dig_count)
print("symbolcount",sym_count)