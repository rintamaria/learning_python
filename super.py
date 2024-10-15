class Company:
    def cname(self):
        return 'google'
class Employee(Company):
    def info(self):
        cname=super().cname()
        print("works at ",cname)
emp=Employee()
emp.info()