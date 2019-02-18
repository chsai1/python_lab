class Persons():


    def __init__(self,name,age,phonenum,email):
        self.name = name
        self.age = age
        self.phonenum = phonenum
        self.email = email
        #semi private variable or protected
        self._ssn = "not_metioned"
        print("Persons ssn  has been created")

    #Printing the person details
    def get_details(self):
        print(f"Name - {self.name}\nAge - {self.age}\nPhone Number - {self.phonenum}\nEmail - {self.email}")

    #creating a method for initialising semi private data member
    def set_person_ssn(self, ssn):
            self._ssn = ssn

    #creating a method for initialising semi private data member
    def get_person_ssn(self):
        return self._ssn

#flight class
class AirlineFlight():

    # initalising the __init__ constructor
    def __init__(self, flightname,flightnum):
        self.flightname = flightname
        self.flightnum = flightnum
        print("Airline flights instance has been created")

#implementing inheritance
class Workers(Persons):

    # initalising the __init__ constructor
    def __init__(self,name,age,phonenum,workerID,email):
        Persons.__init__(self,name,age,phonenum,email)
        self.workerID = workerID
        print("Workers instance has been created")
        #super.__init__(name,age,phone_number)

    # using a super() keyword to call method in parent class
    def print_Customers_details(self):
        super.details()

#Implemented multiple Inhertence
class Flightticket(AirlineFlight,Persons):

    # initalising the __init__ constructor
    def __init__(self,ticketnum,deptdate):
        self.ticketnum = ticketnum
        self.deptdate = deptdate



#Implemented multiple Inhertence
class Customers(Persons,AirlineFlight):

    # initalising the __init__ constructor
    def __init__(self,name,age,phonenum,carryonweight,email):
        Persons.__init__(self, name, age, phonenum, email)
        self.carryonweight = carryonweight

        #creating private variable
        self.__Customers_passportnum = "not updated"

    #creating a method for initialising private data member
    def set_passportnum(self,passportnum):
        self.__Customers_passportnum = passportnum

    #creating a method for retrieving private data member
    def get_passportnum(self):
        return self.__Customers_passportnum

#creating the instance of Person class
person1 = Persons('divya',23,9856774321,'niteesha97@gmail.com')

#initialising the semi private variable or protected
person1.set_person_ssn('432156')

#printing the semi  private variable
print(person1.get_person_ssn())

#other way to print semi private variable(not recommended)
print(person1._ssn)

#creating the instance of Employee class
worker1 = Workers("navya",22,5643872145,'14a0976d43','vgfhg@gmail.com')
worker2 = Workers("rishitha",25,6543218765,'14g5454f65','bhjg@gmail.com')

#super call
worker1.get_details()


#creating the instance of Passenger class
customer1 = Customers("bindu",33,1234567890,'hgfhgfhgf@gmail.com',65)

#initialising the semi private variable or protected
customer1.set_passportnum('p6665432')

#printing the private variable
print(customer1.get_passportnum())

#other way to print private variable(not recommended
#print(passenger1._Passenger__passport_number)   #not working properly