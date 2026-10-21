

#write a program code which will input and store the name and marks of 3 subjects of 5 students

name=[None]*5
marks =[[0,0,0]for i in range (5)] #format [number of colomns] for i in range (no of rows)
                                    #second optn= [[[0]for i in range(number of colomns)]for j in range(no of rows)]

# take input for 5 students

for i in range (5):
    name[i]=input("enter name u want to enter")
    flag=0
    while flag != 3:
        marks[i][flag]=int(input("enter marks of the  subject"))
        flag+=1

# calculate avg marks of each student and store in 1d array,avg

average=[0]*5

#optn = 1
# for i in range(5):
#     total=(marks[i][0])+(marks[i][1])+(marks[i][2])
#     avg=total/3
        

for i in range(5):
    for j in range(3):
        total=0
        total=total+(marks[i][j])
        avg=total/3
        average[i]=avg


#sort the arrays in ascending order of 2nd subject using efficient bubble sort
flag=False
for i in range(4):
    if marks[i][1]>marks[i+1][1]:
        flag=True
        while flag ==True:
            tempname=name[i]
            temp1=marks[i][0]
            temp2=marks[i][1]
            temp3=marks[i][2]
            name[i]=name[i+1]
            marks[i][0]=marks[i+1][0]
            marks[i][1]=marks[i+1][1]
            marks[i][2]=marks[i+1][2]
            name[i+1]=tempname
            marks[i+1][0]=temp1
            marks[i+1][1]=temp2
            marks[i+1][2]=temp3

            flag=False

print(name)
print(marks)


    