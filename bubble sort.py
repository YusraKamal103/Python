

X=int(input("how many numbers do u want to sort")) # asking the user how many numbers they want to sort

array= [ 0 for j in range(X) ]  #declaring an array of size X and initializing it with zeros

for i in range(X):
    num=int(input(f"enter numbers: ")) 
    array[i]=num

print("before sorting",array)
j=X-1

for index in range(X):     
  for count in range(j):
        if array[count] > array[count+1]:
            temp=array[count]
            array[count]=array[count + 1]
            array[count + 1]=temp


print("after sorting",array)  