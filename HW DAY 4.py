web_development=["Asha","Arun","Ajay"]
data_science=["Raju","Anu","Sona"]
ui_ux=["Anju","Varsha","Parvathy"]
all_participants=[web_development,data_science,ui_ux]
print(all_participants)
web_development.append("Arunima")
data_science.insert(1,"Pooja")
ui_ux.pop()
newdata_science=data_science.copy()
data_science.clear()
print(newdata_science)
print(data_science)
print(web_development[:2])
name_lengths = [len(name) for name in newdata_science]
print(name_lengths)
is_asha_present=(
    "Asha" in web_development or
    "Asha" in data_science or
    "Asha" in ui_ux
)
print("Is Asha present in any workshop?", is_asha_present)
first_participants = (web_development[0],newdata_science[0],ui_ux[0])
print(first_participants)