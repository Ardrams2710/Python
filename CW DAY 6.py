attendence=[18,20,19,15,21]
count=0
total_attendence=0
for x in attendence:
    if x>20:
       print("The class is full")
       count=count+1
else:
    print("The class is not full")
print("the class was full in total",count,"days")
for x in attendence:
    total_attendence=total_attendence+x
print("total attendence for all 5 days is:",total_attendence)
