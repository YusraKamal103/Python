#linear search is a simple search algorithm that checks every element in a list until it finds the target value or reaches the end of the list.

arraydata =[10,5,6,7,1,12,13,15,21,8]

def linearsearch(num) : 
    ans=False
    for count in range(10):
        if num == arraydata[count]:
            ans = True
            print(f"answer is true")
    return ans        
       
        

user=input (f"enter num") 
print (linearsearch(user))    
    




