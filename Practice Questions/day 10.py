 #p4 question 3 


class Card :
    #PRIVATE  , __number : INTEGER
    #PRIVATE __color : STRING

 #CONSTRUCTOR
 def __init__(self,Pnumber,Pcolor):
  self.__number=Pnumber
  self.__color=Pcolor


  def Getnumber (self):
   return self.__number
  
  def Getcolor (self):
   return self.__color
  

#DECLARE CARD :ARRAY[1:30]
card_array=[]*30

try:
 f = open("CardValues.txt",mode="r")

 print("file open ")

except IOError:
 print("file notfound")

selected=[False]*20

def choosecard ():
 myflag=False
 
 global selected
 
 while myflag== False :

   val=int(input("enter an integer from 1 to 30: "))
   
   while val<1 or val> 30 :
    val=int(input("INVALID-enter an integer from 1 to 30: "))
   if selected[val-1]== False:
    myflag=True
    selected[val-1]=True
    return val-1
   

#main 

#DECLARE player1: ARRAY [1:4] OF Card
#DECLARE i : INTEGER
   
player1=[]

for i in range(4):
 userinput=choosecard()
 player1.append(card_array [userinput])


for i in range (4):
 print ("number of card : ",player1[i].Getnumber())
 print ("color of card : ",player1[i].Getcolor())

 


 
    