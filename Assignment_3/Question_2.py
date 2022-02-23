# Employee Class
class Employee:
    def __init__(self, fName, lName, idNum, dept, title):
        # Declaring employee variables
        self.firstName = fName
        self.lastName = lName
        self.idNumber = idNum
        self.department = dept
        self.jobTitle = title


# main
if __name__ == '__main__':
    # Employee Information
    empOne = Employee("Susan", "Meyers", 47899, "Accounting", "Vice President")
    empTwo = Employee("Mark", "Jones", 39119, "IT", "Programmer")
    empThree = Employee("Joy", "Rogers", 81774, "Manufacturing", "Engineer")

    # printing employee info from class
    print("Employee One: ", empOne.firstName, empOne.lastName, empOne.idNumber, empOne.department, empOne.jobTitle)
    print("Employee Two: ", empTwo.firstName, empTwo.lastName, empTwo.idNumber, empTwo.department, empTwo.jobTitle)
    print("Employee Three: ", empThree.firstName, empThree.lastName, empThree.idNumber, empThree.department,
          empThree.jobTitle)
