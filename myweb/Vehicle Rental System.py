class Date: 
    def __init__(self, day , month , year):
        self.day = day
        self.month = month
        self.year = year
    def SetDay(self,day):
        self.day = day
    def SetMonth(self, month):
        self.month = month 
    def SetYear (self, year):
        self.year = year
    def GetDay(self):
        return self.day
    def GetYear(self):
        return self.year
    def GetMonth(self):
        return self.month 
    def SetYear(self):
        return self.year
    def Print(self):
        print(self.day , ",",self.month , ",",self.year)
        


class Manager:
    def __init__(self,name,address,phonenumber):
        self.name = name
        self.address = address
        self.phonenumber = phonenumber
    def SetName(self,name):
        self.name = name
    def SetAddress(self, address):
        self.address = address
    def SetPhoneNumber(self, phone):
        self.phonenumber = phone
    def GetName(self):
        return self.name
    def GetAddress(self):
        return self.address
    def GetPhoneNumber(self):
        return self.phonenumber

class Rental:
    def __init__(self , cus_id, reg_no , rentDate , returnDate , Fees):
        self.cus_id = cus_id
        self.reg_no = reg_no
        self.rentDate = rentDate
        self.returnDate = returnDate
        self.Fees = Fees
    def SetCustomerId(self, cus_id):
        self.cus_id = cus_id
    def SetRegistationNumber(self, reg_no):
        self.reg_no = reg_no
    def SetRentDate(self,rentDate):
        self.rentDate = rentDate
    def SetReturnDate(self, returnDate):
        self.returnDate = returnDate
    def SetFees(self, Fees):
        self.Fees = Fees
    def GetCustomerID(self):
        return self.cus_id
    def GetRegistrationNumber(self):
        return self.reg_no
    def GetRentDate(self):
        return self.rentDate
    def GetReturnDate(self):
        return self.returnDate
    def GetFees(self):
        return self.Fees
    def Print(self):
        print("Customer id is :", self.cus_id)
        print("Vehicle Registration Number is ", self.reg_no)
        print("Date is " , end = '')
        self.rentDate.Print()
        print("Return Date is ",end = '')
        self.returnDate.Print()
        print("Fees is ",self.Fees)
    def Write(self):
        fileagrement = open("agrements.txt", 'a')
        cusid = "Customer id is :" + str(self.cus_id) + "\n"
        regg = "Vehicle Registration Number is :" + str(self.reg_no) + "\n"
        rd = "Rent Date is :" + str(self.rentDate.GetDay()) + "," + str(self.rentDate.GetMonth()) + ","+ str(self.rentDate.GetYear())+ "\n"
        rtd = "Return Date is :" + str(self.returnDate.GetDay()) + "," + str(self.returnDate.GetMonth()) + ","+ str(self.returnDate.GetYear()) + "\n"
        fileagrement.write(cusid)
        fileagrement.write(regg)
        fileagrement.write(rd)
        fileagrement.write(rtd)
        fileagrement.write('\n')

class Payment : 
    def __init__(self , total):
        self.total = total
    def SetPayment (self, pay):
        self.total = pay
    def GetPaymen(self):
        return self.total
    
class Customer : 
    def __init__(self,id,name,address,phonenumber):
        self.id = id
        self.name = name
        self.address = address
        self.phonenumber = phonenumber
    def SetID(self,id):
        self.id = id
    def SetName(self,name):
        self.name = name
    def SetAddress(self, address):
        self.address = address
    def SetPhoneNumber(self, phone):
        self.phonenumber = phone
    def GetName(self):
        return self.name
    def GetAddress(self):
        return self.address
    def GetPhoneNumber(self):
        return self.phonenumber
    def GetID(self):
        return self.id
    def Print(self):
        print("The id is :" , self.id)
        print("The name is :", self.name)
        print("The address is : ", self.address)
        print("The phoneNumber is :" ,self.phonenumber)
    def Write(self):
        filecustomer = open("customer.txt", 'a')
        filecustomer.write("The id is :" +  str(self.id) + "\n")
        filecustomer.write("The name is :"+ str(self.name) + "\n")
        filecustomer.write("The address is : " + str(self.address) + "\n")
        filecustomer.write("The phoneNumber is :" + str(self.phonenumber) + "\n")
        filecustomer.write("\n")
class Vehicle :
    def __init__(self, reg_no , type):
        self.reg_no = reg_no
        self.type = type
    def SetRegistrationNumber(self, reg_no):
        self.reg_no = reg_no
    def SetVehicleType(self , type):
        self.type = type
    def GetRegistrationNumber(self):
        return self.reg_no
    def GetVehicleType(self):
        return self.type
    
class Car(Vehicle) :
    def __init__(self,maker,name , color , price, model , reg_no , typee):
        super().__init__(reg_no , typee)
        self.maker = maker 
        self.name = name
        self.color = color
        self.price = price
        self.model = model
    def SetMaker(self, maker):
        self.maker = maker
    def SetName(self, color):
        self.name = color
    def SetColor(self, color):
        self.color = color
    def SetPrice(self, price):
        self.price = price
    def SetModel (self, model ):
        self.model = model
    def GetMaker(self):
        return self.maker
    def GetColor(self):
        return self.color
    def GetPrice(self):
        return self.price
    def GetModel(self):
        return self.model
    def GetName(self):
        return self.name
    def Print(self):
        print("The registration no is :", self.reg_no)
        print("The car maker is :",self.maker)
        print("The car name is :",self.name)
        print("The car model is :",self.model)
        print("The car rent is :",self.price)
        print("The car color is :",self.color)
    def Write(self):
        fileVehicle = open("vehicles.txt", "a")
        fileVehicle.write("The registration no is :" +  str(self.reg_no) + "\n")
        fileVehicle.write("The car maker is :" + str(self.maker) + "\n")
        fileVehicle.write("The car name is :" + str(self.name)+"\n")
        fileVehicle.write("The car model is :" + str(self.model)+ "\n")
        fileVehicle.write("The car rent is :" + str(self.price) + "\n")
        fileVehicle.write("The car color is :" + str(self.color) + "\n")
        fileVehicle.write("\n")
        
class Bus(Vehicle):
    def __init__(self,name,maker , color , price, model , reg_no , typee) :      
        super().__init__(reg_no , typee)
        self.maker = maker 
        self.name = name
        self.color = color
        self.price = price
        self.model = model
    def SetMaker(self, maker):
        self.maker = maker
    def SetColor(self, color):
        self.color = color
    def SetPrice(self, price):
        self.price = price
    def SetModel (self, model ):
        self.model = model
    def SetName(self, name):
        self.name = name
    def GetMaker(self):
        return self.maker
    def GetColor(self):
        return self.color
    def GetPrice(self):
        return self.price
    def GetModel(self):
        return self.model
    def GetName(self):
        return self.name
    def Print(self):
        print("The registration no is :", self.reg_no)
        print("The bus maker is :",self.maker)
        print("The bus name is :",self.name)
        print("The bus model is :",self.model)
        print("The bus rent is :",self.price)
        print("The bus color is :",self.color)
    def Write(self):
        fileVehicle = open("Vehicles.txt", "a")
        fileVehicle.write("The registration no is :" +  str(self.reg_no) + "\n")
        fileVehicle.write("The bus maker is :" + str(self.maker) + "\n")
        fileVehicle.write("The bus name is :" + str(self.name)+"\n")
        fileVehicle.write("The bus model is :" + str(self.model)+ "\n")
        fileVehicle.write("The bus rent is :" + str(self.price) + "\n")
        fileVehicle.write("The bus color is :" + str(self.color) + "\n")
        fileVehicle.write("\n")
        
class MotorBike(Vehicle):
    def __init__(self,maker , name , color , price, model, reg_no , typee):
        super().__init__(reg_no , typee)
        self.maker = maker 
        self.name = name
        self.color = color
        self.price = price
        self.model = model
    def SetMaker(self, maker):
        self.maker = maker
    def SetColor(self, color):
        self.color = color
    def SetPrice(self, price):
        self.price = price
    def SetModel (self, model ):
        self.model = model
    def SetName (self, name):
        self.name = name
    def GetMaker(self):
        return self.maker
    def GetColor(self):
        return self.color
    def GetPrice(self):
        return self.price
    def GetModel(self):
        return self.model
    def GetName (self):
        return self.name
    def Print(self):
        print("The registration no is :", self.reg_no)
        print("The bike maker is :",self.maker)
        print("The bike name is :",self.name)
        print("The bike model is :",self.model)
        print("The bike rent is :",self.price)
        print("The bike color is :",self.color)
    def Write(self):
        fileVehicle = open("vehicles.txt", "a")
        fileVehicle.write("The registration no is :" +  str(self.reg_no) + "\n")
        fileVehicle.write("The bike maker is :"  + str(self.maker) + "\n")
        fileVehicle.write("The bike name is :" + str(self.name)+"\n")
        fileVehicle.write("The bike model is :" + str(self.model)+ "\n")
        fileVehicle.write("The bike rent is :" + str(self.price) + "\n")
        fileVehicle.write("The bike color is :" + str(self.color) + "\n")
        fileVehicle.write("\n")
        

def CalculateFees(day1, day2 , price):
    res = day2-day1
    res = res*price
    return res

CarArray = []
BikeArray = []
BusArray = []
AgrementAray = []
CustomerArray = []
hondaCivic = Car('honda', 'civic','red',5000, 2016, 'lzu4050', 'car')
toyotaCorolla = Car('toyota' , 'corolla', 'white',4000, 2018 , 'len1223', 'car')
honda125 = MotorBike('honda', '125','black',1000, 2001, 'lwf2034', 'bike')
daewoo = Bus('toyota', 'daewoo', 'white' , 10000, 2020 , 'bln5656', 'bus')
CarArray.append(hondaCivic)
CarArray.append(toyotaCorolla)
BikeArray.append(honda125)
BusArray.append(daewoo)

RentDate = Date(5, 12, 2020)
ReturnDate = Date(12 , 12, 2020)
NewCustomer = Customer('123', 'Hammad', 'Lahore', '03102324345')
CustomerArray.append(NewCustomer)
Fees = CalculateFees(RentDate.GetDay() , ReturnDate.GetDay(), hondaCivic.GetPrice())
agreement1 = Rental(NewCustomer.GetID(),hondaCivic.GetRegistrationNumber(),RentDate,ReturnDate, Fees)
AgrementAray.append(agreement1)
id = 1
while(1):
    print("Press 1 for add new vehicle ")
    print("Press 2 for add new customer ")
    print("Press 3 for show all vehicles ")
    print("Press 4 for delete vehicle ")
    print("Press 5 for show customer data ")
    print("Press 6 for show all the rental agreements")
    print("Press 7 for update vehicle rent")
    print("Press 8 for change customer record ")
    print("Press 9 for make agrement of the customer for renting vehicle")
    print("Press 10 for show vehicle specification")
    print("Press 11 for write the rental agreeemnents in the separate file")
    print("Press 12 for writing the vehicles and its specification in separate file")
    print("press 13 for writing the Customers data in separate file")
    print("Press 14 for exit")
    x = int(input ())
    if x == 1 :
        print("Press C for Car , M for motorbike , B for bus")
        inp = input()
        if inp == 'C' :
            reg  = input("Enter the registration number :")
            maker = input("Enter the maker :")
            model = input("Enter the model :")
            name = input("Enter the name :")
            color = input("Enter the color :")
            rent = input("Enter the rent :")
            typee = input("Enter the type of vehicle :")
            NewCar = Car(maker, name, color ,rent, model ,reg ,typee)
            CarArray.append(NewCar)
        elif inp == 'M' :
            reg  = input("Enter the registration number :")
            maker = input("Enter the maker :")
            model = input("Enter the model :")
            name = input("Enter the name :")
            color = input("Enter the color :")
            rent = input("Enter the rent :")
            typee = input("Enter the type of vehicle :")
            NewBike = MotorBike(maker, name, color ,rent, model ,reg ,typee)
            BikeArray.append(NewBike)
            
        elif input == 'B' : 
            reg  = input("Enter the registration number :")
            maker = input("Enter the maker :")
            model = input("Enter the model :")
            name = input("Enter the name :")
            color = input("Enter the color :")
            rent = input("Enter the rent :")
            typee = input("Enter the type of vehicle :")
            NewBus = Bus(maker, name, color ,rent, model ,reg ,typee)
            BusArray.append(NewBus)
    elif x == 2 :
        name = input("Enter the name of customer :")
        address = input("Enter the address of customer :")
        phone = input("Enter the phonenumber of customer :")
        Customerr = Customer(id , name, address ,phone)
        id = id+1
        CustomerArray.append(Customerr)
    elif x== 3 : 
        for cars in CarArray:
            cars.Print()
        for bikes in BikeArray:
            bikes.Print()
        for buses in BusArray:
            buses.Print()
    elif x == 4 : 
        y = input("Enter the registration number :")
        i = 0
        while i < len(CarArray):
            if (CarArray[i].GetRegistrationNumber() == y):
                del CarArray[i]
            i = i+1
        i = 0
        while i < len(BikeArray):
            if (BikeArray[i].GetRegistrationNumber() == y):
                del BikeArray[i]
            i = i+1
        i = 0
        while i < len(BusArray):
            if (BusArray[i].GetRegistrationNumber() == y):
                del BusArray[i]
            i = i+1
    elif x == 5 : 
        i = 0 
        while i < len(CustomerArray):
            CustomerArray[i].Print()
            i = i +1
    elif x== 6 : 
        for agrements in AgrementAray:
            agrements.Print()
    elif x == 8 :
        y= input("Enter the customer name")
        for customers in CustomerArray:
            if(customers.GetName() == y):
                newName = input("Enter the new name")
                newAddress = input("Enter the new address")
                newPhoneNumber = input("Enter the new PhoneNumber")
                customers.SetName(newName)
                customers.SetAddress(newAddress)
                customers.SetPhoneNumber(newPhoneNumber)
        
    elif x== 9 : 
        print("Press 1 for entering a new customer and a new vehicle agreement")
        print("Press 2 for making an agrement wwith the vehicles in the database and customers in the database")
        y= int(input())
        if(y == 1):
            print("Press C for Car , M for motorbike , B for bus")
            inp = input()
            if inp == 'C' :
                reg  = input("Enter the registration number")
                maker = input("Enter the maker ")
                model = input("Enter the model")
                name = input("Enter the name")
                color = input("Enter the color ")
                rent = int(input("Enter the rent "))
                typee = input("Enter the type of vehicle")
                NewCar = Car(maker, name, color ,rent, model ,reg ,typee)
                CarArray.append(NewCar)
                name = input("Enter the name of customer")
                address = input("Enter the address of customer")
                phone = input("Enter the phonenumber of customer")
                Customerr = Customer(id , name, address ,phone)
                id = id+1
                CustomerArray.append(Customerr)
                print("Enter the rent date as day enter month enter year")
                d = int(input())
                m = int(input())
                y = int(input())
                print("Enter the return date as day enter month enter year")
                d1 = int(input())
                m1 = int(input())
                y1 = int(input())
                rentDate = Date(d,m,y)
                returnDate = Date(d1,m1,y1)
                Fees= CalculateFees(rentDate.GetDay(), returnDate.GetDay(),rent)
                NewAggrement = Rental(id , reg ,rentDate ,returnDate , Fees)
                AgrementAray.append(NewAggrement)
            elif inp == 'M' :
                reg  = input("Enter the registration number")
                maker = input("Enter the maker ")
                model = input("Enter the model")
                name = input("Enter the name")
                color = input("Enter the color ")
                rent = int(input("Enter the rent "))
                typee = input("Enter the type of vehicle")
                NewBike = MotorBike(maker, name, color ,rent, model ,reg ,typee)
                BikeArray.append(NewCar)
                name = input("Enter the name of customer")
                address = input("Enter the address of customer")
                phone = input("Enter the phonenumber of customer")
                Customerr = Customer(id , name, address ,phone)
                id = id+1
                CustomerArray.append(Customerr)
                print("Enter the rent date as day enter month enter year")
                d = int(input())
                m = int(input())
                y = int(input())
                print("Enter the return date as day enter month enter year")
                d1 = int(input())
                m1 = int(input())
                y1 = int(input())
                rentDate = Date(d,m,y)
                returnDate = Date(d1,m1,y1)
                Fees= CalculateFees(rentDate.GetDay(), returnDate.GetDay(),rent)
                NewAggrement = Rental(id , reg ,rentDate ,returnDate , Fees)
                
            elif input == 'B' : 
                reg  = input("Enter the registration number")
                maker = input("Enter the maker ")
                model = input("Enter the model")
                name = input("Enter the name")
                color = input("Enter the color ")
                rent = int(input("Enter the rent "))
                typee = input("Enter the type of vehicle")
                NewBus = Bus(maker, name, color ,rent, model ,reg ,typee)
                BusArray.append(NewCar)
                name = input("Enter the name of customer")
                address = input("Enter the address of customer")
                phone = input("Enter the phonenumber of customer")
                Customerr = Customer(id , name, address ,phone)
                id = id+1
                CustomerArray.append(Customerr)
                print("Enter the rent date as day enter month enter year")
                d = int(input())
                m = int(input())
                y = int(input())
                print("Enter the return date as day enter month enter year")
                d1 = int(input())
                m1 = int(input())
                y1 = int(input())
                rentDate = Date(d,m,y)
                returnDate = Date(d1,m1,y1)
                Fees= CalculateFees(rentDate.GetDay(), returnDate.GetDay(),rent)
                NewAggrement = Rental(id , reg ,rentDate ,returnDate , Fees)
        elif y == 2:
            print("Press C for Car , M for motorbike , B for bus")
            inp = input()
            if inp == 'C' :
                reg  = input("Enter the registration number")
                customerid = int(input("Enter the customer id"))
                print("Enter the rent date as day enter month enter year")
                d = int(input())
                m = int(input())
                y = int(input())
                print("Enter the return date as day enter month enter year")
                d1 = int(input())
                m1 = int(input())
                y1 = int(input())
                rentDate = Date(d,m,y)
                returnDate = Date(d1,m1,y1)
                i = 0 
                check1 = 0
                index1 = -1
                while i < len(CustomerArray):
                    if(CustomerArray[i].GetID() == customerid):
                        index1 = i
                        check1 = 1
                    i= i+1
                check2 = 0
                i = 0 
                index2 = -1
                while i < len(CarArray):
                    if(CarArray[i].GetRegistrationNumber() == reg):
                        index2 = i
                        check2 = 1
                    i= i+1
                if(check1 == 1 and check2 == 1):
                    fees =CalculateFees(rentDate.GetDay(), returnDate.GetDay(), CarArray[index2].GetPrice())
                    NewAggrement = Rental(CustomerArray[index1].GetID(),CarArray[index2].GetRegistrationNumber(),rentDate,returnDate,fees)
                    AgrementAray.append(NewAggrement)
                

            elif inp == 'M' :
                reg  = input("Enter the registration number")
                customerid = int(input("Enter the customer id"))
                print("Enter the rent date as day enter month enter year")
                d = int(input())
                m = int(input())
                y = int(input())
                print("Enter the return date as day enter month enter year")
                d1 = int(input())
                m1 = int(input())
                y1 = int(input())
                rentDate = Date(d,m,y)
                returnDate = Date(d1,m1,y1)
                i = 0 
                check1 = 0
                index1 = -1
                while i < len(CustomerArray):
                    if(CustomerArray[i].GetID() == customerid):
                        index1 = i
                        check1 = 1
                    i= i+1
                check2 = 0
                i = 0 
                index2 = -1
                while i < len(CarArray):
                    if(BikeArray[i].GetRegistrationNumber() == reg):
                        index2 = i
                        check2 = 1
                    i= i+1
                if(check1 == 1 and check2 == 1):
                    fees = CalculateFees(rentDate.GetDay(), returnDate.GetDay(), BikeArray[index2].GetPrice())
                    NewAggrement = Rental(CustomerArray[index1].GetID(),BikeArray[index2].GetRegistrationNumber(),rentDate,returnDate,fees)
                    AgrementAray.append(NewAggrement)
                
            elif input == 'B' : 
                reg  = input("Enter the registration number")
                customerid = int(input("Enter the customer id"))
                print("Enter the rent date as day enter month enter year")
                d = int(input())
                m = int(input())
                y = int(input())
                print("Enter the return date as day enter month enter year")
                d1 = int(input())
                m1 = int(input())
                y1 = int(input())
                rentDate = Date(d,m,y)
                returnDate = Date(d1,m1,y1)
                i = 0 
                check1 = 0
                index1 = -1
                while i < len(CustomerArray):
                    if(CustomerArray[i].GetID() == customerid):
                        index1 = i
                        check1 = 1
                    i= i+1
                check2 = 0
                i = 0 
                index2 = -1
                while i < len(CarArray):
                    if(BusArray[i].GetRegistrationNumber() == reg):
                        index2 = i
                        check2 = 1
                    i= i+1
                if(check1 == 1 and check2 == 1):
                    Fees = CalculateFees(rentDate.GetDay(), returnDate.GetDay(), BusArray[index2].GetPrice())
                    NewAggrement = Rental(CustomerArray[index1].GetID(),BusArray[index2].GetRegistrationNumber(),rentDate,returnDate, Fees)
                    AgrementAray.append(NewAggrement)
                    
        
    elif x == 7 :
        y = input("Enter the registration number")
        pricee = input("Enter the new rent")
        i = 0
        while i < len(CarArray):
            if (CarArray[i].GetRegistrationNumber() == y):
                CarArray[i].SetPrice(pricee)
            i = i+1
        i = 0
        while i < len(BikeArray):
            if (BikeArray[i].GetRegistrationNumber() == y):
                BikeArray[i].SetPrice(pricee)
            i = i+1
        i = 0
        while i < len(BusArray):
            if (BusArray[i].GetRegistrationNumber() == y):
                BusArray[i].SetPrice(pricee)
            i = i+1
    elif x == 10 : 
        y = input("Enter the registration number")
        i = 0
        while i < len(CarArray):
            if (CarArray[i].GetRegistrationNumber() == y):
                CarArray[i].Print()
            i = i+1
        i = 0
        while i < len(BikeArray):
            if (BikeArray[i].GetRegistrationNumber() == y):
                BikeArray[i].Print()
            i = i+1
        i = 0
        while i < len(BusArray):
            if (BusArray[i].GetRegistrationNumber() == y):
                BusArray[i].Print()
            i = i+1
    elif x == 11 :
        for agrements in AgrementAray:
            agrements.Write()
    elif x == 12 : 
        for cars in CarArray:
            cars.Write()
        for bikes in BikeArray:
            bikes.Write()
        for buses in BusArray:
            buses.Write()
    elif x == 13 : 
        for customers in CustomerArray:
            customers.Write()
    elif x == 14 :
        break
        
     
    
            
    
    
    
    

