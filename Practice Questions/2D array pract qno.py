

# Attendance Analysis Program
#uses 2D list to store the attendance of students and calculates their attendance percentage 
# and categorizes them into excellent, good, fair, or poor based on their attendance percentage.



TotalStudents=6
TotalDays=30

student_name=["Yusra","Ahmed","Azfar","Faiz","Laiba","Sadia"]
AttendanceDays=[

  [8,16],
  [7,20],
  [18,0],
  [22,1],
  [7,15],
  [9,3],

]

good=0 #initiallizing
excellent=0 #initiallizing
fair=0  #initiallizing
poor=0  #initiallizing

for i in range (TotalStudents):
    total_days=sum(AttendanceDays[i]) #totalling sales
    print(f"Student name:",student_name[i])
    print(f"total days attended",total_days)
    percentage=round((total_days/30)*100)#  calculating percentage
    print(f"Attendence percentage is",percentage)
    if percentage>=90:
        excellent=+1#incrementing
        print(f"excellent")
    elif percentage>=75 and percentage<90:
        good=+1#incrementing
        print(f"good")
    elif percentage>=50 and percentage<75:
        fair=+1#incrementing
        print(f"fair")
    else:
        poor=+1 #incrementing
        print(f"poor")

print(f"fair performances are",fair)
print(f"excellent performances are",excellent)
print(f"good are",good)
print(f"poor are",poor)




    






