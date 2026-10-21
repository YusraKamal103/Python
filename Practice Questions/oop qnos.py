

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

# Group=[None]*5

# Group[0]=(EventItem("Bridge","jump",3))
# Group[1]=(EventItem("Water Wade","swim",4))
# Group[2]=(EventItem("100 mile run ","run ",5))
# Group[3]=(EventItem("Gridlock","drive",2))
# Group[4]=(EventItem("Wall on wall","jump",4))


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

         
         
#__________________________________________________________________________#

#new question

#q1 #9618/41/on/24

# class Horse ():
#     #     PRIVATE __Name : STRING 
#     #     PRIVATE __maxheight , __successpercentage : INTEGER
    
#     def __init__(self,Pname,Pmh,Psp):
#         self.__Name=Pname
#         self.__maxheight=Pmh
#         self.__successpercentage=Psp
        
#     def GetName (self):
#         return self.__Name
    
#     def Getmaxheight (self):
#         return self.__maxheight
    
#     def success (self,Prisk,Pheight):
#         if Pheight > self.__maxheight:
#             return self.__successpercentage*0.2
#         if Pheight<=self.__maxheight:
#             if Prisk ==5 :
#                 return self.__successpercentage*0.6
#             elif Prisk == 4 :
#                 return self.__successpercentage*0.7
#             elif Prisk== 3 :
#                 return self.__successpercentage *0.8
#             elif Prisk == 2 :
#                 return self.__successpercentage*0.9
#             else:
#                 return self.__successpercentage*1
                
                
                                 
        
    
    
# #DECLARE horses:ARRAY [0:2] OF Horse

# horses=[]

# horses.append(Horse("Beauty",150,72))
# horses.append(Horse("Jet",160,65))

# print(horses[0].GetName())
# print(horses[1].GetName())        
        
        
# class Fence ():
#     #PRIVATE __height,__risk : INTEGER
    
#     def __init__(self,Prisk,Pheight):
#         self.__height=Pheight
#         self.__risk=Prisk    
    
#     def Getheight (self):
#         return self.__height
    
#     def Getrisk (self):
#         return self.__risk    
    

# #DECLARE course :ARRAY [0:4] OF Fence
# course=[None]*4

# #DECLARE flag : BOOLEAN
# flag=False

# for i in range (4):
#     flag=False
#     while flag != True :
#         height=int(input("enter height"))
#         risk=int(input("enter risk"))
#         if (height>=70 and height<=180) and (risk>=1 and risk<=5):
#             flag=True
#             course[i]=Fence(risk,height)


# total=[0]*2     

# i=0            
# for i in range (0,2):
#      name=(horses[i].GetName())
#      for j in range (4):
#          result=horses[i].success(course[j].Getrisk(),course[j].Getheight())
#          print("the horse",name," at fence ",j+1," has a chance of ",result," %.")
#          total[i]=total[i]+result
         

# for i in range(2):
#     avg=total[i]/4
#     total[i]=avg
#     name=(horses[i].GetName())
#     print(name,"has an average of ",avg,"% chance of success ")
    
# if total[0]>total[1]:
#     name=horses[0].GetName()
#     print("the horse ",name," has a greater score")
# else:
#     name=horses[1].GetName()
#     print("the horse ",name," has a greater score")

#_________________________________________________________x___________________________



#linked list

class node :
    #PRIVATE data,nxtnode :INTEGER
    
    def __init__(self,Pdata,Pnxtnode):
        self.data=Pdata
        self.nxtnode=Pnxtnode
        
#DECLARE limkedlist : ARRAY [0:11] OF node
#DECLARE startptr , emptylist :INTEGER


startptr=0
emptylist=5

linkedlist=[None]*10

linkedlist=[node(1,1),node(5,4),node(6,7),node(7,-1),node(2,2),node(0,6),node(0,6)
            ,node(0,8),node(56,3),node(0,9),node(0,-1)]

def outputnodes (array,strptr):
    data=""
    nxtptr=array[strptr].nxtnode
    data=array[strptr].data
    
    while nxtptr!= -1 :
        print (data)
        nxtptr=array[nxtptr].nxtnode
        data=array[nxtptr].data
        
outputnodes(linkedlist,startptr)        