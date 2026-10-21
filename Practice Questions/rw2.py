class Card:
 #Number as Integer
 #Colour as string
 def __init__(self, Numberp, Colourp):
  self.__Number = Numberp
  self.__Color=Colourp

  
  def GetNumber(self):
    return self.__Number
 
 
 def GetColour(self):
    return self.__Color


CardArray=[0]*30

try:
 File = open("CardValues.txt",mode="r")

 print("file open ")

except IOError:
 print("file notfound")





for x in range(0,30):
  NumberRead = int(File.readline())
  ColourRead = File.readline()
  CardArray[x] = Card(NumberRead,ColourRead)

File.close

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
 player1.append(CardArray[userinput])


for i in range (4):
 print ("number of card : ",player1[i].GetNumber())
 print ("color of card : ",player1[i].GetColor())

 






