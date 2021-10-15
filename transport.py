import json

class Person:
    def __init__(self,username,password,personType):
        self.username = username
        self.password = password
        self.personType = personType
    
    

class CargoOwner(Person):
    def __init_subclass__(self):
        return super().__init_subclass__()
    def placeOrder():
        print("Temp placeOrder")
    def calShipping():
        print("Temp calShipping")

class Driver(Person):
    def __init__(self,username,password,personType,lorryDetails,driverDetails):
        self.username = username
        self.password = password
        self.personType = personType
        self.lorryDetails = lorryDetails
        self.driverDetails = driverDetails
        return super().__init_subclass__()
    def viewOrders():
        print("Temp viewOrders")
    def acceptOrders():
        print("Temp acceptOrders")
    
class TransportCompany(Person):
    def __init_subclass__(self):
        return super().__init_subclass__()
    def showCustomerOrders():
        print("Temp showCustomerOrders")
    def sendOrder():
        print("Temp sendOrder")

class Order():
    def __init__(self,start,end,miles,weight):
        self.start = start
        self.end = end
        self.miles = miles
        self.weight = weight

"""This function takes the user input and selects if they want to login
   or register, while also taking the value of "typeChoice" to see if 
   they are a Cargo Owner,Driver or Transport company"""

def loginOrRegister(typeChoice):
    print("""
        1:Login
        2:Register
        """)
    choice = int(input("Enter selection: "))
    if choice == 1:
        login(typeChoice)
    if choice == 2:
        if typeChoice == 1:
            registerCargoOwner()
        if typeChoice == 2:
            registerDriver()
        if typeChoice == 3:
            registerTransportCompany()

def login(typeChoice):
    global loggedIn
    # file = "transport.json"
    # data = json.loads(open(file).read())
    # username = input("Enter username ")
    # userList = data["Cargo Owners"][0]
    loggedIn = input("Do you want to login")
    if loggedIn == "Yes":
        loggedIn = True
        if typeChoice == 1:
            mainCargoOwner()
        if typeChoice == 2:
            print("sdf")

    else:
        loggedIn = False
        
def registerCargoOwner():
    username = input("Enter username")
    password = input("Enter password")
    tempObj = CargoOwner(username,password,"Cargo Owner")
    tempObj = vars(tempObj)
    y = json.dumps(tempObj)
    writingToJson(y,"Cargo Owners")
    
def registerDriver():
    username = input("Enter username")
    password = input("Enter password")
    lorryDetails = input("Enter Lorry details")
    driverDetails = input("Enter driver details")
    tempObj = Driver(username,password,"Driver",driverDetails,lorryDetails)
    tempObj = vars(tempObj)
    y = json.dumps(tempObj)
    writingToJson(y,"Drivers")

def registerTransportCompany():
    username = input("Enter username")
    password = input("Enter password")
    tempObj = TransportCompany(username,password,"Transport Comapny")
    tempObj = vars(tempObj)
    y = json.dumps(tempObj)
    writingToJson(y,"Transport Company")

def writingToJson(y,typeOf):
    with open("transport.json","r+") as f:
        fData = json.load(f)
        fData[typeOf].append(y)
        f.seek(0)
        json.dump(fData,f,indent=4)
        for i in fData[typeOf]:
            print(i)
        
def mainCargoOwner():
    
    print("""
        What would you like to do
        1: Calculate shipping rates
        2: Send cargo
        """)
    choice = int(input("Enter selection: "))
    if choice == 1:
        #Add python locaiton api to help shipping rates
        try:
            length = int(input("Enter length: "))
            width = int(input("Enter width: "))
            weight = int(input("Enter weight: "))
            totalPrice = length * width * weight
            print("The estimate for the cargo is £",totalPrice)
        except:
            print("Incorrect values inputted")
        mainCargoOwner()
    if choice == 2:
        start = input("Enter start location: ")
        end = input("Enter end location: ")
        weight = int(input("Enter weight: "))
        miles = int(input("How many miles: "))
        tempObj = Order(start,end,miles,weight)
        tempObj = vars(tempObj)
        y = json.dumps(tempObj)
        writingToJson(y,"Orders")
"""Main function"""

def main():
    print("""
        Select type of user
        1:Cargo Owner
        2:Driver
        3:Transport Company
        """)
    typeChoice = int(input("Enter selection: "))
    if typeChoice == 1:
        loginOrRegister(typeChoice)
    elif typeChoice == 2:
        loginOrRegister(typeChoice)
    elif typeChoice == 3:
        loginOrRegister(typeChoice)
    else:
        print("Invalid input, try again")
        main()
main()