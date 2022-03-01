class Employee:
    def __init__(self, fName, lName, idNum, dept, title):
        self.firstName = fName
        self.lastName = lName
        self.idNumber = idNum
        self.department = dept
        self.jobTitle = title

        self.fullName = self.firstName + " " + self.lastName
        self.email = self.firstName.lower() + "." + self.lastName.lower() + "@company.com"

    def __str__(self):
        return 'Name: {self.firstName} {self.lastName}\nIdNumber: {self.idNumber}\nDepartment: {self.department}\nJob ' \
               'Title: {self.jobTitle}\n'.format(self=self)


def partOne():
    exitFlag = False
    empDict = {}

    while not exitFlag:
        print("1. Look up employee\n2. Add new employee\n3. Change employee\n4. Delete employee\n5. Quit\n")
        option = input("Enter an option using the corresponding number: ")

        if option == '1':
            if len(empDict) < 1:
                print("Dictionary is empty")
            else:
                tempID = int(input("Enter employee ID to look for: "))
                if tempID in empDict:
                    print(empDict[tempID])
                else:
                    print("Employee with ID ", tempID, " not found in dictionary")

        elif option == '2':
            tempFirst = input("Enter first name: ")
            tempLast = input("Enter last name: ")
            tempID = int(input("Enter ID: "))
            tempDept = input("Enter department: ")
            tempTitle = input("Enter job title: ")
            tempEmployee = Employee(tempFirst, tempLast, tempID, tempDept, tempTitle)
            empDict[tempID] = tempEmployee

            print("Employee added:")
            print(empDict[tempID])

        elif option == '3':
            tempID = int(input("Enter the ID of an employee to edit: "))
            if tempID in empDict:
                tempEmployee = empDict.pop(tempID)

                tempFirst = input("Enter first name: ")
                tempLast = input("Enter last name: ")
                tempDept = input("Enter department: ")
                tempTitle = input("Enter job title: ")
                tempEmployee.firstName = tempFirst
                tempEmployee.lastName = tempLast
                tempEmployee.department = tempDept
                tempEmployee.jobTitle = tempTitle

                empDict[tempID] = tempEmployee

                print("Employee added:")
                print(empDict[tempID])
            else:
                print("Employee with ID ", tempID, " not found in dictionary")
            print()

        elif option == '4':
            tempID = int(input("Enter the ID of an employee to delete: "))
            if tempID in empDict:
                tempEmployee = empDict.pop(tempID)
                print("Employee deleted:")
                print(tempEmployee)
            else:
                print("Employee with ID ", tempID, " not found in dictionary")

        elif option == '5':
            exitFlag = True

        else:
            print("Invalid Input, try again.")


if __name__ == '__main__':
    partOne()
