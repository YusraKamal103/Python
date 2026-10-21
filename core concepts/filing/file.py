global numbers
numbers=[0]*25


#b)

#DECLARE skip_lines,count,line : INTEGER
#
def LoadData ():
    global numbers
    skip_lines=0
    
    try:
        count=0
        myfile=open("Data.txt",'r')
        
        line="hello"    
        while line != "" :    
                
            try:
                    newline=int(line=myfile.readline())
                    
                    numbers[count]=newline
                
                    count+=1
                    
            except :
                
                    skip_lines+=1
    
    except IOError:
        print("no file")                
 
LoadData()        
        
print (numbers)        