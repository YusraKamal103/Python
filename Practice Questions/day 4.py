#write a program code to sort array, mylist which contains 10 elemnts
#mylist=[10,100,21,4,71,22,43,31,98,71]
#sort this array using insertion sort

mylist=[10,100,21,4,71,22,43,31,98,71]

flag=False

print("before sorting",mylist)

temp=0

for j in range(1,10):                   # for i in range(i,j,k) i=starting position
                                                           
    key=mylist[j]
    key1=j-1
   

    flag=True

    while (flag==True and key1>=0) :
                                                            #mylist[key1+1]=mylist[key1]
                                                            #mylist[key1]=key  --> imp to write
        if (key<mylist[key1]):

            mylist[key1+1]=mylist[key1]
            mylist[key1]=key

            key1 -= 1
            
            flag=True
        else :
            flag=False

print("after sorting",mylist)

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
