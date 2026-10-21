# Q/- write a pseudocode to define a record data type , student. which 
# will store id,name,age and gender 


class student:

    #DECLARE Id,Age : INTEGER
    #DECLARE Name : STRING
    # DECLARE Gender : CHAR 


    def _init_(self,Pid,Pname,PAge,Pgender):
        self.Id = Pid
        self.Name= Pname
        self.Age=PAge
        self.Gender=Pgender


#DECLARE mystudent: student

mystudent=student(10001, "warda", 17 ,"F")

print("Id",mystudent.Id)
print("name",mystudent.Name)
print("age",mystudent.Age)
print("gender",mystudent.Gender)

myid=int(input("enter id : "))
myName=input("enter name : ")
myage=int(input("enter age : "))
mygender=input("enter gender :")

student1=student(myid,myName,myage,mygender)


# Q/- write a pseudocode to define a record data type , student. which 
# will store id,name,age and gender 


class student:

    #DECLARE Id,Age : INTEGER
    #DECLARE Name : STRING
    # DECLARE Gender : CHAR 


    def _init_(self,Pid,Pname,PAge,Pgender):
        self.Id = Pid
        self.Name= Pname
        self.Age=PAge
        self.Gender=Pgender



mystudent=student(10001, "warda", 17 ,"F")




#q/- write a program code which input and stores id, name, age, and gender of 
#20 students in single 1d array , details which will be declared as a record datatype, Student

#DECLARE Details : ARRAY [0:19] OF student

Details = []

for i in range(5):
    myid=int(input("enter id : "))
    myName=input("enter name : ")
    myage=int(input("enter age : "))
    mygender=input("enter gender :")
    
    student1=student(myid,myName,myage,mygender)


    Details.append(student1)



print (Details[4])


#Q/-  make a record data type Linked List, which will contain node of datatype
#string and next pointer 

#b) declare a global list of 5 elements of type linked list and declare 
#global variables start pointer and free pointer

#c) define a procedure initialize() which will initialize the array
#assign -1 to start pointer and 0 free pointer 


class linkedlist:
    #DECLARE node : STRING
    #DECLARE nxt_ptr : INTEGER

    def __init__(self,Pnode,Pnxt_ptr):
        self.node=Pnode
        self.nxt_ptr=Pnxt_ptr



list=[None]*5

def initialize() :
    str_ptr=-1
    free_ptr=0
   
    for i in range(5):
      x=""
      y=0
      temp=linkedlist(x,y)
      list[i]=temp
      
    
 



print (list[3])



class vehicle :
    #PRIVATE  RegNo : STRING
    #PRIVATE EngineSize : STRING
    #PRIVATE Model :STRING
    #PRIVATE Price : REAL
    #PRIVATE PurchaseDate : DATE

    #Constructor
    def __init__(self,PReg,PPrice ):
        self.RegNo= PReg
        self.Price=PPrice

    def setEngineSize(self,PES):
        self.EnigineSize=PES

    def setModel (self,PM):
        self.Model=PM        
    
    def setPurchaseDate (self,PPD):
        self.PurchaseDate = PPD

    def GetRegNo (self):
        return self.RegNo

    def GetEngineSize (self):
        return self.EnigineSize

    def GetModel (self):
        return self.Model

    def DisplayAll (self):
        print("registration: ",self.RegNo," of car ",self.Model," has a price of ",self.Price, "has engine ", self.EnigineSize)    


MyCar=vehicle("AAA-000",70000)
MyCar.setModel("civic")

print(MyCar.GetModel())



#p4 pg 93 question

class balloon :
    #PRIVATE __health : INTEGER
    #PRIVATE __color : STRING
    #PRIVATE __defenceitem : STRING

    # CONSTRUCTOR
    
    def __init__(self,pcolor,pdefenceitem):
        self.__color=pcolor                           #in the constructor all attributes of the class would start with self
        self.__defenceitem=pdefenceitem 
        self. __health=100

    def GetDefenceitem(self):
            return self.__defenceitem
    
    def changehealth (self,val) :                        #all function or procedure within class will hav first parameter of self
    
         self.__health=val+self.__health

    def checkhealth (self):
         if ( self.__health <= 0) :
              return True
         else:
              return False
         
#DECLARE defitem,COLOR : STRING
         

COLOR=input("enter color: ")
defitem=input("enter defense item: ")
balloon1=balloon(defitem,COLOR)
         
#DECLARE balloon2 : balloon
def defend (balloon2):
     opstrength=int(input("enter opponent strength:  "))
     balloon2.changehealth(-opstrength)

     print("defence item:  ",balloon2.GetDefenceitem())
     myhealth=balloon2.checkhealth()
     if myhealth== True:
          print("defence failed")
     else:
          print("defence suceeded ")



myballoon = defend(balloon1)         
