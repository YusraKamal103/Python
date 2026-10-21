

#linked list q)1

class node :
    def __init__(self,Pdata,Pnextnode):
         self.data=Pdata
         self.nextnode=Pnextnode



#DECLARE linkedlist:ARRAY []       

linkedlist=[None]*10
startpointer=0
emptylist=5

# linkedlist[0]=node(1,1)        #method 1
# linkedlist[1]=node(5,4)
# linkedlist[2]=node(6,7)
# linkedlist[3]=node(7,-1)


#method2
linkedlist=[node(1,1),node(5,4),node(6,7),node(7,-1),node(2,2),node(0,6),node(0,8),node(0,8),node(56,3),node(0,9),node(0,-1)]

def outputnodes (arraylist,strptr):
    #DECLARE current:INTEGER

    current=strptr
    while current != -1 :
        
        print(arraylist[current].data)
        current=arraylist[current].nextnode
        


outputnodes(linkedlist,startpointer)    
    


def addnode (array,emptylist,strptr):
    data_to_add=input("print")