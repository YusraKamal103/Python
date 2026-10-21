#This program counts how many numbers entered by the user are out of the specified range (greater than 1000 and less than 9999).

count_out_of_range=0



for i in range(10):
    number=float(input("enter number"))
    if number>1000 and number<9999:
        count_out_of_range=+1

print("number out of range are",count_out_of_range)


