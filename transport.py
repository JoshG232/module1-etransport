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
    def __init_subclass__(self,lorryDetails,driverDetails):
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

def loginOrRegister(typeChoice):
    print("""
        1:Login
        2:Register
        """)
    choice = int(input("Enter selection: "))
    if choice == 1:
        login()
    if choice == 2:
        register()
        
        
def login():
    print("login") 
        
def register():
    print("register")

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



main()