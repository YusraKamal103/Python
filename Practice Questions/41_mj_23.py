
# #q1

# #DECLARE DataArray : ARRAY [0:25] OF INTEGER

# DataArray =[0]*25

# try :
#     myfile=open("Data.txt",'r')
#     for i in range (25) :
        
#         line=int(myfile.readline())
#         DataArray[i]=line
# except IOError :
#     print("file doesnot exist")  
    

# def PrintArray (array):
    
#    line=" " 
#    for i in range (len(array)):
        
#     line = line + " " + str((array[i]))
        
        
        
#    print(line)    
                
# PrintArray(DataArray)


# def LinearSearch (array,tofind):
    
#     count=0
    
#     for i in range (len(array)):
#         if array[i] == tofind :
#             count +=1
    
    
#     return count


# #main

# flag=False


# while flag != True:
#     val=int(input("enter a value between 0 to 100 insclusive: "))
#     if val>=0 and val <= 100 :
#         flag = True


# result=LinearSearch(DataArray,val)
# print(f"the value {val} is found {result} times")


# #q2

# class vehicle ():
#     #PRIVATE __maxspeed,__currentspeed,__increase,__horipos : INTEGER
#     #PRIVATE __id : STRING
    
#     def __init__(self,Pmax,Pincrease,Pid):
#         self.__maxspeed=Pmax
        
#         self.__increase = Pincrease
        
#         self.__id = Pid
        
#         self.__currentspeed = 0
#         self.__horipos =0
    
#     def Getcurrentspeed (self):
#         return self.__currentspeed
    
#     def GetIncreaseAmount (self):
#         return self.__increase
    
#     def GetHorizontalPosition (self):
#         return self.__horipos
    
#     def GetMaxSpeed (self):
#         return self.__maxspeed    
    
#     def SetCurrentSpeed (self,Pcs):
#         self.__currentspeed=Pcs
        
#     def SetHorizontalPosition (self,Php):
#         self.__horipos=Php
        
#     def IncreaseSpeed (self):
#       if self.__increase+ self.__currentspeed <= self.__maxspeed :
            
#             self.__currentspeed=self.__increase+ self.__currentspeed
#             self.__horipos=self.__horipos + self.__currentspeed
    
#     def display (self ) :
#         print("speed is ",self.__currentspeed)
#         print("horizontal position is ",self.__horipos)                
        
# class Helicopter (vehicle):
#     #PRIVATE __verticalpos ,__verticalchan , __maxheight : INTEGER
    
#     def __init__(self, Pmax, Pincrease, Pid,Pverticalchange,Pmaxheight):
#         super().__init__(Pmax, Pincrease, Pid)
        
#         self.__verticalchange=Pverticalchange
#         self.__maxheight=Pmaxheight 
#         self.__verticalpos=0  
    
#     def IncreaseSpeed(self):
#         while ( self.__verticalpos + self.__verticalchange) <= self.__maxheight :
#             self.__verticalpos=self.__verticalpos + self.__verticalchange
#             while (self.__increase + self.__currentspeed) <= self.__maxspeed :
#                 self.__currentspeed= (self.__increase + self.__currentspeed)
#                 self.__horipos=self.__horipos+self.__currentspeed
        
#         num=vehicle.GetIncreaseAmount(self)
            
#         if num + (vehicle.Getcurrentspeed(self)) <= vehicle.GetMaxSpeed(self) :
            
#             self.__currentspeed=(vehicle.GetIncreaseAmount)+ (vehicle.Getcurrentspeed(self))
            
#             self.__horipos= vehicle.GetHorizontalPosition(self)+ (vehicle.Getcurrentspeed(self))
    
    
#     def GetVerticalPosition (self):
#         return self.__verticalpos
    
#     def display (self ) :
#         print("speed is ",self.__currentspeed)
#         print("horizontal position is ",self.__horipos)
#         print("vertical position is ",self.__verticalpos)
        
        
        
# car=vehicle(100,20,"Tiger")       
# new_helicopter=Helicopter(350,40,"Lion",3,100)

# car.IncreaseSpeed()
# car.IncreaseSpeed()
# car.display()

# print(" ")

# new_helicopter.IncreaseSpeed()
# new_helicopter.IncreaseSpeed()
# new_helicopter.display()
        
                   
                   
                   
# #q3
                   
# #DECLARE Animal : ARRAY [0:20] OF STRING


# Animal = [None]*20

# #DECLARE Colour : ARRAY[0:10] OF STRING


# colour = [None]*10

# #DECLARE animaltp,colourtp : INTEGER
# global animaltp
# global colourtp
# animaltp=0
# colourtp=0
                   
# def PushAnimal (data):
   
#     global animaltp
#     global colourtp
#     if animaltp == 20 :
#         return False
#     else:
#         Animal[animaltp]=data
#         animaltp+=1
#         return True                   
    
    
# def PopAnimal ():
#     #DECLARE returndata : STRING
#     global animaltp
#     global colourtp

    
#     if animaltp == 0 :
#         return " "
#     else:
#         animaltp-=1
#         returndata=Animal[animaltp-1]
       
#         return returndata    


# def PushColour (data) :
#     global colourtp
#     global animaltp
   
#     if colourtp == 10 :
#         return False
#     else:
#         colour[colourtp]=data
#         colourtp+=1
#         return True                   
    

# def PopColour ():
#     #DECLARE returndata : STRING
  
#     global colourtp
#     global animaltp
#     if colourtp == 0 :
#         return " "
#     else:
        
        
#         colourtp-=1
#         returndata=colour[colourtp-1]
#         return returndata    


   
# def ReadData ():
   
#     global colourtp
#     global animaltp
    
#     try:
#         file=open("AnimalData.txt",'r')
#         line="..."
#         while animaltp != 21 or line != "":
#             line=file.readline
#             PushAnimal(line)
        
#     except IOError:
#         print(" animal file doesnot exist")
        
#     try:
#         file=open("ColourData.txt",'r')
#         line="..."
#         while colourtp != 11 or line != "":
#             line=file.readline
#             PushColour(line)
        
#     except IOError:
#         print(" colour file doesnot exist")        
        
        
# def OutputItem() :
    
    
#     global colourtp
#     global animaltp
    
#     animals=PopAnimal()
#     colours=PopColour()
    
#     if animals != " " and colours != " " :
#         line= str(colours) + str(animals)
#         print(line)
#     elif animals!= " " and colours == " ":
#         PushAnimal(animals)
#         print("No colour")
        
#     elif animals == " " and colours != " ":
#         PushColour(colours)
#         print("no animal")    
           
# print(Animal)      
# ReadData()
# OutputItem()               
# OutputItem()
# OutputItem()
# OutputItem()




# -------------------------------
# Global Declarations (Part a)
# -------------------------------

Animal = [None] * 21   # 0 to 20
Colour = [None] * 11   # 0 to 10

AnimalTopPointer = 0
ColourTopPointer = 0


# -------------------------------
# PushAnimal (Part b i)
# -------------------------------

def PushAnimal(DataToPush):
    global AnimalTopPointer

    if AnimalTopPointer == 20:
        return False
    else:
        Animal[AnimalTopPointer] = DataToPush
        AnimalTopPointer += 1
        return True


# -------------------------------
# PopAnimal
# -------------------------------

def PopAnimal():
    global AnimalTopPointer

    if AnimalTopPointer == 0:
        return ""
    else:
        AnimalTopPointer -= 1
        return Animal[AnimalTopPointer]


# -------------------------------
# PushColour
# -------------------------------

def PushColour(DataToPush):
    global ColourTopPointer

    if ColourTopPointer == 10:
        return False
    else:
        Colour[ColourTopPointer] = DataToPush
        ColourTopPointer += 1
        return True


# -------------------------------
# PopColour
# -------------------------------

def PopColour():
    global ColourTopPointer

    if ColourTopPointer == 0:
        return ""
    else:
        ColourTopPointer -= 1
        return Colour[ColourTopPointer]


# -------------------------------
# ReadData (Part b v)
# -------------------------------

def ReadData():
    global AnimalTopPointer, ColourTopPointer

    # Read Animal data
    try:
        file = open("AnimalData.txt", "r")
        line = file.readline().strip()

        while line != "":
            PushAnimal(line)
            line = file.readline().strip()

        file.close()

    except IOError:
        print("Animal file does not exist")

    # Read Colour data
    try:
        file = open("ColourData.txt", "r")
        line = file.readline().strip()

        while line != "":
            PushColour(line)
            line = file.readline().strip()

        file.close()

    except IOError:
        print("Colour file does not exist")


# -------------------------------
# OutputItem (Part c)
# -------------------------------

def OutputItem():
    animal = PopAnimal()
    colour = PopColour()

    if animal != "" and colour != "":
        print(colour + " " + animal)

    elif animal != "" and colour == "":
        PushAnimal(animal)
        print("No colour")

    elif animal == "" and colour != "":
        PushColour(colour)
        print("No animal")


# -------------------------------
# Main Program (Part d)
# -------------------------------

ReadData()

OutputItem()
OutputItem()
OutputItem()
OutputItem()