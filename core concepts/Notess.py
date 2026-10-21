

# use int(input("xyz"))

# use float for real numbers float(input("xyz"))

# control and backslash at the samtime will comment all

# div = //    mod= %     ^= **

# another way to print
# (f"minimum age is {min} of {minstd})



studentAge= [15,19,14,20,17,10,11,21,27,16]   #define student age

Details=[]
Details.append(4)    #!!!!!! use append to create locations (adds 4 to the array)

# function to give student age length 
len(studentAge())   


#------------------------------------


#2d array
LinkedList=[]
for i in range(0,19):
    LinkedList.append([-1, i +1])
# HashTable = [[Record(-1,"")]*10 for i in range(100)]  100x10 1st column integer 2nd till 10th column string

#to update 2d array
arraynodes= [[1,1,2],[1,2,5], [3,4,6],[2,0,2]]

Grid = [[0 for x in range(columns)] for y in range(rows)]
result:
[
 [0,0,0,0],
 [0,0,0,0],
 [0,0,0,0]
]
 
# OR

grid = []
for row in range(3):
    temp = []

    for col in range(4):
        temp.append(0)

    grid.append(temp)

print(grid)

output =
[0,0,0,0],
[0,0,0,0],
[0,0,0,0]

# read every row of 2d array = 
for row in grid:
    print(row)


# read every element for 2d array
# for Row in range(No.ofrows):
    # for Col in range(No.ofColums):
        # print(Grid[Row][Col])
# OR
for row in range(len(grid)):
    for column in range(len(grid[row])):  #if dont know number of columns
        print(grid[row][column])

# find an item in 2d arra=
for row in range(len(grid)):
    for col in range(len(grid[r])):

        if grid[r][c] == 99:
            print("Found at:", r, c)




#for i in range(i,j,k) i=starting position (by default 0), j-1=ending position, k=stepping (bydefault 1)


#-------------------------------------

#filing
#dont forget to use exception handling evry single time while using files

#write= w      #read= r     #append= a
f= <filename>, mode=<modetype>
f= open("alpha.txt" , mode="w") 
f.write(collegename)
f.close()
newline= f.readline()

for line in f
    print(line, split())   #makes list
f.close()

for Line in File:    if dont know number of lines in file
    print(Line.strip())


file= open("BinaryData.txt", mode="r")
    for line in file:
       returnval= Enqueue(line.strip())


f.write(name+  '\n')        #change line

thisline= f.readline().split(",")          #impppp    splits "12,24,65" into a list thisline of  [12, 24, 65]
HashTable[0].key = thisline[0]    #12
HashTable[0].key = thisline[1]     #24
HashTable[0].key = thisline[2]    #65
InsertIntoHash()



class Manager(Employee):
    def __init__(self, PBonusValue, PHourlyPay, PEmployeeNumber, PJobTitle):
         super().__init__(PName, PSound, PSize, PIntelligence)

# remember since private variables are used in oop, use this in inheritence
def Description(self):
        Mystring = super().Description()        #this parttttt Day17Qestion3
        message= Mystring    + ". Its territory is " + str(self.__TerritorySize) + " square miles."
        return message


class NewRecord:
    def __init__(self, PKey, PItem1, PItem2):   #dont use private for records
        self.Key= PKey
        self.Item1= PItem1
        self.item2= PItem2


for i, std in enumerate(Details, 1):     #watch this from sir video record data type
    print(f"Student Name: {std.name}, Age: {std.age}, Gender: {std.gender} 

Details = ["Ali", "Sara", "John"]

for i, std in enumerate(Details, 1):
    print(i, std) 
    
    #gives:
       1 Ali
       2 Sara
       3 John


#------------------------------------------------
# must write:
import random
# then use the random command


random.random(): Returns a random floating-point number between 0.0 and 1.0 (exclusive of 1.0).
# Random float between 0.0 and 1.0
print(random.random())

random.randint(a, b): Returns a random integer (both endpoints included).
# Random integer between 1 and 10
print(random.randint(1, 10))

random.uniform(a, b):
# Returns a random floating-point number between a and b (inclusive).
# Random float between 1.5 and 5.5

random.choice(sequence): Selects a single random element from a non-empty sequence like a list, tuple, or string.

random.shuffle(list): Reorders the elements of a list in-place.
# Random choice from a list
colors = ['red', 'blue', 'green']
print(random.choice(colors))
Use code with caution.

# random.sample(population, k): Returns a list of \(k\) unique elements chosen from the population without replacement.

random()Returns a random float between 0.0 and 1.0. eg random.random()
randint(a, b)Returns a random integer between a and b (both included). eg random.randint(1, 10)
uniform(a, b)Returns a random float between a and b. eg random.uniform(1.5, 5.5)
choice(seq)Returns a single random element from a sequence (list, tuple, etc.). eg random.choice(['apple', 'banana'])
shuffle(list)Reorders the elements of a list in place. eg random.shuffle(my_list)
sample(seq, k)Returns a list of k unique random elements from a sequence. eg random.sample(range(100), 5)

remember can break out of for by writing 
 break
in next line inside loop



def RecursiveBinarySearch(Array,Lower,Upper,FindVal):
   if Upper<Lower:
       return -1
   else:
       Middle= (Upper+Lower)//2
       if Array[Middle]== FindVal:
           return Middle
       elif Array[Middle]> FindVal:
           return RecursiveBinarySearch(Array, Lower, Middle-1, FindVal)
       else:
           return RecursiveBinarySearch(Array, Middle+1, Upper, FindVal)
 

#rememberrrr in the ned when it says "write the program code for..."
always alwayyssss gether up all the previous things you write in the main code together and take ss


A-LEVEL PYTHON LIBRARY ROUTINES

1. TYPE CONVERSION
int()
float()
str()
chr()
ord()  #ord('A') is 65

2. STRING ROUTINES
len(text)
text.upper()
text.lower()
text.find("x")
text.replace("a","b")
text.split()
text.strip()
text[start:end]
"-".join(list)
            my_list = ['apple', 'banana', 'cherry']
            result = "-".join(my_list)

print(result) 
# Output: apple-banana-cherry

SEARCH STRING LETTER BY LETTER

Method 1:
for letter in text:
    print(letter)

Method 2 (with index):
for i in range(len(text)):
    print(i, text[i])

Search for a letter:
for i in range(len(text)):
    if text[i] == "A":
        print("Found at", i)



3. NUMBER ROUTINES
max()
min()
abs()
pow()
round()

4. RANDOM
random.randint()
random.choice()
random.shuffle()

5. LISTS
append()
insert()
remove()
pop()
sort()
reverse()

6. FILES
open()
readline()
readlines()
write()
close()

7. MATH
math.sqrt()
math.floor()
math.ceil()
math.pi

8. 2D ARRAYS
board = [[0]*10 for _ in range(10)]
board[row][col]

9. OOP
__init__()
object.method()


#loop though string
for Letter in word:
   print(Letter)

#loop through array
for Item in Data:
   print(Item)

#loop through indices
for i in range(len(Data)):
   print(Data[i])

#loop hrough file
for Line in File:
    print(Line)


#slice word
Word[1:4]

#find
Word.find("a")

#replace
Word.replace("a","b")