# Employee Class
class Employee:
    def __init__(self, fName, lName, idNum, dept, title):
        # Declaring employee Variables
        self.firstName = fName
        self.lastName = lName
        self.idNumber = idNum
        self.department = dept
        self.jobTitle = title

        # setting employees full name
        self.full = self.firstName + " " + self.lastName
        # setting employees email
        self.email = self.firstName.lower() + "." + self.lastName.lower() + "@company.com"


# main
if __name__ == '__main__':
    # Employee information
    empOne = Employee("Susan", "Meyers", 47899, "Accounting", "Vice President")
    empTwo = Employee("Mark", "Jones", 39119, "IT", "Programmer")
    empThree = Employee("Joy", "Rogers", 81774, "Manufacturing", "Engineer")

    # prints full name and email
    print("Employee One Full Name: ", empOne.full)
    print("Employee One Email: ", empOne.email)
