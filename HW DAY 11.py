from tracker import create_record
from datetime import datetime
import json
records=[create_record("Goa", "Relaxing beaches", "05-06-2022"),create_record("Jaipur", "Loved the forts", "12-01-2023"),create_record("Bangalore", "Great weather", "20-09-2023")]
for record in records:
    date_obj=datetime.strptime(record["visit_date"],"%d-%m-%Y")
    record["visit_date"]=date_obj.strftime("%B %d, %Y")
json_data=json.dumps(records,indent=4)
print(json_data)
parsed_data=json.loads(json_data)
print("Travel records")
for record in parsed_data:
    print(f"city:{record['city']},Date:{record['visit_date']},comment:{record['comment']}")
