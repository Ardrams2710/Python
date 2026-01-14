from tripdata import create_trip
from datetime import datetime
import json
trips=[create_trip("Mumbai","16-08-2025","City of dreams"),
      create_trip("Jaipur","18-05-2025","Pink city"),
      create_trip("Hyderabad","20-12-2025","City of pearls")]
for trip in trips:
    date_obj=datetime.strptime(trip["date_visited"],"%d-%m-%y")
    trip["date_visited"]=date_obj.strftime("%B %d,%y")
json_data=json.dumps(trips,indent=4)
print(json_data)
