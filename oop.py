
# This is a simble class for he company employees
class Employee:
    # create a constructor that initiates the first name, last name and email of the company employees
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.email = firstname + "." + lastname + "@mutualism.co.za"

    def employee_id(self):
        return "{} {} and the email is :{}".format(self.firstname, self.lastname, self.email)


emp_1 = Employee("Sibusiso","Mgidi")
emp_2 = Employee("Mxolisi","Mgidi")
emp_3 = Employee("Cindy","Nakana")
emp_4 = Employee("Mohale","Khoza")

print(emp_1.employee_id())
print(emp_2.employee_id())
print(emp_3.employee_id())
print(emp_4.employee_id())




# instance variables: contains data that is unique to every employee
