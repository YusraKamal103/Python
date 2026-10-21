#write a program code using control loop to input age of 15 students and calculate avg

total=0 #initializing total is mandatory

for i in range(15):
    age=int(input("enter age: "))
    total= total + age
    

avg=total/15

print("the average",avg)




#write a program codethat will input 10 integers
#and output sum of positive and output how many numbers were negitive

neg=0
sum=0

for i in range(10):
    num=int(input("enter number: "))
    if (num<0 ):
        neg=neg+1
    else:
        sum=sum+num    

print("the number of negitive numbers are ",neg)
print("the sum of positive numbers ",sum)




#for remainder a%b
#for quotient = a//b

#write a program codethat will input 10 positive integers 
# find out and output how many integers were even


even=0
odd=0

for i in range(10):
    num=int(input(f"enter positive number "))  #for equals to ==
    if (num%2==0):                             # for not equal to !=
        even+=1
    else:
        odd+=1


print(f"number of even numbers are ",even)       
print (f"odd numbers are ",odd)



#hw
#take input of 10 students age and name
#output the maximum and minimum age 

name=input("enter name ")

age=int(input("enter age "))



max=age
min=age
min=999
max=0 

for i in range(9):
    
    name=input("enter name ")

    age=int(input("enter age "))
    
    if (age>max):
        max=age
        maxname=name
    elif (age<min):
        min=age
        minname=name


print("the maximum age entered was ",max," which is of" ,maxname)
print("the minimum age eneterd was  ",min," which is of ",minname)


#write a program code to input and store age of 10 students in a 1d array,student age

#in python there are lists i 
