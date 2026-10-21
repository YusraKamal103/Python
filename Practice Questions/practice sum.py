sum=0   #initializing sum

for i in range(5):
    integer=int(input(f"enter an integer"))
    sum=sum+integer  #adding all the integers

if (sum%3==0):
    print(f"sum is divisible by 3")
else:
    print(f"sum is not divisible by 3") 



