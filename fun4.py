#assign a different name to function and call it through the new name
def display_student(name,age):
    print(name,age)
display_student("emma",26)
showstudent=display_student
showstudent("emma",26)