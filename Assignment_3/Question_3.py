class Employee():
    def __init__(self, fName, lName, idNum, dept, title):
        self.firstName = fName
        self.lastName = lName
        self.idNumber = idNum
        self.department = dept
        self.jobTitle = title

        self.fullName = self.firstName + " " + self.lastName
        self.email = self.firstName.lower() + "." + self.lastName.lower() + "@company.com"


if __name__ == '__main__':
    def __str__(self):
        return 'Name: {self.firstName} {self.lastName}\nIdNumber: {self.idNumber}\nDepartment: {self.department}\nJob ' \
               'Title: {self.jobTitle}\n'.format(self=self)


    empOne = Employee("Susan", "Meyers", 47899, "Accounting", "Vice President")
    empTwo = Employee("Mark", "Jones", 39119, "IT", "Programmer")
    empThree = Employee("Joy", "Rogers", 81774, "Manufacturing", "Engineer")

    print("Employee One Full Name: ", empOne.fullName)
    print("Employee One Email: ", empOne.email)
    print()
