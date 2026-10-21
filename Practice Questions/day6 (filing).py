#filing
#creating a connection
# F = open(<filename>,mode=<modetype>)
# write=w read=r append=a


f=open("myfile.txt",mode="w")


f.write=("yusra")

#input name of 10 students and write it in the file

file=open("students.txt","w")

for i in range (5):
    name=input("enter name")
    file.write(name)
    file.write("\n")
file.close()

# read from the file

#optn 1
f=open("students.txt","r")

newline=f.readline()
while newline!= "":
    print(newline,end="")
    newline=f.readline()
f.close()


#optn2
f=open("students.txt","r")

for line in f:
    print(line,end="")
f.close()


# split funct

mystring="ali,fahad,hamza"

word=mystring.split(",")
print(word)
