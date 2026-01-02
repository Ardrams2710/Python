fruits=["kiwi","watermelon","plum"]
vegetables=["tomato","carrot","beetroot"]
beverages=["water","coffee","tea"]
fruits.append("orange")
vegetables.insert(1,"drumstick")
beverages.pop()
inventory=[fruits,vegetables,beverages]
print(inventory)
print(fruits[:2])
print (vegetables[-1])
fruit_length=[len(x) for x in fruits]
print(fruit_length)
print("water" in beverages)
first_item=(fruits[0],vegetables[0],beverages[0])
print(first_item)