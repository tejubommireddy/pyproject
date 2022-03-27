# define a static variable and across that throught the class
# class static_method():
#     print("hi welcome to python")

# static variable that through a instance
class Employee:
    company = "youtube"
    def __init__(self,first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def get_email(self):
        return f'{self.first_name}.{self.last_name}@{Employee.company}.com'
emp1 = Employee()

