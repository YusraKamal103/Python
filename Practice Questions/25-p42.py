# #9618/41/o/n/25

# #q1)

# # DECLARE Stack : ARRAY [0:30] of INTEGER

# Stack=[0]*31

# TopOfStack=-1 # integer

# def push (num):
#     if TopOfStack == 30 :
#         return False
#     else:
#         TopOfStack+=1
#         Stack[TopOfStack]=num
#         return True
    
# def pop ():
#     if TopOfStack == -1 :
#         return -999
#     else:
#         temp=Stack[TopOfStack] # integer
#         TopOfStack-=1
        
#         return temp

        
        
        
#q2

# class Train :
#     #PRIVATE __TrainIdNumber : STRING
#     #PRIVATE __Route : INTEGER    
    
#     def __init__(self,Pid,Proute):
#         self.__TrainIdNumber=Pid
#         self.__Route=Proute
        
#     def GetTrainNumber (self):
#         return self.__TrainIdNumber
    
#     def GetRoute (self):
#         return self.__Route
    
    
# train1=Train("12ADV",134)
# train2=Train("22ART",20)       
# train3=Train("9FKF",3)
# train4=Train("21VBC",24)

# class Station :
#     #PRIVATE __StationId : STRING
#     #PRIVATE __NumberPlatforms,__NumberTrains : INTEGER
#     #PRIVATE Trains : ARRAY [0:9] OF Train
    
#     def __init__(self,Pstationid,Pplatforms):
        
#         self.__NumberPlatforms = Pplatforms
#         self.__StationId = Pstationid
#         self.Trains=[]
#         self.__NumberTrains=0
        
        
#     def AddTrain (self,Ptrain):
#             if  self.__NumberTrains <= self.__NumberPlatforms :
#                 self.Trains.append(Ptrain)
#                 self.__NumberTrains +=1
#                 return True
#             else :
#                 return False
            
            
#     def GetTrains (self,message):
#         if self.__NumberPlatforms == 0:
#             message= "There are no trains "
#             return message
#         else :
#             message= "the trains at station id: "+ self.__StationId + "\n"
#             i=self.__NumberTrains
#             for i in range (i):
#                 message = message + self.Trains[i].GetTrainNumber() + "on route number: " + self.Trains[i].GetRoute() + "\n"
            
#             return message    
            
            
# station_STH=Station("STH",2)
# station_NTH=Station("NTH",1) 

           
           
#q3

class Record () :
    def __init__(self,Pkey,Pdata):
        self.key=Pkey # INTEGER
        self.data=Pdata # STRING
        
global HashTable

HashTable=[[[0]for range in(10)] for range in (100)]

def Initializehasharray ():
    global HashTable
    
    for i in range (100):
        for j in range (10):
            HashTable[i,j]=None
            
            
            
            

