
# #day 1

# ###OOP

# #create a class car with :
# #brand
# #speed
# #method : show detail


# class Car :
    
#     def __init__(self,Pbrand,Pspeed): #constructor
        
#         self.brand=Pbrand
#         self.speed=Pspeed
        
#     def ShowDetails (self): #method
#         print("brand",self.brand)  
#         print("speed",self.speed)
        
#     #GETTER
    
#     def get_speed (self):
#         return self.speed
    
#     #SETTER 
    
#     def set_speed (self,Pspeed):
#         if Pspeed >= 0 :
#             self.speed=Pspeed
#         else :
#             print("invalid speed")
                    
        
# car1=Car("BMW",350)
# car2=Car("honda",100)        

# car1.ShowDetails()
# print(car1.speed)

# car1.set_speed(90)
# print(car1.get_speed())
        
          
#-------------------------------------------------------------

# #day 2

# #ON/23/P42/Q3

# from datetime import datetime
# class Character :
#     #DECLARE CharacterName : STRING
#     #DCELARE DOB : DATE
#     #DECLARE intelligence : REAL
#     #DECLARE speed : INTEGER
    
#     def __init__(self,Pcname,pdob,pintel,pspeed):
#         self.CharacterName=Pcname
#         self.DOB=pdob
#         self.intelligence=pintel
#         self.speed=pspeed
        
        
#     def GetIntelligence (self):
#         return self.intelligence
    
#     def GetName (self):
#         return self.CharacterName
    
#     def SetIntelligence (self,Pintell):
#         self.intelligence=Pintell
    
#     def Learn (self):
        
#          self.intelligence=self.intelligence * 1.1
            
#     def ReturnAge (self):
#         return 2023-(self.DOB.year)  
    
# FirstCharacter=Character("Royal" , datetime(2019,1,1),70,30)

# FirstCharacter.Learn()
# print("Name",FirstCharacter.GetName(),"with age",FirstCharacter.ReturnAge(),"with intelligence",FirstCharacter.GetIntelligence())

# class MagicCharacter (Character):     
#     def __init__(self, Pcname, pdob, pintel, pspeed,Pelement):
#         super().__init__(Pcname, pdob, pintel, pspeed)
        
#         #DECLARE Element : STRING        
        
#         self.Element=Pelement   
        
        
#     def Learn(self):
#         if self.Element == "fire" or  self.Element == "water":
#             super().SetIntelligence(super().GetIntelligence()*1.2)
#         elif self.Element == "earth" :
#             super().SetIntelligence(super().GetIntelligence()*1.3)
#         else:
#             super().SetIntelligence(super().GetIntelligence()*1.1)                  
            
            
# FirstMagic=MagicCharacter("Light",datetime(2018,3,3),75,22,"fire")  

# FirstMagic.Learn()          
# print("Name",FirstMagic.GetName(),"with age",FirstMagic.ReturnAge(),"with intelligence",FirstMagic.GetIntelligence(),"with element ",FirstMagic.Element)

#-------------------------------------------------------------------------------------------------------------------------------
#   day 3





# class EventItem()  :
#     #PRIVATE __eventname : STRING
#     #PRIVATE __type : STRING 
#     #PRIVATE __difficulty : INTEGER
    
#     def __init__(self,Peventname,Ptype,Pdifficulty):
        
#         self.__eventname=Peventname
#         self.__type=Ptype
#         self.__difficulty=Pdifficulty
        
#     def Getname (self):
#         return self.__eventname
#     def Getdifficulty (self):
#         return self.__difficulty
#     def Gettype (self):
#         return self.__type
    
    
# #main

# #DECLARE Group: ARRAY [0:5] OF EventItem

# Group=[]

# Group.append(EventItem("Bridge","jump",3))
# Group.append(EventItem("Water Wade","swim",4))
# Group.append(EventItem("100 mile run ","run ",5))
# Group.append(EventItem("Gridlock","drive",2))
# Group.append(EventItem("Wall on wall","jump",4))




# class Character() :
#     # PRIVATE __CharacterName : STRING 
#     # PRIVATE __Jump,__Swim,__Run,__Drive : INTEGER
    
#     def __init__ (self,PCN,PJ,PS,PR,PD):
#         self.__CharacterName=PCN
#         self.__Jump=PJ
#         self.__Run=PR
#         self.__Swim=PS
#         self.__Drive=PD
        
#     def GetName(self):
#         return self.__CharacterName
    
#     def CalculateScore (self,eventtype, difficulty):
        
#         if eventtype=="jump":
#             skill=self.__Jump
#         elif eventtype=="run":
#             skill==self.__Run
#         elif eventtype=="swim":
#             skill=self.__Swim
#         else:
#             skill=self.__Drive
            
#         if skill>=difficulty :
#             return 100
#         else:            
    
#             difference= skill-difficulty
#             if difference == 1:
#                 return 80
#             elif difference == 2:
#                 return 60
#             elif difference == 3:
#                 return 40
#             elif difference == 4:
#                 return 20
#             else:
#                 return 0
    
            
      
        
# p1=Character("Tarz",5,3,5,1)
# p2=Character("Geni",2,2,3,4)            

# #main

# p1pts=0
# p2pts=0
# p1score =0
# p2score=2

# for x in range (5):
#     p1score=p1.CalculateScore(Group(x).Gettype(),Group(x).Getdifficulty())
#     p2score=p2.CalculateScore(Group(x).gettype(),Group(x).getdifficulty())
#     if p1score>p2score :
#         p1pts=p1pts + 1
#         print (p1.GetName(),"u hav won this event")
#         if p1score > p2score:
#             P1Points = P1Points + 1
#             print(p1.GetName(), "you win this event")
#         elif p2score > p1score:
#             P2Points = P2Points + 1
#             print(p2.GetName(), "you win this event")
#         else:
#             print("This event is a draw")
# if p1pts > p2pts:
#  print(p1.GetName(), "you have won with", P1Points)
# elif p2pts>p1pts:
#  print(p1.GetName(), "you have won with", P2Points)
# else:
#  print("It's a draw")

#---------------------------------------------------------------------


# #

# StackVowel=[0]*100       
# StackConsonant=[0]*100


# global VowelTop
# global ConsonantTop

# VowelTop=0
# ConsonantTop=0

# def PushData (data) :
#     global VowelTop,ConsonantTop,StackConsonant,StackVowel
    
#     if data in ['a','e','i','o','u']:
#         if VowelTop <= 100:
#             StackVowel.append(data)
#            # StackVowel[VowelTop]=data
#             VowelTop+=1
#         else:
#             print("Stack is full")    
#     else :
#         if ConsonantTop <= 100 :
#             StackConsonant[ConsonantTop]=data
#             ConsonantTop+=1
#         else:
#             print("Stack is full")    


# def ReadData ():
                        
#     try :
        
#         file=open("StackData.txt",'r')
#         for line in file :
            
#             PushData(line.strip())
#         file.close()    
        
#     except IOError :
        
#         print("file doesnot exist")   
        

# def PopVowel ():
    
#     global StackVowel,VowelTop
    
#     if VowelTop !=  0 :
#         data=StackVowel[VowelTop]
#         VowelTop-=1
        
#     else :
#         data="No Data" 
        
#     return data       
                

# def PopConsonant ():
    
#     global StackConsonant,ConsonantTop
    
#     if ConsonantTop != 0 :
#         data=StackConsonant[ConsonantTop]
#         ConsonantTop-=1
#     else :
#         data="No Data" 
        
#     return data               


# def PopVowel ():
    
#     global StackVowel,VowelTop
    
#     if VowelTop -1>= 0 :
       
#         VowelTop-=1
#         data=StackVowel[VowelTop]
#         del StackVowel [-1]
#     else :
#         data="No Data" 
        
#     return data       
                

# def PopConsonant ():
    
#     global StackConsonant,ConsonantTop
    
#     if ConsonantTop -1>= 0 :
       
#         ConsonantTop-=1
#         data=StackConsonant[ConsonantTop]
#         del StackConsonant [-1]
#     else :
#         data="No Data" 
        
#     return data     

# VowelTop=0
# ConsonantTop=0

# ReadData()
# letters=""
# data=""

# for i in range (5):
#     flag=False
#     while flag==False:
#         choice=input("vowel or consonant").lower()
#         if choice == "vowel":
#             data=PopVowel()
#             if data != "No Data" :
#                 letters = letters + str(data)
#                 flag= True
#             else:
#                 print("no vowels left") 
#         else:
#             data==PopConsonant()
#             if data != "No Data" :
#                 letters=letters + str(data)       
#                 flag=True
            
#             else:
#                 print("no consonant left")    

# print(letters)


#-----------------------------------------------------------------------
#day3

# def IterativeCalculate (number):
#     Tofind=number #integer
#     Total=0
#     while number != 0 :
#         if Tofind % number == 0 :
#             Total=Total+number
        
#         number=number-1
        
#     return Total    


# print(IterativeCalculate(10))

# def RecursiveValue (number,Tofind) :
    
#     if number == 0 :
#         return 0
#     else:
#         if Tofind % number == 0 :
#             return (number + RecursiveValue(number-1,Tofind))
#         else :
#            return     RecursiveValue(number-1,Tofind)
       
       
       
# print(RecursiveValue(50,50))       

#------------------------------------------

#DECLARE NumberArray:ARRAY[0:7] OF INTEGER
NumberArray=[100,85,644,22,15,8,1]

#DECLARE lastitem , checkitem : INTEGER
# DECLARE  loopagain : BOOLEAN

def RecursiveInsertion(array,NumberElements) :
    
    if NumberElements<=1 :
        return array
    else :
        RecursiveInsertion(array,NumberElements-1)
        lastitem=array[NumberElements-1]
        checkitem=NumberElements - 2
        
    loopagain=True
    if checkitem <0 :
        loopagain=False
    else :
        if array[checkitem]<lastitem:
            loopagain=False
            
            
    while loopagain :
        array[checkitem+1]  = array[checkitem]
        checkitem=checkitem-1
        if checkitem<0 :
            loopagain=False
        else :
            if array[checkitem]< lastitem :
                loopagain=False

    array[checkitem+1]= lastitem
    return array 


result=RecursiveInsertion(NumberArray,7)

print("RECURSIVE")

print(result)



    
        