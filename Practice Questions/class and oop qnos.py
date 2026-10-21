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
CARD=[]*30

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
  
  