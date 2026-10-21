

#p4 qno 4

class vehicle:
    #PRIVATE __ID : STRING
    #PRIVATE __maxspeed,__currentspeed,__increaseamount : INTEGER
    #PRIVATE __horizontalpos : INTEGER
    

    #constructor

    def __init__(self,Pmaxspeed,PID,Pincreaseamount):
        
        self.__ID=PID
        self.__maxspeed=Pmaxspeed
        self.__icreaseamount=Pincreaseamount

        self.__horizontalpos=0
        self.__currentspeed=0

        def GETcurrentspeed(self):
            return self.__currentspeed
        
        def GETincreasespeed (self):
            return self.__increasespeed
        
        def GEThorizontalpos(self):
            return self . __horizontalpos
        
        def GETmaxspeed (self):
            return self.__maxspeed
        
        def SETcurrentspeed (self,Pcurrentspeed):
            self.__currentspeed=Pcurrentspeed

        def SEThorizontalpos (self,Phorizontalpos):
              self.__horizontalpos=Phorizontalpos

        def increasespeed (self):
            self.__currentspeed=self.__currentspeed+ self.__increaseamount
            if self.__currentspeed>self.__maxspeed:
                self.__currentspeed=self.__maxspeed
                
            self.__horizontalpos=self.__horizontalpos+self.__currentspeed

    


    def displaydata (self):
       print("current speed is  ",self.__currentspeed)
       print ("horizontal position is ",self.__horizontalpos)










class helicopter(vehicle):
    #PRIVATE __verticalposition ,__varticalchange, __maxheight :INTEGER

    #CONSTRUCTOR
 def __init__(self,Pid,Pmaxspeed,Pincreaseamount,Pverticalchange,Pmaxheight):
       super().__init__(self,Pmaxspeed,Pid,Pincreaseamount)     #vehicle.__init__(self,Pmaxspeed,Pid,Pincreaseamount) 

       self.__maxheight=Pmaxheight
       self.__verticalchange=Pverticalchange
       self.__verticalposition=0



 def  Getverticalposition (self):
     return self.__verticalposition
 
 #polymorphism
 def increasespeed (self):
     self.__verticalposition += self.__verticalchange  # A=A+B ------ A+=B
     if self.__verticalposition > self.__maxheight :
         self.__verticalposition = self.__maxheight
     return super().increasespeed()    
 
 def displaydata(self):
     return super().displaydata()
     print("vertical position is ",self.__verticalposition)


mycar = vehicle("Tiger",100,20)
myhelicopter = helicopter("Lion",350,40,3,100)

print("My car")
mycar.increasespeed ()
mycar.increasespeed()
mycar.displaydata()

print("my helicopter")

myhelicopter.displaydata
myhelicopter.increasespeed()
myhelicopter.increasespeed()




 


                
                
                 
        
   
   
   

          
  
         

                  
    

        




        
        