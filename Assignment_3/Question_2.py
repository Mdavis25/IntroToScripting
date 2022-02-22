class Employee:
    # init function takes first and last name, id number, department and job title
    # as arguments and sets values in the object
    def __init__(self, fName, lName, idNum, dept, title):
        self.firstName = fName
        self.lastName = lName
        self.idNumber = idNum
        self.department = dept
        self.jobTitle = title


if __name__ == '__main__':
    empOne = Employee("Susan", "Meyers", 47899, "Accounting", "Vice President")
    empTwo = Employee("Mark", "Jones", 39119, "IT", "Programmer")
    empThree = Employee("Joy", "Rogers", 81774, "Manufacturing", "Engineer")

    print(empOne, "\n")
    print(empTwo, "\n")
    print(empThree, "\n")
