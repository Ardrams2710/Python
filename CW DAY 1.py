import random
apple,orange,grape=15.5,20,10.25
total=apple+orange+grape
print("total volume",total)
volume_int=int(total)
print("total volume",volume_int)
print(type(volume_int))
volume_str=str(total)
print("total volume",volume_str)
print(type(volume_str))
bonus_liters=(random.randrange(5, 10))
final_total=total+bonus_liters
print("final total",final_total)


