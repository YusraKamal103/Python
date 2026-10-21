
# write a python code to input 3 subjects marks and take out average

sub1=int(input("enter subject marks"))
sub2=int(input("enter subject marks"))
sub3=int(input("enter subject marks"))

avg=(sub1+sub2+sub3)/3

print("the average is ",avg)

# write a code which will prompt the user to input percentage of a student and output pass 
#if percentage is greater than 70% and fail if less

perct=float(input(f"enter percentage"))
if (perct >= 70 ):
    print("PASS")
else:
    print("fail")


#take input of percentage
# if percent >     



percentage=float(input("enter your percentage "))

if (percentage>= 90):
    print("A*")
elif (percentage>=80 and percentage < 90) :
    print("A")
elif (percentage>=70 and percentage< 80):
    print("B")
else :
    print("U*")


#take input marks of three subjects and output there remarks accordingly
 
sub1=int(input("enter subject marks"))
sub2=int(input("enter subject marks"))
sub3=int(input("enter subject marks"))

avg=(sub1+sub2+sub3)/3

if (avg>=90) :
    print("excellent")
elif (avg>=80):
    print("good")
elif (avg>=70 ):
    print("satisfactory")
else :
    print("needs improvement")
