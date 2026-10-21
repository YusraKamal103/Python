# This program demonstrates the use of functions with arguments and return values

def cube(num):
    
    cubenum=num*num*num
    return cubenum

num=int(input(f"input number"))
ans=cube(num)
print(ans)