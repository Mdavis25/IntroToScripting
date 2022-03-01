# Employee Class
class Employee:
    def __init__(self, fName, lName, idNum, dept, title):
        # declares variables for employee
        self.firstName = fName
        self.lastName = lName
        self.idNumber = idNum
        self.department = dept
        self.jobTitle = title

    def __str__(self):
        return 'Name: {self.firstName} {self.lastName}\nIdNumber: {self.idNumber}\nDepartment: {self.department}\nJob ' \
               'Title: {self.jobTitle}\n'.format(self=self)


# function partOne that looks up, adds, deletes, or changes the Employees
def empEnter():
    # flag to exit the program
    exitFlag = False
    empDict = {}

    # while option is not equal to 5
    while not exitFlag:
        print("\n1. Look up employee\n2. Add new employee\n3. Change employee\n4. Delete employee\n5. Quit\n")
        option = input("Enter an option using the corresponding number: ")

        # if option is equal to 1
        if option == '1':
            # if the dictionary does not have at least one employee
            if len(empDict) < 1:
                print("\nDictionary is empty")
            else:
                # user enters id
                tempID = int(input("Enter employee ID to look for: "))
                # if the id matches, print id
                if tempID in empDict:
                    print(empDict[tempID])
                else:
                    # id didn't match
                    print("Employee with ID ", tempID, " not found in dictionary")

        # if id equals 2
        elif option == '2':
            # user enters employee information
            tempFirst = input("Enter first name: ")
            tempLast = input("Enter last name: ")
            tempID = int(input("Enter ID: "))
            tempDept = input("Enter department: ")
            tempTitle = input("Enter job title: ")
            tempEmployee = Employee(tempFirst, tempLast, tempID, tempDept, tempTitle)
            empDict[tempID] = tempEmployee

            # prints employee
            print("\nEmployee added:", empDict[tempID])

        # if id equals 3
        elif option == '3':
            # user enters employee id
            tempID = int(input("Enter the ID of an employee to edit: "))
            if tempID in empDict:
                tempEmployee = empDict.pop(tempID)

                # user enters new employee information
                tempFirst = input("Enter first name: ")
                tempLast = input("Enter last name: ")
                tempDept = input("Enter department: ")
                tempTitle = input("Enter job title: ")
                tempEmployee.firstName = tempFirst
                tempEmployee.lastName = tempLast
                tempEmployee.department = tempDept
                tempEmployee.jobTitle = tempTitle

                # sets employee information
                empDict[tempID] = tempEmployee

                print("Employee added:")
                print(empDict[tempID])
            else:
                # prints if id is not found
                print("\nEmployee with ID ", tempID, " not found in dictionary")

        # if option equals 4
        elif option == '4':
            # user enters employee to delete
            tempID = int(input("Enter the ID of an employee to delete: "))
            if tempID in empDict:
                # deletes employee
                tempEmployee = empDict.pop(tempID)
                print("Employee deleted:")
                print(tempEmployee)
            else:
                # prints if id is not found
                print("\nEmployee with ID ", tempID, " not found in dictionary")

        # exits program
        elif option == '5':
            exitFlag = True

        # user entered invalid input
        else:
            print("Invalid Input, please input 1-5.")


# main
if __name__ == '__main__':
    empEnter()
