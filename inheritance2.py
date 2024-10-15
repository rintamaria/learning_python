# multiple inheritance
class Person:
    def pinfo(self,name,age):
        print('name:',name,'age:',age)
class Company:
    def cinfo(self,cname,location):
        print('name:',cname,'location',location)
class Employee(Person,Company):
    def einfo(self,salary,skill):
        print('salary:',salary,'skill',skill)
emp=Employee()
emp.pinfo('jess',20)
emp.cinfo('google','usa')
emp.einfo(120000,'ai')