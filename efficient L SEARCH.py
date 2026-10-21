#efficient Linear SEARCH
numbers=[23,56,44,78,34,99,76] 

search=int(input("enter the number u want to find "))

i=0
found=False
pos=0
while i<7 and found == False: 
    if search == numbers[i] :
         found=True
         pos=i+1
    i=+1

if found:
     print("value found",pos)
else:
     print("value not found")     