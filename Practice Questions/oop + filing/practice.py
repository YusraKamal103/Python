

# # this is a program to read and write high scores from a file and manage them in arrays.

# #DECLARE score_array : ARRAY [0:11] OF INTEGER

# #DECLARE name_array : ARRAY [0:11] OF INTEGER




# global score_array
# global name_array

# score_array=[0]*12
# name_array=[""]*12

# def ReadHighScores ():
    
#     global score_array
#     global name_array
   
#     try:
#         file=open("HighScore.txt",'r')
        
#         for i in range(10):
#             data=file.readline().strip()
#             data2=int(file.readline().strip()) 
#             name_array[i]=data
#             score_array[i]=data2

#         file.close()   

       
    


#     except IOError:
#         print("file doesnot exist")


# def OutputHighScores ():
    
    
#     global score_array
#     global name_array        

#     for i in range(10):
#         name=name_array[i]
#         score=str(score_array[i])
#         temp =name + " " + score
#         print(temp)

           


# ReadHighScores()
# print("before")
# OutputHighScores()



# flag=False

# while flag!= True :
#     name=input("enter name of 3 characters ")
#     score=-1
#     score=int(input("enter score "))
#     if len(name.strip())==3 and score>=1 and score<= 100000 :
#         name=name
#         score=score
#         flag=True

# def newlist(x,y):
#     global name_array
#     global score_array


#     score_array[10]=y
#     name_array[10]=x


#     for i in range (11):
#         for j in range (10):
#             if score_array[j]<score_array[j+1]:
#                 tempscore=score_array[j]
#                 score_array[j]=score_array[j+1]
#                 score_array[j+1]=tempscore
#                 tempname=name_array[j]
#                 name_array[j]=name_array[j+1]
#                 name_array[j+1]=tempname


# newlist(name,score)
# print("after")
# OutputHighScores()

# def WriteTopTen():
    
#     global score_array
#     global name_array
 
#     newfile=open("NewHighScore.txt",'w')
#     for i in range (10):
#         newfile.write(name_array[i]+"\n")
#         newfile.write(str(score_array[i])+ "\n")
#     newfile.close()    

#----------------------------------------   

# this is a program that uses a class to store student details and then prints the details of the second student in the list.


class student :
    #DECLARE Id,age : INTEGER
    # DECLARE name : STRING
    # DECLARE gender : cHAR

    def __init__(self,Pid,Pname,Page,Pgender):
        self.id=Pid
        self.name=Pname
        self.age=Page
        self.gender=Pgender


details=[]*5
for i in range (2):
    id=int(input("enter id"))
    name=input("enter name")
    age=int(input("enter age"))
    gender=input("enter gender")

    details[i]=student(id,name,age,gender)

print(details[1])
   

