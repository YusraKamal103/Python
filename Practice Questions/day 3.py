

name = "yusra "

print(f"my name is {name} yayyyy") #in order to add the variable output in between the string
                                    #but it only works if u write f


# write a program code which will input percentage of students
#and will calculate the avg
#display results when an invalid percentage is entered


avg=0
total=0
invalid=False
count=0


score= int(input("enter the percentage of student "))

while invalid == False :
    
    if (score > 100 and score< 0 ):
        invalid = True
        avg = total/count
        print (f"the average of {count} students calculated is {avg}")
    else:
        total=total + score 
        count =count + 1


#for declaring an array 
#DECLARE age : ARRAY[1:10] OF INTEGER --> in pseudocode
# age=[0]*10 -->in python
#inside the [ ] initialization is done 

#age=[67]*5 
#the whole array is initialised with the number 67




#sort the following array 
#Age= [15,19,14,20,17,10,11,21,27,16]   


Age= [15,19,14,20,17,10,11,21,27,16]   
j= 10
temp=0

flag=False
print("before sorting",Age)
for i in range (j):
    for i in range(j-1):
        flag=-1
        if Age[i]> Age[i+1]:
             temp= Age[i+1]
             Age[i+1]=Age[i]
             Age[i]=temp
             flag=True
    j=j-1    
    if (flag!=True): #!means does not equal to
        break      
   
print("after sorting ",Age)


#binary search
# age = [10, 11, 14, 15, 16, 17, 19, 20, 21, 27]
#search this array using binary search


age=[10, 11, 14, 15, 16, 17, 19, 20, 21, 27]

mid=int((0+9)/2)
data=int(input("enter the value u want to search : "))

top=0
bottom=9
found=False


while top<=bottom and found==False:
    if data==age[mid]:
        print(f"the number {data} is found at {mid}")
        found=True
    elif data>age[mid]:
        top=mid+1
        mid=int((top+bottom)/2)
    elif data<age[mid]:
        bottom=mid-1
        mid=int((top+bottom)/2)


if found==False:
    print("the value  is not found")