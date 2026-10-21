
# Iterative approach

def IterartiveCalculate (number):
   tofind=number
   total=0
   
   while number != 0:
      if tofind % number == 0 :
         total=total+number
         
         
      number-=1
   
   return total

# Recursive approach
def RecursiveValue (number,tofind):
   
   if number==0 :
      return 0
   else:
      if tofind % number == 0 :
         return(number + RecursiveValue(number-1, tofind))
      else:
         return (RecursiveValue(number-1,tofind))
      
out=RecursiveValue(50,50)      
print(out)         
         
   
   

