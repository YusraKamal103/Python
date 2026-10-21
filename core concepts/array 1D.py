#write a python code that inputs name of 5 students 
#and saves it in an array

name=["" for i in range(5)]

for count in range(5):
    name[count]=input(f"enter name")

print(name)    



#takes input of 10 students marks
#prints the highest marks

max=-1000

marks=[0.0 for i in range(10)]
 

for count in range(10):
    marks[count]=int(input(f"enter your marks"))

for j in range(10):
    if marks[j]> max :
        max=marks[j]


print("highest marks are: ",max)