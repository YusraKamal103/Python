
#open a file for write 
#enter three names using a function


myfile = open("myfile.txt","w")

def names():

 for i in range (3):
    name = input ("enter name  ")
    myfile.write(name)
    myfile.write("\n")



names()
  
#enter a num and take out its square
#store the number in a file



num=int(input(f"enter num which u want to square "))
sq=num*num
sq=str(sq)
myfile.write(sq)
myfile.write("\n")
       



