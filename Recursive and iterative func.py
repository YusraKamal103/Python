

#practice
#recursive function
def unknown ( x , y ):
   
   
   
 if x<y :
   print(x+y)
   return(unknown(x+1, y)*2)
 elif x==y :
   return (1)
 else:
   print(x+y)
   return(unknown((x-1,y)//2))

a=15
b=15

print("x is ",a)
print("y is ",b)
print(unknown(a,b))

#iterative function


def iterativeunknown (x,y):
    total=1
    
    while (x!=y):
        print(x+y)
        if x<y:
            x=+1
            total=total*2
        elif x>y :
            x=-1
            total=int(total/2)
    return(total)


print(iterativeunknown(15,15))
