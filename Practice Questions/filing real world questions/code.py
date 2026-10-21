 
 
 
 
class Employee :
    #PRIVATE __HourlyPay : FLOAT
    #PRIVATE __EmployeeNumber : STRING
    #PRIVATE __JobTittle : STRING
    #PRIVATE __PayYear2022 : ARRAY [0:51] OF FLOAT
    
    def __init__(self,php,pen,pjt):
        self.__HourlyPay=php
        self.__EmployeeNumber=pen
        self.__JobTittle=pjt
        self.__PayYear2022=[0.0]*52
    
    def GetEmployeeNumber (self):
        return self.__EmployeeNumber
    
    def SetPay (self,weekno,hours) :
        self.__PayYear2022[weekno]=hours*self.__HourlyPay
        
    def Gettotalpay(self):
        sum=0
        for i in range (52):
            sum=sum+self.__PayYear2022[i]
            
        return sum
    
    
class Manager (Employee) :
    
    #PRIVATE __BonusValue : FLOAT
    
    def __init__(self, php, pen, pjt,pbv):
        super().__init__(php, pen, pjt) 
        self.__BonusValue = pbv
        
    def SetPay(self, weekno, hours,bonus):
        bonus=bonus/100
        hours=hours+(hours*bonus)
        return super().SetPay(weekno, hours)
    
    
global EmployeeArray
EmployeeArray=[]*8

try :
    file=open("Employees.txt")
    for i in range (8):
        flag=False
        hourlypay=file.readline()
        employeenum=file.readline()
        temp=file.readline()
        try :
            
            bonusvalue=float(temp)
            jobtittle=file.readline()
            flag=True
        except:
            jobtittle=temp
            
        if flag==False :
            EmployeeArray[i]=Employee(hourlypay,employeenum,jobtittle)
        else :
            EmployeeArray[i]=Manager(hourlypay,employeenum,jobtittle,bonusvalue)
        
except :
    print("file doesnot exist")
    
    
def EnterHours ():
    try :
        file=open("HoursWeek1.txt")
        line="xyz"
        while line != "" :
            line=file.readline().strip()
            found=False
            i=0
            while not found :
                if EmployeeArray[i].__employeenumber == line :
                    hours=file.readline().strip()
                    Employee.SetPay(1,hours)
                    
            
    except :

        print("no file")        
        
        
EnterHours()
for i in range (7):
    
    EmployeeArray[i].Gettotalpay()