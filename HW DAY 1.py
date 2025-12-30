import random
rice,sugar,oil=45,40,130
rice_qty,sugar_qty,oil_qty=3,2.5,1.8
rice_total=rice*rice_qty
sugar_total=sugar*sugar_qty
oil_total=oil*oil_qty
print("total price of rice",rice_total)
print("total price of sugar",sugar_total)
print("total price of oil",oil_total)
total_bill=rice_total+sugar_total+oil_total
print("total bill",total_bill)
total_bill_int=int(total_bill)
print("total bill in integer",total_bill_int)
total_bill_str=str(total_bill)
print("total bill in string",total_bill_str)
delivery_charge=random.randrange(5, 10)
print("final bill including delivery charge",total_bill+delivery_charge)