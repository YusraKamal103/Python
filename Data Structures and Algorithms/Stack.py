

#stack
#q1

#a)

#DECLARE StackData:ARRAY[1:10]
#DECLARE stackptr,value : integer

global StackData
StackData=[0]*10
global stackptr
stackptr=0

def outputstack ():
    global StackData
    global stackptr

    for i in range (10):
        print(StackData[i])

    print("stack pointer value is ",stackptr)


def  push(value):
    global stackptr
    global StackData
    
    if stackptr == 10 :
        return False
    else:
        
        StackData[stackptr]=value
        stackptr+=1
        return True

for x in range(11):
    val=int(input("enter value: "))
    space_avlbl=push(val)
    if space_avlbl==True:
        print("value is stored in stack")
    else:
        print("the stack was full")



outputstack()     






