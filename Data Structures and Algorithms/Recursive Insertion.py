#------------------------------------------

#DECLARE NumberArray:ARRAY[0:7] OF INTEGER
NumberArray=[100,85,644,22,15,8,1]

#DECLARE lastitem , checkitem : INTEGER
# DECLARE  loopagain : BOOLEAN

def RecursiveInsertion(array,NumberElements) :
    
    if NumberElements<=1 :
        return array
    else :
        RecursiveInsertion(array,NumberElements-1)
        lastitem=array[NumberElements-1]
        checkitem=NumberElements - 2
        
    loopagain=True
    if checkitem <0 :
        loopagain=False
    else :
        if array[checkitem]<lastitem:
            loopagain=False
            
            
    while loopagain :
        array[checkitem+1]  = array[checkitem]
        checkitem=checkitem-1
        if checkitem<0 :
            loopagain=False
        else :
            if array[checkitem]< lastitem :
                loopagain=False

    array[checkitem+1]= lastitem
    return array 


result=RecursiveInsertion(NumberArray,7)

print("RECURSIVE")

print(result)



    
        