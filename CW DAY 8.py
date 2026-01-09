class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show_details(self):
        print("name:",self.name,"age:",self.age)
class Employee(person):
    def __init__(self,name,age,employee_id):
        super().__init__(name,age)
        self.employee_id=employee_id
    def show_details(self):
       print("name:",self.name,"age:",self.age,"employee_id:",self.employee_id)
class partTime(person):
    def __init__(self,name,age,working_hours):
         super().__init__(name,age)
         self.working_hours=working_hours
    def show_details(self):
        print("name:",self.name,"age:",self.age,"workinghours:",self.working_hours)
class consultant(Employee,partTime):
    def __init__(self,name,age,employee_id,working_hours,project_name):
        person.__init__(self,name,age)
        self.employee_id = employee_id
        self.working_hours = working_hours
        self.project_name = project_name
    def show_details(self):
        print("name:",self.name,"age:",self.age,"employee_id:",self.employee_id,"workinghours:",self.working_hours,self.project_name)
Person = person("Arathy", 26)
employee= Employee("Sona",29,"E108")
PartTime = partTime("Kevin", 24, 24.5)
Consultant= consultant("Ashish", 25, "106", 12.5, "Cyber Security Audit")
Person.show_details()
employee.show_details()
PartTime.show_details()
Consultant.show_details()

